import 'dart:convert';
import 'dart:io';
import 'package:flutter/foundation.dart';
import '../models/mock_exam_model.dart';

class UserDataState {
  final double targetScore;
  final int userTotalAttempted;
  final int userTotalCorrect;
  final double userCurrentNetScore;
  final List<MockExam> completedExams;
  final Set<String> bookmarkedQuestionIds;
  final Set<String> wrongQuestionIds;
  final bool isDarkMode;

  UserDataState({
    required this.targetScore,
    required this.userTotalAttempted,
    required this.userTotalCorrect,
    required this.userCurrentNetScore,
    required this.completedExams,
    required this.bookmarkedQuestionIds,
    required this.wrongQuestionIds,
    required this.isDarkMode,
  });
}

class PersistenceService {
  static final PersistenceService _instance = PersistenceService._internal();
  factory PersistenceService() => _instance;
  PersistenceService._internal();

  File? _getLocalFile() {
    try {
      if (kIsWeb) return null;
      // Store in current directory or user home/app directory
      return File('kpss_user_data.json');
    } catch (_) {
      return null;
    }
  }

  Future<void> saveUserData({
    required double targetScore,
    required int userTotalAttempted,
    required int userTotalCorrect,
    required double userCurrentNetScore,
    required List<MockExam> completedExams,
    required Set<String> bookmarkedQuestionIds,
    required Set<String> wrongQuestionIds,
    required bool isDarkMode,
  }) async {
    try {
      final file = _getLocalFile();
      if (file == null) return;

      final Map<String, dynamic> data = {
        'targetScore': targetScore,
        'userTotalAttempted': userTotalAttempted,
        'userTotalCorrect': userTotalCorrect,
        'userCurrentNetScore': userCurrentNetScore,
        'bookmarkedQuestionIds': bookmarkedQuestionIds.toList(),
        'wrongQuestionIds': wrongQuestionIds.toList(),
        'isDarkMode': isDarkMode,
        'completedExams': completedExams.map((exam) => exam.toJson()).toList(),
      };

      final String jsonStr = jsonEncode(data);
      await file.writeAsString(jsonStr);
    } catch (e) {
      debugPrint('Error saving user data to persistence: $e');
    }
  }

  Future<UserDataState?> loadUserData() async {
    try {
      final file = _getLocalFile();
      if (file == null || !await file.exists()) return null;

      final String jsonStr = await file.readAsString();
      if (jsonStr.trim().isEmpty) return null;

      final Map<String, dynamic> data = jsonDecode(jsonStr);

      final double targetScore = (data['targetScore'] as num?)?.toDouble() ?? 88.5;
      final int userTotalAttempted = (data['userTotalAttempted'] as num?)?.toInt() ?? 142;
      final int userTotalCorrect = (data['userTotalCorrect'] as num?)?.toInt() ?? 118;
      final double userCurrentNetScore = (data['userCurrentNetScore'] as num?)?.toDouble() ?? 81.25;

      final Set<String> bookmarkedQuestionIds = (data['bookmarkedQuestionIds'] as List? ?? [])
          .map((e) => e.toString())
          .toSet();

      final Set<String> wrongQuestionIds = (data['wrongQuestionIds'] as List? ?? [])
          .map((e) => e.toString())
          .toSet();

      final bool isDarkMode = data['isDarkMode'] as bool? ?? true;

      final List<MockExam> completedExams = (data['completedExams'] as List? ?? [])
          .map((e) => MockExam.fromJson(e as Map<String, dynamic>))
          .toList();

      return UserDataState(
        targetScore: targetScore,
        userTotalAttempted: userTotalAttempted,
        userTotalCorrect: userTotalCorrect,
        userCurrentNetScore: userCurrentNetScore,
        completedExams: completedExams,
        bookmarkedQuestionIds: bookmarkedQuestionIds,
        wrongQuestionIds: wrongQuestionIds,
        isDarkMode: isDarkMode,
      );
    } catch (e) {
      debugPrint('Error loading user data from persistence: $e');
      return null;
    }
  }
}
