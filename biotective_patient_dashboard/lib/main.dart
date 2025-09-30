import 'package:biotective_patient_dashboard/widgets/main_layout.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const BioTectiveApp());
}

class BioTectiveApp extends StatelessWidget {
  const BioTectiveApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'BioTective Dashboard',

      // Define the overall theme for the application
      theme: ThemeData(
        brightness: Brightness.dark,
        primarySwatch: Colors.blue,
        scaffoldBackgroundColor: const Color(
          0xFFF8F8F8,
        ), // Light grey background
        fontFamily: 'Roboto',
        appBarTheme: const AppBarTheme(
          backgroundColor: Colors.white,
          elevation: 1, // Subtle shadow for the app bar
          iconTheme: IconThemeData(color: Colors.black87),
          titleTextStyle: TextStyle(
            color: Colors.black87,
            fontSize: 20,
            fontWeight: FontWeight.w500,
          ),
        ),
      ),

      home: const MainLayout(),
    );
  }
}