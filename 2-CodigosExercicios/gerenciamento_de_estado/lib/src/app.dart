import 'package:flutter/material.dart';
import '../src/telas/login_tela.dart';

class App extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'Login',
        home: Scaffold(
          body: LoginTela(),
        ));
  }
}
