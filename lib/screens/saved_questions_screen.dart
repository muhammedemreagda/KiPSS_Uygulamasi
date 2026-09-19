import 'package:flutter/material.dart';
import '../models/kpss_models.dart';
import '../services/data_service.dart';
import 'quiz_screen.dart';

class SavedQuestionsScreen extends StatefulWidget {
  final int initialTabIndex;
  const SavedQuestionsScreen({super.key, this.initialTabIndex = 0});

  @override
  State<SavedQuestionsScreen> createState() => _SavedQuestionsScreenState();
}

class _SavedQuestionsScreenState extends State<SavedQuestionsScreen> with SingleTickerProviderStateMixin {
  final DataService _dataService = DataService();
  late TabController _tabController;
  final Set<String> _expandedExplanations = {};

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 2, vsync: this, initialIndex: widget.initialTabIndex);
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  void _startCustomQuiz(List<QuestionModel> questions, String title) {
    if (questions.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Test başlatmak için soru bulunamadı!')),
      );
      return;
    }
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => QuizScreen(
          topic: TopicModel(
            id: 'custom-saved',
            courseId: 'general',
            title: title,
            slug: 'custom',
            importanceWeight: 1.0,
            sortOrder: 1,
          ),
          customQuestions: questions,
        ),
      ),
    ).then((_) => setState(() {}));
  }

  @override
  Widget build(BuildContext context) {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final bookmarkedList = _dataService.getBookmarkedQuestions();
    final wrongList = _dataService.getWrongQuestions();

    final bgColor = isDark ? const Color(0xFF0F172A) : const Color(0xFFF1F5F9);
    final cardBgColor = isDark ? const Color(0xFF1E293B) : Colors.white;
    final textColor = isDark ? Colors.white : const Color(0xFF0F172A);
    final subTextColor = isDark ? Colors.white60 : const Color(0xFF64748B);

    return Scaffold(
      backgroundColor: bgColor,
      appBar: AppBar(
        title: Text(
          'Sorularım & Havuz 📚',
          style: TextStyle(color: textColor, fontWeight: FontWeight.bold),
        ),
        bottom: TabBar(
          controller: _tabController,
          indicatorColor: const Color(0xFF00CEC9),
          labelColor: const Color(0xFF00CEC9),
          unselectedLabelColor: subTextColor,
          labelStyle: const TextStyle(fontWeight: FontWeight.bold, fontSize: 13.5),
          tabs: [
            Tab(
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Icon(Icons.star_rounded, size: 18),
                  const SizedBox(width: 6),
                  Flexible(
                    child: Text(
                      'Favorilerim (${bookmarkedList.length})',
                      overflow: TextOverflow.ellipsis,
                    ),
                  ),
                ],
              ),
            ),
            Tab(
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Icon(Icons.cancel_outlined, size: 18),
                  const SizedBox(width: 6),
                  Flexible(
                    child: Text(
                      'Yanlışlarım (${wrongList.length})',
                      overflow: TextOverflow.ellipsis,
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
      body: TabBarView(
        controller: _tabController,
        children: [
          // --- TAB 1: FAVORİ SORULARIM ---
          _buildQuestionList(
            questions: bookmarkedList,
            emptyMessage: 'Henüz favorilere eklenmiş soru yok.\nTest ve denemelerde yıldız ikonuna basarak soruları buraya kaydedebilirsiniz!',
            emptyIcon: Icons.star_border_rounded,
            cardBgColor: cardBgColor,
            textColor: textColor,
            subTextColor: subTextColor,
            isBookmarkedTab: true,
          ),

          // --- TAB 2: YANLIŞ SORULARIM ---
          _buildQuestionList(
            questions: wrongList,
            emptyMessage: 'Tebrikler! Yanlış sorular havuzunuz boş.\nÇözdüğünüz denemelerde yanlış yaptığınız tüm sorular otomatik olarak buraya eklenir.',
            emptyIcon: Icons.check_circle_outline_rounded,
            cardBgColor: cardBgColor,
            textColor: textColor,
            subTextColor: subTextColor,
            isBookmarkedTab: false,
          ),
        ],
      ),
    );
  }

  Widget _buildQuestionList({
    required List<QuestionModel> questions,
    required String emptyMessage,
    required IconData emptyIcon,
    required Color cardBgColor,
    required Color textColor,
    required Color subTextColor,
    required bool isBookmarkedTab,
  }) {
    final isDark = Theme.of(context).brightness == Brightness.dark;

    if (questions.isEmpty) {
      return Center(
        child: Padding(
          padding: const EdgeInsets.all(32.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(emptyIcon, size: 64, color: const Color(0xFF00CEC9).withValues(alpha: 0.5)),
              const SizedBox(height: 16),
              Text(
                emptyMessage,
                textAlign: TextAlign.center,
                style: TextStyle(color: subTextColor, fontSize: 14, height: 1.5),
              ),
            ],
          ),
        ),
      );
    }

    return Column(
      children: [
        // Action Bar for starting practice quiz
        Container(
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
          color: cardBgColor,
          child: Row(
            children: [
              Expanded(
                child: ElevatedButton.icon(
                  onPressed: () {
                    final title = isBookmarkedTab ? 'Favori Sorular Özel Testi' : 'Yanlış Sorular Özel Tekrar Testi';
                    _startCustomQuiz(questions, title);
                  },
                  icon: const Icon(Icons.play_arrow_rounded, color: Colors.white),
                  label: FittedBox(
                    fit: BoxFit.scaleDown,
                    child: Text(
                      isBookmarkedTab ? 'Favorilerle Test Başlat (${questions.length})' : 'Yanlışlarla Tekrar Çöz (${questions.length})',
                      style: const TextStyle(fontWeight: FontWeight.bold, color: Colors.white),
                    ),
                  ),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: isBookmarkedTab ? const Color(0xFF0984E3) : const Color(0xFFE17055),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                    padding: const EdgeInsets.symmetric(vertical: 12, horizontal: 12),
                  ),
                ),
              ),
              if (!isBookmarkedTab && questions.isNotEmpty) ...[
                const SizedBox(width: 8),
                IconButton(
                  tooltip: 'Tüm Yanlışları Temizle',
                  icon: const Icon(Icons.delete_sweep_rounded, color: Colors.redAccent),
                  onPressed: () {
                    showDialog(
                      context: context,
                      builder: (ctx) => AlertDialog(
                        backgroundColor: cardBgColor,
                        title: Text('Yanlışlar Havuzunu Temizle', style: TextStyle(color: textColor)),
                        content: Text('Tüm yanlış soru kayıtları silinsin mi?', style: TextStyle(color: subTextColor)),
                        actions: [
                          TextButton(onPressed: () => Navigator.pop(ctx), child: const Text('İptal')),
                          ElevatedButton(
                            onPressed: () {
                              _dataService.clearWrongQuestions();
                              Navigator.pop(ctx);
                              setState(() {});
                            },
                            style: ElevatedButton.styleFrom(backgroundColor: Colors.redAccent),
                            child: const Text('Temizle', style: TextStyle(color: Colors.white)),
                          )
                        ],
                      ),
                    );
                  },
                )
              ]
            ],
          ),
        ),

        // Questions List
        Expanded(
          child: ListView.separated(
            padding: const EdgeInsets.all(16),
            itemCount: questions.length,
            separatorBuilder: (ctx, i) => const SizedBox(height: 12),
            itemBuilder: (ctx, index) {
              final q = questions[index];
              final topic = _dataService.getTopicById(q.topicId);
              final course = topic != null ? _dataService.getCourseById(topic.courseId) : null;
              final isExpanded = _expandedExplanations.contains(q.id);

              return Container(
                padding: const EdgeInsets.all(16),
                decoration: BoxDecoration(
                  color: cardBgColor,
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(color: isDark ? Colors.white.withValues(alpha: 0.05) : Colors.grey.shade200),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    // Topic Header & Actions (Overflow Fixed with Expanded!)
                    Row(
                      children: [
                        Expanded(
                          child: Container(
                            padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
                            decoration: BoxDecoration(
                              color: const Color(0xFF00CEC9).withValues(alpha: 0.15),
                              borderRadius: BorderRadius.circular(8),
                            ),
                            child: Text(
                              '${course?.title ?? 'Ders'} • ${topic?.title ?? 'Konu'}',
                              overflow: TextOverflow.ellipsis,
                              maxLines: 1,
                              style: const TextStyle(
                                color: Color(0xFF00CEC9),
                                fontSize: 11.5,
                                fontWeight: FontWeight.bold,
                              ),
                            ),
                          ),
                        ),
                        const SizedBox(width: 8),
                        Row(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            IconButton(
                              constraints: const BoxConstraints(),
                              padding: const EdgeInsets.all(6),
                              icon: Icon(
                                _dataService.isBookmarked(q.id) ? Icons.star_rounded : Icons.star_border_rounded,
                                color: const Color(0xFFFFD166),
                                size: 22,
                              ),
                              onPressed: () {
                                setState(() {
                                  _dataService.toggleBookmark(q.id);
                                });
                              },
                            ),
                            if (!isBookmarkedTab)
                              IconButton(
                                constraints: const BoxConstraints(),
                                padding: const EdgeInsets.all(6),
                                icon: const Icon(Icons.check_circle_outline_rounded, color: Colors.green, size: 20),
                                tooltip: 'Öğrendim (Havuzdan Çıkar)',
                                onPressed: () {
                                  setState(() {
                                    _dataService.removeWrongQuestion(q.id);
                                  });
                                },
                              ),
                          ],
                        )
                      ],
                    ),
                    const SizedBox(height: 10),

                    // Question Text
                    Text(
                      q.questionText,
                      style: TextStyle(color: textColor, fontSize: 14.5, fontWeight: FontWeight.w600, height: 1.4),
                    ),
                    const SizedBox(height: 12),

                    // Options List (Overflow Fixed with Expanded!)
                    ...q.options.map((opt) {
                      final isCorrectOption = opt.key == q.correctOption;
                      return Container(
                        margin: const EdgeInsets.only(bottom: 6),
                        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
                        decoration: BoxDecoration(
                          color: isCorrectOption
                              ? Colors.green.withValues(alpha: 0.15)
                              : (isDark ? Colors.white.withValues(alpha: 0.05) : Colors.grey.withValues(alpha: 0.06)),
                          borderRadius: BorderRadius.circular(10),
                          border: Border.all(
                            color: isCorrectOption ? Colors.green : Colors.transparent,
                            width: 1,
                          ),
                        ),
                        child: Row(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            CircleAvatar(
                              radius: 11,
                              backgroundColor: isCorrectOption ? Colors.green : Colors.grey.withValues(alpha: 0.3),
                              child: Text(
                                opt.key,
                                style: TextStyle(
                                  fontSize: 11,
                                  fontWeight: FontWeight.bold,
                                  color: isCorrectOption ? Colors.white : textColor,
                                ),
                              ),
                            ),
                            const SizedBox(width: 10),
                            Expanded(
                              child: Text(
                                opt.text,
                                style: TextStyle(
                                  color: isCorrectOption ? Colors.green : textColor,
                                  fontSize: 13,
                                  fontWeight: isCorrectOption ? FontWeight.bold : FontWeight.normal,
                                  height: 1.3,
                                ),
                              ),
                            ),
                            if (isCorrectOption) ...[
                              const SizedBox(width: 6),
                              const Icon(Icons.check_circle_rounded, color: Colors.green, size: 16),
                            ],
                          ],
                        ),
                      );
                    }),
                    const SizedBox(height: 8),

                    // Solution Toggle
                    InkWell(
                      onTap: () {
                        setState(() {
                          if (isExpanded) {
                            _expandedExplanations.remove(q.id);
                          } else {
                            _expandedExplanations.add(q.id);
                          }
                        });
                      },
                      child: Padding(
                        padding: const EdgeInsets.symmetric(vertical: 4.0),
                        child: Row(
                          children: [
                            const Icon(Icons.lightbulb_outline_rounded, color: Color(0xFF00CEC9), size: 16),
                            const SizedBox(width: 6),
                            Text(
                              isExpanded ? 'Detaylı Çözümü Gizle' : 'Detaylı Çözümü Gör',
                              style: const TextStyle(color: Color(0xFF00CEC9), fontSize: 12, fontWeight: FontWeight.bold),
                            ),
                            Icon(
                              isExpanded ? Icons.keyboard_arrow_up_rounded : Icons.keyboard_arrow_down_rounded,
                              color: const Color(0xFF00CEC9),
                              size: 18,
                            ),
                          ],
                        ),
                      ),
                    ),

                    if (isExpanded) ...[
                      const SizedBox(height: 8),
                      Container(
                        padding: const EdgeInsets.all(12),
                        decoration: BoxDecoration(
                          color: const Color(0xFF00CEC9).withValues(alpha: 0.1),
                          borderRadius: BorderRadius.circular(10),
                          border: Border.all(color: const Color(0xFF00CEC9).withValues(alpha: 0.3)),
                        ),
                        child: Text(
                          q.explanation,
                          style: TextStyle(color: textColor, fontSize: 12.5, height: 1.4),
                        ),
                      ),
                    ]
                  ],
                ),
              );
            },
          ),
        ),
      ],
    );
  }
}
