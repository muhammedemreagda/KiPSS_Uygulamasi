import 'dart:async';
import 'package:flutter/material.dart';
import '../models/mock_exam_model.dart';
import '../services/data_service.dart';
import 'exam_result_screen.dart';

class MockExamScreen extends StatefulWidget {
  final MockExam exam;

  const MockExamScreen({super.key, required this.exam});

  @override
  State<MockExamScreen> createState() => _MockExamScreenState();
}

class _MockExamScreenState extends State<MockExamScreen> {
  int _currentIndex = 0;
  Timer? _timer;
  late MockExam _exam;
  String _paletteFilter = 'all'; // 'all', 'flagged', 'blank', 'answered'

  @override
  void initState() {
    super.initState();
    _exam = widget.exam;
    _exam.startTime = DateTime.now();
    _startTimer();
  }

  void _startTimer() {
    _timer = Timer.periodic(const Duration(seconds: 1), (timer) {
      if (_exam.remainingTimeSeconds > 0) {
        setState(() {
          _exam.remainingTimeSeconds--;
        });
      } else {
        _timer?.cancel();
        _finishExam(isTimeUp: true);
      }
    });
  }

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }

  String _formatTimer(int totalSeconds) {
    int hours = totalSeconds ~/ 3600;
    int minutes = (totalSeconds % 3600) ~/ 60;
    int seconds = totalSeconds % 60;

    if (hours > 0) {
      return '${hours.toString().padLeft(2, '0')}:${minutes.toString().padLeft(2, '0')}:${seconds.toString().padLeft(2, '0')}';
    }
    return '${minutes.toString().padLeft(2, '0')}:${seconds.toString().padLeft(2, '0')}';
  }

  void _finishExam({bool isTimeUp = false}) {
    _timer?.cancel();
    _exam.isCompleted = true;
    _exam.endTime = DateTime.now();

    // Save completed exam to user's history and trigger weak topic analytics
    DataService().saveCompletedExam(_exam);

    if (isTimeUp) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Sınav süreniz doldu! Sonuçlarınız hesaplanıyor...'),
          backgroundColor: Colors.orange,
        ),
      );
    }

    Navigator.pushReplacement(
      context,
      MaterialPageRoute(
        builder: (context) => ExamResultScreen(exam: _exam),
      ),
    );
  }

  // Jump directly to the first question of a specific course
  void _jumpToCourse(String courseName) {
    int targetIndex = _exam.questions.indexWhere((q) => q.courseName == courseName);
    if (targetIndex != -1) {
      setState(() {
        _currentIndex = targetIndex;
      });
      ScaffoldMessenger.of(context).hideCurrentSnackBar();
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text('$courseName testine geçildi (Soru ${targetIndex + 1})'),
          duration: const Duration(seconds: 1),
          behavior: SnackBarBehavior.floating,
        ),
      );
    }
  }

  void _jumpToNextFlaggedQuestion() {
    int nextFlagged = _exam.questions.indexWhere((q) => q.isFlagged, _currentIndex + 1);
    if (nextFlagged == -1) {
      nextFlagged = _exam.questions.indexWhere((q) => q.isFlagged);
    }

    if (nextFlagged != -1) {
      setState(() {
        _currentIndex = nextFlagged;
      });
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('İşaretlenmiş (Daha Sonra Bakılacak) soru bulunmuyor.'),
          duration: Duration(seconds: 1),
        ),
      );
    }
  }

  void _showFinishConfirmationDialog() {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final dialogBg = isDark ? const Color(0xFF1E293B) : Colors.white;
    final textColor = isDark ? Colors.white : const Color(0xFF0F172A);
    final subTextColor = isDark ? Colors.white70 : const Color(0xFF64748B);

    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          backgroundColor: dialogBg,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
          title: Text(
            'Sınavı Bitir',
            style: TextStyle(fontWeight: FontWeight.bold, color: textColor),
          ),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text('Sınavı sonlandırmak istediğinize emin misiniz?', style: TextStyle(color: subTextColor)),
              const SizedBox(height: 14),
              Container(
                padding: const EdgeInsets.all(12),
                decoration: BoxDecoration(
                  color: isDark ? Colors.white10 : Colors.grey.shade100,
                  borderRadius: BorderRadius.circular(12),
                ),
                child: Column(
                  children: [
                    _buildDialogRow('Cevaplanan:', '${_exam.answeredCount} Soru', const Color(0xFF00CEC9), subTextColor),
                    const SizedBox(height: 4),
                    _buildDialogRow('Boş Bırakılan:', '${_exam.blankCount} Soru', const Color(0xFFFF7675), subTextColor),
                    const SizedBox(height: 4),
                    _buildDialogRow('İşaretlenen (Daha Sonra):', '${_exam.flaggedCount} Soru', const Color(0xFFFDCB6E), subTextColor),
                  ],
                ),
              ),
            ],
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.pop(context),
              child: const Text('Devam Et', style: TextStyle(color: Colors.grey)),
            ),
            ElevatedButton(
              onPressed: () {
                Navigator.pop(context);
                _finishExam();
              },
              style: ElevatedButton.styleFrom(
                backgroundColor: const Color(0xFF00CEC9),
                foregroundColor: const Color(0xFF0F172A),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
              ),
              child: const Text('Evet, Bitir', style: TextStyle(fontWeight: FontWeight.bold)),
            ),
          ],
        );
      },
    );
  }

  Widget _buildDialogRow(String label, String value, Color color, Color subTextColor) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        Text(label, style: TextStyle(fontSize: 12, color: subTextColor)),
        Text(value, style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: color)),
      ],
    );
  }

  void _showQuestionPaletteModal() {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final bgColor = isDark ? const Color(0xFF0F172A) : Colors.white;
    final textColor = isDark ? Colors.white : const Color(0xFF0F172A);

    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: bgColor,
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
      ),
      builder: (context) {
        return StatefulBuilder(
          builder: (context, setModalState) {
            List<int> filteredIndices = [];
            for (int i = 0; i < _exam.totalQuestions; i++) {
              final item = _exam.questions[i];
              if (_paletteFilter == 'flagged' && !item.isFlagged) continue;
              if (_paletteFilter == 'blank' && !item.isBlank) continue;
              if (_paletteFilter == 'answered' && !item.isAnswered) continue;
              filteredIndices.add(i);
            }

            return Container(
              height: MediaQuery.of(context).size.height * 0.75,
              padding: const EdgeInsets.all(16),
              child: Column(
                children: [
                  Container(
                    width: 40,
                    height: 4,
                    decoration: BoxDecoration(
                      color: isDark ? Colors.white24 : Colors.grey.shade300,
                      borderRadius: BorderRadius.circular(2),
                    ),
                  ),
                  const SizedBox(height: 12),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text(
                        'Soru Gezinti Paleti 🎯',
                        style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: textColor),
                      ),
                      IconButton(
                        icon: Icon(Icons.close, color: textColor),
                        onPressed: () => Navigator.pop(context),
                      ),
                    ],
                  ),
                  const SizedBox(height: 10),

                  // Filter Chips
                  SingleChildScrollView(
                    scrollDirection: Axis.horizontal,
                    child: Row(
                      children: [
                        _buildFilterChip('Tümü (${_exam.totalQuestions})', 'all', setModalState, isDark, textColor),
                        _buildFilterChip('Boş (${_exam.blankCount})', 'blank', setModalState, isDark, textColor),
                        _buildFilterChip('Cevaplanan (${_exam.answeredCount})', 'answered', setModalState, isDark, textColor),
                        _buildFilterChip('İşaretli (${_exam.flaggedCount})', 'flagged', setModalState, isDark, textColor),
                      ],
                    ),
                  ),
                  const SizedBox(height: 16),

                  // Grid of Questions
                  Expanded(
                    child: filteredIndices.isEmpty
                        ? const Center(
                            child: Text('Bu filtreye uygun soru bulunamadı.'),
                          )
                        : GridView.builder(
                            gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                              crossAxisCount: 6,
                              crossAxisSpacing: 8,
                              mainAxisSpacing: 8,
                            ),
                            itemCount: filteredIndices.length,
                            itemBuilder: (ctx, idx) {
                              final index = filteredIndices[idx];
                              final item = _exam.questions[index];
                              final isCurrent = index == _currentIndex;

                              Color cellBg = isDark ? const Color(0xFF1E293B) : Colors.grey.shade200;
                              Color cellTextColor = textColor;

                              if (item.isFlagged) {
                                cellBg = const Color(0xFFFDCB6E);
                                cellTextColor = const Color(0xFF2D3436);
                              } else if (item.isAnswered) {
                                cellBg = const Color(0xFF00CEC9);
                                cellTextColor = const Color(0xFF0F172A);
                              }

                              return InkWell(
                                onTap: () {
                                  setState(() {
                                    _currentIndex = index;
                                  });
                                  Navigator.pop(context);
                                },
                                borderRadius: BorderRadius.circular(10),
                                child: Container(
                                  decoration: BoxDecoration(
                                    color: cellBg,
                                    borderRadius: BorderRadius.circular(10),
                                    border: isCurrent
                                        ? Border.all(color: const Color(0xFF6C5CE7), width: 3)
                                        : Border.all(color: Colors.transparent),
                                  ),
                                  alignment: Alignment.center,
                                  child: Text(
                                    '${index + 1}',
                                    style: TextStyle(
                                      color: cellTextColor,
                                      fontWeight: FontWeight.bold,
                                      fontSize: 13,
                                    ),
                                  ),
                                ),
                              );
                            },
                          ),
                  ),
                ],
              ),
            );
          },
        );
      },
    );
  }

  Widget _buildFilterChip(String label, String value, StateSetter setModalState, bool isDark, Color textColor) {
    final isSelected = _paletteFilter == value;
    return Padding(
      padding: const EdgeInsets.only(right: 6.0),
      child: ChoiceChip(
        label: Text(label),
        selected: isSelected,
        selectedColor: const Color(0xFF00CEC9),
        backgroundColor: isDark ? const Color(0xFF1E293B) : Colors.grey.shade200,
        side: BorderSide(color: isSelected ? const Color(0xFF00CEC9) : Colors.transparent),
        labelStyle: TextStyle(
          color: isSelected ? const Color(0xFF0F172A) : textColor,
          fontSize: 11,
          fontWeight: isSelected ? FontWeight.bold : FontWeight.w600,
        ),
        onSelected: (selected) {
          if (selected) {
            setModalState(() {
              _paletteFilter = value;
            });
          }
        },
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final bgColor = isDark ? const Color(0xFF0F172A) : const Color(0xFFF1F5F9);
    final cardBgColor = isDark ? const Color(0xFF1E293B) : Colors.white;
    final textColor = isDark ? Colors.white : const Color(0xFF0F172A);
    final subTextColor = isDark ? Colors.white60 : const Color(0xFF64748B);

    final currentItem = _exam.questions[_currentIndex];
    final question = currentItem.question;

    // Distinct list of courses in this exam for Subject Jump Bar
    final courseNames = _exam.questions.map((q) => q.courseName).toSet().toList();

    return PopScope(
      canPop: false,
      onPopInvokedWithResult: (didPop, result) {
        if (didPop) return;
        _showFinishConfirmationDialog();
      },
      child: Scaffold(
        backgroundColor: bgColor,
        appBar: AppBar(
          backgroundColor: Colors.transparent,
          elevation: 0,
          title: Row(
            children: [
              const Icon(Icons.timer_outlined, color: Color(0xFF00CEC9), size: 20),
              const SizedBox(width: 6),
              Text(
                _formatTimer(_exam.remainingTimeSeconds),
                style: const TextStyle(
                  color: Color(0xFF00CEC9),
                  fontWeight: FontWeight.bold,
                  fontSize: 16,
                ),
              ),
            ],
          ),
          actions: [
            IconButton(
              icon: Badge(
                label: Text('${_exam.flaggedCount}'),
                isLabelVisible: _exam.flaggedCount > 0,
                backgroundColor: const Color(0xFFFDCB6E),
                textColor: Colors.black87,
                child: const Icon(Icons.bookmark_rounded, color: Colors.amber),
              ),
              tooltip: 'İşaretli Sorulara Git',
              onPressed: _jumpToNextFlaggedQuestion,
            ),
            IconButton(
              icon: Icon(Icons.grid_view_rounded, color: textColor),
              tooltip: 'Soru Paleti',
              onPressed: _showQuestionPaletteModal,
            ),
            TextButton(
              onPressed: _showFinishConfirmationDialog,
              child: const Text(
                'Bitir',
                style: TextStyle(
                  color: Color(0xFFFF7675),
                  fontWeight: FontWeight.bold,
                  fontSize: 15,
                ),
              ),
            ),
          ],
        ),
        body: Column(
          children: [
            // SUBJECT JUMP BAR (Dersler Arası Hızlı Kayma Çubuğu)
            if (courseNames.length > 1)
              Container(
                height: 44,
                color: cardBgColor,
                child: ListView.builder(
                  scrollDirection: Axis.horizontal,
                  padding: const EdgeInsets.symmetric(horizontal: 10),
                  itemCount: courseNames.length,
                  itemBuilder: (context, idx) {
                    final cName = courseNames[idx];
                    final isCurrentCourse = currentItem.courseName == cName;

                    return Padding(
                      padding: const EdgeInsets.only(right: 6.0, bottom: 6),
                      child: ActionChip(
                        label: Text(cName),
                        backgroundColor: isCurrentCourse
                            ? const Color(0xFF00CEC9)
                            : (isDark ? const Color(0xFF0F172A) : Colors.grey.shade200),
                        labelStyle: TextStyle(
                          color: isCurrentCourse ? const Color(0xFF0F172A) : textColor,
                          fontSize: 11,
                          fontWeight: isCurrentCourse ? FontWeight.bold : FontWeight.normal,
                        ),
                        onPressed: () => _jumpToCourse(cName),
                      ),
                    );
                  },
                ),
              ),

            // Question Header Progress Bar
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
              color: cardBgColor,
              child: Row(
                children: [
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          '${currentItem.courseName} • ${currentItem.topicTitle}',
                          overflow: TextOverflow.ellipsis,
                          style: const TextStyle(
                            color: Color(0xFF00CEC9),
                            fontWeight: FontWeight.bold,
                            fontSize: 12,
                          ),
                        ),
                        const SizedBox(height: 2),
                        Text(
                          'Soru ${_currentIndex + 1} / ${_exam.totalQuestions}',
                          style: TextStyle(color: subTextColor, fontSize: 11),
                        ),
                      ],
                    ),
                  ),
                  IconButton(
                    icon: Icon(
                      currentItem.isFlagged ? Icons.bookmark_rounded : Icons.bookmark_border_rounded,
                      color: currentItem.isFlagged ? const Color(0xFFFDCB6E) : subTextColor,
                    ),
                    tooltip: currentItem.isFlagged ? 'İşareti Kaldır' : 'Daha Sonra Bak (İşaretle)',
                    onPressed: () {
                      setState(() {
                        currentItem.isFlagged = !currentItem.isFlagged;
                      });
                    },
                  ),
                ],
              ),
            ),

            // QUESTION CONTENT & OPTIONS
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

                    // Options List
                    ...question.options.map((opt) {
                      final isSelected = currentItem.selectedOptionKey == opt.key;

                      return Container(
                        margin: const EdgeInsets.only(bottom: 10),
                        child: InkWell(
                          onTap: () {
                            setState(() {
                              if (isSelected) {
                                currentItem.selectedOptionKey = null; // Clear answer
                              } else {
                                currentItem.selectedOptionKey = opt.key;
                              }
                            });
                          },
                          borderRadius: BorderRadius.circular(14),
                          child: Container(
                            padding: const EdgeInsets.all(14),
                            decoration: BoxDecoration(
                              color: isSelected
                                  ? const Color(0xFF00CEC9).withValues(alpha: 0.2)
                                  : cardBgColor,
                              borderRadius: BorderRadius.circular(14),
                              border: Border.all(
                                color: isSelected ? const Color(0xFF00CEC9) : (isDark ? Colors.white.withValues(alpha: 0.05) : Colors.grey.shade200),
                                width: isSelected ? 2 : 1,
                              ),
                            ),
                            child: Row(
                              children: [
                                CircleAvatar(
                                  radius: 12,
                                  backgroundColor: isSelected
                                      ? const Color(0xFF00CEC9)
                                      : (isDark ? Colors.white10 : Colors.grey.shade200),
                                  child: Text(
                                    opt.key,
                                    style: TextStyle(
                                      fontSize: 11,
                                      fontWeight: FontWeight.bold,
                                      color: isSelected ? const Color(0xFF0F172A) : textColor,
                                    ),
                                  ),
                                ),
                                const SizedBox(width: 12),
                                Expanded(
                                  child: Text(
                                    opt.text,
                                    style: TextStyle(
                                      color: textColor,
                                      fontSize: 13.5,
                                      fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
                                    ),
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ),
                      );
                    }),
                  ],
                ),
              ),
            ),

            // BOTTOM PREV / NEXT NAVIGATION BAR
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
              color: cardBgColor,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  OutlinedButton.icon(
                    onPressed: _currentIndex > 0
                        ? () {
                            setState(() {
                              _currentIndex--;
                            });
                          }
                        : null,
                    icon: const Icon(Icons.arrow_back_rounded, size: 16),
                    label: const Text('Önceki Soru'),
                  ),
                  OutlinedButton.icon(
                    onPressed: () {
                      setState(() {
                        currentItem.selectedOptionKey = null;
                      });
                    },
                    icon: const Icon(Icons.clear_rounded, size: 16, color: Colors.orange),
                    label: const Text('Temizle', style: TextStyle(color: Colors.orange, fontSize: 12)),
                  ),
                  ElevatedButton.icon(
                    onPressed: _currentIndex < _exam.totalQuestions - 1
                        ? () {
                            setState(() {
                              _currentIndex++;
                            });
                          }
                        : _showFinishConfirmationDialog,
                    style: ElevatedButton.styleFrom(
                      backgroundColor: const Color(0xFF00CEC9),
                      foregroundColor: const Color(0xFF0F172A),
                    ),
                    icon: Icon(_currentIndex < _exam.totalQuestions - 1 ? Icons.arrow_forward_rounded : Icons.check_circle_rounded, size: 16),
                    label: Text(_currentIndex < _exam.totalQuestions - 1 ? 'Sonraki Soru' : 'Sınavı Bitir'),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
