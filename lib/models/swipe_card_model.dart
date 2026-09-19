import 'post_model.dart';

class SwipeCardModel {
  final String id;
  final String courseId;
  final String courseTitle;
  final String topicId;
  final String topicTitle;
  final String cardTitle;
  final String frontContent;
  final String backContent;
  final String fullSummary;
  final List<String> keyPoints;
  int likeCount;
  bool isLiked;
  String? userReaction;
  List<CommentModel> comments;

  SwipeCardModel({
    required this.id,
    required this.courseId,
    required this.courseTitle,
    required this.topicId,
    required this.topicTitle,
    required this.cardTitle,
    required this.frontContent,
    required this.backContent,
    required this.fullSummary,
    required this.keyPoints,
    this.likeCount = 0,
    this.isLiked = false,
    this.userReaction,
    List<CommentModel>? comments,
  }) : comments = comments ?? [];
}
