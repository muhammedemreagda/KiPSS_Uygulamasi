import 'package:flutter/material.dart';
import '../models/post_model.dart';
import '../services/auth_service.dart';
import '../services/community_service.dart';
import '../services/data_service.dart';
import 'auth_screen.dart';

class ProfileScreen extends StatefulWidget {
  const ProfileScreen({super.key});

  @override
  State<ProfileScreen> createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
  final AuthService _auth = AuthService();
  final DataService _dataService = DataService();
  final CommunityService _communityService = CommunityService();

  void _openAuthScreen() {
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => const AuthScreen()),
    ).then((_) => setState(() {}));
  }

  @override
  Widget build(BuildContext context) {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final bgColor = isDark ? const Color(0xFF0F172A) : const Color(0xFFF1F5F9);
    final cardBgColor = isDark ? const Color(0xFF1E293B) : Colors.white;
    final textColor = isDark ? Colors.white : const Color(0xFF0F172A);
    final subTextColor = isDark ? Colors.white60 : Colors.black54;

    final user = _auth.currentUser;

    if (user == null) {
      return Scaffold(
        backgroundColor: bgColor,
        appBar: AppBar(title: Text('Profilim 👤', style: TextStyle(color: textColor, fontWeight: FontWeight.bold))),
        body: Center(
          child: Padding(
            padding: const EdgeInsets.all(24),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Icon(Icons.account_circle_outlined, size: 80, color: Color(0xFF00CEC9)),
                const SizedBox(height: 16),
                Text('Kullanıcı Hesabı Bulunamadı', style: TextStyle(color: textColor, fontSize: 18, fontWeight: FontWeight.bold)),
                const SizedBox(height: 8),
                Text('Toplulukta paylaşım yapmak, yorum yazmak ve verilerinizi yedeklemek için hesap açın.', textAlign: TextAlign.center, style: TextStyle(color: subTextColor, fontSize: 13)),
                const SizedBox(height: 24),
                ElevatedButton.icon(
                  onPressed: _openAuthScreen,
                  icon: const Icon(Icons.login_rounded),
                  label: const Text('Giriş Yap / Kayıt Ol', style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: const Color(0xFF00CEC9),
                    foregroundColor: const Color(0xFF0F172A),
                    padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 14),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
                  ),
                ),
              ],
            ),
          ),
        ),
      );
    }

    final userPosts = _communityService.posts.where((p) => p.userId == user.id || p.username == user.username).toList();

    return Scaffold(
      backgroundColor: bgColor,
      appBar: AppBar(
        title: Text('Profilim 👤', style: TextStyle(color: textColor, fontWeight: FontWeight.bold)),
        actions: [
          IconButton(
            icon: const Icon(Icons.logout_rounded, color: Colors.redAccent),
            tooltip: 'Çıkış Yap',
            onPressed: () {
              _auth.logout();
              setState(() {});
            },
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // --- USER CARD ---
            Container(
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                gradient: const LinearGradient(
                  colors: [Color(0xFF0F2027), Color(0xFF203A43), Color(0xFF2C5364)],
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                ),
                borderRadius: BorderRadius.circular(24),
                border: Border.all(color: const Color(0xFF00CEC9).withValues(alpha: 0.3)),
              ),
              child: Row(
                children: [
                  CircleAvatar(
                    radius: 32,
                    backgroundColor: const Color(0xFF00CEC9).withValues(alpha: 0.2),
                    child: Text(user.avatarUrl, style: const TextStyle(fontSize: 32)),
                  ),
                  const SizedBox(width: 16),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(user.displayName, style: const TextStyle(color: Colors.white, fontSize: 20, fontWeight: FontWeight.bold)),
                        const SizedBox(height: 2),
                        Text('@${user.username}', style: const TextStyle(color: Colors.white70, fontSize: 13)),
                        const SizedBox(height: 8),
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                          decoration: BoxDecoration(
                            color: const Color(0xFF00CEC9).withValues(alpha: 0.2),
                            borderRadius: BorderRadius.circular(10),
                            border: Border.all(color: const Color(0xFF00CEC9)),
                          ),
                          child: Text(user.badge, style: const TextStyle(color: Color(0xFF00CEC9), fontSize: 11, fontWeight: FontWeight.bold)),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 16),

            // --- STATS ROW ---
            Row(
              children: [
                _buildStatBox('Tahmini Net', _dataService.userCurrentNetScore.toStringAsFixed(1), Icons.bar_chart_rounded, cardBgColor, textColor, subTextColor),
                const SizedBox(width: 10),
                _buildStatBox('Hedef Puan', '${_dataService.targetScore}', Icons.flag_rounded, cardBgColor, textColor, subTextColor),
                const SizedBox(width: 10),
                _buildStatBox('Paylaşım', '${userPosts.length}', Icons.chat_rounded, cardBgColor, textColor, subTextColor),
              ],
            ),
            const SizedBox(height: 24),

            // --- USER POSTS SECTION ---
            Text('Paylaşımlarım (${userPosts.length})', style: TextStyle(color: textColor, fontSize: 18, fontWeight: FontWeight.bold)),
            const SizedBox(height: 12),

            if (userPosts.isEmpty)
              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(24),
                decoration: BoxDecoration(color: cardBgColor, borderRadius: BorderRadius.circular(16)),
                child: Center(
                  child: Text('Henüz toplulukta gönderi paylaşmadınız.\n"Keşfet" alanından soru sorabilir veya not paylaşabilirsiniz!', textAlign: TextAlign.center, style: TextStyle(color: subTextColor)),
                ),
              )
            else
              ...userPosts.map((p) {
                return Container(
                  margin: const EdgeInsets.only(bottom: 10),
                  padding: const EdgeInsets.all(14),
                  decoration: BoxDecoration(color: cardBgColor, borderRadius: BorderRadius.circular(14)),
                  child: Row(
                    children: [
                      Text(p.category.title.split(' ').first, style: const TextStyle(fontSize: 20)),
                      const SizedBox(width: 12),
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(p.title, style: TextStyle(color: textColor, fontWeight: FontWeight.bold, fontSize: 14)),
                            Text('${p.likeCount} Beğeni • ${p.comments.length} Yorum', style: TextStyle(color: subTextColor, fontSize: 11)),
                          ],
                        ),
                      ),
                    ],
                  ),
                );
              }),
          ],
        ),
      ),
    );
  }

  Widget _buildStatBox(String label, String value, IconData icon, Color cardBg, Color textClr, Color subClr) {
    return Expanded(
      child: Container(
        padding: const EdgeInsets.all(14),
        decoration: BoxDecoration(color: cardBg, borderRadius: BorderRadius.circular(16)),
        child: Column(
          children: [
            Icon(icon, color: const Color(0xFF00CEC9), size: 22),
            const SizedBox(height: 6),
            Text(value, style: TextStyle(color: textClr, fontSize: 18, fontWeight: FontWeight.bold)),
            const SizedBox(height: 2),
            Text(label, style: TextStyle(color: subClr, fontSize: 11)),
          ],
        ),
      ),
    );
  }
}
