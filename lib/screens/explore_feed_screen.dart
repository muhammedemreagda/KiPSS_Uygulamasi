import 'package:flutter/material.dart';
import '../models/post_model.dart';
import '../models/swipe_card_model.dart';
import '../services/community_service.dart';
import '../services/swipe_feed_service.dart';
import '../widgets/swipe_card_widget.dart';
import 'create_post_modal.dart';
import 'post_detail_screen.dart';

class ExploreFeedScreen extends StatefulWidget {
  const ExploreFeedScreen({super.key});

  @override
  State<ExploreFeedScreen> createState() => _ExploreFeedScreenState();
}

class _ExploreFeedScreenState extends State<ExploreFeedScreen> with SingleTickerProviderStateMixin {
  late TabController _tabController;
  final CommunityService _communityService = CommunityService();
  final SwipeFeedService _swipeService = SwipeFeedService();

  PostCategory? _selectedCategory;
  SwipeCardModel? _currentSwipeCard;
  String _lastSwipeMode = 'Rastgele 🎲';
  String _topNotificationBanner = '';

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 2, vsync: this);
    _tabController.addListener(_onTabChanged);
    _loadPosts();
    _loadInitialSwipeCard();
  }

  void _onTabChanged() {
    if (mounted) setState(() {});
  }

  @override
  void dispose() {
    _tabController.removeListener(_onTabChanged);
    _tabController.dispose();
    super.dispose();
  }

  Future<void> _loadPosts() async {
    await _communityService.loadPosts();
    if (mounted) setState(() {});
  }

  void _loadInitialSwipeCard() {
    _swipeService.initializeFeed();
    setState(() {
      _currentSwipeCard = _swipeService.getRandomCard();
      _lastSwipeMode = 'Rastgele 🎲';
    });
  }

  void _onSwipeDown() {
    if (_currentSwipeCard == null) return;
    final nextCard = _swipeService.getRandomCard(excludeId: _currentSwipeCard!.id);
    setState(() {
      _currentSwipeCard = nextCard;
      _lastSwipeMode = 'Rastgele Bilgi 🎲';
      _topNotificationBanner = '🎲 Rastgele Hap Bilgi Getirildi!';
    });
  }

  void _onSwipeRight() {
    if (_currentSwipeCard == null) return;
    final nextCard = _swipeService.getSameCourseCard(
      currentCourseId: _currentSwipeCard!.courseId,
      excludeId: _currentSwipeCard!.id,
    );
    setState(() {
      _currentSwipeCard = nextCard;
      _lastSwipeMode = 'Aynı Ders: ${_currentSwipeCard!.courseTitle} 📚';
      _topNotificationBanner = '📚 Aynı Ders (${_currentSwipeCard!.courseTitle}) Getirildi!';
    });
  }

  void _onSwipeLeft() {
    if (_currentSwipeCard == null) return;
    final nextCard = _swipeService.getSameTopicCard(
      currentTopicId: _currentSwipeCard!.topicId,
      excludeId: _currentSwipeCard!.id,
    );
    setState(() {
      _currentSwipeCard = nextCard;
      _lastSwipeMode = 'Aynı Konu: ${_currentSwipeCard!.topicTitle} 🎯';
      _topNotificationBanner = '🎯 Aynı Konu (${_currentSwipeCard!.topicTitle}) Getirildi!';
    });
  }

  void _openCreatePostModal() {
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) => const CreatePostModal(),
    ).then((updated) {
      if (updated == true && mounted) {
        setState(() {});
      }
    });
  }

  void _openPostDetail(PostModel post) {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => PostDetailScreen(post: post),
      ),
    ).then((_) => setState(() {}));
  }

  @override
  Widget build(BuildContext context) {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final bgColor = isDark ? const Color(0xFF0F172A) : const Color(0xFFF1F5F9);
    final cardBgColor = isDark ? const Color(0xFF1E293B) : Colors.white;
    final textColor = isDark ? Colors.white : const Color(0xFF0F172A);
    final subTextColor = isDark ? Colors.white60 : const Color(0xFF64748B);

    return Scaffold(
      backgroundColor: bgColor,
      appBar: AppBar(
        title: Text(
          'Keşfet & Akış 🌐',
          style: TextStyle(color: textColor, fontWeight: FontWeight.bold),
        ),
        bottom: TabBar(
          controller: _tabController,
          indicatorColor: const Color(0xFF00CEC9),
          labelColor: const Color(0xFF00CEC9),
          unselectedLabelColor: subTextColor,
          labelStyle: const TextStyle(fontWeight: FontWeight.bold, fontSize: 13.5),
          tabs: const [
            Tab(icon: Icon(Icons.touch_app_rounded, size: 20), text: '⚡ 3D Hap Bilgiler'),
            Tab(icon: Icon(Icons.forum_rounded, size: 20), text: '💬 Topluluk Gönderileri'),
          ],
        ),
      ),
      // FAB ONLY displays when Tab 2 (Topluluk Gönderileri) is active!
      floatingActionButton: _tabController.index == 1
          ? FloatingActionButton.extended(
              onPressed: _openCreatePostModal,
              backgroundColor: const Color(0xFF00CEC9),
              foregroundColor: const Color(0xFF0F172A),
              icon: const Icon(Icons.edit_note_rounded),
              label: const Text('Gönderi Paylaş', style: TextStyle(fontWeight: FontWeight.bold)),
            )
          : null,
      body: TabBarView(
        controller: _tabController,
        children: [
          // --- TAB 1: 3D MICRO-LEARNING SWIPE FEED ---
          _buildSwipeFeedTab(textColor, subTextColor, cardBgColor, isDark),

          // --- TAB 2: COMMUNITY POSTS FORUM ---
          _buildCommunityPostsTab(textColor, subTextColor, cardBgColor, isDark),
        ],
      ),
    );
  }

  Widget _buildSwipeFeedTab(Color textColor, Color subTextColor, Color cardBgColor, bool isDark) {
    return Column(
      children: [
        const SizedBox(height: 10),

        // Gestures Guide Bar (Clean & Responsive)
        Container(
          margin: const EdgeInsets.symmetric(horizontal: 16),
          padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
          decoration: BoxDecoration(
            color: cardBgColor,
            borderRadius: BorderRadius.circular(16),
            border: Border.all(color: isDark ? Colors.white.withValues(alpha: 0.08) : Colors.grey.shade200),
          ),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: [
              _buildGestureGuideItem('⬇️ Aşağı', 'Rastgele', () => _onSwipeDown()),
              Container(width: 1, height: 22, color: isDark ? Colors.white24 : Colors.grey.shade300),
              _buildGestureGuideItem('➡️ Sağa', 'Aynı Ders', () => _onSwipeRight()),
              Container(width: 1, height: 22, color: isDark ? Colors.white24 : Colors.grey.shade300),
              _buildGestureGuideItem('⬅️ Sola', 'Aynı Konu', () => _onSwipeLeft()),
            ],
          ),
        ),

        const SizedBox(height: 6),

        // Non-intrusive Top Animated Banner Status (Never blocks bottom buttons!)
        AnimatedContainer(
          duration: const Duration(milliseconds: 300),
          padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 5),
          decoration: BoxDecoration(
            color: const Color(0xFF6C5CE7).withValues(alpha: 0.12),
            borderRadius: BorderRadius.circular(14),
          ),
          child: Text(
            _topNotificationBanner.isNotEmpty ? _topNotificationBanner : 'Mod: $_lastSwipeMode',
            overflow: TextOverflow.ellipsis,
            style: const TextStyle(color: Color(0xFF6C5CE7), fontSize: 11.5, fontWeight: FontWeight.bold),
          ),
        ),

        const SizedBox(height: 6),

        // Micro-Learning Interactive 3D Card
        Expanded(
          child: _currentSwipeCard == null
              ? const Center(child: CircularProgressIndicator(color: Color(0xFF00CEC9)))
              : SwipeCardWidget(
                  card: _currentSwipeCard!,
                  onSwipeDown: _onSwipeDown,
                  onSwipeRight: _onSwipeRight,
                  onSwipeLeft: _onSwipeLeft,
                ),
        ),

        // Bottom Action Controls (100% Free of FAB or SnackBar Overlaps!)
        Padding(
          padding: const EdgeInsets.only(left: 16, right: 16, bottom: 16, top: 4),
          child: Row(
            children: [
              Expanded(
                child: OutlinedButton.icon(
                  onPressed: _onSwipeLeft,
                  style: OutlinedButton.styleFrom(
                    padding: const EdgeInsets.symmetric(vertical: 12),
                    side: const BorderSide(color: Color(0xFF6C5CE7)),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
                  ),
                  icon: const Icon(Icons.arrow_back_rounded, size: 16, color: Color(0xFF6C5CE7)),
                  label: FittedBox(
                    fit: BoxFit.scaleDown,
                    child: const Text('Aynı Konu', style: TextStyle(fontSize: 12.5, fontWeight: FontWeight.bold, color: Color(0xFF6C5CE7))),
                  ),
                ),
              ),
              const SizedBox(width: 8),
              ElevatedButton.icon(
                onPressed: _onSwipeDown,
                style: ElevatedButton.styleFrom(
                  backgroundColor: const Color(0xFF6C5CE7),
                  foregroundColor: Colors.white,
                  padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
                ),
                icon: const Icon(Icons.shuffle_rounded, size: 18),
                label: const Text('Rastgele', style: TextStyle(fontSize: 13, fontWeight: FontWeight.bold)),
              ),
              const SizedBox(width: 8),
              Expanded(
                child: OutlinedButton.icon(
                  onPressed: _onSwipeRight,
                  style: OutlinedButton.styleFrom(
                    padding: const EdgeInsets.symmetric(vertical: 12),
                    side: const BorderSide(color: Color(0xFF6C5CE7)),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
                  ),
                  icon: const Icon(Icons.arrow_forward_rounded, size: 16, color: Color(0xFF6C5CE7)),
                  label: FittedBox(
                    fit: BoxFit.scaleDown,
                    child: const Text('Aynı Ders', style: TextStyle(fontSize: 12.5, fontWeight: FontWeight.bold, color: Color(0xFF6C5CE7))),
                  ),
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }

  Widget _buildGestureGuideItem(String title, String subtitle, VoidCallback onTap) {
    return InkWell(
      onTap: onTap,
      borderRadius: BorderRadius.circular(10),
      child: Column(
        children: [
          Text(title, style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 12)),
          const SizedBox(height: 2),
          Text(subtitle, style: const TextStyle(color: Color(0xFF00CEC9), fontSize: 10.5, fontWeight: FontWeight.w600)),
        ],
      ),
    );
  }

  Widget _buildCommunityPostsTab(Color textColor, Color subTextColor, Color cardBgColor, bool isDark) {
    final filteredPosts = _communityService.getPostsByCategory(_selectedCategory);

    return Column(
      children: [
        // --- CATEGORY FILTER CHIPS ---
        SingleChildScrollView(
          scrollDirection: Axis.horizontal,
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
          child: Row(
            children: [
              ChoiceChip(
                label: const Text('Tüm Gönderiler'),
                selected: _selectedCategory == null,
                selectedColor: const Color(0xFF00CEC9),
                backgroundColor: cardBgColor,
                labelStyle: TextStyle(
                  color: _selectedCategory == null ? const Color(0xFF0F172A) : textColor,
                  fontWeight: _selectedCategory == null ? FontWeight.bold : FontWeight.normal,
                ),
                onSelected: (selected) {
                  if (selected) setState(() => _selectedCategory = null);
                },
              ),
              const SizedBox(width: 8),
              ...PostCategory.values.map((cat) {
                final isSelected = _selectedCategory == cat;
                return Padding(
                  padding: const EdgeInsets.only(right: 8.0),
                  child: ChoiceChip(
                    label: Text(cat.title),
                    selected: isSelected,
                    selectedColor: const Color(0xFF00CEC9),
                    backgroundColor: cardBgColor,
                    labelStyle: TextStyle(
                      color: isSelected ? const Color(0xFF0F172A) : textColor,
                      fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
                    ),
                    onSelected: (selected) {
                      if (selected) setState(() => _selectedCategory = cat);
                    },
                  ),
                );
              }),
            ],
          ),
        ),

        // --- POSTS LIST ---
        Expanded(
          child: !_communityService.isLoaded
              ? const Center(child: CircularProgressIndicator(color: Color(0xFF00CEC9)))
              : filteredPosts.isEmpty
                  ? Center(
                      child: Text(
                        'Bu kategoride henüz gönderi paylaşılmadı.\nİlk gönderiyi sen paylaş!',
                        textAlign: TextAlign.center,
                        style: TextStyle(color: subTextColor, fontSize: 14),
                      ),
                    )
                  : ListView.separated(
                      padding: const EdgeInsets.all(16),
                      itemCount: filteredPosts.length,
                      separatorBuilder: (ctx, i) => const SizedBox(height: 12),
                      itemBuilder: (ctx, index) {
                        final post = filteredPosts[index];

                        return InkWell(
                          onTap: () => _openPostDetail(post),
                          borderRadius: BorderRadius.circular(18),
                          child: Container(
                            padding: const EdgeInsets.all(16),
                            decoration: BoxDecoration(
                              color: cardBgColor,
                              borderRadius: BorderRadius.circular(18),
                              border: Border.all(color: isDark ? Colors.white.withValues(alpha: 0.05) : Colors.grey.shade200),
                            ),
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                // User Header
                                Row(
                                  children: [
                                    CircleAvatar(
                                      radius: 18,
                                      backgroundColor: const Color(0xFF00CEC9).withValues(alpha: 0.2),
                                      child: Text(post.userAvatar, style: const TextStyle(fontSize: 18)),
                                    ),
                                    const SizedBox(width: 10),
                                    Expanded(
                                      child: Column(
                                        crossAxisAlignment: CrossAxisAlignment.start,
                                        children: [
                                          Text(
                                            post.username,
                                            style: TextStyle(color: textColor, fontWeight: FontWeight.bold, fontSize: 14),
                                          ),
                                          Text(
                                            post.userBadge,
                                            style: const TextStyle(color: Color(0xFF00CEC9), fontSize: 10, fontWeight: FontWeight.w600),
                                          ),
                                        ],
                                      ),
                                    ),
                                    Container(
                                      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                                      decoration: BoxDecoration(
                                        color: const Color(0xFF00CEC9).withValues(alpha: 0.15),
                                        borderRadius: BorderRadius.circular(8),
                                      ),
                                      child: Text(
                                        post.category.title,
                                        style: const TextStyle(color: Color(0xFF00CEC9), fontSize: 10, fontWeight: FontWeight.bold),
                                      ),
                                    ),
                                  ],
                                ),
                                const SizedBox(height: 12),

                                // Title & Body
                                Text(
                                  post.title,
                                  style: TextStyle(color: textColor, fontSize: 16, fontWeight: FontWeight.bold),
                                ),
                                const SizedBox(height: 6),
                                Text(
                                  post.content,
                                  maxLines: 3,
                                  overflow: TextOverflow.ellipsis,
                                  style: TextStyle(color: subTextColor, fontSize: 13.5, height: 1.4),
                                ),
                                const SizedBox(height: 14),

                                // Footer Info Bar (Likes & Comments)
                                Row(
                                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                                  children: [
                                    Row(
                                      children: [
                                        IconButton(
                                          icon: const Icon(Icons.favorite_rounded, color: Colors.redAccent, size: 20),
                                          onPressed: () {
                                            setState(() {
                                              _communityService.toggleLike(post.id);
                                            });
                                          },
                                        ),
                                        Text(
                                          '${post.likeCount}',
                                          style: const TextStyle(color: Colors.redAccent, fontWeight: FontWeight.bold, fontSize: 13),
                                        ),
                                        const SizedBox(width: 16),
                                        Icon(Icons.chat_bubble_outline_rounded, color: subTextColor, size: 18),
                                        const SizedBox(width: 6),
                                        Text(
                                          '${post.comments.length} Yorum',
                                          style: TextStyle(color: subTextColor, fontSize: 12.5),
                                        ),
                                      ],
                                    ),
                                    const Icon(Icons.arrow_forward_ios_rounded, color: Color(0xFF00CEC9), size: 14),
                                  ],
                                )
                              ],
                            ),
                          ),
                        );
                      },
                    ),
        ),
      ],
    );
  }
}
