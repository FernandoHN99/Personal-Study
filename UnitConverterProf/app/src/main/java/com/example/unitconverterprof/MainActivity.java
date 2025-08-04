package com.example.unitconverterprof;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity
{
    private Button carrega_tela1;
    private Button carrega_tela2;
    private Button carrega_tela3;
    private Button carrega_tela4;
    private Context context;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.tela_principal);   // vinculando o tipo de layout
        context=MainActivity.this;                 // iniciando context

        // vinculando o botão

        carrega_tela1=findViewById(R.id.botao1);
        carrega_tela2=findViewById(R.id.botao2);
        carrega_tela3=findViewById(R.id.botao3);

        // rotina do botão carrega_tela1

        carrega_tela1.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View view)
            {
                Intent mintent = new Intent(context,tela1.class);
                startActivity(mintent);       // mudando para a tela 1
                finish();                     // fecha a tela atual
            }
        });

        // rotina do botão carrega_tela1

        carrega_tela2.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View view)
            {
                Intent mintent = new Intent(context,tela2.class);
                startActivity(mintent);       // mudando para a tela 2
                finish();                     // fecha a tela atual
            }
        });

        carrega_tela3.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View view)
            {
                Intent mintent = new Intent(context,tela3.class);
                startActivity(mintent);       // mudando para a tela 2
                finish();                     // fecha a tela atual
            }
        });



    }
}