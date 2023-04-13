package com.example.unitconverterprof;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class tela3 extends AppCompatActivity
{
    private Button converter;
    private Button voltar;
    private RadioButton ra1;
    private RadioButton ra2;
    private RadioButton ra3;
    private RadioButton ra4;
    private TextView textode;
    private TextView textopara;
    private EditText textoedit;
    private Context context;
    private double aux;
    private String str;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.tela3);   // vinculando o tipo de layout
        context= tela3.this;               // iniciando context

        // vinculando o botão

        converter=findViewById(R.id.converter);
        voltar=findViewById(R.id.voltar);
        ra1=findViewById(R.id.ra1);
        ra2=findViewById(R.id.ra2);
        ra3=findViewById(R.id.ra3);
        ra4=findViewById(R.id.ra4);
        textode=findViewById(R.id.textode);
        textopara=findViewById(R.id.textopara);
        textoedit=findViewById(R.id.textodeedit);

        ra1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view)
            {
                str = "Para Kj: ";
                textopara.setText(str);
                textode.setText("De J");
            }
        });

        ra2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view)
            {
                str = "Para J: ";
                textopara.setText(str);
                textode.setText("De Kj");
            }
        });

        ra3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view)
            {
                str = "Para cal: ";
                textopara.setText(str);
                textode.setText("De J");
            }
        });

        ra4.setOnClickListener(new View.OnClickListener() {
        @Override
        public void onClick(View view)
        {
            str = "Para J: ";
            textopara.setText(str);
            textode.setText("De cal");
        }
    });

        // rotina do botão converter

        converter.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view){
                if (ra1.isChecked()) {               // kg para g
                    aux=Double.valueOf(textoedit.getText().toString());
                    str= "Para Kj: " + String.valueOf(aux/1000);
                    textopara.setText(str);

                } else if (ra2.isChecked())   {     // g para kg
                    aux=Double.valueOf(textoedit.getText().toString());
                    str= "Para J: " + String.valueOf(aux*1000);
                    textopara.setText(str);

                } else if (ra3.isChecked())  {      // kg para t
                    aux=Double.valueOf(textoedit.getText().toString());
                    str= "Para cal: " + String.valueOf(aux*0.000239006);
                    textopara.setText(str);
                }
                else if (ra4.isChecked()) {     // t para kg
                    aux=Double.valueOf(textoedit.getText().toString());
                    str= "Para J: " + String.valueOf(aux/0.239006);
                    textopara.setText(str);
                }
            }
        });

        // rotina do botão voltar

        voltar.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View view)
            {
                Intent mintent = new Intent(context,MainActivity.class);
                startActivity(mintent);       // mudando para a tela principal
                finish();                     // fecha a tela atual
            }
        });





    }




}