class UserModel {
  final String id;
  final String username;
  final String displayName;
  final String email;
  final double targetScore;
  final String examLevel; // 'lisans', 'onlisans', 'lise'
  final String badge;
  final String avatarUrl;
  final DateTime createdAt;

  UserModel({
    required this.id,
    required this.username,
    required this.displayName,
    required this.email,
    this.targetScore = 88.5,
    this.examLevel = 'lisans',
    this.badge = '🎯 KPSS Adayı',
    this.avatarUrl = '🎓',
    DateTime? createdAt,
  }) : createdAt = createdAt ?? DateTime.now();

  factory UserModel.fromJson(Map<String, dynamic> json) {
    return UserModel(
      id: json['id'] ?? '',
      username: json['username'] ?? 'kpss_adayi',
      displayName: json['display_name'] ?? 'KPSS Adayı',
      email: json['email'] ?? '',
      targetScore: (json['target_score'] as num?)?.toDouble() ?? 88.5,
      examLevel: json['exam_level'] ?? 'lisans',
      badge: json['badge'] ?? '🎯 KPSS Adayı',
      avatarUrl: json['avatar_url'] ?? '🎓',
      createdAt: json['created_at'] != null
          ? DateTime.tryParse(json['created_at']) ?? DateTime.now()
          : DateTime.now(),
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'username': username,
      'display_name': displayName,
      'email': email,
      'target_score': targetScore,
      'exam_level': examLevel,
      'badge': badge,
      'avatar_url': avatarUrl,
      'created_at': createdAt.toIso8601String(),
    };
  }

  UserModel copyWith({
    String? displayName,
    double? targetScore,
    String? examLevel,
    String? badge,
    String? avatarUrl,
  }) {
    return UserModel(
      id: id,
      username: username,
      displayName: displayName ?? this.displayName,
      email: email,
      targetScore: targetScore ?? this.targetScore,
      examLevel: examLevel ?? this.examLevel,
      badge: badge ?? this.badge,
      avatarUrl: avatarUrl ?? this.avatarUrl,
      createdAt: createdAt,
    );
  }
}
