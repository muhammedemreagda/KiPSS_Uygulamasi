import 'package:flutter/material.dart';
import '../models/mock_exam_model.dart';
import '../services/data_service.dart';
import 'mock_exam_screen.dart';

class ExamSetupModal extends StatefulWidget {
  const ExamSetupModal({super.key});

  @override
  State<ExamSetupModal> createState() => _ExamSetupModalState();
}

class _ExamSetupModalState extends State<ExamSetupModal> {
  ExamType _selectedType = ExamType.full;
  String _selectedCourseId = 'course-turkce';
  int _customQuestionCount = 15;

  @override
  Widget build(BuildContext context) {
    final dataService = DataService();
    final courses = dataService.courses;

    final isDark = Theme.of(context).brightness == Brightness.dark;
    final bgColor = isDark ? const Color(0xFF0F172A) : Colors.white;
    final cardBgColor = isDark ? const Color(0xFF1E293B) : const Color(0xFFF8FAFC);
    final textColor = isDark ? Colors.white : const Color(0xFF0F172A);
    final subTextColor = isDark ? Colors.white60 : const Color(0xFF64748B);

    return Container(
      padding: EdgeInsets.only(
        left: 20,
        right: 20,
        top: 20,
        bottom: MediaQuery.of(context).viewInsets.bottom + 20,
      ),
      decoration: BoxDecoration(
        color: bgColor,
        borderRadius: const BorderRadius.vertical(top: Radius.circular(24)),
        border: const Border(top: BorderSide(color: Color(0xFF00CEC9), width: 1.5)),
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Center(
            child: Container(
              width: 40,
              height: 4,
              decoration: BoxDecoration(
                color: isDark ? Colors.white24 : Colors.grey.shade300,
                borderRadius: BorderRadius.circular(2),
              ),
            ),
          ),
          const SizedBox(height: 16),
          Row(
            children: [
              Container(
                padding: const EdgeInsets.all(8),
                decoration: BoxDecoration(
                  color: const Color(0xFF00CEC9).withValues(alpha: 0.2),
                  borderRadius: BorderRadius.circular(12),
                ),
                child: const Icon(
                  Icons.assignment_outlined,
                  color: Color(0xFF00CEC9),
                ),
              ),
              const SizedBox(width: 12),
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Deneme Sınavı Oluştur 📝',
                    style: TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                      color: textColor,
                    ),
                  ),
                  Text(
                    'Sınav türünü ve soru sayısını seçin',
                    style: TextStyle(
                      fontSize: 12,
                      color: subTextColor,
                    ),
                  ),
                ],
              ),
            ],
          ),
          const SizedBox(height: 20),

          // Exam Type Cards
          _buildTypeOption(
            type: ExamType.full,
            title: 'Tam Gerçek KPSS Denemesi',
            subtitle: '120 Soru • 130 Dakika • Tüm Müfredat',
            icon: Icons.timer_outlined,
            color: const Color(0xFF00CEC9),
            cardBgColor: cardBgColor,
            textColor: textColor,
            subTextColor: subTextColor,
            isDark: isDark,
          ),
          const SizedBox(height: 10),
          _buildTypeOption(
            type: ExamType.mini,
            title: 'Hızlı Mini Deneme',
            subtitle: '30 Soru • 35 Dakika • Karma Pratik',
            icon: Icons.flash_on_rounded,
            color: const Color(0xFFFDCB6E),
            cardBgColor: cardBgColor,
            textColor: textColor,
            subTextColor: subTextColor,
            isDark: isDark,
          ),
          const SizedBox(height: 10),
          _buildTypeOption(
            type: ExamType.customSubject,
            title: 'Özel Branş Denemesi',
            subtitle: 'Seçeceğiniz tek bir ders üzerinden özel test',
            icon: Icons.topic_outlined,
            color: const Color(0xFF6C5CE7),
            cardBgColor: cardBgColor,
            textColor: textColor,
            subTextColor: subTextColor,
            isDark: isDark,
          ),

          if (_selectedType == ExamType.customSubject) ...[
            const SizedBox(height: 16),
            Container(
              padding: const EdgeInsets.all(14),
              decoration: BoxDecoration(
                color: cardBgColor,
                borderRadius: BorderRadius.circular(16),
                border: Border.all(color: const Color(0xFF6C5CE7).withValues(alpha: 0.3)),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text('Ders Seçin:', style: TextStyle(fontWeight: FontWeight.bold, color: textColor, fontSize: 13)),
                  const SizedBox(height: 8),
                  DropdownButtonFormField<String>(
                    value: _selectedCourseId,
                    dropdownColor: cardBgColor,
                    style: TextStyle(color: textColor, fontSize: 13.5),
                    decoration: InputDecoration(
                      contentPadding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
                      filled: true,
                      fillColor: isDark ? Colors.white.withValues(alpha: 0.05) : Colors.grey.shade100,
                      border: OutlineInputBorder(borderRadius: BorderRadius.circular(10), borderSide: BorderSide.none),
                    ),
                    items: courses.map((c) => DropdownMenuItem(value: c.id, child: Text(c.title))).toList(),
                    onChanged: (val) {
                      if (val != null) setState(() => _selectedCourseId = val);
                    },
                  ),
                  const SizedBox(height: 12),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text('Soru Sayısı: $_customQuestionCount Soru', style: TextStyle(color: textColor, fontWeight: FontWeight.w600, fontSize: 13)),
                      Slider(
                        value: _customQuestionCount.toDouble(),
                        min: 5,
                        max: 30,
                        divisions: 5,
                        activeColor: const Color(0xFF6C5CE7),
                        onChanged: (v) => setState(() => _customQuestionCount = v.toInt()),
                      ),
                    ],
                  )
                ],
              ),
            ),
          ],

          const SizedBox(height: 24),

          // START EXAM BUTTON
          SizedBox(
            width: double.infinity,
            height: 50,
            child: ElevatedButton.icon(
              onPressed: () {
                MockExam newExam;
                if (_selectedType == ExamType.full) {
                  newExam = dataService.generateFullMockExam();
                } else if (_selectedType == ExamType.mini) {
                  newExam = dataService.generateMiniMockExam();
                } else {
                  newExam = dataService.generateSubjectMockExam(
                    courseId: _selectedCourseId,
                    questionCount: _customQuestionCount,
                  );
                }

                Navigator.pop(context); // Close modal
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => MockExamScreen(exam: newExam),
                  ),
                );
              },
              style: ElevatedButton.styleFrom(
                backgroundColor: const Color(0xFF00CEC9),
                foregroundColor: const Color(0xFF0F172A),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
              ),
              icon: const Icon(Icons.play_arrow_rounded),
              label: const Text(
                'Sınavı Başlat 🚀',
                style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildTypeOption({
    required ExamType type,
    required String title,
    required String subtitle,
    required IconData icon,
    required Color color,
    required Color cardBgColor,
    required Color textColor,
    required Color subTextColor,
    required bool isDark,
  }) {
    final isSelected = _selectedType == type;

    return InkWell(
      onTap: () => setState(() => _selectedType = type),
      borderRadius: BorderRadius.circular(16),
      child: Container(
        padding: const EdgeInsets.all(14),
        decoration: BoxDecoration(
          color: isSelected ? color.withValues(alpha: 0.15) : cardBgColor,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(
            color: isSelected ? color : (isDark ? Colors.white.withValues(alpha: 0.05) : Colors.grey.shade200),
            width: isSelected ? 2 : 1,
          ),
        ),
        child: Row(
          children: [
            Icon(icon, color: isSelected ? color : subTextColor, size: 24),
            const SizedBox(width: 12),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    title,
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      fontSize: 14,
                      color: isSelected ? color : textColor,
                    ),
                  ),
                  const SizedBox(height: 2),
                  Text(
                    subtitle,
                    style: TextStyle(fontSize: 11.5, color: subTextColor),
                  ),
                ],
              ),
            ),
            Radio<ExamType>(
              value: type,
              groupValue: _selectedType,
              activeColor: color,
              onChanged: (val) {
                if (val != null) setState(() => _selectedType = val);
              },
            ),
          ],
        ),
      ),
    );
  }
}
