import 'package:flutter/material.dart';
import '../services/kpss_score_calculator.dart';

class ScoreCalculatorScreen extends StatefulWidget {
  const ScoreCalculatorScreen({super.key});

  @override
  State<ScoreCalculatorScreen> createState() => _ScoreCalculatorScreenState();
}

class _ScoreCalculatorScreenState extends State<ScoreCalculatorScreen> {
  int _gyCorrect = 40;
  int _gyWrong = 10;
  int _gkCorrect = 42;
  int _gkWrong = 8;

  final TextEditingController _gyCorrectCtrl = TextEditingController();
  final TextEditingController _gyWrongCtrl = TextEditingController();
  final TextEditingController _gkCorrectCtrl = TextEditingController();
  final TextEditingController _gkWrongCtrl = TextEditingController();

  @override
  void initState() {
    super.initState();
    _updateControllers();
  }

  void _updateControllers() {
    _gyCorrectCtrl.text = '$_gyCorrect';
    _gyWrongCtrl.text = '$_gyWrong';
    _gkCorrectCtrl.text = '$_gkCorrect';
    _gkWrongCtrl.text = '$_gkWrong';
  }

  @override
  void dispose() {
    _gyCorrectCtrl.dispose();
    _gyWrongCtrl.dispose();
    _gkCorrectCtrl.dispose();
    _gkWrongCtrl.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final bgColor = isDark ? const Color(0xFF0F172A) : const Color(0xFFF1F5F9);
    final cardBgColor = isDark ? const Color(0xFF1E293B) : Colors.white;
    final textColor = isDark ? Colors.white : const Color(0xFF0F172A);
    final subTextColor = isDark ? Colors.white60 : const Color(0xFF64748B);

    double gyNet = KpssScoreCalculator.calculateNet(_gyCorrect, _gyWrong);
    double gkNet = KpssScoreCalculator.calculateNet(_gkCorrect, _gkWrong);
    double totalNet = gyNet + gkNet;

    final results = KpssScoreCalculator.calculate5YearScores(
      gyNet: gyNet,
      gkNet: gkNet,
    );

    return Scaffold(
      backgroundColor: bgColor,
      appBar: AppBar(
        title: Text('KPSS Net & Puan Simülatörü 🧮', style: TextStyle(color: textColor, fontWeight: FontWeight.bold)),
        backgroundColor: Colors.transparent,
        elevation: 0,
        leading: IconButton(
          icon: Icon(Icons.arrow_back_ios_new_rounded, color: textColor),
          onPressed: () => Navigator.pop(context),
        ),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // --- HEADER INFO CARD ---
            Container(
              padding: const EdgeInsets.all(18),
              decoration: BoxDecoration(
                gradient: const LinearGradient(
                  colors: [Color(0xFF00CEC9), Color(0xFF0984E3)],
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                ),
                borderRadius: BorderRadius.circular(20),
                boxShadow: [
                  BoxShadow(
                    color: const Color(0xFF00CEC9).withValues(alpha: 0.3),
                    blurRadius: 12,
                    offset: const Offset(0, 6),
                  ),
                ],
              ),
              child: Row(
                children: [
                  Container(
                    padding: const EdgeInsets.all(10),
                    decoration: BoxDecoration(
                      color: Colors.white.withValues(alpha: 0.2),
                      shape: BoxShape.circle,
                    ),
                    child: const Icon(Icons.calculate_rounded, color: Colors.white, size: 26),
                  ),
                  const SizedBox(width: 12),
                  const Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          'Resmi ÖSYM KPSS Puan Robotu 🎯',
                          style: TextStyle(
                            color: Colors.white,
                            fontSize: 16,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                        SizedBox(height: 3),
                        Text(
                          'Son 5 yılın ÖSYM net/puan dağılımlarına göre tam uyumlu hesaplama.',
                          style: TextStyle(color: Colors.white70, fontSize: 12),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),

            const SizedBox(height: 20),

            // --- NET INPUT CARDS ---
            Row(
              children: [
                // GY CARD
                Expanded(
                  child: _buildNetInputCard(
                    title: 'Genel Yetenek (60)',
                    correctCtrl: _gyCorrectCtrl,
                    wrongCtrl: _gyWrongCtrl,
                    netVal: gyNet,
                    cardBgColor: cardBgColor,
                    textColor: textColor,
                    subTextColor: subTextColor,
                    isDark: isDark,
                    onCorrectChanged: (v) => setState(() => _gyCorrect = v),
                    onWrongChanged: (v) => setState(() => _gyWrong = v),
                  ),
                ),
                const SizedBox(width: 12),
                // GK CARD
                Expanded(
                  child: _buildNetInputCard(
                    title: 'Genel Kültür (60)',
                    correctCtrl: _gkCorrectCtrl,
                    wrongCtrl: _gkWrongCtrl,
                    netVal: gkNet,
                    cardBgColor: cardBgColor,
                    textColor: textColor,
                    subTextColor: subTextColor,
                    isDark: isDark,
                    onCorrectChanged: (v) => setState(() => _gkCorrect = v),
                    onWrongChanged: (v) => setState(() => _gkWrong = v),
                  ),
                ),
              ],
            ),

            const SizedBox(height: 20),

            // --- TOTAL NET SUMMARY CARD ---
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 16),
              decoration: BoxDecoration(
                color: cardBgColor,
                borderRadius: BorderRadius.circular(18),
                border: Border.all(color: const Color(0xFF00CEC9).withValues(alpha: 0.4), width: 1.5),
              ),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Row(
                    children: [
                      const Icon(Icons.analytics_rounded, color: Color(0xFF00CEC9), size: 24),
                      const SizedBox(width: 10),
                      Text(
                        'Toplam Net Sayısı',
                        style: TextStyle(color: textColor, fontWeight: FontWeight.bold, fontSize: 15),
                      ),
                    ],
                  ),
                  Text(
                    '${totalNet.toStringAsFixed(2)} Net',
                    style: const TextStyle(color: Color(0xFF00CEC9), fontWeight: FontWeight.bold, fontSize: 20),
                  ),
                ],
              ),
            ),

            const SizedBox(height: 24),

            // --- 5 YEAR COMPARISON TABLE ---
            Text(
              '📊 Yıllara Göre Tahmini ÖSYM KPSS Puanları',
              style: TextStyle(color: textColor, fontSize: 16, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 12),

            ...results.map((r) => Container(
                  margin: const EdgeInsets.only(bottom: 12),
                  padding: const EdgeInsets.all(16),
                  decoration: BoxDecoration(
                    color: cardBgColor,
                    borderRadius: BorderRadius.circular(18),
                    border: Border.all(color: isDark ? Colors.white.withValues(alpha: 0.05) : Colors.grey.shade200),
                  ),
                  child: Column(
                    children: [
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Text(
                            r.label,
                            style: TextStyle(color: textColor, fontWeight: FontWeight.bold, fontSize: 15),
                          ),
                          Container(
                            padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                            decoration: BoxDecoration(
                              color: const Color(0xFF6C5CE7).withValues(alpha: 0.15),
                              borderRadius: BorderRadius.circular(10),
                            ),
                            child: Text(
                              'P3: ${r.p3Score.toStringAsFixed(2)}',
                              style: const TextStyle(color: Color(0xFF6C5CE7), fontWeight: FontWeight.bold, fontSize: 14),
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 12),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceAround,
                        children: [
                          _buildScorePill('P3 (Lisans)', r.p3Score.toStringAsFixed(2), const Color(0xFF6C5CE7)),
                          _buildScorePill('P1 (GY Ağ.)', r.p1Score.toStringAsFixed(2), const Color(0xFF00CEC9)),
                          _buildScorePill('P2 (GK Ağ.)', r.p2Score.toStringAsFixed(2), const Color(0xFF00B894)),
                        ],
                      ),
                    ],
                  ),
                )),
          ],
        ),
      ),
    );
  }

  Widget _buildNetInputCard({
    required String title,
    required TextEditingController correctCtrl,
    required TextEditingController wrongCtrl,
    required double netVal,
    required Color cardBgColor,
    required Color textColor,
    required Color subTextColor,
    required bool isDark,
    required ValueChanged<int> onCorrectChanged,
    required ValueChanged<int> onWrongChanged,
  }) {
    return Container(
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: cardBgColor,
        borderRadius: BorderRadius.circular(18),
        border: Border.all(color: isDark ? Colors.white.withValues(alpha: 0.05) : Colors.grey.shade200),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          FittedBox(
            fit: BoxFit.scaleDown,
            alignment: Alignment.centerLeft,
            child: Text(title, style: TextStyle(color: textColor, fontWeight: FontWeight.bold, fontSize: 13.5)),
          ),
          const SizedBox(height: 12),

          // Correct Count Input
          Row(
            children: [
              const Text('D:', style: TextStyle(color: Colors.green, fontWeight: FontWeight.bold, fontSize: 13)),
              const SizedBox(width: 6),
              Expanded(
                child: TextField(
                  controller: correctCtrl,
                  keyboardType: TextInputType.number,
                  style: TextStyle(color: textColor, fontSize: 13.5, fontWeight: FontWeight.bold),
                  decoration: InputDecoration(
                    contentPadding: const EdgeInsets.symmetric(horizontal: 10, vertical: 8),
                    filled: true,
                    fillColor: isDark ? Colors.white.withValues(alpha: 0.05) : Colors.grey.shade100,
                    border: OutlineInputBorder(borderRadius: BorderRadius.circular(10), borderSide: BorderSide.none),
                  ),
                  onChanged: (val) {
                    int c = int.tryParse(val) ?? 0;
                    onCorrectChanged(c.clamp(0, 60));
                  },
                ),
              ),
            ],
          ),
          const SizedBox(height: 8),

          // Wrong Count Input
          Row(
            children: [
              const Text('Y:', style: TextStyle(color: Colors.redAccent, fontWeight: FontWeight.bold, fontSize: 13)),
              const SizedBox(width: 6),
              Expanded(
                child: TextField(
                  controller: wrongCtrl,
                  keyboardType: TextInputType.number,
                  style: TextStyle(color: textColor, fontSize: 13.5, fontWeight: FontWeight.bold),
                  decoration: InputDecoration(
                    contentPadding: const EdgeInsets.symmetric(horizontal: 10, vertical: 8),
                    filled: true,
                    fillColor: isDark ? Colors.white.withValues(alpha: 0.05) : Colors.grey.shade100,
                    border: OutlineInputBorder(borderRadius: BorderRadius.circular(10), borderSide: BorderSide.none),
                  ),
                  onChanged: (val) {
                    int w = int.tryParse(val) ?? 0;
                    onWrongChanged(w.clamp(0, 60));
                  },
                ),
              ),
            ],
          ),
          const SizedBox(height: 12),

          // Net Value Pill
          Container(
            width: double.infinity,
            padding: const EdgeInsets.symmetric(vertical: 6),
            decoration: BoxDecoration(
              color: const Color(0xFF00CEC9).withValues(alpha: 0.15),
              borderRadius: BorderRadius.circular(10),
            ),
            child: Text(
              '${netVal.toStringAsFixed(2)} Net',
              textAlign: TextAlign.center,
              style: const TextStyle(color: Color(0xFF00CEC9), fontWeight: FontWeight.bold, fontSize: 13),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildScorePill(String label, String score, Color color) {
    return Column(
      children: [
        Text(label, style: const TextStyle(fontSize: 11, color: Colors.grey)),
        const SizedBox(height: 2),
        Text(score, style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: color)),
      ],
    );
  }
}
