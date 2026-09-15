import '../models/kpss_models.dart';

enum ExamType {
  full, // 120 Questions (130 mins)
  mini, // 30 Questions (35 mins)
  customSubject, // 5-30 Questions (custom time)
}

enum QuestionUserStatus {
  unanswered,
  answered,
  flagged, // Daha Sonra Bak
}

class ExamQuestionItem {
  final QuestionModel question;
  final String courseName;
  final String topicTitle;
  String? selectedOptionKey;
  bool isFlagged;

  ExamQuestionItem({
    required this.question,
    required this.courseName,
    required this.topicTitle,
    this.selectedOptionKey,
    this.isFlagged = false,
  });

  bool get isAnswered => selectedOptionKey != null;
  bool get isCorrect => selectedOptionKey == question.correctOption;
  bool get isWrong => selectedOptionKey != null && selectedOptionKey != question.correctOption;
  bool get isBlank => selectedOptionKey == null;

  factory ExamQuestionItem.fromJson(Map<String, dynamic> json) {
    return ExamQuestionItem(
      question: QuestionModel.fromJson(json['question'] ?? {}),
      courseName: json['course_name'] ?? 'Genel',
      topicTitle: json['topic_title'] ?? 'Konu',
      selectedOptionKey: json['selected_option_key'],
      isFlagged: json['is_flagged'] ?? false,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'question': question.toJson(),
      'course_name': courseName,
      'topic_title': topicTitle,
      'selected_option_key': selectedOptionKey,
      'is_flagged': isFlagged,
    };
  }
}

class MockExam {
  final String id;
  final String title;
  final ExamType type;
  final List<ExamQuestionItem> questions;
  final int totalTimeSeconds;
  int remainingTimeSeconds;
  bool isCompleted;
  DateTime? startTime;
  DateTime? endTime;

  MockExam({
    required this.id,
    required this.title,
    required this.type,
    required this.questions,
    required this.totalTimeSeconds,
    int? remainingTimeSeconds,
    this.isCompleted = false,
    this.startTime,
    this.endTime,
  }) : remainingTimeSeconds = remainingTimeSeconds ?? totalTimeSeconds;

  factory MockExam.fromJson(Map<String, dynamic> json) {
    String typeStr = json['type'] ?? 'full';
    ExamType typeEnum = ExamType.full;
    if (typeStr == 'mini') typeEnum = ExamType.mini;
    if (typeStr == 'customSubject') typeEnum = ExamType.customSubject;

    final exam = MockExam(
      id: json['id'] ?? '',
      title: json['title'] ?? '',
      type: typeEnum,
      questions: (json['questions'] as List? ?? []).map((e) => ExamQuestionItem.fromJson(e)).toList(),
      totalTimeSeconds: json['total_time_seconds'] ?? 7800,
      remainingTimeSeconds: json['remaining_time_seconds'],
      isCompleted: json['is_completed'] ?? true,
      startTime: json['start_time'] != null ? DateTime.tryParse(json['start_time']) : null,
      endTime: json['end_time'] != null ? DateTime.tryParse(json['end_time']) : null,
    );
    return exam;
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'title': title,
      'type': type.name,
      'questions': questions.map((q) => q.toJson()).toList(),
      'total_time_seconds': totalTimeSeconds,
      'remaining_time_seconds': remainingTimeSeconds,
      'is_completed': isCompleted,
      'start_time': startTime?.toIso8601String(),
      'end_time': endTime?.toIso8601String(),
    };
  }

  int get totalQuestions => questions.length;
  int get answeredCount => questions.where((q) => q.isAnswered).length;
  int get flaggedCount => questions.where((q) => q.isFlagged).length;
  int get blankCount => questions.where((q) => q.isBlank).length;
  int get correctCount => questions.where((q) => q.isCorrect).length;
  int get wrongCount => questions.where((q) => q.isWrong).length;

  double get netScore {
    double net = correctCount - (wrongCount / 4.0);
    return net < 0 ? 0.0 : net;
  }

  // Group questions by course
  Map<String, List<ExamQuestionItem>> get questionsByCourse {
    Map<String, List<ExamQuestionItem>> map = {};
    for (var item in questions) {
      map.putIfAbsent(item.courseName, () => []).add(item);
    }
    return map;
  }

  // Compute net per course
  Map<String, Map<String, dynamic>> get courseBreakdown {
    Map<String, Map<String, dynamic>> breakdown = {};
    questionsByCourse.forEach((courseName, items) {
      int correct = items.where((i) => i.isCorrect).length;
      int wrong = items.where((i) => i.isWrong).length;
      int blank = items.where((i) => i.isBlank).length;
      double net = correct - (wrong / 4.0);
      breakdown[courseName] = {
        'total': items.length,
        'correct': correct,
        'wrong': wrong,
        'blank': blank,
        'net': net < 0 ? 0.0 : net,
      };
    });
    return breakdown;
  }

  // Estimated KPSS P3 Score simulation
  double get estimatedKpssScore {
    if (type == ExamType.full) {
      // Real KPSS Lisans P3 estimation
      // Base score 40 + (Net * 0.5)
      double score = 45.0 + (netScore * 0.45);
      return score > 100.0 ? 100.0 : (score < 40.0 ? 40.0 : score);
    } else {
      // Scaled for mini or custom
      double accuracyRatio = netScore / totalQuestions;
      double score = 45.0 + (accuracyRatio * 50.0);
      return score > 100.0 ? 100.0 : score;
    }
  }
}
