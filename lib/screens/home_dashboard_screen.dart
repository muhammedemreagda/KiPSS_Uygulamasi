import 'dart:async';
import 'package:flutter/material.dart';
import '../services/data_service.dart';
import '../services/auth_service.dart';
import '../services/kpss_countdown_service.dart';
import '../models/kpss_models.dart';
import '../theme/app_theme.dart';
import 'course_detail_screen.dart';
import 'exam_setup_modal.dart';
import 'score_calculator_screen.dart';
import 'exam_history_screen.dart';
import 'saved_questions_screen.dart';
import 'explore_feed_screen.dart';
import 'profile_screen.dart';

class HomeDashboardScreen extends StatefulWidget {
  const HomeDashboardScreen({super.key});

  @override
  State<HomeDashboardScreen> createState() => _HomeDashboardScreenState();
}

class _HomeDashboardScreenState extends State<HomeDashboardScreen> {
  final DataService _dataService = DataService();
  final AuthService _auth = AuthService();
  int _currentTabIndex = 0;
  Timer? _timer;

  @override
  void initState() {
    super.initState();
    _loadData();

    // Live 1-second timer ticker for second-accurate countdown
    _timer = Timer.periodic(const Duration(seconds: 1), (timer) {
      if (mounted) {
        setState(() {});
      }
    });
  }

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }

  Future<void> _loadData() async {
    await _auth.initSession();
    await _dataService.loadSampleData();
    if (mounted) setState(() {});
  }

  IconData _getCourseIcon(String iconName) {
    switch (iconName) {
      case 'menu_book': return Icons.menu_book_rounded;
      case 'calculate': return Icons.calculate_rounded;
      case 'history_edu': return Icons.history_edu_rounded;
      case 'public': return Icons.public_rounded;
      case 'gavel': return Icons.gavel_rounded;
      case 'newspaper': return Icons.newspaper_rounded;
      default: return Icons.school_rounded;
    }
  }

  void _openExamSetup() {
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) => const ExamSetupModal(),
    );
  }

  void _openScoreCalculator() {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => const ScoreCalculatorScreen(),
      ),
    );
  }

  void _openExamHistory() {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => const ExamHistoryScreen(),
      ),
    );
  }

  void _openSavedQuestions({int tabIndex = 0}) {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => SavedQuestionsScreen(initialTabIndex: tabIndex),
      ),
    ).then((_) => setState(() {}));
  }

  void _toggleThemeMode() {
    setState(() {
      AppTheme.toggleTheme();
      _dataService.saveState();
    });
  }

  void _showTargetScoreDialog() {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final dialogBg = isDark ? const Color(0xFF1E293B) : Colors.white;
    final textColor = isDark ? Colors.white : const Color(0xFF0F172A);

    final TextEditingController targetCtrl = TextEditingController(
      text: _dataService.targetScore.toString(),
    );

    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          backgroundColor: dialogBg,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
          title: Row(
            children: [
              const Icon(Icons.flag_rounded, color: Color(0xFF00CEC9)),
              const SizedBox(width: 8),
              Text(
                'Hedef Puanınızı Düzenleyin',
                style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: textColor),
              ),
            ],
          ),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Text(
                'Atamada hedeflediğiniz KPSS Lisans P3 puanını girin:',
                style: TextStyle(fontSize: 12, color: isDark ? Colors.white70 : Colors.black54),
              ),
              const SizedBox(height: 14),
              TextField(
                controller: targetCtrl,
                keyboardType: const TextInputType.numberWithOptions(decimal: true),
                autofocus: true,
                style: TextStyle(color: textColor),
                decoration: InputDecoration(
                  labelText: 'Hedef Puan',
                  labelStyle: const TextStyle(color: Color(0xFF00CEC9)),
                  suffixText: 'Puan',
                  border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
                ),
              ),
            ],
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.pop(context),
              child: const Text('İptal', style: TextStyle(color: Colors.grey)),
            ),
            ElevatedButton(
              onPressed: () {
                double? parsed = double.tryParse(targetCtrl.text);
                if (parsed != null && parsed >= 40 && parsed <= 100) {
                  setState(() {
                    _dataService.setTargetScore(parsed);
                  });
                }
                Navigator.pop(context);
              },
              style: ElevatedButton.styleFrom(
                backgroundColor: const Color(0xFF00CEC9),
                foregroundColor: const Color(0xFF0F172A),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
              ),
              child: const Text('Kaydet', style: TextStyle(fontWeight: FontWeight.bold)),
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final bgColor = isDark ? const Color(0xFF0F172A) : const Color(0xFFF1F5F9);
    final cardBgColor = isDark ? const Color(0xFF1E293B) : Colors.white;

    return Scaffold(
      backgroundColor: bgColor,
      body: IndexedStack(
        index: _currentTabIndex,
        children: [
          // TAB 0: HOME DASHBOARD
          _buildHomeDashboardTab(context),
          // TAB 1: EXPLORE FEED (Topluluk & Keşfet)
          const ExploreFeedScreen(),
          // TAB 2: SAVED QUESTIONS (Sorularım & Havuz)
          const SavedQuestionsScreen(),
          // TAB 3: USER PROFILE (Profilim)
          const ProfileScreen(),
        ],
      ),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _currentTabIndex,
        onTap: (index) {
          setState(() {
            _currentTabIndex = index;
          });
        },
        type: BottomNavigationBarType.fixed,
        backgroundColor: cardBgColor,
        selectedItemColor: const Color(0xFF00CEC9),
        unselectedItemColor: isDark ? Colors.white54 : Colors.black45,
        selectedLabelStyle: const TextStyle(fontWeight: FontWeight.bold, fontSize: 11),
        unselectedLabelStyle: const TextStyle(fontSize: 11),
        items: const [
          BottomNavigationBarItem(
            icon: Icon(Icons.home_rounded),
            label: 'Ana Sayfa',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.explore_rounded),
            label: 'Keşfet',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.star_rounded),
            label: 'Sorularım',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.person_rounded),
            label: 'Profilim',
          ),
        ],
      ),
    );
  }

  Widget _buildHomeDashboardTab(BuildContext context) {
    final targetYear = KpssCountdownService.getTargetYear();
    final remainingTimeStr = KpssCountdownService.getRemainingFormatted();
    final isDark = Theme.of(context).brightness == Brightness.dark;

    final cardBgColor = isDark ? const Color(0xFF1E293B) : Colors.white;
    final textColor = isDark ? Colors.white : const Color(0xFF0F172A);
    final subTextColor = isDark ? Colors.white60 : Colors.black54;

    final bookmarkedCount = _dataService.bookmarkedQuestionIds.length;
    final wrongCount = _dataService.wrongQuestionIds.length;

    return Scaffold(
      backgroundColor: Colors.transparent,
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        titleSpacing: 16,
        title: Row(
          children: [
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      Text(
                        'KıPSS',
                        style: TextStyle(
                          fontSize: 24,
                          fontWeight: FontWeight.w900,
                          color: textColor,
                          letterSpacing: 1.5,
                        ),
                      ),
                      const SizedBox(width: 6),
                      // Winking Badge
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                        decoration: BoxDecoration(
                          color: const Color(0xFF00CEC9).withValues(alpha: 0.15),
                          borderRadius: BorderRadius.circular(8),
                          border: Border.all(color: const Color(0xFF00CEC9), width: 0.8),
                        ),
                        child: const Text(
                          '😉 kıps!',
                          style: TextStyle(
                            color: Color(0xFF00CEC9),
                            fontSize: 10,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      )
                    ],
                  ),
                  const SizedBox(height: 2),
                  // Dynamic Second-Accurate Countdown Timer Badge
                  Row(
                    children: [
                      const Icon(Icons.timer_outlined, color: Color(0xFF00CEC9), size: 12),
                      const SizedBox(width: 4),
                      Flexible(
                        child: Text(
                          '$targetYear KPSS: $remainingTimeStr',
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          style: const TextStyle(
                            color: Color(0xFF00CEC9),
                            fontSize: 11,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ),
                    ],
                  ),
                ],
              ),
            ),
          ],
        ),
        actions: [
          // Theme Switcher Button
          IconButton(
            icon: Icon(
              isDark ? Icons.wb_sunny_rounded : Icons.nightlight_round,
              color: isDark ? const Color(0xFFFFD166) : const Color(0xFF6C5CE7),
              size: 22,
            ),
            tooltip: isDark ? 'Aydınlık Mod' : 'Karanlık Mod',
            onPressed: _toggleThemeMode,
          ),
          IconButton(
            icon: Icon(Icons.history_edu_rounded, color: textColor, size: 22),
            tooltip: 'Deneme Geçmişim',
            onPressed: _openExamHistory,
          ),
          IconButton(
            icon: Icon(Icons.calculate_outlined, color: textColor, size: 22),
            tooltip: 'Net & Puan Hesapla',
            onPressed: _openScoreCalculator,
          ),
          const SizedBox(width: 4),
        ],
      ),
      body: !_dataService.isLoaded
          ? const Center(child: CircularProgressIndicator(color: Color(0xFF00CEC9)))
          : SingleChildScrollView(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // --- DASHBOARD HERO STATS CARD ---
                  InkWell(
                    onTap: _showTargetScoreDialog,
                    borderRadius: BorderRadius.circular(24),
                    child: Container(
                      width: double.infinity,
                      padding: const EdgeInsets.all(18),
                      decoration: BoxDecoration(
                        gradient: const LinearGradient(
                          colors: [Color(0xFF0F2027), Color(0xFF203A43), Color(0xFF2C5364)],
                          begin: Alignment.topLeft,
                          end: Alignment.bottomRight,
                        ),
                        borderRadius: BorderRadius.circular(24),
                        border: Border.all(
                          color: const Color(0xFF00CEC9).withValues(alpha: 0.3),
                          width: 1,
                        ),
                        boxShadow: [
                          BoxShadow(
                            color: const Color(0xFF00CEC9).withValues(alpha: 0.2),
                            blurRadius: 20,
                            offset: const Offset(0, 8),
                          )
                        ],
                      ),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              const Text(
                                'Tahmini KPSS Neti',
                                style: TextStyle(
                                  color: Colors.white70,
                                  fontSize: 13.5,
                                  fontWeight: FontWeight.w500,
                                ),
                              ),
                              Container(
                                padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                                decoration: BoxDecoration(
                                  color: const Color(0xFF00CEC9).withValues(alpha: 0.2),
                                  borderRadius: BorderRadius.circular(12),
                                  border: Border.all(color: const Color(0xFF00CEC9)),
                                ),
                                child: Row(
                                  children: [
                                    Text(
                                      'Hedef: ${_dataService.targetScore}',
                                      style: const TextStyle(
                                        color: Color(0xFF00CEC9),
                                        fontSize: 11.5,
                                        fontWeight: FontWeight.bold,
                                      ),
                                    ),
                                    const SizedBox(width: 4),
                                    const Icon(Icons.edit, color: Color(0xFF00CEC9), size: 11),
                                  ],
                                ),
                              )
                            ],
                          ),
                          const SizedBox(height: 10),
                          Row(
                            crossAxisAlignment: CrossAxisAlignment.baseline,
                            textBaseline: TextBaseline.alphabetic,
                            children: [
                              Text(
                                _dataService.userCurrentNetScore.toStringAsFixed(2),
                                style: const TextStyle(
                                  color: Colors.white,
                                  fontSize: 34,
                                  fontWeight: FontWeight.bold,
                                ),
                              ),
                              const SizedBox(width: 8),
                              const Text(
                                '/ 120 Net',
                                style: TextStyle(color: Colors.white54, fontSize: 15),
                              ),
                            ],
                          ),
                          const SizedBox(height: 14),
                          ClipRRect(
                            borderRadius: BorderRadius.circular(10),
                            child: LinearProgressIndicator(
                              value: _dataService.userCurrentNetScore / 120,
                              minHeight: 8,
                              backgroundColor: Colors.white10,
                              color: const Color(0xFF00CEC9),
                            ),
                          ),
                          const SizedBox(height: 14),
                          Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              _buildMiniStat('Çözülen Soru', '${_dataService.userTotalAttempted}'),
                              _buildMiniStat('Doğru Yanıt', '${_dataService.userTotalCorrect}'),
                              _buildMiniStat('Doğruluk Oranı', '%${((_dataService.userTotalCorrect / _dataService.userTotalAttempted) * 100).toStringAsFixed(0)}'),
                            ],
                          )
                        ],
                      ),
                    ),
                  ),
                  const SizedBox(height: 14),

                  // --- TWO FEATURE CARDS ROW (Deneme Sınavı & Net Hesaplayıcı) ---
                  Row(
                    children: [
                      // Deneme Çöz Card
                      Expanded(
                        child: InkWell(
                          onTap: _openExamSetup,
                          borderRadius: BorderRadius.circular(20),
                          child: Container(
                            padding: const EdgeInsets.all(14),
                            decoration: BoxDecoration(
                              gradient: const LinearGradient(
                                colors: [Color(0xFF0984E3), Color(0xFF74B9FF)],
                                begin: Alignment.topLeft,
                                end: Alignment.bottomRight,
                              ),
                              borderRadius: BorderRadius.circular(20),
                              boxShadow: [
                                BoxShadow(
                                  color: const Color(0xFF0984E3).withValues(alpha: 0.3),
                                  blurRadius: 10,
                                  offset: const Offset(0, 5),
                                ),
                              ],
                            ),
                            child: const Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Icon(Icons.assignment_outlined, color: Colors.white, size: 26),
                                SizedBox(height: 8),
                                FittedBox(
                                  fit: BoxFit.scaleDown,
                                  alignment: Alignment.centerLeft,
                                  child: Text(
                                    'Deneme Çöz',
                                    style: TextStyle(
                                      color: Colors.white,
                                      fontWeight: FontWeight.bold,
                                      fontSize: 15,
                                    ),
                                  ),
                                ),
                                SizedBox(height: 2),
                                Text(
                                  '120 Soru / Mini / Tek Ders',
                                  maxLines: 1,
                                  overflow: TextOverflow.ellipsis,
                                  style: TextStyle(color: Colors.white70, fontSize: 10),
                                ),
                              ],
                            ),
                          ),
                        ),
                      ),
                      const SizedBox(width: 10),

                      // Net & 5 Yıllık Puan Simülatörü Card
                      Expanded(
                        child: InkWell(
                          onTap: _openScoreCalculator,
                          borderRadius: BorderRadius.circular(20),
                          child: Container(
                            padding: const EdgeInsets.all(14),
                            decoration: BoxDecoration(
                              gradient: const LinearGradient(
                                colors: [Color(0xFF00CEC9), Color(0xFF81ECEC)],
                                begin: Alignment.topLeft,
                                end: Alignment.bottomRight,
                              ),
                              borderRadius: BorderRadius.circular(20),
                              boxShadow: [
                                BoxShadow(
                                  color: const Color(0xFF00CEC9).withValues(alpha: 0.3),
                                  blurRadius: 10,
                                  offset: const Offset(0, 5),
                                ),
                              ],
                            ),
                            child: const Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Icon(Icons.calculate_rounded, color: Color(0xFF2D3436), size: 26),
                                SizedBox(height: 8),
                                FittedBox(
                                  fit: BoxFit.scaleDown,
                                  alignment: Alignment.centerLeft,
                                  child: Text(
                                    'Net & Puan Hesapla',
                                    style: TextStyle(
                                      color: Color(0xFF2D3436),
                                      fontWeight: FontWeight.bold,
                                      fontSize: 15,
                                    ),
                                  ),
                                ),
                                SizedBox(height: 2),
                                Text(
                                  'Son 5 Yıl ÖSYM Puanları',
                                  maxLines: 1,
                                  overflow: TextOverflow.ellipsis,
                                  style: TextStyle(color: Color(0xFF2D3436), fontSize: 10),
                                ),
                              ],
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 14),

                  // --- YANLIŞLARIM & FAVORİLERİM BANNER ---
                  InkWell(
                    onTap: () => _openSavedQuestions(tabIndex: 0),
                    borderRadius: BorderRadius.circular(16),
                    child: Container(
                      padding: const EdgeInsets.all(14),
                      decoration: BoxDecoration(
                        color: cardBgColor,
                        borderRadius: BorderRadius.circular(16),
                        border: Border.all(color: const Color(0xFFFFD166).withValues(alpha: 0.5)),
                      ),
                      child: Row(
                        children: [
                          Container(
                            padding: const EdgeInsets.all(8),
                            decoration: BoxDecoration(
                              color: const Color(0xFFFFD166).withValues(alpha: 0.2),
                              shape: BoxShape.circle,
                            ),
                            child: const Icon(Icons.star_rounded, color: Color(0xFFFFD166), size: 20),
                          ),
                          const SizedBox(width: 12),
                          Expanded(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text(
                                  'Yanlışlarım & Favori Sorularım',
                                  style: TextStyle(
                                    color: textColor,
                                    fontWeight: FontWeight.bold,
                                    fontSize: 14,
                                  ),
                                ),
                                const SizedBox(height: 2),
                                Text(
                                  '⭐ $bookmarkedCount Favori • ❌ $wrongCount Yanlış Soru Havuzu',
                                  maxLines: 1,
                                  overflow: TextOverflow.ellipsis,
                                  style: TextStyle(color: subTextColor, fontSize: 11),
                                ),
                              ],
                            ),
                          ),
                          const SizedBox(width: 6),
                          const Icon(Icons.arrow_forward_ios_rounded, color: Color(0xFFFFD166), size: 14),
                        ],
                      ),
                    ),
                  ),
                  const SizedBox(height: 12),

                  // --- EXAM HISTORY & WEAK TOPIC ANALYTICS BANNER ---
                  InkWell(
                    onTap: _openExamHistory,
                    borderRadius: BorderRadius.circular(16),
                    child: Container(
                      padding: const EdgeInsets.all(14),
                      decoration: BoxDecoration(
                        color: cardBgColor,
                        borderRadius: BorderRadius.circular(16),
                        border: Border.all(color: const Color(0xFF00CEC9).withValues(alpha: 0.4)),
                      ),
                      child: Row(
                        children: [
                          Container(
                            padding: const EdgeInsets.all(8),
                            decoration: BoxDecoration(
                              color: const Color(0xFF00CEC9).withValues(alpha: 0.2),
                              shape: BoxShape.circle,
                            ),
                            child: const Icon(Icons.analytics_rounded, color: Color(0xFF00CEC9), size: 20),
                          ),
                          const SizedBox(width: 12),
                          Expanded(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text(
                                  'Deneme Geçmişim & Zayıf Konularım',
                                  style: TextStyle(
                                    color: textColor,
                                    fontWeight: FontWeight.bold,
                                    fontSize: 14,
                                  ),
                                ),
                                const SizedBox(height: 2),
                                Text(
                                  'Deneme sonuçlarını incele, zayıf alt konuları gör.',
                                  maxLines: 1,
                                  overflow: TextOverflow.ellipsis,
                                  style: TextStyle(color: subTextColor, fontSize: 11),
                                ),
                              ],
                            ),
                          ),
                          const SizedBox(width: 6),
                          const Icon(Icons.arrow_forward_ios_rounded, color: Color(0xFF00CEC9), size: 14),
                        ],
                      ),
                    ),
                  ),
                  const SizedBox(height: 20),

                  // --- DERSLER BAŞLIĞI ---
                  Text(
                    'Dersler & Konu Ağacı',
                    style: TextStyle(
                      color: textColor,
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 12),

                  // --- DERSLER GRİD ---
                  ListView.separated(
                    shrinkWrap: true,
                    physics: const NeverScrollableScrollPhysics(),
                    itemCount: _dataService.courses.length,
                    separatorBuilder: (ctx, i) => const SizedBox(height: 10),
                    itemBuilder: (ctx, index) {
                      final course = _dataService.courses[index];
                      final topics = _dataService.getTopicsByCourse(course.id);
                      final category = _dataService.categories.firstWhere(
                        (c) => c.id == course.categoryId,
                        orElse: () => CategoryModel(id: '', code: 'GY', title: 'Genel Yetenek', sortOrder: 1),
                      );

                      return InkWell(
                        onTap: () {
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                              builder: (ctx) => CourseDetailScreen(course: course),
                            ),
                          );
                        },
                        borderRadius: BorderRadius.circular(16),
                        child: Container(
                          padding: const EdgeInsets.all(14),
                          decoration: BoxDecoration(
                            color: cardBgColor,
                            borderRadius: BorderRadius.circular(16),
                            border: Border.all(color: isDark ? Colors.white.withValues(alpha: 0.05) : Colors.grey.withValues(alpha: 0.15)),
                          ),
                          child: Row(
                            children: [
                              Container(
                                width: 46,
                                height: 46,
                                decoration: BoxDecoration(
                                  gradient: const LinearGradient(
                                    colors: [
                                      Color(0xFF00CEC9),
                                      Color(0xFF0984E3),
                                    ],
                                  ),
                                  borderRadius: BorderRadius.circular(12),
                                ),
                                child: Icon(
                                  _getCourseIcon(course.iconName),
                                  color: Colors.white,
                                  size: 24,
                                ),
                              ),
                              const SizedBox(width: 14),
                              Expanded(
                                child: Column(
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    Row(
                                      children: [
                                        Flexible(
                                          child: Text(
                                            course.title,
                                            maxLines: 1,
                                            overflow: TextOverflow.ellipsis,
                                            style: TextStyle(
                                              color: textColor,
                                              fontSize: 16,
                                              fontWeight: FontWeight.bold,
                                            ),
                                          ),
                                        ),
                                        const SizedBox(width: 8),
                                        Container(
                                          padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                                          decoration: BoxDecoration(
                                            color: isDark ? Colors.white10 : Colors.grey.shade200,
                                            borderRadius: BorderRadius.circular(6),
                                          ),
                                          child: Text(
                                            category.code,
                                            style: TextStyle(
                                              color: subTextColor,
                                              fontSize: 9.5,
                                              fontWeight: FontWeight.bold,
                                            ),
                                          ),
                                        )
                                      ],
                                    ),
                                    const SizedBox(height: 3),
                                    Text(
                                      '${topics.length} Konu Başlığı • Hap Bilgi & Quiz',
                                      maxLines: 1,
                                      overflow: TextOverflow.ellipsis,
                                      style: TextStyle(
                                        color: subTextColor,
                                        fontSize: 12,
                                      ),
                                    ),
                                  ],
                                ),
                              ),
                              Icon(
                                Icons.chevron_right_rounded,
                                color: subTextColor,
                                size: 22,
                              ),
                            ],
                          ),
                        ),
                      );
                    },
                  ),
                ],
              ),
            ),
    );
  }

  Widget _buildMiniStat(String label, String value) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          label,
          style: const TextStyle(color: Colors.white54, fontSize: 10.5),
        ),
        const SizedBox(height: 2),
        Text(
          value,
          style: const TextStyle(
            color: Colors.white,
            fontWeight: FontWeight.bold,
            fontSize: 14,
          ),
        ),
      ],
    );
  }
}
