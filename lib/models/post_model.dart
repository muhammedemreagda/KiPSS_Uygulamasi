enum PostCategory {
  question, // ❓ Soru Sor (Çözülemedi)
  flashcard, // 💡 Hap Bilgi (Kodlama / Not)
  netScore, // 🎯 Net Paylaşımı
  general, // 💬 Genel Sohbet
}

extension PostCategoryExtension on PostCategory {
  String get title {
    switch (this) {
      case PostCategory.question:
        return '❓ Soru Sor';
      case PostCategory.flashcard:
        return '💡 Hap Bilgi';
      case PostCategory.netScore:
        return '🎯 Net Paylaşımı';
      case PostCategory.general:
        return '💬 Genel Sohbet';
    }
  }

  String get codeName {
    switch (this) {
      case PostCategory.question:
        return 'question';
      case PostCategory.flashcard:
        return 'flashcard';
      case PostCategory.netScore:
        return 'netScore';
      case PostCategory.general:
        return 'general';
    }
  }

  static PostCategory fromCode(String code) {
    switch (code) {
      case 'question':
        return PostCategory.question;
      case 'flashcard':
        return PostCategory.flashcard;
      case 'netScore':
        return PostCategory.netScore;
      default:
        return PostCategory.general;
    }
  }
}

class CommentModel {
  final String id;
  final String postId;
  final String userId;
  final String username;
  final String userAvatar;
  final String content;
  final DateTime timestamp;
  bool isBestSolution;

  CommentModel({
    required this.id,
    required this.postId,
    required this.userId,
    required this.username,
    required this.userAvatar,
    required this.content,
    DateTime? timestamp,
    this.isBestSolution = false,
  }) : timestamp = timestamp ?? DateTime.now();

  factory CommentModel.fromJson(Map<String, dynamic> json) {
    return CommentModel(
      id: json['id'] ?? '',
      postId: json['post_id'] ?? '',
      userId: json['user_id'] ?? '',
      username: json['username'] ?? 'Kullanıcı',
      userAvatar: json['user_avatar'] ?? '👤',
      content: json['content'] ?? '',
      timestamp: json['timestamp'] != null
          ? DateTime.tryParse(json['timestamp']) ?? DateTime.now()
          : DateTime.now(),
      isBestSolution: json['is_best_solution'] ?? false,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'post_id': postId,
      'user_id': userId,
      'username': username,
      'user_avatar': userAvatar,
      'content': content,
      'timestamp': timestamp.toIso8601String(),
      'is_best_solution': isBestSolution,
    };
  }
}

class PostModel {
  final String id;
  final String userId;
  final String username;
  final String userAvatar;
  final String userBadge;
  final PostCategory category;
  final String title;
  final String content;
  final DateTime timestamp;
  int likeCount;
  Set<String> likedUserIds;
  List<CommentModel> comments;

  PostModel({
    required this.id,
    required this.userId,
    required this.username,
    required this.userAvatar,
    required this.userBadge,
    required this.category,
    required this.title,
    required this.content,
    DateTime? timestamp,
    this.likeCount = 0,
    Set<String>? likedUserIds,
    List<CommentModel>? comments,
  })  : timestamp = timestamp ?? DateTime.now(),
        likedUserIds = likedUserIds ?? {},
        comments = comments ?? [];

  factory PostModel.fromJson(Map<String, dynamic> json) {
    return PostModel(
      id: json['id'] ?? '',
      userId: json['user_id'] ?? '',
      username: json['username'] ?? 'Aday',
      userAvatar: json['user_avatar'] ?? '🎓',
      userBadge: json['user_badge'] ?? '🎯 KPSS Adayı',
      category: PostCategoryExtension.fromCode(json['category'] ?? 'general'),
      title: json['title'] ?? '',
      content: json['content'] ?? '',
      timestamp: json['timestamp'] != null
          ? DateTime.tryParse(json['timestamp']) ?? DateTime.now()
          : DateTime.now(),
      likeCount: json['like_count'] ?? 0,
      likedUserIds: (json['liked_user_ids'] as List? ?? []).map((e) => e.toString()).toSet(),
      comments: (json['comments'] as List? ?? []).map((c) => CommentModel.fromJson(c)).toList(),
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'user_id': userId,
      'username': username,
      'user_avatar': userAvatar,
      'user_badge': userBadge,
      'category': category.codeName,
      'title': title,
      'content': content,
      'timestamp': timestamp.toIso8601String(),
      'like_count': likeCount,
      'liked_user_ids': likedUserIds.toList(),
      'comments': comments.map((c) => c.toJson()).toList(),
    };
  }
}
