class KpssCountdownService {
  /// Returns the next upcoming KPSS Lisans Exam DateTime.
  /// Standard ÖSYM KPSS Lisans exam is held in September.
  static DateTime getNextExamDate() {
    final now = DateTime.now();

    // 2026 KPSS Lisans: 6 September 2026, 10:15 AM
    final exam2026 = DateTime(2026, 9, 6, 10, 15);
    if (now.isBefore(exam2026)) {
      return exam2026;
    }

    // 2027 KPSS Lisans: 5 September 2027, 10:15 AM
    final exam2027 = DateTime(2027, 9, 5, 10, 15);
    if (now.isBefore(exam2027)) {
      return exam2027;
    }

    // Fallback: 1 year from now
    return DateTime(now.year + 1, 9, 5, 10, 15);
  }

  /// Formats remaining time with live ticking days, hours, minutes, and seconds
  static String getRemainingFormatted() {
    final now = DateTime.now();
    final examDate = getNextExamDate();
    final difference = examDate.difference(now);

    if (difference.isNegative) {
      return 'Sınav Günü!';
    }

    final days = difference.inDays;
    final hours = difference.inHours % 24;
    final minutes = difference.inMinutes % 60;
    final seconds = difference.inSeconds % 60;

    return '$days G $hours Sa $minutes Dk $seconds Sn';
  }

  /// Returns target exam year
  static int getTargetYear() {
    return getNextExamDate().year;
  }
}
