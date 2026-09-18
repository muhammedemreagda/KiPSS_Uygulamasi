import 'package:flutter/material.dart';
import '../models/mock_exam_model.dart';
import '../services/data_service.dart';
import 'exam_result_screen.dart';
import 'quick_note_screen.dart';

class ExamHistoryScreen extends StatefulWidget {
  const ExamHistoryScreen({super.key});

  @override
  State<ExamHistoryScreen> createState() => _ExamHistoryScreenState();
}

class _ExamHistoryScreenState extends State<ExamHistoryScreen> with SingleTickerProviderStateMixin {
  late TabController _tabController;
  final DataService _dataService = DataService();

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 2, vsync: this);
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final bgColor = isDark ? const Color(0xFF0F172A) : const Color(0xFFF1F5F9);
    final cardBgColor = isDark ? const Color(0xFF1E293B) : Colors.white;
    final textColor = isDark ? Colors.white : const Color(0xFF0F172A);
    final subTextColor = isDark ? Colors.white60 : const Color(0xFF64748B);

    final completedExams = _dataService.completedExams;
    final weakTopics = _dataService.getWeakTopicsAnalytics();

    return Scaffold(
      backgroundColor: bgColor,
      appBar: AppBar(
        title: Text('Deneme Geçmişim & Zayıf Konular 📊', style: TextStyle(fontWeight: FontWeight.bold, color: textColor)),
        backgroundColor: Colors.transparent,
        elevation: 0,
        leading: IconButton(
          icon: Icon(Icons.arrow_back_ios_new_rounded, color: textColor),
          onPressed: () => Navigator.pop(context),
        ),
        bottom: TabBar(
          controller: _tabController,
          indicatorColor: const Color(0xFF00CEC9),
          indicatorWeight: 3,
          labelColor: const Color(0xFF00CEC9),
          unselectedLabelColor: subTextColor,
          labelStyle: const TextStyle(fontWeight: FontWeight.bold, fontSize: 13),
          unselectedLabelStyle: const TextStyle(fontWeight: FontWeight.normal),
          tabs: const [
            Tab(icon: Icon(Icons.history_rounded), text: 'Çözülen Denemeler'),
            Tab(icon: Icon(Icons.analytics_rounded), text: '🔥 Zayıf Konularım'),
          ],
        ),
      ),
      body: TabBarView(
        controller: _tabController,
        children: [
          // TAB 1: Completed Exam History
          _buildExamHistoryTab(completedExams, textColor, subTextColor, cardBgColor, isDark),

          // TAB 2: Weak Topic Analytics & Mistake Map
          _buildWeakTopicsTab(weakTopics, textColor, subTextColor, cardBgColor, isDark),
        ],
      ),
    );
  }

  Widget _buildExamHistoryTab(List<MockExam> exams, Color textColor, Color subTextColor, Color cardBgColor, bool isDark) {
    if (exams.isEmpty) {
      return Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(Icons.assignment_late_outlined, size: 60, color: subTextColor.withValues(alpha: 0.5)),
            const SizedBox(height: 12),
            Text(
              'Henüz çözülen deneme sınavınız bulunmuyor.',
              style: TextStyle(color: subTextColor, fontSize: 14),
            ),
          ],
        ),
      );
    }

    return ListView.builder(
      padding: const EdgeInsets.all(16),
      itemCount: exams.length,
      itemBuilder: (context, index) {
        final exam = exams[index];
        final formattedDate = exam.startTime != null
            ? '${exam.startTime!.day}.${exam.startTime!.month}.${exam.startTime!.year}'
            : 'Bugün';

        return Container(
          margin: const EdgeInsets.only(bottom: 14),
          padding: const EdgeInsets.all(16),
          decoration: BoxDecoration(
            color: cardBgColor,
            borderRadius: BorderRadius.circular(18),
            border: Border.all(color: isDark ? Colors.white.withValues(alpha: 0.05) : Colors.grey.shade200),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Expanded(
                    child: Text(
                      exam.title,
                      overflow: TextOverflow.ellipsis,
                      style: TextStyle(
                        fontWeight: FontWeight.bold,
                        fontSize: 15,
                        color: textColor,
                      ),
                    ),
                  ),
                  const SizedBox(width: 8),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                    decoration: BoxDecoration(
                      color: const Color(0xFF00CEC9).withValues(alpha: 0.15),
                      borderRadius: BorderRadius.circular(8),
                    ),
                    child: Text(
                      formattedDate,
                      style: const TextStyle(
                        color: Color(0xFF00CEC9),
                        fontSize: 11,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 12),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceAround,
                children: [
                  _buildStatPill('Net Puan', exam.netScore.toStringAsFixed(2), const Color(0xFF00CEC9)),
                  _buildStatPill('Doğru', '${exam.correctCount}', const Color(0xFF00B894)),
                  _buildStatPill('Yanlış', '${exam.wrongCount}', const Color(0xFFFF7675)),
                  _buildStatPill('Boş', '${exam.blankCount}', const Color(0xFFFDCB6E)),
                ],
              ),
              const SizedBox(height: 14),
              SizedBox(
                width: double.infinity,
                child: OutlinedButton.icon(
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (ctx) => ExamResultScreen(exam: exam),
                      ),
                    );
                  },
                  style: OutlinedButton.styleFrom(
                    side: const BorderSide(color: Color(0xFF00CEC9)),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                  ),
                  icon: const Icon(Icons.analytics_outlined, color: Color(0xFF00CEC9), size: 18),
                  label: const Text(
                    'Detaylı Karne & Çözümleri Gör',
                    style: TextStyle(color: Color(0xFF00CEC9), fontWeight: FontWeight.bold, fontSize: 13),
                  ),
                ),
              ),
            ],
          ),
        );
      },
    );
  }

  Widget _buildStatPill(String label, String val, Color valColor) {
    return Column(
      children: [
        Text(label, style: const TextStyle(fontSize: 10.5, color: Colors.grey)),
        const SizedBox(height: 2),
        Text(val, style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: valColor)),
      ],
    );
  }

  Widget _buildWeakTopicsTab(List<WeakTopicReportItem> weakTopics, Color textColor, Color subTextColor, Color cardBgColor, bool isDark) {
    if (weakTopics.isEmpty) {
      return Center(
        child: Padding(
          padding: const EdgeInsets.all(24.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Icon(Icons.verified_user_rounded, size: 64, color: Color(0xFF00B894)),
              const SizedBox(height: 16),
              Text(
                'Zayıf Konu Tespit Edilmedi! 🎉',
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: textColor),
              ),
              const SizedBox(height: 8),
              Text(
                'Çözdüğünüz deneme sınavlarında yanlış yaptığınız konular burada analiz edilir.',
                textAlign: TextAlign.center,
                style: TextStyle(color: subTextColor, fontSize: 13),
              ),
            ],
          ),
        ),
      );
    }

    return ListView.builder(
      padding: const EdgeInsets.all(16),
      itemCount: weakTopics.length,
      itemBuilder: (context, index) {
        final item = weakTopics[index];
        final quickNote = _dataService.getQuickNoteByTopic(item.topicId);

        return Container(
          margin: const EdgeInsets.only(bottom: 12),
          padding: const EdgeInsets.all(16),
          decoration: BoxDecoration(
            color: cardBgColor,
            borderRadius: BorderRadius.circular(16),
            border: Border.all(color: Colors.redAccent.withValues(alpha: 0.3)),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Expanded(
                    child: Text(
                      '${item.courseTitle} • ${item.topicTitle}',
                      overflow: TextOverflow.ellipsis,
                      style: TextStyle(
                        fontWeight: FontWeight.bold,
                        fontSize: 14.5,
                        color: textColor,
                      ),
                    ),
                  ),
                  const SizedBox(width: 8),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                    decoration: BoxDecoration(
                      color: Colors.redAccent.withValues(alpha: 0.15),
                      borderRadius: BorderRadius.circular(8),
                    ),
                    child: Text(
                      '${item.wrongCount} Yanlış / ${item.blankCount} Boş',
                      style: const TextStyle(
                        color: Colors.redAccent,
                        fontSize: 11,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 10),
              Row(
                children: [
                  Expanded(
                    child: ClipRRect(
                      borderRadius: BorderRadius.circular(4),
                      child: LinearProgressIndicator(
                        value: item.accuracyPercentage / 100,
                        minHeight: 6,
                        backgroundColor: isDark ? Colors.white10 : Colors.grey.shade200,
                        valueColor: const AlwaysStoppedAnimation<Color>(Colors.redAccent),
                      ),
                    ),
                  ),
                  const SizedBox(width: 10),
                  Text(
                    'Başarı: %${item.accuracyPercentage.toStringAsFixed(0)}',
                    style: const TextStyle(fontSize: 11.5, fontWeight: FontWeight.bold, color: Colors.redAccent),
                  ),
                ],
              ),
              if (quickNote != null) ...[
                const SizedBox(height: 12),
                SizedBox(
                  width: double.infinity,
                  child: ElevatedButton.icon(
                    onPressed: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (ctx) => QuickNoteScreen(
                            quickNote: quickNote,
                            topicTitle: item.topicTitle,
                          ),
                        ),
                      );
                    },
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.redAccent.withValues(alpha: 0.15),
                      foregroundColor: Colors.redAccent,
                      elevation: 0,
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                    ),
                    icon: const Icon(Icons.menu_book_rounded, size: 16),
                    label: const Text('Konu Özetini Oku ve Tekrar Et', style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold)),
                  ),
                ),
              ]
            ],
          ),
        );
      },
    );
  }
}
