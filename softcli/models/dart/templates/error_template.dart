class %$class_name implements Exception {
  %$class_name({
    required this.error,
    this.message,
    this.stackTrace,
  });

  final String error;

  final String? message;

  final StackTrace? stackTrace;

  @override
  String toString() {
    return '$runtimeType {error: $error, message: $message}';
  }

  Map<String, dynamic> toMap() {
    return {
      'error': error,
      'message': message,
    };
  }
}
