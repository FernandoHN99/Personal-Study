import 'package:flutter/material.dart';
import '../models/image_model.dart';

class ImageList extends StatelessWidget {
  final List<ImageModel> imagens;
  ImageList(this.imagens);

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      itemCount: imagens.length,
      itemBuilder: (BuildContext context, int index) {
        return Container(
          margin: EdgeInsets.all(4.0),
          width: MediaQuery.of(context).size.width * 0.2, // Define a largura do Container como 20% da largura da tela
          decoration: BoxDecoration(
            border: Border.all(color: Colors.grey),
            borderRadius: BorderRadius.circular(8.0),
          ),
          child: ClipRRect(
            borderRadius: BorderRadius.circular(8.0),
            child: Align(
              alignment: Alignment.center,
              child: Image.network(
                imagens[index].url,
                fit: BoxFit.contain,
              ),
            ),
          ),
        );
      },
    );
  }
}
