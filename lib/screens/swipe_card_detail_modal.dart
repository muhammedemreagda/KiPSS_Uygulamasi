import 'package:flutter/material.dart';
import '../models/swipe_card_model.dart';
import '../models/post_model.dart';
import '../services/auth_service.dart';

class SwipeCardDetailModal extends StatefulWidget {
  final SwipeCardModel card;
  final VoidCallback onReactionChanged;

  const SwipeCardDetailModal({
    super.key,
    required this.card,
    required this.onReactionChanged,
  });

  @override
  State<SwipeCardDetailModal> createState() => _SwipeCardDetailModalState();
}

class _SwipeCardDetailModalState extends State<SwipeCardDetailModal> {
  final TextEditingController _commentController = TextEditingController();
  final AuthService _authService = AuthService();

  @override
  void dispose() {
    _commentController.dispose();
    super.dispose();
  }

  void _addComment() {
    final text = _commentController.text.trim();
    if (text.isEmpty) return;

    final user = _authService.currentUser;
    final newComment = CommentModel(
      id: 'c-${DateTime.now().millisecondsSinceEpoch}',
      postId: widget.card.id,
      userId: user?.id ?? 'guest',
      username: user?.username ?? 'KPSS Adayı',
      userAvatar: user?.avatarUrl ?? '👤',
      content: text,
      timestamp: DateTime.now(),
    );

    setState(() {
      widget.card.comments.add(newComment);
      _commentController.clear();
    });

    widget.onReactionChanged();
  }

  @override
  Widget build(BuildContext context) {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final bgColor = isDark ? const Color(0xFF0F172A) : Colors.white;
    final cardBgColor = isDark ? const Color(0xFF1E293B) : const Color(0xFFF8FAFC);
    final textColor = isDark ? Colors.white : const Color(0xFF0F172A);
    final subTextColor = isDark ? Colors.white60 : Colors.black54;

    final card = widget.card;

    return Container(
      height: MediaQuery.of(context).size.height * 0.88,
      decoration: BoxDecoration(
        color: bgColor,
        borderRadius: const BorderRadius.vertical(top: Radius.circular(28)),
      ),
      child: Column(
        children: [
          // Drag Handle
          const SizedBox(height: 12),
          Container(
            width: 48,
            height: 5,
            decoration: BoxDecoration(
              color: isDark ? Colors.white24 : Colors.grey.shade300,
              borderRadius: BorderRadius.circular(10),
            ),
          ),
          const SizedBox(height: 12),

          // Header Bar
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 20),
            child: Row(
              children: [
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
                  decoration: BoxDecoration(
                    color: const Color(0xFF6C5CE7).withValues(alpha: 0.15),
                    borderRadius: BorderRadius.circular(10),
                  ),
                  child: Text(
                    '${card.courseTitle} • ${card.topicTitle}',
                    style: const TextStyle(
                      color: Color(0xFF6C5CE7),
                      fontWeight: FontWeight.bold,
                      fontSize: 12,
                    ),
                  ),
                ),
                const Spacer(),
                IconButton(
                  icon: const Icon(Icons.close_rounded),
                  onPressed: () => Navigator.pop(context),
                  color: textColor,
                ),
              ],
            ),
          ),

          const Divider(height: 1),

          // Content Scroll View
          Expanded(
            child: ListView(
              padding: const EdgeInsets.all(20),
              children: [
                // Title
                Text(
                  card.cardTitle,
                  style: TextStyle(
                    color: textColor,
                    fontSize: 22,
                    fontWeight: FontWeight.bold,
                    height: 1.3,
                  ),
                ),
                const SizedBox(height: 16),

                // Question / Concept Box
                Container(
                  padding: const EdgeInsets.all(16),
                  decoration: BoxDecoration(
                    color: cardBgColor,
                    borderRadius: BorderRadius.circular(16),
                    border: Border.all(color: const Color(0xFF6C5CE7).withValues(alpha: 0.3)),
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const Row(
                        children: [
                          Icon(Icons.help_outline_rounded, color: Color(0xFF6C5CE7), size: 18),
                          SizedBox(width: 6),
                          Text(
                            'Soru / Konu Özeti',
                            style: TextStyle(color: Color(0xFF6C5CE7), fontWeight: FontWeight.bold, fontSize: 13),
                          ),
                        ],
                      ),
                      const SizedBox(height: 8),
                      Text(
                        card.frontContent,
                        style: TextStyle(color: textColor, fontSize: 15, height: 1.45, fontWeight: FontWeight.w500),
                      ),
                    ],
                  ),
                ),

                const SizedBox(height: 16),

                // Answer / Explanation Box
                Container(
                  padding: const EdgeInsets.all(16),
                  decoration: BoxDecoration(
                    color: const Color(0xFF00CEC9).withValues(alpha: 0.1),
                    borderRadius: BorderRadius.circular(16),
                    border: Border.all(color: const Color(0xFF00CEC9).withValues(alpha: 0.3)),
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const Row(
                        children: [
                          Icon(Icons.check_circle_outline_rounded, color: Color(0xFF00B894), size: 18),
                          SizedBox(width: 6),
                          Text(
                            'Çözüm / Önemli Not',
                            style: TextStyle(color: Color(0xFF00B894), fontWeight: FontWeight.bold, fontSize: 13),
                          ),
                        ],
                      ),
                      const SizedBox(height: 8),
                      Text(
                        card.backContent,
                        style: TextStyle(color: textColor, fontSize: 14.5, height: 1.45),
                      ),
                    ],
                  ),
                ),

                if (card.keyPoints.isNotEmpty) ...[
                  const SizedBox(height: 20),
                  Text(
                    '📌 Anahtar İpuçları (Sınavlık Kısımlar)',
                    style: TextStyle(color: textColor, fontSize: 16, fontWeight: FontWeight.bold),
                  ),
                  const SizedBox(height: 10),
                  ...card.keyPoints.map((kp) => Container(
                        margin: const EdgeInsets.only(bottom: 8),
                        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
                        decoration: BoxDecoration(
                          color: cardBgColor,
                          borderRadius: BorderRadius.circular(12),
                        ),
                        child: Row(
                          children: [
                            const Icon(Icons.star_rounded, color: Colors.amber, size: 18),
                            const SizedBox(width: 10),
                            Expanded(
                              child: Text(
                                kp,
                                style: TextStyle(color: textColor, fontSize: 13.5, fontWeight: FontWeight.w500),
                              ),
                            ),
                          ],
                        ),
                      )),
                ],

                const SizedBox(height: 24),
                Row(
                  children: [
                    const Icon(Icons.forum_rounded, color: Color(0xFF00CEC9), size: 20),
                    const SizedBox(width: 8),
                    Text(
                      'Topluluk Yorumları (${card.comments.length})',
                      style: TextStyle(color: textColor, fontSize: 17, fontWeight: FontWeight.bold),
                    ),
                  ],
                ),
                const SizedBox(height: 12),

                if (card.comments.isEmpty)
                  Padding(
                    padding: const EdgeInsets.symmetric(vertical: 16),
                    child: Text(
                      'Henüz yorum yapılmamış. İlk yorumu sen yaz!',
                      style: TextStyle(color: subTextColor, fontStyle: FontStyle.italic),
                    ),
                  )
                else
                  ...card.comments.map((c) => Container(
                        margin: const EdgeInsets.only(bottom: 10),
                        padding: const EdgeInsets.all(12),
                        decoration: BoxDecoration(
                          color: cardBgColor,
                          borderRadius: BorderRadius.circular(14),
                        ),
                        child: Row(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            CircleAvatar(
                              radius: 16,
                              backgroundColor: const Color(0xFF00CEC9).withValues(alpha: 0.2),
                              child: Text(c.userAvatar, style: const TextStyle(fontSize: 16)),
                            ),
                            const SizedBox(width: 10),
                            Expanded(
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Text(
                                    c.username,
                                    style: TextStyle(color: textColor, fontWeight: FontWeight.bold, fontSize: 13),
                                  ),
                                  const SizedBox(height: 2),
                                  Text(
                                    c.content,
                                    style: TextStyle(color: textColor.withValues(alpha: 0.9), fontSize: 13),
                                  ),
                                ],
                              ),
                            ),
                          ],
                        ),
                      )),

                const SizedBox(height: 80), // Extra scroll spacing for input keyboard
              ],
            ),
          ),

          // Bottom Comment Bar Input
          Container(
            padding: EdgeInsets.only(
              left: 16,
              right: 16,
              top: 10,
              bottom: MediaQuery.of(context).viewInsets.bottom + 12,
            ),
            decoration: BoxDecoration(
              color: isDark ? const Color(0xFF1E293B) : Colors.white,
              boxShadow: [
                BoxShadow(
                  color: Colors.black.withValues(alpha: 0.08),
                  blurRadius: 10,
                  offset: const Offset(0, -3),
                ),
              ],
            ),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _commentController,
                    decoration: InputDecoration(
                      hintText: 'Düşünceni veya cevabını yaz...',
                      hintStyle: TextStyle(color: subTextColor, fontSize: 13.5),
                      filled: true,
                      fillColor: isDark ? const Color(0xFF0F172A) : const Color(0xFFF1F5F9),
                      contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(24),
                        borderSide: BorderSide.none,
                      ),
                    ),
                    style: TextStyle(color: textColor, fontSize: 14),
                  ),
                ),
                const SizedBox(width: 10),
                IconButton(
                  onPressed: _addComment,
                  icon: const Icon(Icons.send_rounded),
                  color: const Color(0xFF00CEC9),
                  style: IconButton.styleFrom(
                    backgroundColor: const Color(0xFF00CEC9).withValues(alpha: 0.15),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
