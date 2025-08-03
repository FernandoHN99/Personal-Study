import 'package:flutter/material.dart';
import '../blocs/bloc.dart';

class LoginTela extends StatelessWidget {
  final bloc = Bloc();
  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();

  // Construtor
  LoginTela() {
    // Adicione os ouvintes aqui para garantir que sejam registrados apenas uma vez
    bloc.email.listen((emailValue) {
      print('E-mail: $emailValue');
    });

    bloc.password.listen((passwordValue) {
      print('Senha: $passwordValue');
    });
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: EdgeInsets.all(20.0),
      child: Column(
        children: [
          emailField(),
          passwordField(),
          Container(
            margin: EdgeInsets.only(top: 12.0),
            child: Row(
              children: [
                Expanded(
                  child: submitButton(),
                )
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget emailField() {
    return TextField(
      controller: emailController,
      keyboardType: TextInputType.emailAddress,
      decoration: InputDecoration(
        hintText: 'seu@email.com',
        labelText: 'Endereço de e-mail'),
    );
  }

  Widget passwordField() {
    return TextField(
      controller: passwordController,
      obscureText: true,
      decoration: InputDecoration(
          hintText: "Senha", labelText: "Senha"),
    );
  }

  Widget submitButton() {
    return ElevatedButton(
        onPressed: () => processarLogin(),
        child: Text('Login'));
  }

  void processarLogin() {
    final email = emailController.text;
    final password = passwordController.text;

    // Adicionar a lógica de autenticação, chamada à API, etc.
    bloc.changeEmail(email);
    bloc.changePassword(password);
    
  }
}
