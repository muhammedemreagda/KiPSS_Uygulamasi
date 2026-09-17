import 'package:flutter/material.dart';
import '../models/kpss_models.dart';
import '../services/data_service.dart';

class QuizScreen extends StatefulWidget {
  final String? topicTitle;
  final TopicModel? topic;
  final List<QuestionModel>? questions;
  final List<QuestionModel>? customQuestions;

  const QuizScreen({
    super.key,
    this.topicTitle,
    this.topic,
    this.questions,
    this.customQuestions,
  });

  @override
  State<QuizScreen> createState() => _QuizScreenState();
}

class _QuizScreenState extends State<QuizScreen> {
  final DataService _dataService = DataService();
  late List<QuestionModel> _questions;
  int _currentIndex = 0;
  String? _selectedOptionKey;
  bool _isAnswered = false;
  int _scoreCount = 0;

  String get effectiveTitle => widget.topicTitle ?? widget.topic?.title ?? 'Konu Testi';

  @override
  void initState() {
    super.initState();
    final sourceList = widget.customQuestions ?? widget.questions ?? [];
    _questions = List<QuestionModel>.from(sourceList)..shuffle();
  }

  void _onOptionSelected(String optionKey) {
    if (_isAnswered) return;

    final currentQuestion = _questions[_currentIndex];
    final bool isCorrect = (optionKey == currentQuestion.correctOption);

    setState(() {
      _selectedOptionKey = optionKey;
      _isAnswered = true;
      if (isCorrect) {
        _scoreCount++;
      } else {
        _dataService.addWrongQuestion(currentQuestion.id);
      }
    });

    _dataService.recordAttempt(isCorrect: isCorrect);
  }

  void _nextQuestion() {
    if (_currentIndex < _questions.length - 1) {
      setState(() {
        _currentIndex++;
        _selectedOptionKey = null;
        _isAnswered = false;
      });
    } else {
      _showResultDialog();
    }
  }

  void _showResultDialog() {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final dialogBg = isDark ? const Color(0xFF1E293B) : Colors.white;
    final textColor = isDark ? Colors.white : const Color(0xFF0F172A);

    showDialog(
      context: context,
      barrierDismissible: false,
      builder: (ctx) => AlertDialog(
        backgroundColor: dialogBg,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(24)),
        title: Text(
          'Quiz Tamamlandı! 🎉',
          textAlign: TextAlign.center,
          style: TextStyle(color: textColor, fontWeight: FontWeight.bold),
        ),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text(
              '${_questions.length} sorudan $_scoreCount doğru yanıt verdin.',
              textAlign: TextAlign.center,
              style: TextStyle(color: isDark ? Colors.white70 : Colors.black54, fontSize: 16),
            ),
            const SizedBox(height: 16),
            Container(
              padding: const EdgeInsets.all(16),
              decoration: BoxDecoration(
                color: const Color(0xFF00CEC9).withValues(alpha: 0.15),
                borderRadius: BorderRadius.circular(16),
                border: Border.all(color: const Color(0xFF00CEC9)),
              ),
              child: Text(
                'Başarı Oranı: %${((_scoreCount / _questions.length) * 100).toStringAsFixed(0)}',
                style: const TextStyle(
                  color: Color(0xFF00CEC9),
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
          ],
        ),
        actions: [
          SizedBox(
            width: double.infinity,
            child: ElevatedButton(
              style: ElevatedButton.styleFrom(
                backgroundColor: const Color(0xFF00CEC9),
                foregroundColor: const Color(0xFF0F172A),
                padding: const EdgeInsets.symmetric(vertical: 14),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(14),
                ),
              ),
              onPressed: () {
                Navigator.pop(ctx); // Close dialog
                Navigator.pop(context); // Close quiz
              },
              child: const Text(
                'Derslere Dön',
                style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
              ),
            ),
          )
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final bgColor = isDark ? const Color(0xFF0F172A) : const Color(0xFFF1F5F9);
    final cardBgColor = isDark ? const Color(0xFF1E293B) : Colors.white;
    final textColor = isDark ? Colors.white : const Color(0xFF0F172A);
    final subTextColor = isDark ? Colors.white70 : Colors.black54;

    if (_questions.isEmpty) {
      return Scaffold(
        backgroundColor: bgColor,
        appBar: AppBar(
          backgroundColor: Colors.transparent,
          elevation: 0,
          leading: IconButton(
            icon: Icon(Icons.close_rounded, color: textColor),
            onPressed: () => Navigator.pop(context),
          ),
          title: Text(effectiveTitle, style: TextStyle(color: textColor)),
        ),
        body: Center(
          child: Text('Bu konu için test sorusu henüz yüklenmedi.', style: TextStyle(color: subTextColor)),
        ),
      );
    }

    final currentQ = _questions[_currentIndex];
    final isBookmarked = _dataService.isBookmarked(currentQ.id);

    return Scaffold(
      backgroundColor: bgColor,
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        leading: IconButton(
          icon: Icon(Icons.close_rounded, color: textColor),
          onPressed: () => Navigator.pop(context),
        ),
        title: Text(
          effectiveTitle,
          style: TextStyle(color: textColor, fontSize: 18, fontWeight: FontWeight.bold),
        ),
        actions: [
          IconButton(
            icon: Icon(
              isBookmarked ? Icons.star_rounded : Icons.star_border_rounded,
              color: const Color(0xFFFFD166),
              size: 26,
            ),
            tooltip: isBookmarked ? 'Favorilerden Çıkar' : 'Favorilere Ekle',
            onPressed: () {
              setState(() {
                _dataService.toggleBookmark(currentQ.id);
              });
            },
          ),
          const SizedBox(width: 8),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // PROGRESS & SCORE BAR
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text(
                  'Soru ${_currentIndex + 1} / ${_questions.length}',
                  style: TextStyle(color: subTextColor, fontWeight: FontWeight.bold),
                ),
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                  decoration: BoxDecoration(
                    color: const Color(0xFF00CEC9).withValues(alpha: 0.15),
                    borderRadius: BorderRadius.circular(10),
                    border: Border.all(color: const Color(0xFF00CEC9)),
                  ),
                  child: Text(
                    'KPSS Seviye ${currentQ.difficultyLevel}',
                    style: const TextStyle(color: Color(0xFF00CEC9), fontSize: 12, fontWeight: FontWeight.bold),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 10),
            ClipRRect(
              borderRadius: BorderRadius.circular(6),
              child: LinearProgressIndicator(
                value: (_currentIndex + 1) / _questions.length,
                minHeight: 6,
                backgroundColor: isDark ? Colors.white10 : Colors.grey.shade300,
                color: const Color(0xFF00CEC9),
              ),
            ),
            const SizedBox(height: 24),

            // QUESTION STEM CARD
            Container(
              width: double.infinity,
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                color: cardBgColor,
                borderRadius: BorderRadius.circular(20),
                border: Border.all(color: isDark ? Colors.white.withValues(alpha: 0.08) : Colors.grey.withValues(alpha: 0.15)),
              ),
              child: Text(
                currentQ.questionText,
                style: TextStyle(
                  color: textColor,
                  fontSize: 17,
                  fontWeight: FontWeight.w600,
                  height: 1.5,
                ),
              ),
            ),
            const SizedBox(height: 20),

            // OPTIONS LIST
            ...currentQ.options.map((opt) {
              final bool isSelected = (_selectedOptionKey == opt.key);
              final bool isCorrectOpt = (opt.key == currentQ.correctOption);

              Color optionBgColor = cardBgColor;
              Color borderColor = isDark ? Colors.white.withValues(alpha: 0.08) : Colors.grey.withValues(alpha: 0.15);
              Color optTextColor = textColor;

              if (_isAnswered) {
                if (isCorrectOpt) {
                  optionBgColor = const Color(0xFF00B894).withValues(alpha: 0.2);
                  borderColor = const Color(0xFF00B894);
                  optTextColor = isDark ? const Color(0xFFA7F3D0) : Colors.green.shade800;
                } else if (isSelected && !isCorrectOpt) {
                  optionBgColor = Colors.red.withValues(alpha: 0.2);
                  borderColor = Colors.redAccent;
                  optTextColor = isDark ? Colors.redAccent.shade100 : Colors.red.shade800;
                }
              }

              return Padding(
                padding: const EdgeInsets.only(bottom: 12.0),
                child: InkWell(
                  onTap: () => _onOptionSelected(opt.key),
                  borderRadius: BorderRadius.circular(16),
                  child: Container(
                    padding: const EdgeInsets.all(16),
                    decoration: BoxDecoration(
                      color: optionBgColor,
                      borderRadius: BorderRadius.circular(16),
                      border: Border.all(color: borderColor, width: 1.5),
                    ),
                    child: Row(
                      children: [
                        Container(
                          width: 36,
                          height: 36,
                          decoration: BoxDecoration(
                            color: isDark ? Colors.white10 : Colors.grey.shade200,
                            borderRadius: BorderRadius.circular(10),
                          ),
                          child: Center(
                            child: Text(
                              opt.key,
                              style: TextStyle(
                                color: optTextColor,
                                fontWeight: FontWeight.bold,
                                fontSize: 16,
                              ),
                            ),
                          ),
                        ),
                        const SizedBox(width: 14),
                        Expanded(
                          child: Text(
                            opt.text,
                            style: TextStyle(
                              color: optTextColor,
                              fontSize: 15,
                              fontWeight: FontWeight.w500,
                            ),
                          ),
                        ),
                        if (_isAnswered && isCorrectOpt)
                          const Icon(Icons.check_circle_rounded, color: Color(0xFF00B894), size: 22)
                        else if (_isAnswered && isSelected && !isCorrectOpt)
                          const Icon(Icons.cancel_rounded, color: Colors.redAccent, size: 22),
                      ],
                    ),
                  ),
                ),
              );
            }),

            // EXPLANATION CARD (Appears when answered)
            if (_isAnswered) ...[
              const SizedBox(height: 16),
              Container(
                padding: const EdgeInsets.all(18),
                decoration: BoxDecoration(
                  color: const Color(0xFF00CEC9).withValues(alpha: 0.1),
                  borderRadius: BorderRadius.circular(20),
                  border: Border.all(color: const Color(0xFF00CEC9).withValues(alpha: 0.4)),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    const Row(
                      children: [
                        Icon(Icons.lightbulb_rounded, color: Color(0xFF00CEC9), size: 20),
                        SizedBox(width: 8),
                        Text(
                          'Çözüm Açıklaması',
                          style: TextStyle(
                            color: Color(0xFF00CEC9),
                            fontWeight: FontWeight.bold,
                            fontSize: 15,
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 10),
                    Text(
                      currentQ.explanation,
                      style: TextStyle(
                        color: textColor.withValues(alpha: 0.9),
                        fontSize: 14,
                        height: 1.5,
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 24),
              SizedBox(
                width: double.infinity,
                height: 52,
                child: ElevatedButton.icon(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: const Color(0xFF00CEC9),
                    foregroundColor: const Color(0xFF0F172A),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(16),
                    ),
                  ),
                  icon: const Icon(Icons.arrow_forward_rounded),
                  label: Text(
                    _currentIndex < _questions.length - 1 ? 'Sonraki Soru' : 'Sonuçları Gör',
                    style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
                  ),
                  onPressed: _nextQuestion,
                ),
              ),
              const SizedBox(height: 20),
            ],
          ],
        ),
      ),
    );
  }
}
