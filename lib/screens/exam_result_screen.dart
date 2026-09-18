import 'package:flutter/material.dart';
import '../models/mock_exam_model.dart';

class ExamResultScreen extends StatefulWidget {
  final MockExam exam;

  const ExamResultScreen({super.key, required this.exam});

  @override
  State<ExamResultScreen> createState() => _ExamResultScreenState();
}

class _ExamResultScreenState extends State<ExamResultScreen> {
  bool _isReviewing = false;
  int _reviewIndex = 0;
  String _reviewFilter = 'all'; // 'all', 'wrong', 'blank', 'correct'

  @override
  Widget build(BuildContext context) {
    if (_isReviewing) {
      return _buildReviewView();
    }
    return _buildResultSummaryView();
  }

  Widget _buildResultSummaryView() {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final bgColor = isDark ? const Color(0xFF0F172A) : const Color(0xFFF1F5F9);
    final cardBgColor = isDark ? const Color(0xFF1E293B) : Colors.white;
    final textColor = isDark ? Colors.white : const Color(0xFF0F172A);

    final exam = widget.exam;
    final breakdown = exam.courseBreakdown;

    return Scaffold(
      backgroundColor: bgColor,
      appBar: AppBar(
        title: Text('Sınav Sonucu ve Karne 📊', style: TextStyle(fontWeight: FontWeight.bold, color: textColor)),
        backgroundColor: Colors.transparent,
        elevation: 0,
        automaticallyImplyLeading: false,
        actions: [
          IconButton(
            icon: Icon(Icons.home_outlined, color: textColor),
            onPressed: () {
              Navigator.popUntil(context, (route) => route.isFirst);
            },
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            // Score Header Card with Turquoise Gradient
            Container(
              width: double.infinity,
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                gradient: const LinearGradient(
                  colors: [Color(0xFF0F2027), Color(0xFF203A43), Color(0xFF2C5364)],
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                ),
                borderRadius: BorderRadius.circular(24),
                border: Border.all(color: const Color(0xFF00CEC9).withValues(alpha: 0.4)),
                boxShadow: [
                  BoxShadow(
                    color: const Color(0xFF00CEC9).withValues(alpha: 0.2),
                    blurRadius: 15,
                    offset: const Offset(0, 8),
                  ),
                ],
              ),
              child: Column(
                children: [
                  Text(
                    exam.title,
                    textAlign: TextAlign.center,
                    style: const TextStyle(
                      color: Colors.white70,
                      fontSize: 13,
                      fontWeight: FontWeight.w500,
                    ),
                  ),
                  const SizedBox(height: 12),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Column(
                        children: [
                          const Text(
                            'TOPLAM NET',
                            style: TextStyle(
                              color: Color(0xFF00CEC9),
                              fontSize: 11,
                              fontWeight: FontWeight.bold,
                              letterSpacing: 1,
                            ),
                          ),
                          const SizedBox(height: 4),
                          Text(
                            exam.netScore.toStringAsFixed(2),
                            style: const TextStyle(
                              color: Colors.white,
                              fontSize: 36,
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                        ],
                      ),
                    ],
                  ),
                  const SizedBox(height: 16),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceAround,
                    children: [
                      _buildHeaderStatItem('Doğru', '${exam.correctCount}', const Color(0xFF00B894)),
                      _buildHeaderStatItem('Yanlış', '${exam.wrongCount}', const Color(0xFFFF7675)),
                      _buildHeaderStatItem('Boş', '${exam.blankCount}', const Color(0xFFFDCB6E)),
                    ],
                  ),
                ],
              ),
            ),

            const SizedBox(height: 20),

            // Ders Bazlı Karne Card
            Container(
              padding: const EdgeInsets.all(16),
              decoration: BoxDecoration(
                color: cardBgColor,
                borderRadius: BorderRadius.circular(20),
                border: Border.all(color: isDark ? Colors.white.withValues(alpha: 0.05) : Colors.grey.shade200),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      const Icon(Icons.bar_chart_rounded, color: Color(0xFF00CEC9)),
                      const SizedBox(width: 8),
                      Text(
                        'Ders Bazlı Performans Karnesi',
                        style: TextStyle(
                          fontSize: 16,
                          fontWeight: FontWeight.bold,
                          color: textColor,
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 16),
                  ...breakdown.entries.map((entry) {
                    final courseName = entry.key;
                    final stats = entry.value;
                    final total = stats['total'] as int;
                    final correct = stats['correct'] as int;
                    final wrong = stats['wrong'] as int;
                    final blank = stats['blank'] as int;
                    final net = stats['net'] as double;
                    final ratio = total > 0 ? (net / total) : 0.0;

                    return Padding(
                      padding: const EdgeInsets.only(bottom: 14.0),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              Expanded(
                                child: Text(
                                  courseName,
                                  overflow: TextOverflow.ellipsis,
                                  style: TextStyle(
                                    fontWeight: FontWeight.bold,
                                    fontSize: 14,
                                    color: textColor,
                                  ),
                                ),
                              ),
                              const SizedBox(width: 8),
                              FittedBox(
                                fit: BoxFit.scaleDown,
                                child: Text(
                                  '${net.toStringAsFixed(2)} Net  ($correct D / $wrong Y / $blank B)',
                                  style: const TextStyle(
                                    fontSize: 12,
                                    fontWeight: FontWeight.bold,
                                    color: Color(0xFF00CEC9),
                                  ),
                                ),
                              ),
                            ],
                          ),
                          const SizedBox(height: 6),
                          ClipRRect(
                            borderRadius: BorderRadius.circular(4),
                            child: LinearProgressIndicator(
                              value: ratio < 0 ? 0 : (ratio > 1 ? 1 : ratio),
                              minHeight: 8,
                              backgroundColor: isDark ? Colors.white10 : Colors.grey.shade200,
                              valueColor: AlwaysStoppedAnimation<Color>(
                                ratio > 0.7
                                    ? const Color(0xFF00B894)
                                    : (ratio > 0.4 ? const Color(0xFFFDCB6E) : const Color(0xFFFF7675)),
                              ),
                            ),
                          ),
                        ],
                      ),
                    );
                  }),
                ],
              ),
            ),

            const SizedBox(height: 24),

            // Action Buttons
            Row(
              children: [
                Expanded(
                  child: OutlinedButton.icon(
                    onPressed: () {
                      setState(() {
                        _isReviewing = true;
                        _reviewIndex = 0;
                        _reviewFilter = 'all';
                      });
                    },
                    style: OutlinedButton.styleFrom(
                      side: const BorderSide(color: Color(0xFF00CEC9)),
                      padding: const EdgeInsets.symmetric(vertical: 14),
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
                    ),
                    icon: const Icon(Icons.remove_red_eye_rounded, color: Color(0xFF00CEC9)),
                    label: const Text(
                      'Soruları İncele',
                      style: TextStyle(color: Color(0xFF00CEC9), fontWeight: FontWeight.bold),
                    ),
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: ElevatedButton.icon(
                    onPressed: () {
                      Navigator.popUntil(context, (route) => route.isFirst);
                    },
                    style: ElevatedButton.styleFrom(
                      backgroundColor: const Color(0xFF00CEC9),
                      foregroundColor: const Color(0xFF0F172A),
                      padding: const EdgeInsets.symmetric(vertical: 14),
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
                    ),
                    icon: const Icon(Icons.home_rounded),
                    label: const Text(
                      'Ana Sayfaya Dön',
                      style: TextStyle(fontWeight: FontWeight.bold),
                    ),
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildHeaderStatItem(String label, String value, Color color) {
    return Column(
      children: [
        Text(label, style: const TextStyle(color: Colors.white60, fontSize: 11)),
        const SizedBox(height: 2),
        Text(value, style: TextStyle(color: color, fontSize: 18, fontWeight: FontWeight.bold)),
      ],
    );
  }

  Widget _buildReviewView() {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final bgColor = isDark ? const Color(0xFF0F172A) : const Color(0xFFF1F5F9);
    final cardBgColor = isDark ? const Color(0xFF1E293B) : Colors.white;
    final textColor = isDark ? Colors.white : const Color(0xFF0F172A);
    final subTextColor = isDark ? Colors.white60 : const Color(0xFF64748B);

    final allQuestions = widget.exam.questions;
    List<ExamQuestionItem> filteredList = allQuestions;

    if (_reviewFilter == 'wrong') {
      filteredList = allQuestions.where((q) => q.isWrong).toList();
    } else if (_reviewFilter == 'blank') {
      filteredList = allQuestions.where((q) => q.isBlank).toList();
    } else if (_reviewFilter == 'correct') {
      filteredList = allQuestions.where((q) => q.isCorrect).toList();
    }

    if (filteredList.isEmpty) {
      return Scaffold(
        backgroundColor: bgColor,
        appBar: AppBar(
          title: Text('Soru Çözüm İncelemesi', style: TextStyle(color: textColor)),
          leading: IconButton(
            icon: Icon(Icons.arrow_back_rounded, color: textColor),
            onPressed: () => setState(() => _isReviewing = false),
          ),
        ),
        body: Center(
          child: Text('Bu filtreye uygun soru bulunamadı.', style: TextStyle(color: subTextColor)),
        ),
      );
    }

    if (_reviewIndex >= filteredList.length) {
      _reviewIndex = 0;
    }

    final item = filteredList[_reviewIndex];
    final question = item.question;

    return Scaffold(
      backgroundColor: bgColor,
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        leading: IconButton(
          icon: Icon(Icons.arrow_back_rounded, color: textColor),
          onPressed: () => setState(() => _isReviewing = false),
        ),
        title: Text(
          'Soru ${_reviewIndex + 1} / ${filteredList.length}',
          style: TextStyle(color: textColor, fontWeight: FontWeight.bold, fontSize: 16),
        ),
        actions: [
          PopupMenuButton<String>(
            icon: Icon(Icons.filter_list_rounded, color: textColor),
            onSelected: (val) {
              setState(() {
                _reviewFilter = val;
                _reviewIndex = 0;
              });
            },
            itemBuilder: (ctx) => [
              const PopupMenuItem(value: 'all', child: Text('Tüm Sorular')),
              const PopupMenuItem(value: 'wrong', child: Text('Yanlışlar')),
              const PopupMenuItem(value: 'blank', child: Text('Boş Bırakılanlar')),
              const PopupMenuItem(value: 'correct', child: Text('Doğrular')),
            ],
          ),
        ],
      ),
      body: Column(
        children: [
          // Top Course Tag & Quick Question Jump (Overflow fixed with Expanded!)
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
            color: cardBgColor,
            child: Row(
              children: [
                Expanded(
                  child: Container(
                    padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                    decoration: BoxDecoration(
                      color: const Color(0xFF00CEC9).withValues(alpha: 0.15),
                      borderRadius: BorderRadius.circular(10),
                      border: Border.all(color: const Color(0xFF00CEC9)),
                    ),
                    child: Text(
                      '${item.courseName} • ${item.topicTitle}',
                      overflow: TextOverflow.ellipsis,
                      style: const TextStyle(
                        color: Color(0xFF00CEC9),
                        fontSize: 11.5,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                ),
                const SizedBox(width: 8),
                _buildStatusBadge(item),
              ],
            ),
          ),

          // Question Content
          Expanded(
            child: SingleChildScrollView(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Container(
                    width: double.infinity,
                    padding: const EdgeInsets.all(18),
                    decoration: BoxDecoration(
                      color: cardBgColor,
                      borderRadius: BorderRadius.circular(18),
                      border: Border.all(color: isDark ? Colors.white.withValues(alpha: 0.05) : Colors.grey.shade200),
                    ),
                    child: Text(
                      question.questionText,
                      style: TextStyle(
                        fontSize: 15.5,
                        fontWeight: FontWeight.w600,
                        color: textColor,
                        height: 1.5,
                      ),
                    ),
                  ),
                  const SizedBox(height: 16),

                  // Options
                  ...question.options.map((option) {
                    bool isUserSelected = item.selectedOptionKey == option.key;
                    bool isCorrect = question.correctOption == option.key;

                    Color borderColor = isDark ? Colors.white10 : Colors.grey.shade300;
                    Color optBgColor = cardBgColor;
                    IconData? icon;
                    Color iconColor = Colors.grey;

                    if (isCorrect) {
                      borderColor = const Color(0xFF00B894);
                      optBgColor = const Color(0xFF00B894).withValues(alpha: 0.18);
                      icon = Icons.check_circle;
                      iconColor = const Color(0xFF00B894);
                    } else if (isUserSelected && !isCorrect) {
                      borderColor = Colors.redAccent;
                      optBgColor = Colors.red.withValues(alpha: 0.18);
                      icon = Icons.cancel;
                      iconColor = Colors.redAccent;
                    }

                    return Container(
                      margin: const EdgeInsets.only(bottom: 10),
                      padding: const EdgeInsets.all(14),
                      decoration: BoxDecoration(
                        color: optBgColor,
                        borderRadius: BorderRadius.circular(14),
                        border: Border.all(color: borderColor, width: 1.5),
                      ),
                      child: Row(
                        children: [
                          CircleAvatar(
                            radius: 12,
                            backgroundColor: isCorrect ? const Color(0xFF00B894) : (isUserSelected ? Colors.redAccent : (isDark ? Colors.white10 : Colors.grey.shade200)),
                            child: Text(
                              option.key,
                              style: TextStyle(
                                fontSize: 11,
                                fontWeight: FontWeight.bold,
                                color: (isCorrect || isUserSelected) ? Colors.white : textColor,
                              ),
                            ),
                          ),
                          const SizedBox(width: 12),
                          Expanded(
                            child: Text(
                              option.text,
                              style: TextStyle(
                                color: textColor,
                                fontSize: 13.5,
                                fontWeight: (isCorrect || isUserSelected) ? FontWeight.bold : FontWeight.normal,
                              ),
                            ),
                          ),
                          if (icon != null) Icon(icon, color: iconColor, size: 20),
                        ],
                      ),
                    );
                  }),

                  const SizedBox(height: 16),

                  // Solution Box
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
                            Icon(Icons.lightbulb_outline_rounded, color: Color(0xFF00CEC9), size: 18),
                            SizedBox(width: 6),
                            Text(
                              'Çözüm ve Açıklama',
                              style: TextStyle(color: Color(0xFF00CEC9), fontWeight: FontWeight.bold, fontSize: 13),
                            ),
                          ],
                        ),
                        const SizedBox(height: 8),
                        Text(
                          question.explanation,
                          style: TextStyle(color: textColor, fontSize: 13.5, height: 1.45),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          ),

          // Bottom Navigation Buttons
          Container(
            padding: const EdgeInsets.all(12),
            color: cardBgColor,
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                OutlinedButton.icon(
                  onPressed: _reviewIndex > 0
                      ? () {
                          setState(() {
                            _reviewIndex--;
                          });
                        }
                      : null,
                  icon: const Icon(Icons.arrow_back_rounded),
                  label: const Text('Önceki'),
                ),
                Text(
                  '${_reviewIndex + 1} / ${filteredList.length}',
                  style: TextStyle(color: textColor, fontWeight: FontWeight.bold),
                ),
                ElevatedButton.icon(
                  onPressed: _reviewIndex < filteredList.length - 1
                      ? () {
                          setState(() {
                            _reviewIndex++;
                          });
                        }
                      : null,
                  style: ElevatedButton.styleFrom(backgroundColor: const Color(0xFF00CEC9), foregroundColor: const Color(0xFF0F172A)),
                  icon: const Icon(Icons.arrow_forward_rounded),
                  label: const Text('Sonraki'),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildStatusBadge(ExamQuestionItem item) {
    if (item.isCorrect) {
      return Container(
        padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
        decoration: BoxDecoration(color: Colors.green.withValues(alpha: 0.2), borderRadius: BorderRadius.circular(8)),
        child: const Text('✅ Doğru', style: TextStyle(color: Colors.green, fontSize: 11, fontWeight: FontWeight.bold)),
      );
    } else if (item.isWrong) {
      return Container(
        padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
        decoration: BoxDecoration(color: Colors.red.withValues(alpha: 0.2), borderRadius: BorderRadius.circular(8)),
        child: const Text('❌ Yanlış', style: TextStyle(color: Colors.redAccent, fontSize: 11, fontWeight: FontWeight.bold)),
      );
    } else {
      return Container(
        padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
        decoration: BoxDecoration(color: Colors.amber.withValues(alpha: 0.2), borderRadius: BorderRadius.circular(8)),
        child: const Text('⚪ Boş', style: TextStyle(color: Colors.amber, fontSize: 11, fontWeight: FontWeight.bold)),
      );
    }
  }
}
