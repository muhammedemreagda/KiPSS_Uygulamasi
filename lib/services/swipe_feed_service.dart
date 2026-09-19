import 'dart:math';
import '../models/swipe_card_model.dart';
import '../models/post_model.dart';
import 'data_service.dart';

class SwipeFeedService {
  static final SwipeFeedService _instance = SwipeFeedService._internal();
  factory SwipeFeedService() => _instance;
  SwipeFeedService._internal();

  final Random _random = Random();
  final DataService _dataService = DataService();

  List<SwipeCardModel> _allCardsPool = [];
  bool isInitialized = false;

  void initializeFeed() {
    if (isInitialized && _allCardsPool.isNotEmpty) return;

    List<SwipeCardModel> pool = [];

    // 1. Convert QuickNotes into Swipe Cards
    for (var note in _dataService.quickNotes) {
      final topic = _dataService.getTopicById(note.topicId);
      final course = topic != null ? _dataService.getCourseById(topic.courseId) : null;

      // Add main note summary card
      pool.add(
        SwipeCardModel(
          id: 'note-${note.id}',
          courseId: course?.id ?? 'genel',
          courseTitle: course?.title ?? 'Genel KPSS',
          topicId: topic?.id ?? note.topicId,
          topicTitle: topic?.title ?? 'Önemli Konu',
          cardTitle: note.title,
          frontContent: note.summary,
          backContent: note.content,
          fullSummary: note.content,
          keyPoints: note.keyPoints,
          likeCount: 12 + _random.nextInt(45),
          comments: [
            CommentModel(
              id: 'c1',
              postId: 'note-${note.id}',
              userId: 'u101',
              username: 'KpssDereceAdayı',
              userAvatar: '🎯',
              content: 'Bu bilgi tam sınavda çıkabilecek türden, not aldım!',
              timestamp: DateTime.now().subtract(const Duration(hours: 3)),
            ),
            CommentModel(
              id: 'c2',
              postId: 'note-${note.id}',
              userId: 'u102',
              username: 'TarihAvcısı',
              userAvatar: '📜',
              content: 'ÖSYM son 3 yılda bu konudan 2 soru sordu, dikkat edin.',
              timestamp: DateTime.now().subtract(const Duration(hours: 1)),
            ),
          ],
        ),
      );

      // Add individual flashcards from note if available
      for (int i = 0; i < note.flashcards.length; i++) {
        final fc = note.flashcards[i];
        pool.add(
          SwipeCardModel(
            id: 'fc-${note.id}-$i',
            courseId: course?.id ?? 'genel',
            courseTitle: course?.title ?? 'Genel KPSS',
            topicId: topic?.id ?? note.topicId,
            topicTitle: topic?.title ?? 'Kavram Kartı',
            cardTitle: '${note.title} • Kart #${fc.cardNumber}',
            frontContent: fc.title,
            backContent: fc.body,
            fullSummary: '${fc.title}\n\n${fc.body}\n\nKonu Özeti:\n${note.summary}',
            keyPoints: note.keyPoints,
            likeCount: 8 + _random.nextInt(30),
            comments: [],
          ),
        );
      }
    }

    // 2. Convert Questions into Micro-Learning Cards
    for (var q in _dataService.questions) {
      final topic = _dataService.getTopicById(q.topicId);
      final course = topic != null ? _dataService.getCourseById(topic.courseId) : null;

      final correctOptText = q.options.firstWhere(
        (o) => o.key == q.correctOption,
        orElse: () => q.options.first,
      ).text;

      pool.add(
        SwipeCardModel(
          id: 'q-${q.id}',
          courseId: course?.id ?? 'genel',
          courseTitle: course?.title ?? 'Genel KPSS',
          topicId: topic?.id ?? q.topicId,
          topicTitle: topic?.title ?? 'Çıkmış Soru Tipi',
          cardTitle: 'Soru & Çözüm Analizi 💡',
          frontContent: q.questionText,
          backContent: '✅ Doğru Cevap: (${q.correctOption}) $correctOptText\n\n📌 Açıklama:\n${q.explanation}',
          fullSummary: 'SORU:\n${q.questionText}\n\nÇÖZÜM:\n${q.explanation}',
          keyPoints: ['Doğru Cevap: ${q.correctOption}', 'Zorluk Seviyesi: ${q.difficultyLevel}/5'],
          likeCount: 15 + _random.nextInt(60),
          comments: [
            CommentModel(
              id: 'cq1',
              postId: 'q-${q.id}',
              userId: 'u103',
              username: 'MatematikDehası',
              userAvatar: '📐',
              content: 'Açıklama çok net olmuş, teşekkürler!',
              timestamp: DateTime.now().subtract(const Duration(minutes: 45)),
            ),
          ],
        ),
      );
    }

    // Shuffle pool for variety
    pool.shuffle(_random);
    _allCardsPool = pool;
    isInitialized = true;
  }

  SwipeCardModel getRandomCard({String? excludeId}) {
    initializeFeed();
    if (_allCardsPool.isEmpty) {
      return _fallbackCard();
    }
    List<SwipeCardModel> candidates = _allCardsPool.where((c) => c.id != excludeId).toList();
    if (candidates.isEmpty) candidates = _allCardsPool;
    return candidates[_random.nextInt(candidates.length)];
  }

  SwipeCardModel getSameCourseCard({required String currentCourseId, String? excludeId}) {
    initializeFeed();
    final matching = _allCardsPool.where((c) => c.courseId == currentCourseId && c.id != excludeId).toList();
    if (matching.isNotEmpty) {
      return matching[_random.nextInt(matching.length)];
    }
    return getRandomCard(excludeId: excludeId);
  }

  SwipeCardModel getSameTopicCard({required String currentTopicId, String? excludeId}) {
    initializeFeed();
    final matching = _allCardsPool.where((c) => c.topicId == currentTopicId && c.id != excludeId).toList();
    if (matching.isNotEmpty) {
      return matching[_random.nextInt(matching.length)];
    }
    // Fall back to same course or random
    return getRandomCard(excludeId: excludeId);
  }

  SwipeCardModel _fallbackCard() {
    return SwipeCardModel(
      id: 'fallback-1',
      courseId: 'course-tarih',
      courseTitle: 'Tarih',
      topicId: 'tarih-1',
      topicTitle: 'İslamiyet Öncesi Türk Tarihi',
      cardTitle: 'Kut Anlayışı',
      frontContent: 'İslamiyet öncesi Türk devletlerinde hükümdarlara yönetme yetkisinin Tanrı tarafından verildiğine inanılması sistemine ne ad verilir?',
      backContent: '✅ Kut Anlayışı!\n\nKut, kan yoluyla babadan oğula geçerdi. Bu durum taht kavgalarına ve Türk devletlerinin çabuk yıkılmasına neden olmuştur.',
      fullSummary: 'Kut Anlayışı ve Veraset Sistemi detaylı incelemesi...',
      keyPoints: ['Tanrısal Yetki', 'Babadan Oğula Geçiş', 'Taht Kavgaları Sebebi'],
      likeCount: 42,
    );
  }
}
