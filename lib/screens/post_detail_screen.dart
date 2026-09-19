import 'package:flutter/material.dart';
import '../models/post_model.dart';
import '../services/community_service.dart';

class PostDetailScreen extends StatefulWidget {
  final PostModel post;
  const PostDetailScreen({super.key, required this.post});

  @override
  State<PostDetailScreen> createState() => _PostDetailScreenState();
}

class _PostDetailScreenState extends State<PostDetailScreen> {
  final CommunityService _communityService = CommunityService();
  final TextEditingController _commentController = TextEditingController();

  void _submitComment() {
    final text = _commentController.text.trim();
    if (text.isEmpty) return;

    setState(() {
      _communityService.addComment(widget.post.id, text);
      _commentController.clear();
    });
    FocusScope.of(context).unfocus();
  }

  void _toggleLike() {
    setState(() {
      _communityService.toggleLike(widget.post.id);
    });
  }

  @override
  Widget build(BuildContext context) {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final bgColor = isDark ? const Color(0xFF0F172A) : const Color(0xFFF1F5F9);
    final cardBgColor = isDark ? const Color(0xFF1E293B) : Colors.white;
    final textColor = isDark ? Colors.white : const Color(0xFF0F172A);
    final subTextColor = isDark ? Colors.white60 : Colors.black54;

    final post = widget.post;

    return Scaffold(
      backgroundColor: bgColor,
      appBar: AppBar(
        title: Text(post.category.title, style: TextStyle(color: textColor, fontWeight: FontWeight.bold)),
      ),
      body: Column(
        children: [
          Expanded(
            child: SingleChildScrollView(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // --- POST HEADER ---
                  Row(
                    children: [
                      CircleAvatar(
                        radius: 20,
                        backgroundColor: const Color(0xFF00CEC9).withValues(alpha: 0.2),
                        child: Text(post.userAvatar, style: const TextStyle(fontSize: 20)),
                      ),
                      const SizedBox(width: 12),
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(post.username, style: TextStyle(color: textColor, fontWeight: FontWeight.bold, fontSize: 15)),
                            const SizedBox(height: 2),
                            Text(post.userBadge, style: const TextStyle(color: Color(0xFF00CEC9), fontSize: 11, fontWeight: FontWeight.w600)),
                          ],
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 16),

                  // --- POST TITLE & CONTENT ---
                  Text(post.title, style: TextStyle(color: textColor, fontSize: 18, fontWeight: FontWeight.bold)),
                  const SizedBox(height: 10),
                  Text(post.content, style: TextStyle(color: textColor, fontSize: 15, height: 1.5)),
                  const SizedBox(height: 16),

                  // --- LIKE & COMMENT STATS BAR ---
                  Row(
                    children: [
                      InkWell(
                        onTap: _toggleLike,
                        borderRadius: BorderRadius.circular(10),
                        child: Container(
                          padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                          decoration: BoxDecoration(
                            color: const Color(0xFF00CEC9).withValues(alpha: 0.15),
                            borderRadius: BorderRadius.circular(10),
                          ),
                          child: Row(
                            children: [
                              const Icon(Icons.favorite_rounded, color: Colors.redAccent, size: 18),
                              const SizedBox(width: 6),
                              Text('${post.likeCount} Beğeni', style: const TextStyle(color: Colors.redAccent, fontWeight: FontWeight.bold, fontSize: 13)),
                            ],
                          ),
                        ),
                      ),
                      const SizedBox(width: 16),
                      Row(
                        children: [
                          Icon(Icons.chat_bubble_outline_rounded, color: subTextColor, size: 18),
                          const SizedBox(width: 6),
                          Text('${post.comments.length} Yorum', style: TextStyle(color: subTextColor, fontSize: 13, fontWeight: FontWeight.bold)),
                        ],
                      ),
                    ],
                  ),
                  const Divider(height: 32),

                  // --- COMMENTS SECTION ---
                  Text('Yorumlar ve Çözümler (${post.comments.length})', style: TextStyle(color: textColor, fontSize: 16, fontWeight: FontWeight.bold)),
                  const SizedBox(height: 12),

                  if (post.comments.isEmpty)
                    Padding(
                      padding: const EdgeInsets.symmetric(vertical: 20),
                      child: Center(
                        child: Text('Henüz yorum yapılmadı.\nİlk yanıtı veya çözümü sen yaz!', textAlign: TextAlign.center, style: TextStyle(color: subTextColor)),
                      ),
                    )
                  else
                    ...post.comments.map((c) {
                      return Container(
                        margin: const EdgeInsets.only(bottom: 12),
                        padding: const EdgeInsets.all(14),
                        decoration: BoxDecoration(
                          color: c.isBestSolution ? Colors.green.withValues(alpha: 0.12) : cardBgColor,
                          borderRadius: BorderRadius.circular(14),
                          border: Border.all(color: c.isBestSolution ? Colors.green : isDark ? Colors.white10 : Colors.grey.shade300),
                        ),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Row(
                              mainAxisAlignment: MainAxisAlignment.spaceBetween,
                              children: [
                                Row(
                                  children: [
                                    CircleAvatar(
                                      radius: 14,
                                      backgroundColor: Colors.grey.withValues(alpha: 0.2),
                                      child: Text(c.userAvatar, style: const TextStyle(fontSize: 14)),
                                    ),
                                    const SizedBox(width: 8),
                                    Text(c.username, style: TextStyle(color: textColor, fontWeight: FontWeight.bold, fontSize: 13)),
                                  ],
                                ),
                                if (c.isBestSolution)
                                  Container(
                                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                                    decoration: BoxDecoration(
                                      color: Colors.green,
                                      borderRadius: BorderRadius.circular(8),
                                    ),
                                    child: const Text('En İyi Çözüm ✅', style: TextStyle(color: Colors.white, fontSize: 10, fontWeight: FontWeight.bold)),
                                  )
                              ],
                            ),
                            const SizedBox(height: 8),
                            Text(c.content, style: TextStyle(color: textColor, fontSize: 13.5, height: 1.4)),
                            if (post.category == PostCategory.question && !c.isBestSolution) ...[
                              const SizedBox(height: 6),
                              Align(
                                alignment: Alignment.centerRight,
                                child: TextButton(
                                  onPressed: () {
                                    setState(() {
                                      _communityService.markBestSolution(post.id, c.id);
                                    });
                                  },
                                  child: const Text('En İyi Çözüm Olarak İşaretle', style: TextStyle(color: Color(0xFF00CEC9), fontSize: 11, fontWeight: FontWeight.bold)),
                                ),
                              ),
                            ]
                          ],
                        ),
                      );
                    }),
                ],
              ),
            ),
          ),

          // --- COMMENT INPUT BOX ---
          Container(
            padding: const EdgeInsets.all(12),
            color: cardBgColor,
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _commentController,
                    style: TextStyle(color: textColor),
                    decoration: InputDecoration(
                      hintText: 'Yorumunuzu veya çözümünüzü yazın...',
                      hintStyle: TextStyle(color: subTextColor, fontSize: 13),
                      border: OutlineInputBorder(borderRadius: BorderRadius.circular(16)),
                      contentPadding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
                    ),
                  ),
                ),
                const SizedBox(width: 8),
                IconButton(
                  icon: const Icon(Icons.send_rounded, color: Color(0xFF00CEC9)),
                  onPressed: _submitComment,
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
