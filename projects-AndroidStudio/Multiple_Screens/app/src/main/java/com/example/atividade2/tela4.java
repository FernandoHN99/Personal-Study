package com.example.atividade2;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.Button;
import android.widget.ImageView;

import androidx.appcompat.app.AppCompatActivity;

public class tela4 extends AppCompatActivity implements Animation.AnimationListener
{
    private Button carrega_telaprin;
    private Button girar;
    private ImageView imagem;
    private Context context;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.tela4);   // vinculando o tipo de layout
        context= tela4.this;               // iniciando context

        // vinculando o botão

        carrega_telaprin=findViewById(R.id.botao1);
        girar=findViewById(R.id.botao4);
        imagem=findViewById(R.id.imagem);

        // rotina do botão carrega_telaprin

        carrega_telaprin.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View view)
            {
                Intent mintent = new Intent(context,MainActivity.class);
                startActivity(mintent);       // mudando para a tela principal
                finish();                     // fecha a tela atual
            }
        });

        // rotina do botão que faz girar a figura

        girar.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View view)
            {
            // carregando animação
            Animation anim =  AnimationUtils.loadAnimation(context,R.anim.deslocar);
            anim.setAnimationListener(tela4.this);
            imagem.requestLayout();
            imagem.setAnimation(anim); // animação no imageView
            anim.start();              // iniciando a animação
            }
        });



    }


    // evento de início da animação
    @Override
    public void onAnimationStart(Animation animation)
    {
    carrega_telaprin.setEnabled(false); // desabilita botões até que a mesma animação tenha terminado
    girar.setEnabled(false);
    }

    // evento de término da animação
    @Override
    public void onAnimationEnd(Animation animation)
    {
    carrega_telaprin.setEnabled(true);// reabilita botões
    girar.setEnabled(true);
    }

    @Override
    public void onAnimationRepeat(Animation animation)
    {
    }


}