import 'dart:convert';
import 'dart:math';
import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';
import '../models/kpss_models.dart';
import '../models/mock_exam_model.dart';
import '../theme/app_theme.dart';
import 'persistence_service.dart';

class WeakTopicReportItem {
  final String courseId;
  final String courseTitle;
  final String topicId;
  final String topicTitle;
  final int totalQuestions;
  final int wrongCount;
  final int blankCount;
  final int correctCount;

  WeakTopicReportItem({
    required this.courseId,
    required this.courseTitle,
    required this.topicId,
    required this.topicTitle,
    required this.totalQuestions,
    required this.wrongCount,
    required this.blankCount,
    required this.correctCount,
  });

  double get accuracyPercentage => totalQuestions > 0 ? (correctCount / totalQuestions) * 100 : 0.0;
}

class DataService {
  static final DataService _instance = DataService._internal();
  factory DataService() => _instance;
  DataService._internal();

  List<CategoryModel> categories = [];
  List<CourseModel> courses = [];
  List<TopicModel> topics = [];
  List<QuickNoteModel> quickNotes = [];
  List<QuestionModel> questions = [];

  // Completed Exam History
  List<MockExam> completedExams = [];

  // Bookmarked & Wrong Question IDs
  Set<String> bookmarkedQuestionIds = {};
  Set<String> wrongQuestionIds = {};

  String targetExamLevel = 'lisans'; // 'lisans', 'onlisans', 'lise'
  double targetScore = 88.5;
  int userTotalAttempted = 142;
  int userTotalCorrect = 118;
  double userCurrentNetScore = 81.25;

  bool isLoaded = false;
  final Random _random = Random();
  final PersistenceService _persistence = PersistenceService();

  Future<void> loadSampleData() async {
    if (isLoaded) return;
    try {
      final String jsonString = await rootBundle.loadString('assets/data/sample_data.json');
      final Map<String, dynamic> data = json.decode(jsonString);

      categories = (data['categories'] as List? ?? []).map((e) => CategoryModel.fromJson(e)).toList();
      courses = (data['courses'] as List? ?? []).map((e) => CourseModel.fromJson(e)).toList();
      topics = (data['topics'] as List? ?? []).map((e) => TopicModel.fromJson(e)).toList();
      quickNotes = (data['quick_notes'] as List? ?? []).map((e) => QuickNoteModel.fromJson(e)).toList();
      questions = (data['questions'] as List? ?? []).map((e) => QuestionModel.fromJson(e)).toList();

      isLoaded = true;

      // Restore saved user state from persistence if available
      final savedState = await _persistence.loadUserData();
      if (savedState != null) {
        targetScore = savedState.targetScore;
        userTotalAttempted = savedState.userTotalAttempted;
        userTotalCorrect = savedState.userTotalCorrect;
        userCurrentNetScore = savedState.userCurrentNetScore;
        completedExams = savedState.completedExams;
        bookmarkedQuestionIds = savedState.bookmarkedQuestionIds;
        wrongQuestionIds = savedState.wrongQuestionIds;
        AppTheme.setThemeMode(savedState.isDarkMode);
      } else {
        _initDemoExamHistory();
      }
    } catch (e) {
      debugPrint('Error loading sample data: $e');
      isLoaded = true; // Always set isLoaded to true so app never hangs!
    }
  }

  void _initDemoExamHistory() {
    if (completedExams.isNotEmpty) return;
    try {
      final demoExam = generateFullMockExam();
      demoExam.isCompleted = true;
      demoExam.startTime = DateTime.now().subtract(const Duration(days: 1));
      demoExam.endTime = DateTime.now().subtract(const Duration(days: 1, hours: -2));

      for (int i = 0; i < demoExam.questions.length; i++) {
        final item = demoExam.questions[i];
        final wrongOpt = item.question.options.where((o) => o.key != item.question.correctOption).toList();

        if (item.topicTitle.contains('Çember') || item.topicTitle.contains('Üçgen')) {
          if (wrongOpt.isNotEmpty) {
            item.selectedOptionKey = wrongOpt.first.key;
            wrongQuestionIds.add(item.question.id);
          }
        } else if (i % 5 == 0) {
          item.selectedOptionKey = null; // Blank
        } else if (i % 7 == 0) {
          if (wrongOpt.isNotEmpty) {
            item.selectedOptionKey = wrongOpt.first.key;
            wrongQuestionIds.add(item.question.id);
          }
        } else {
          item.selectedOptionKey = item.question.correctOption;
        }
      }

      completedExams.add(demoExam);
      saveState();
    } catch (e) {
      debugPrint('Error initializing demo exam history: $e');
    }
  }

  Future<void> saveState() async {
    await _persistence.saveUserData(
      targetScore: targetScore,
      userTotalAttempted: userTotalAttempted,
      userTotalCorrect: userTotalCorrect,
      userCurrentNetScore: userCurrentNetScore,
      completedExams: completedExams,
      bookmarkedQuestionIds: bookmarkedQuestionIds,
      wrongQuestionIds: wrongQuestionIds,
      isDarkMode: AppTheme.isDarkMode,
    );
  }

  void setTargetScore(double newScore) {
    targetScore = newScore;
    saveState();
  }

  void saveCompletedExam(MockExam exam) {
    exam.isCompleted = true;
    completedExams.insert(0, exam); // Newest first

    userTotalAttempted += exam.totalQuestions;
    userTotalCorrect += exam.correctCount;
    userCurrentNetScore = exam.netScore;

    // Automatically add all wrong questions to wrongQuestionIds
    for (var item in exam.questions) {
      if (item.isWrong) {
        wrongQuestionIds.add(item.question.id);
      }
    }

    saveState();
  }

  // --- BOOKMARK / FAVORITE QUESTION MANAGEMENT ---
  bool isBookmarked(String questionId) => bookmarkedQuestionIds.contains(questionId);

  void toggleBookmark(String questionId) {
    if (bookmarkedQuestionIds.contains(questionId)) {
      bookmarkedQuestionIds.remove(questionId);
    } else {
      bookmarkedQuestionIds.add(questionId);
    }
    saveState();
  }

  List<QuestionModel> getBookmarkedQuestions() {
    return questions.where((q) => bookmarkedQuestionIds.contains(q.id)).toList();
  }

  // --- WRONG QUESTION POOL MANAGEMENT ---
  bool isWrongQuestion(String questionId) => wrongQuestionIds.contains(questionId);

  void addWrongQuestion(String questionId) {
    wrongQuestionIds.add(questionId);
    saveState();
  }

  void removeWrongQuestion(String questionId) {
    wrongQuestionIds.remove(questionId);
    saveState();
  }

  void clearWrongQuestions() {
    wrongQuestionIds.clear();
    saveState();
  }

  List<QuestionModel> getWrongQuestions() {
    return questions.where((q) => wrongQuestionIds.contains(q.id)).toList();
  }

  List<WeakTopicReportItem> getWeakTopicsAnalytics() {
    Map<String, Map<String, int>> topicStats = {};

    for (var exam in completedExams) {
      for (var item in exam.questions) {
        String topicId = item.question.topicId;
        topicStats.putIfAbsent(topicId, () => {'total': 0, 'correct': 0, 'wrong': 0, 'blank': 0});

        topicStats[topicId]!['total'] = topicStats[topicId]!['total']! + 1;
        if (item.isCorrect) {
          topicStats[topicId]!['correct'] = topicStats[topicId]!['correct']! + 1;
        } else if (item.isWrong) {
          topicStats[topicId]!['wrong'] = topicStats[topicId]!['wrong']! + 1;
        } else if (item.isBlank) {
          topicStats[topicId]!['blank'] = topicStats[topicId]!['blank']! + 1;
        }
      }
    }

    List<WeakTopicReportItem> reports = [];

    topicStats.forEach((topicId, stats) {
      final topic = getTopicById(topicId);
      if (topic == null) return;
      final course = getCourseById(topic.courseId);

      int total = stats['total']!;
      int wrong = stats['wrong']!;
      int blank = stats['blank']!;
      int correct = stats['correct']!;

      if (wrong > 0 || blank > 0) {
        reports.add(WeakTopicReportItem(
          courseId: topic.courseId,
          courseTitle: course?.title ?? 'Ders',
          topicId: topicId,
          topicTitle: topic.title,
          totalQuestions: total,
          wrongCount: wrong,
          blankCount: blank,
          correctCount: correct,
        ));
      }
    });

    reports.sort((a, b) => (b.wrongCount + b.blankCount).compareTo(a.wrongCount + a.blankCount));
    return reports;
  }

  List<CourseModel> getCoursesByCategory(String categoryId) {
    return courses.where((c) => c.categoryId == categoryId).toList();
  }

  List<TopicModel> getTopicsByCourse(String courseId) {
    return topics.where((t) => t.courseId == courseId).toList();
  }

  QuickNoteModel? getQuickNoteByTopic(String topicId) {
    try {
      return quickNotes.firstWhere((n) => n.topicId == topicId);
    } catch (_) {
      return null;
    }
  }

  List<QuestionModel> getQuestionsByTopic(String topicId) {
    return questions.where((q) => q.topicId == topicId).toList();
  }

  CourseModel? getCourseById(String courseId) {
    try {
      return courses.firstWhere((c) => c.id == courseId);
    } catch (_) {
      return null;
    }
  }

  TopicModel? getTopicById(String topicId) {
    try {
      return topics.firstWhere((t) => t.id == topicId);
    } catch (_) {
      return null;
    }
  }

  void recordAttempt({required bool isCorrect}) {
    userTotalAttempted++;
    if (isCorrect) userTotalCorrect++;
    double accuracy = userTotalCorrect / userTotalAttempted;
    userCurrentNetScore = (accuracy * 120) * 0.85;
    saveState();
  }

  List<QuestionModel> _sampleQuestions(List<QuestionModel> pool, int count) {
    if (pool.isEmpty) return [];
    List<QuestionModel> shuffled = List.from(pool)..shuffle(_random);
    return shuffled.take(count).toList();
  }

  List<ExamQuestionItem> _toExamItems(List<QuestionModel> qList) {
    List<ExamQuestionItem> items = qList.map((q) {
      final topic = getTopicById(q.topicId);
      final course = topic != null ? getCourseById(topic.courseId) : null;
      return ExamQuestionItem(
        question: q,
        courseName: course?.title ?? 'Genel',
        topicTitle: topic?.title ?? 'Konu',
      );
    }).toList();

    items.sort((a, b) {
      final topicA = getTopicById(a.question.topicId);
      final topicB = getTopicById(b.question.topicId);
      final courseA = topicA != null ? getCourseById(topicA.courseId) : null;
      final courseB = topicB != null ? getCourseById(topicB.courseId) : null;

      int courseOrderA = courseA?.sortOrder ?? 99;
      int courseOrderB = courseB?.sortOrder ?? 99;

      if (courseOrderA != courseOrderB) {
        return courseOrderA.compareTo(courseOrderB);
      }

      int topicOrderA = topicA?.sortOrder ?? 99;
      int topicOrderB = topicB?.sortOrder ?? 99;
      return topicOrderA.compareTo(topicOrderB);
    });

    return items;
  }

  MockExam generateFullMockExam() {
    List<QuestionModel> selected = [];

    final turkceQuestions = questions.where((q) => getTopicById(q.topicId)?.courseId == 'course-turkce').toList();
    final matQuestions = questions.where((q) => getTopicById(q.topicId)?.courseId == 'course-matematik').toList();
    final tarihQuestions = questions.where((q) => getTopicById(q.topicId)?.courseId == 'course-tarih').toList();
    final cogQuestions = questions.where((q) => getTopicById(q.topicId)?.courseId == 'course-cografya').toList();
    final vatQuestions = questions.where((q) => getTopicById(q.topicId)?.courseId == 'course-vatandaslik').toList();
    final gunQuestions = questions.where((q) => getTopicById(q.topicId)?.courseId == 'course-guncel').toList();

    selected.addAll(_sampleQuestions(turkceQuestions, 30));
    selected.addAll(_sampleQuestions(matQuestions, 30));
    selected.addAll(_sampleQuestions(tarihQuestions, 27));
    selected.addAll(_sampleQuestions(cogQuestions, 18));
    selected.addAll(_sampleQuestions(vatQuestions, 9));
    selected.addAll(_sampleQuestions(gunQuestions, 6));

    return MockExam(
      id: 'exam-${DateTime.now().millisecondsSinceEpoch}',
      title: 'Tam Gerçek KPSS Genel Yetenek - Genel Kültür Denemesi',
      type: ExamType.full,
      questions: _toExamItems(selected),
      totalTimeSeconds: 130 * 60, // 130 dakika
    );
  }

  MockExam generateMiniMockExam() {
    List<QuestionModel> selected = [];

    final turkceQuestions = questions.where((q) => getTopicById(q.topicId)?.courseId == 'course-turkce').toList();
    final matQuestions = questions.where((q) => getTopicById(q.topicId)?.courseId == 'course-matematik').toList();
    final tarihQuestions = questions.where((q) => getTopicById(q.topicId)?.courseId == 'course-tarih').toList();
    final cogQuestions = questions.where((q) => getTopicById(q.topicId)?.courseId == 'course-cografya').toList();
    final vatQuestions = questions.where((q) => getTopicById(q.topicId)?.courseId == 'course-vatandaslik').toList();
    final gunQuestions = questions.where((q) => getTopicById(q.topicId)?.courseId == 'course-guncel').toList();

    selected.addAll(_sampleQuestions(turkceQuestions, 8));
    selected.addAll(_sampleQuestions(matQuestions, 8));
    selected.addAll(_sampleQuestions(tarihQuestions, 7));
    selected.addAll(_sampleQuestions(cogQuestions, 4));
    selected.addAll(_sampleQuestions(vatQuestions, 2));
    selected.addAll(_sampleQuestions(gunQuestions, 1));

    return MockExam(
      id: 'exam-mini-${DateTime.now().millisecondsSinceEpoch}',
      title: 'Hızlı Pratik KPSS Mini Denemesi (30 Soru)',
      type: ExamType.mini,
      questions: _toExamItems(selected),
      totalTimeSeconds: 35 * 60, // 35 dakika
    );
  }

  MockExam generateSubjectMockExam({required String courseId, required int questionCount}) {
    final course = getCourseById(courseId);
    final courseTitle = course?.title ?? 'Ders';

    final courseQuestions = questions.where((q) {
      final t = getTopicById(q.topicId);
      return t?.courseId == courseId;
    }).toList();

    final selected = _sampleQuestions(courseQuestions, questionCount);

    int totalMinutes = (questionCount * 1.25).ceil();

    return MockExam(
      id: 'exam-subject-${DateTime.now().millisecondsSinceEpoch}',
      title: '$courseTitle Özel Branş Denemesi ($questionCount Soru)',
      type: ExamType.customSubject,
      questions: _toExamItems(selected),
      totalTimeSeconds: totalMinutes * 60,
    );
  }

  // Generate a practice exam specifically from wrong or bookmarked questions
  MockExam generateCustomPracticeExam({required List<QuestionModel> selectedQuestions, required String title}) {
    return MockExam(
      id: 'exam-custom-${DateTime.now().millisecondsSinceEpoch}',
      title: title,
      type: ExamType.customSubject,
      questions: _toExamItems(selectedQuestions),
      totalTimeSeconds: (selectedQuestions.length * 90), // 1.5 min per q
    );
  }
}
