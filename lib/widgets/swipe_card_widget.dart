import 'dart:math';
import 'package:flutter/material.dart';
import '../models/swipe_card_model.dart';
import '../screens/swipe_card_detail_modal.dart';

class SwipeCardWidget extends StatefulWidget {
  final SwipeCardModel card;
  final VoidCallback onSwipeDown;
  final VoidCallback onSwipeRight;
  final VoidCallback onSwipeLeft;

  const SwipeCardWidget({
    super.key,
    required this.card,
    required this.onSwipeDown,
    required this.onSwipeRight,
    required this.onSwipeLeft,
  });

  @override
  State<SwipeCardWidget> createState() => _SwipeCardWidgetState();
}

class _SwipeCardWidgetState extends State<SwipeCardWidget> with SingleTickerProviderStateMixin {
  late AnimationController _flipController;
  late Animation<double> _flipAnimation;
  bool _isFront = true;

  double _dragOffsetX = 0.0;
  double _dragOffsetY = 0.0;

  @override
  void initState() {
    super.initState();
    _flipController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 400),
    );
    _flipAnimation = Tween<double>(begin: 0, end: 1).animate(
      CurvedAnimation(parent: _flipController, curve: Curves.easeInOut),
    );
  }

  @override
  void didUpdateWidget(covariant SwipeCardWidget oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.card.id != widget.card.id) {
      _flipController.reset();
      _isFront = true;
      _dragOffsetX = 0.0;
      _dragOffsetY = 0.0;
    }
  }

  @override
  void dispose() {
    _flipController.dispose();
    super.dispose();
  }

  void _flipCard() {
    if (_isFront) {
      _flipController.forward();
    } else {
      _flipController.reverse();
    }
    setState(() {
      _isFront = !_isFront;
    });
  }

  void _openDetailModal() {
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) => SwipeCardDetailModal(
        card: widget.card,
        onReactionChanged: () => setState(() {}),
      ),
    ).then((_) => setState(() {}));
  }

  @override
  Widget build(BuildContext context) {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final cardBgColor = isDark ? const Color(0xFF1E293B) : Colors.white;
    final textColor = isDark ? Colors.white : const Color(0xFF0F172A);
    final subTextColor = isDark ? Colors.white70 : const Color(0xFF64748B);

    return GestureDetector(
      onTap: _flipCard,
      onPanUpdate: (details) {
        setState(() {
          _dragOffsetX += details.delta.dx;
          _dragOffsetY += details.delta.dy;
        });
      },
      onPanEnd: (details) {
        const double threshold = 70.0;

        if (_dragOffsetY > threshold && _dragOffsetY.abs() > _dragOffsetX.abs()) {
          // Swipe Down -> Random Card
          widget.onSwipeDown();
        } else if (_dragOffsetX > threshold && _dragOffsetX.abs() > _dragOffsetY.abs()) {
          // Swipe Right -> Same Course
          widget.onSwipeRight();
        } else if (_dragOffsetX < -threshold && _dragOffsetX.abs() > _dragOffsetY.abs()) {
          // Swipe Left -> Same Topic
          widget.onSwipeLeft();
        }

        setState(() {
          _dragOffsetX = 0.0;
          _dragOffsetY = 0.0;
        });
      },
      child: Transform.translate(
        offset: Offset(_dragOffsetX * 0.4, _dragOffsetY * 0.4),
        child: AnimatedBuilder(
          animation: _flipAnimation,
          builder: (context, child) {
            final angle = _flipAnimation.value * pi;
            final isUnder = (angle > pi / 2);

            return Transform(
              transform: Matrix4.identity()
                ..setEntry(3, 2, 0.001)
                ..rotateY(angle),
              alignment: Alignment.center,
              child: Container(
                width: double.infinity,
                margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                padding: const EdgeInsets.all(20),
                decoration: BoxDecoration(
                  color: cardBgColor,
                  borderRadius: BorderRadius.circular(28),
                  boxShadow: [
                    BoxShadow(
                      color: const Color(0xFF6C5CE7).withValues(alpha: isDark ? 0.25 : 0.12),
                      blurRadius: 20,
                      offset: const Offset(0, 8),
                    ),
                  ],
                  border: Border.all(
                    color: isDark ? const Color(0xFF6C5CE7).withValues(alpha: 0.3) : Colors.grey.shade200,
                    width: 1.5,
                  ),
                ),
                child: isUnder
                    ? Transform(
                        transform: Matrix4.identity()..rotateY(pi),
                        alignment: Alignment.center,
                        child: _buildBackContent(context, textColor, subTextColor, isDark),
                      )
                    : _buildFrontContent(context, textColor, subTextColor, isDark),
              ),
            );
          },
        ),
      ),
    );
  }

  Widget _buildFrontContent(BuildContext context, Color textColor, Color subTextColor, bool isDark) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // Top Badges (Overflow Fixed with Expanded!)
        Row(
          children: [
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
              decoration: BoxDecoration(
                gradient: const LinearGradient(
                  colors: [Color(0xFF6C5CE7), Color(0xFFA29BFE)],
                ),
                borderRadius: BorderRadius.circular(10),
              ),
              child: Text(
                widget.card.courseTitle,
                style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 11.5),
              ),
            ),
            const SizedBox(width: 8),
            Expanded(
              child: Container(
                padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
                decoration: BoxDecoration(
                  color: const Color(0xFF00CEC9).withValues(alpha: 0.15),
                  borderRadius: BorderRadius.circular(10),
                ),
                child: Text(
                  widget.card.topicTitle,
                  overflow: TextOverflow.ellipsis,
                  maxLines: 1,
                  style: const TextStyle(color: Color(0xFF00CEC9), fontWeight: FontWeight.w600, fontSize: 11.5),
                ),
              ),
            ),
          ],
        ),

        const SizedBox(height: 16),

        // Title
        Text(
          widget.card.cardTitle,
          style: TextStyle(
            color: textColor,
            fontSize: 19,
            fontWeight: FontWeight.bold,
          ),
        ),
        const SizedBox(height: 12),

        // Front Content Body Scrollable
        Expanded(
          child: SingleChildScrollView(
            child: Text(
              widget.card.frontContent,
              style: TextStyle(
                color: textColor.withValues(alpha: 0.9),
                fontSize: 15.5,
                height: 1.5,
                fontWeight: FontWeight.w400,
              ),
            ),
          ),
        ),

        const SizedBox(height: 8),

        // Tap to Flip Prompt
        Center(
          child: Container(
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 5),
            decoration: BoxDecoration(
              color: Colors.amber.withValues(alpha: 0.15),
              borderRadius: BorderRadius.circular(20),
            ),
            child: const Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                Icon(Icons.touch_app_rounded, size: 15, color: Colors.amber),
                SizedBox(width: 6),
                Text(
                  'Çözüm ve Detay İçin Karta Dokun 🔄',
                  style: TextStyle(color: Colors.amber, fontSize: 11.5, fontWeight: FontWeight.bold),
                ),
              ],
            ),
          ),
        ),

        const SizedBox(height: 12),
        Divider(color: isDark ? Colors.white12 : Colors.grey.shade200),
        const SizedBox(height: 4),

        // Action Bar (Like, Comment, Detail)
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceAround,
          children: [
            InkWell(
              onTap: () {
                setState(() {
                  widget.card.isLiked = !widget.card.isLiked;
                  if (widget.card.isLiked) {
                    widget.card.likeCount++;
                  } else {
                    widget.card.likeCount--;
                  }
                });
              },
              child: Row(
                children: [
                  Icon(
                    widget.card.isLiked ? Icons.favorite_rounded : Icons.favorite_border_rounded,
                    color: widget.card.isLiked ? Colors.redAccent : subTextColor,
                    size: 20,
                  ),
                  const SizedBox(width: 5),
                  Text(
                    '${widget.card.likeCount}',
                    style: TextStyle(
                      color: widget.card.isLiked ? Colors.redAccent : subTextColor,
                      fontWeight: FontWeight.bold,
                      fontSize: 12.5,
                    ),
                  ),
                ],
              ),
            ),
            InkWell(
              onTap: _openDetailModal,
              child: Row(
                children: [
                  Icon(Icons.chat_bubble_outline_rounded, color: subTextColor, size: 19),
                  const SizedBox(width: 5),
                  Text(
                    '${widget.card.comments.length} Yorum',
                    style: TextStyle(color: subTextColor, fontSize: 12.5, fontWeight: FontWeight.w600),
                  ),
                ],
              ),
            ),
            ElevatedButton.icon(
              onPressed: _openDetailModal,
              style: ElevatedButton.styleFrom(
                backgroundColor: const Color(0xFF6C5CE7),
                foregroundColor: Colors.white,
                padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
              ),
              icon: const Icon(Icons.open_in_full_rounded, size: 15),
              label: const Text('Detaylar', style: TextStyle(fontSize: 11.5, fontWeight: FontWeight.bold)),
            ),
          ],
        ),
      ],
    );
  }

  Widget _buildBackContent(BuildContext context, Color textColor, Color subTextColor, bool isDark) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          children: [
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
              decoration: BoxDecoration(
                color: const Color(0xFF00B894).withValues(alpha: 0.2),
                borderRadius: BorderRadius.circular(10),
              ),
              child: const Row(
                children: [
                  Icon(Icons.verified_rounded, color: Color(0xFF00B894), size: 15),
                  SizedBox(width: 6),
                  Text(
                    'Cevap & Çözüm Analizi',
                    style: TextStyle(color: Color(0xFF00B894), fontWeight: FontWeight.bold, fontSize: 11.5),
                  ),
                ],
              ),
            ),
            const Spacer(),
            IconButton(
              icon: const Icon(Icons.flip_to_front_rounded),
              onPressed: _flipCard,
              color: const Color(0xFF6C5CE7),
            ),
          ],
        ),
        const SizedBox(height: 14),
        Expanded(
          child: SingleChildScrollView(
            child: Text(
              widget.card.backContent,
              style: TextStyle(
                color: textColor,
                fontSize: 15,
                height: 1.5,
                fontWeight: FontWeight.w500,
              ),
            ),
          ),
        ),
        const SizedBox(height: 12),
        SizedBox(
          width: double.infinity,
          child: ElevatedButton.icon(
            onPressed: _openDetailModal,
            style: ElevatedButton.styleFrom(
              backgroundColor: const Color(0xFF00CEC9),
              foregroundColor: const Color(0xFF0F172A),
              padding: const EdgeInsets.symmetric(vertical: 10),
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
            ),
            icon: const Icon(Icons.forum_rounded, size: 18),
            label: const Text(
              'Tüm Notu Göster ve Yorum Yap',
              style: TextStyle(fontWeight: FontWeight.bold, fontSize: 13),
            ),
          ),
        ),
      ],
    );
  }
}
