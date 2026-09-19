import 'dart:convert';
import 'dart:io';
import 'package:flutter/foundation.dart';
import '../models/user_model.dart';

class AuthService {
  static final AuthService _instance = AuthService._internal();
  factory AuthService() => _instance;
  AuthService._internal();

  UserModel? currentUser;

  File? _getAuthFile() {
    try {
      if (kIsWeb) return null;
      return File('kpss_user_session.json');
    } catch (_) {
      return null;
    }
  }

  Future<void> initSession() async {
    try {
      final file = _getAuthFile();
      if (file == null || !await file.exists()) {
        // Create default demo user session if none exists
        _createDefaultDemoSession();
        return;
      }

      final jsonStr = await file.readAsString();
      if (jsonStr.trim().isEmpty) {
        _createDefaultDemoSession();
        return;
      }

      final Map<String, dynamic> data = jsonDecode(jsonStr);
      currentUser = UserModel.fromJson(data);
    } catch (e) {
      debugPrint('Error initializing user session: $e');
      _createDefaultDemoSession();
    }
  }

  void _createDefaultDemoSession() {
    currentUser = UserModel(
      id: 'user-demo-1',
      username: 'kpss_derece_adayi',
      displayName: 'Ahmet Yılmaz',
      email: 'ahmet@kpss.com',
      targetScore: 91.5,
      examLevel: 'lisans',
      badge: '🔥 90+ Hedefli',
      avatarUrl: '🎓',
    );
    saveSession();
  }

  Future<void> saveSession() async {
    try {
      final file = _getAuthFile();
      if (file == null || currentUser == null) return;
      await file.writeAsString(jsonEncode(currentUser!.toJson()));
    } catch (e) {
      debugPrint('Error saving session: $e');
    }
  }

  Future<bool> register({
    required String username,
    required String displayName,
    required String email,
    required String password,
    double targetScore = 88.5,
    String avatarUrl = '🎓',
  }) async {
    final newUser = UserModel(
      id: 'user-${DateTime.now().millisecondsSinceEpoch}',
      username: username.toLowerCase().replaceAll(' ', '_'),
      displayName: displayName,
      email: email,
      targetScore: targetScore,
      badge: '✨ Yeni Aday',
      avatarUrl: avatarUrl,
    );
    currentUser = newUser;
    await saveSession();
    return true;
  }

  Future<bool> login({required String emailOrUsername, required String password}) async {
    currentUser = UserModel(
      id: 'user-${DateTime.now().millisecondsSinceEpoch}',
      username: emailOrUsername.contains('@') ? emailOrUsername.split('@').first : emailOrUsername,
      displayName: emailOrUsername.split('@').first,
      email: emailOrUsername.contains('@') ? emailOrUsername : '$emailOrUsername@kpss.com',
      targetScore: 89.0,
      badge: '🎯 KPSS Adayı',
      avatarUrl: '🚀',
    );
    await saveSession();
    return true;
  }

  Future<bool> loginWithGoogle() async {
    currentUser = UserModel(
      id: 'user-google-${DateTime.now().millisecondsSinceEpoch}',
      username: 'google_adayi',
      displayName: 'Google ile Bağlandı',
      email: 'adayi@gmail.com',
      targetScore: 90.0,
      badge: '🌐 Google Adayı',
      avatarUrl: '🎯',
    );
    await saveSession();
    return true;
  }

  Future<bool> loginWithApple() async {
    currentUser = UserModel(
      id: 'user-apple-${DateTime.now().millisecondsSinceEpoch}',
      username: 'apple_adayi',
      displayName: 'Apple Adayı',
      email: 'adayi@icloud.com',
      targetScore: 90.0,
      badge: '🍏 Apple Adayı',
      avatarUrl: '🍎',
    );
    await saveSession();
    return true;
  }

  void logout() {
    currentUser = null;
    try {
      final file = _getAuthFile();
      if (file != null && file.existsSync()) {
        file.deleteSync();
      }
    } catch (_) {}
  }

  void updateProfile({
    String? displayName,
    double? targetScore,
    String? badge,
    String? avatarUrl,
  }) {
    if (currentUser == null) return;
    currentUser = currentUser!.copyWith(
      displayName: displayName,
      targetScore: targetScore,
      badge: badge,
      avatarUrl: avatarUrl,
    );
    saveSession();
  }
}
