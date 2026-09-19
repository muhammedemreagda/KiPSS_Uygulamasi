import 'dart:convert';
import 'dart:io';
import 'dart:math';
import 'package:flutter/foundation.dart';
import '../models/post_model.dart';
import 'auth_service.dart';

class CommunityService {
  static final CommunityService _instance = CommunityService._internal();
  factory CommunityService() => _instance;
  CommunityService._internal();

  List<PostModel> posts = [];
  bool isLoaded = false;
  final AuthService _auth = AuthService();

  File? _getPostsFile() {
    try {
      if (kIsWeb) return null;
      return File('kpss_community_posts.json');
    } catch (_) {
      return null;
    }
  }

  Future<void> loadPosts() async {
    if (isLoaded) return;
    try {
      final file = _getPostsFile();
      if (file != null && await file.exists()) {
        final jsonStr = await file.readAsString();
        if (jsonStr.trim().isNotEmpty) {
          final List dataList = jsonDecode(jsonStr);
          posts = dataList.map((e) => PostModel.fromJson(e)).toList();
          isLoaded = true;
          return;
        }
      }
      _initDemoPosts();
      isLoaded = true;
    } catch (e) {
      debugPrint('Error loading community posts: $e');
      _initDemoPosts();
      isLoaded = true;
    }
  }

  void _initDemoPosts() {
    posts = [
      PostModel(
        id: 'post-1',
        userId: 'user-tarih-1',
        username: 'tarih_hocasi_99',
        userAvatar: '👑',
        userBadge: '🔥 Tarih Derecesi',
        category: PostCategory.question,
        title: 'Tarih Sorusu: Mondros sonrası ilk işgal edilen toprak?',
        content: 'Arkadaşlar selam! Mondros Ateşkes Antlaşması imzalandıktan hemen sonra işgal edilen ilk Osmanlı toprağı neresidir? Karıştıranlar için açıklayabilir misiniz?',
        timestamp: DateTime.now().subtract(const Duration(hours: 2)),
        likeCount: 24,
        likedUserIds: {'user-demo-1'},
        comments: [
          CommentModel(
            id: 'c-1',
            postId: 'post-1',
            userId: 'user-tarih-pro',
            username: 'Mustafa Hoca',
            userAvatar: '🎓',
            content: 'Doğru cevap MUSUL\'dur arkadaşlar. İngilizler 3 Kasım 1918\'de 7. maddeye dayanarak Musul\'u işgal etmiştir. Anadolu\'da ilk işgal edilen yer ise İskenderun\'dur!',
            isBestSolution: true,
          ),
          CommentModel(
            id: 'c-2',
            postId: 'post-1',
            userId: 'user-2',
            username: 'Zeynep_Kpss',
            userAvatar: '📚',
            content: 'Harika bir soru, Anadolu ile Genel Osmanlı ayrımına dikkat etmek lazım!',
          ),
        ],
      ),
      PostModel(
        id: 'post-2',
        userId: 'user-mat-1',
        username: 'matematik_kodlama',
        userAvatar: '🚀',
        userBadge: '⚡ Matematik Canavarı',
        category: PostCategory.flashcard,
        title: 'EBOB-EKOK Süper Kısayol Formülü! 💡',
        content: 'İki pozitif tam sayının çarpımı, bu sayıların EBOB\'u ile EKOK\'unun çarpımına eşittir!\n\n📌 Formül: a x b = EBOB(a,b) x EKOK(a,b)\n\nProblemlerde doğrudan zaman kazandırır, kaydetmeyi unutmayın!',
        timestamp: DateTime.now().subtract(const Duration(hours: 5)),
        likeCount: 42,
        likedUserIds: {'user-demo-1'},
        comments: [
          CommentModel(
            id: 'c-3',
            postId: 'post-2',
            userId: 'user-3',
            username: 'Emre_Lisans',
            userAvatar: '🏆',
            content: 'Geçen seneki sınavda tam da bu kuralı kullanarak 30 saniyede çözmüştüm!',
          ),
        ],
      ),
      PostModel(
        id: 'post-3',
        userId: 'user-demo-1',
        username: 'kpss_derece_adayi',
        userAvatar: '🎓',
        userBadge: '🔥 90+ Hedefli',
        category: PostCategory.netScore,
        title: 'Bugünkü Tam Deneme Netim: 89.25 Net! 🎯',
        content: 'Türkçe: 27.5 Net | Mat: 25 Net | Tarih: 22 Net | Coğ: 14.75 Net.\nSon 2 ay kala hedefim 93 Net\'i aşmak! Pes etmek yok, çalışmaya devam!',
        timestamp: DateTime.now().subtract(const Duration(hours: 8)),
        likeCount: 56,
        comments: [
          CommentModel(
            id: 'c-4',
            postId: 'post-3',
            userId: 'user-4',
            username: 'Selin_Onlisans',
            userAvatar: '🌟',
            content: 'Tebrikler! Matematikte kalan 5 net için hangi konulara ağırlık veriyorsun?',
          ),
        ],
      ),
    ];
    savePosts();
  }

  Future<void> savePosts() async {
    try {
      final file = _getPostsFile();
      if (file == null) return;
      final jsonStr = jsonEncode(posts.map((p) => p.toJson()).toList());
      await file.writeAsString(jsonStr);
    } catch (e) {
      debugPrint('Error saving posts: $e');
    }
  }

  List<PostModel> getPostsByCategory(PostCategory? category) {
    if (category == null) return posts;
    return posts.where((p) => p.category == category).toList();
  }

  void createPost({
    required String title,
    required String content,
    required PostCategory category,
  }) {
    final user = _auth.currentUser;
    final newPost = PostModel(
      id: 'post-${DateTime.now().millisecondsSinceEpoch}',
      userId: user?.id ?? 'user-guest',
      username: user?.username ?? 'Anonim Aday',
      userAvatar: user?.avatarUrl ?? '🎓',
      userBadge: user?.badge ?? '🎯 KPSS Adayı',
      category: category,
      title: title,
      content: content,
    );
    posts.insert(0, newPost); // Newest first
    savePosts();
  }

  void toggleLike(String postId) {
    final user = _auth.currentUser;
    final userId = user?.id ?? 'user-demo-1';
    final post = posts.firstWhere((p) => p.id == postId, orElse: () => posts.first);

    if (post.likedUserIds.contains(userId)) {
      post.likedUserIds.remove(userId);
      post.likeCount = max(0, post.likeCount - 1);
    } else {
      post.likedUserIds.add(userId);
      post.likeCount++;
    }
    savePosts();
  }

  void addComment(String postId, String commentContent) {
    final user = _auth.currentUser;
    final post = posts.firstWhere((p) => p.id == postId, orElse: () => posts.first);

    final comment = CommentModel(
      id: 'c-${DateTime.now().millisecondsSinceEpoch}',
      postId: postId,
      userId: user?.id ?? 'user-demo-1',
      username: user?.displayName ?? 'KPSS Adayı',
      userAvatar: user?.avatarUrl ?? '🎓',
      content: commentContent,
    );
    post.comments.add(comment);
    savePosts();
  }

  void markBestSolution(String postId, String commentId) {
    final post = posts.firstWhere((p) => p.id == postId, orElse: () => posts.first);
    for (var c in post.comments) {
      c.isBestSolution = (c.id == commentId);
    }
    savePosts();
  }
}
