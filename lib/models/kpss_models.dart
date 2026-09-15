int _parseInt(dynamic val, [int fallback = 0]) {
  if (val is int) return val;
  if (val is double) return val.toInt();
  if (val is String) return int.tryParse(val) ?? fallback;
  return fallback;
}

double _parseDouble(dynamic val, [double fallback = 0.0]) {
  if (val is double) return val;
  if (val is int) return val.toDouble();
  if (val is String) return double.tryParse(val) ?? fallback;
  return fallback;
}

class CategoryModel {
  final String id;
  final String code;
  final String title;
  final int sortOrder;

  CategoryModel({
    required this.id,
    required this.code,
    required this.title,
    required this.sortOrder,
  });

  factory CategoryModel.fromJson(Map<String, dynamic> json) {
    return CategoryModel(
      id: json['id'] ?? '',
      code: json['code'] ?? '',
      title: json['title'] ?? '',
      sortOrder: _parseInt(json['sort_order']),
    );
  }
}

class CourseModel {
  final String id;
  final String categoryId;
  final String code;
  final String title;
  final String iconName;
  final int sortOrder;

  CourseModel({
    required this.id,
    required this.categoryId,
    required this.code,
    required this.title,
    required this.iconName,
    required this.sortOrder,
  });

  factory CourseModel.fromJson(Map<String, dynamic> json) {
    return CourseModel(
      id: json['id'] ?? '',
      categoryId: json['category_id'] ?? '',
      code: json['code'] ?? '',
      title: json['title'] ?? '',
      iconName: json['icon_name'] ?? 'menu_book',
      sortOrder: _parseInt(json['sort_order']),
    );
  }
}

class TopicModel {
  final String id;
  final String courseId;
  final String? parentId;
  final String title;
  final String slug;
  final double importanceWeight;
  final int sortOrder;

  TopicModel({
    required this.id,
    required this.courseId,
    this.parentId,
    required this.title,
    required this.slug,
    required this.importanceWeight,
    required this.sortOrder,
  });

  factory TopicModel.fromJson(Map<String, dynamic> json) {
    return TopicModel(
      id: json['id'] ?? '',
      courseId: json['course_id'] ?? '',
      parentId: json['parent_id'],
      title: json['title'] ?? '',
      slug: json['slug'] ?? '',
      importanceWeight: _parseDouble(json['importance_weight'], 1.0),
      sortOrder: _parseInt(json['sort_order']),
    );
  }
}

class FlashcardItem {
  final int cardNumber;
  final String title;
  final String body;

  FlashcardItem({
    required this.cardNumber,
    required this.title,
    required this.body,
  });

  factory FlashcardItem.fromJson(Map<String, dynamic> json) {
    return FlashcardItem(
      cardNumber: _parseInt(json['card_number'], 1),
      title: json['title'] ?? '',
      body: json['body'] ?? '',
    );
  }
}

class QuickNoteModel {
  final String id;
  final String topicId;
  final String title;
  final String summary;
  final String content;
  final List<String> keyPoints;
  final List<FlashcardItem> flashcards;
  final String sourceReference;
  final bool isVerified;
  final int readTimeSeconds;

  QuickNoteModel({
    required this.id,
    required this.topicId,
    required this.title,
    required this.summary,
    required this.content,
    required this.keyPoints,
    required this.flashcards,
    required this.sourceReference,
    required this.isVerified,
    required this.readTimeSeconds,
  });

  factory QuickNoteModel.fromJson(Map<String, dynamic> json) {
    return QuickNoteModel(
      id: json['id'] ?? '',
      topicId: json['topic_id'] ?? '',
      title: json['title'] ?? '',
      summary: json['summary'] ?? '',
      content: json['content'] ?? '',
      keyPoints: (json['key_points'] as List? ?? []).map((e) => e.toString()).toList(),
      flashcards: (json['flashcards'] as List? ?? []).map((e) => FlashcardItem.fromJson(e)).toList(),
      sourceReference: json['source_reference'] ?? '2026 ÖSYM Müfredatı & Çıkmış Sorular Archive',
      isVerified: json['is_verified'] ?? true,
      readTimeSeconds: _parseInt(json['read_time_seconds'], 180),
    );
  }
}

class QuestionOptionModel {
  final String key;
  final String text;

  QuestionOptionModel({required this.key, required this.text});

  factory QuestionOptionModel.fromJson(Map<String, dynamic> json) {
    return QuestionOptionModel(
      key: json['key'] ?? '',
      text: json['text'] ?? '',
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'key': key,
      'text': text,
    };
  }
}

class QuestionModel {
  final String id;
  final String topicId;
  final String questionText;
  final List<QuestionOptionModel> options;
  final String correctOption;
  final String explanation;
  final int difficultyLevel;

  QuestionModel({
    required this.id,
    required this.topicId,
    required this.questionText,
    required this.options,
    required this.correctOption,
    required this.explanation,
    required this.difficultyLevel,
  });

  factory QuestionModel.fromJson(Map<String, dynamic> json) {
    return QuestionModel(
      id: json['id'] ?? '',
      topicId: json['topic_id'] ?? '',
      questionText: json['question_text'] ?? '',
      options: (json['options'] as List? ?? []).map((e) => QuestionOptionModel.fromJson(e)).toList(),
      correctOption: json['correct_option'] ?? 'A',
      explanation: json['explanation'] ?? '',
      difficultyLevel: _parseInt(json['difficulty_level'], 3),
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'topic_id': topicId,
      'question_text': questionText,
      'options': options.map((o) => o.toJson()).toList(),
      'correct_option': correctOption,
      'explanation': explanation,
      'difficulty_level': difficultyLevel,
    };
  }
}
