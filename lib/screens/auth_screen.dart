import 'package:flutter/material.dart';
import '../services/auth_service.dart';

class AuthScreen extends StatefulWidget {
  const AuthScreen({super.key});

  @override
  State<AuthScreen> createState() => _AuthScreenState();
}

class _AuthScreenState extends State<AuthScreen> with SingleTickerProviderStateMixin {
  late TabController _tabController;
  final AuthService _auth = AuthService();

  // Register Controllers
  final TextEditingController _regNameCtrl = TextEditingController();
  final TextEditingController _regUsernameCtrl = TextEditingController();
  final TextEditingController _regEmailCtrl = TextEditingController();
  final TextEditingController _regPassCtrl = TextEditingController();
  String _selectedAvatar = '🎓';
  final double _targetScore = 90.0;

  // Login Controllers
  final TextEditingController _loginUserCtrl = TextEditingController();
  final TextEditingController _loginPassCtrl = TextEditingController();

  final List<String> _avatars = ['🎓', '🚀', '👑', '⚡', '🏆', '🌟', '📚', '🧠', '📜', '🎯', '🦉', '💡'];

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 2, vsync: this);
  }

  @override
  void dispose() {
    _regNameCtrl.dispose();
    _regUsernameCtrl.dispose();
    _regEmailCtrl.dispose();
    _regPassCtrl.dispose();
    _loginUserCtrl.dispose();
    _loginPassCtrl.dispose();
    _tabController.dispose();
    super.dispose();
  }

  void _handleRegister() async {
    if (_regNameCtrl.text.isEmpty || _regUsernameCtrl.text.isEmpty || _regEmailCtrl.text.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Lütfen tüm zorunlu alanları doldurun!')),
      );
      return;
    }

    await _auth.register(
      username: _regUsernameCtrl.text,
      displayName: _regNameCtrl.text,
      email: _regEmailCtrl.text,
      password: _regPassCtrl.text,
      targetScore: _targetScore,
      avatarUrl: _selectedAvatar,
    );

    if (mounted) Navigator.pop(context, true);
  }

  void _handleLogin() async {
    if (_loginUserCtrl.text.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Kullanıcı adı veya e-posta giriniz!')),
      );
      return;
    }

    await _auth.login(
      emailOrUsername: _loginUserCtrl.text,
      password: _loginPassCtrl.text,
    );

    if (mounted) Navigator.pop(context, true);
  }

  void _handleGoogleLogin() async {
    await _auth.loginWithGoogle();
    if (mounted) Navigator.pop(context, true);
  }

  void _handleAppleLogin() async {
    await _auth.loginWithApple();
    if (mounted) Navigator.pop(context, true);
  }

  @override
  Widget build(BuildContext context) {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final bgColor = isDark ? const Color(0xFF0F172A) : const Color(0xFFF1F5F9);
    final cardBgColor = isDark ? const Color(0xFF1E293B) : Colors.white;
    final textColor = isDark ? Colors.white : const Color(0xFF0F172A);
    final subTextColor = isDark ? Colors.white70 : const Color(0xFF64748B);

    return Scaffold(
      backgroundColor: bgColor,
      appBar: AppBar(
        title: Text('Kullanıcı Hesabı 👤', style: TextStyle(color: textColor, fontWeight: FontWeight.bold)),
        backgroundColor: Colors.transparent,
        elevation: 0,
        leading: IconButton(
          icon: Icon(Icons.arrow_back_ios_new_rounded, color: textColor),
          onPressed: () => Navigator.pop(context),
        ),
        bottom: TabBar(
          controller: _tabController,
          indicatorColor: const Color(0xFF00CEC9),
          labelColor: const Color(0xFF00CEC9),
          unselectedLabelColor: subTextColor,
          labelStyle: const TextStyle(fontWeight: FontWeight.bold, fontSize: 14),
          tabs: const [
            Tab(text: 'Giriş Yap'),
            Tab(text: 'Hesap Oluştur'),
          ],
        ),
      ),
      body: TabBarView(
        controller: _tabController,
        children: [
          // --- LOGIN TAB ---
          SingleChildScrollView(
            padding: const EdgeInsets.all(20),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text('KıPSS Hesabınıza Giriş Yapın 🔑', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Color(0xFF00CEC9))),
                const SizedBox(height: 6),
                Text('Toplulukta paylaşım yapmak, yorum yazmak ve verilerinizi korumak için giriş yapın.', style: TextStyle(color: subTextColor, fontSize: 13)),
                const SizedBox(height: 20),

                // SOCIAL LOGINS (Google & Apple)
                _buildSocialButtons(cardBgColor, textColor, isDark),

                const SizedBox(height: 20),
                Row(
                  children: [
                    Expanded(child: Divider(color: isDark ? Colors.white12 : Colors.grey.shade300)),
                    Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 12),
                      child: Text('veya e-posta ile', style: TextStyle(color: subTextColor, fontSize: 12)),
                    ),
                    Expanded(child: Divider(color: isDark ? Colors.white12 : Colors.grey.shade300)),
                  ],
                ),
                const SizedBox(height: 20),

                TextField(
                  controller: _loginUserCtrl,
                  style: TextStyle(color: textColor),
                  decoration: InputDecoration(
                    labelText: 'Kullanıcı Adı veya E-Posta',
                    labelStyle: TextStyle(color: subTextColor),
                    filled: true,
                    fillColor: cardBgColor,
                    border: OutlineInputBorder(borderRadius: BorderRadius.circular(14), borderSide: BorderSide.none),
                  ),
                ),
                const SizedBox(height: 14),
                TextField(
                  controller: _loginPassCtrl,
                  obscureText: true,
                  style: TextStyle(color: textColor),
                  decoration: InputDecoration(
                    labelText: 'Şifre',
                    labelStyle: TextStyle(color: subTextColor),
                    filled: true,
                    fillColor: cardBgColor,
                    border: OutlineInputBorder(borderRadius: BorderRadius.circular(14), borderSide: BorderSide.none),
                  ),
                ),
                const SizedBox(height: 20),
                SizedBox(
                  width: double.infinity,
                  height: 48,
                  child: ElevatedButton(
                    onPressed: _handleLogin,
                    style: ElevatedButton.styleFrom(
                      backgroundColor: const Color(0xFF00CEC9),
                      foregroundColor: const Color(0xFF0F172A),
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
                    ),
                    child: const Text('Giriş Yap', style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
                  ),
                ),
              ],
            ),
          ),

          // --- REGISTER TAB ---
          SingleChildScrollView(
            padding: const EdgeInsets.all(20),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text('Aramıza Katılın 🚀', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Color(0xFF00CEC9))),
                const SizedBox(height: 6),
                Text('KPSS adaylarıyla etkileşime geçmek için hemen profilinizi oluşturun.', style: TextStyle(color: subTextColor, fontSize: 13)),
                const SizedBox(height: 16),

                // SOCIAL LOGINS SHORTCUTS
                _buildSocialButtons(cardBgColor, textColor, isDark),

                const SizedBox(height: 16),
                Row(
                  children: [
                    Expanded(child: Divider(color: isDark ? Colors.white12 : Colors.grey.shade300)),
                    Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 12),
                      child: Text('veya profilinizi özelleştirin', style: TextStyle(color: subTextColor, fontSize: 12)),
                    ),
                    Expanded(child: Divider(color: isDark ? Colors.white12 : Colors.grey.shade300)),
                  ],
                ),
                const SizedBox(height: 16),

                // Avatar Picker (Overflow Fixed with Wrap!)
                Text('Avatar Seçin:', style: TextStyle(fontWeight: FontWeight.bold, color: textColor)),
                const SizedBox(height: 10),
                Wrap(
                  spacing: 10,
                  runSpacing: 10,
                  children: _avatars.map((av) {
                    final isSelected = _selectedAvatar == av;
                    return InkWell(
                      onTap: () => setState(() => _selectedAvatar = av),
                      borderRadius: BorderRadius.circular(30),
                      child: Container(
                        padding: const EdgeInsets.all(10),
                        decoration: BoxDecoration(
                          color: isSelected ? const Color(0xFF00CEC9).withValues(alpha: 0.25) : cardBgColor,
                          shape: BoxShape.circle,
                          border: Border.all(
                            color: isSelected ? const Color(0xFF00CEC9) : (isDark ? Colors.white10 : Colors.grey.shade300),
                            width: 2,
                          ),
                        ),
                        child: Text(av, style: const TextStyle(fontSize: 22)),
                      ),
                    );
                  }).toList(),
                ),
                const SizedBox(height: 18),

                TextField(
                  controller: _regNameCtrl,
                  style: TextStyle(color: textColor),
                  decoration: InputDecoration(
                    labelText: 'Ad Soyad',
                    labelStyle: TextStyle(color: subTextColor),
                    filled: true,
                    fillColor: cardBgColor,
                    border: OutlineInputBorder(borderRadius: BorderRadius.circular(14), borderSide: BorderSide.none),
                  ),
                ),
                const SizedBox(height: 12),
                TextField(
                  controller: _regUsernameCtrl,
                  style: TextStyle(color: textColor),
                  decoration: InputDecoration(
                    labelText: 'Kullanıcı Adı (@kpss_adayi)',
                    labelStyle: TextStyle(color: subTextColor),
                    filled: true,
                    fillColor: cardBgColor,
                    border: OutlineInputBorder(borderRadius: BorderRadius.circular(14), borderSide: BorderSide.none),
                  ),
                ),
                const SizedBox(height: 12),
                TextField(
                  controller: _regEmailCtrl,
                  keyboardType: TextInputType.emailAddress,
                  style: TextStyle(color: textColor),
                  decoration: InputDecoration(
                    labelText: 'E-Posta Adresi',
                    labelStyle: TextStyle(color: subTextColor),
                    filled: true,
                    fillColor: cardBgColor,
                    border: OutlineInputBorder(borderRadius: BorderRadius.circular(14), borderSide: BorderSide.none),
                  ),
                ),
                const SizedBox(height: 12),
                TextField(
                  controller: _regPassCtrl,
                  obscureText: true,
                  style: TextStyle(color: textColor),
                  decoration: InputDecoration(
                    labelText: 'Şifre',
                    labelStyle: TextStyle(color: subTextColor),
                    filled: true,
                    fillColor: cardBgColor,
                    border: OutlineInputBorder(borderRadius: BorderRadius.circular(14), borderSide: BorderSide.none),
                  ),
                ),
                const SizedBox(height: 20),

                SizedBox(
                  width: double.infinity,
                  height: 48,
                  child: ElevatedButton(
                    onPressed: _handleRegister,
                    style: ElevatedButton.styleFrom(
                      backgroundColor: const Color(0xFF00CEC9),
                      foregroundColor: const Color(0xFF0F172A),
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
                    ),
                    child: const Text('Hesabı Oluştur & Başla', style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildSocialButtons(Color cardBgColor, Color textColor, bool isDark) {
    return Column(
      children: [
        OutlinedButton.icon(
          onPressed: _handleGoogleLogin,
          style: OutlinedButton.styleFrom(
            backgroundColor: cardBgColor,
            side: BorderSide(color: isDark ? Colors.white24 : Colors.grey.shade300),
            padding: const EdgeInsets.symmetric(vertical: 12, horizontal: 16),
            minimumSize: const Size(double.infinity, 48),
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
          ),
          icon: Image.network(
            'https://lh3.googleusercontent.com/COxituaJu2vqBJOfVTdUKVmgZAgWAxeCyaCWXvxwqaWiXJSpfyux60-tTSO0wFVoTLqD=w300',
            width: 20,
            height: 20,
            errorBuilder: (ctx, e, st) => const Icon(Icons.g_mobiledata_rounded, color: Colors.redAccent, size: 24),
          ),
          label: Text(
            'Google ile Devam Et',
            style: TextStyle(color: textColor, fontWeight: FontWeight.bold, fontSize: 14),
          ),
        ),
        const SizedBox(height: 10),
        OutlinedButton.icon(
          onPressed: _handleAppleLogin,
          style: OutlinedButton.styleFrom(
            backgroundColor: isDark ? Colors.white : const Color(0xFF0F172A),
            foregroundColor: isDark ? const Color(0xFF0F172A) : Colors.white,
            padding: const EdgeInsets.symmetric(vertical: 12, horizontal: 16),
            minimumSize: const Size(double.infinity, 48),
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
          ),
          icon: Icon(Icons.apple_rounded, size: 22, color: isDark ? const Color(0xFF0F172A) : Colors.white),
          label: Text(
            'Apple ile Devam Et',
            style: TextStyle(color: isDark ? const Color(0xFF0F172A) : Colors.white, fontWeight: FontWeight.bold, fontSize: 14),
          ),
        ),
      ],
    );
  }
}
