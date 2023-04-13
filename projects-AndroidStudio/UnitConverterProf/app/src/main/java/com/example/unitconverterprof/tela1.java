package com.example.unitconverterprof;

import android.content.Context;
import android.content.Intent;
import android.graphics.drawable.Animatable;
import android.os.Bundle;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.RadioButton;
import android.widget.TextView;


import androidx.appcompat.app.AppCompatActivity;

import java.util.ArrayList;

public class tela1 extends AppCompatActivity
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
        setContentView(R.layout.tela1);   // vinculando o tipo de layout
        context=tela1.this;               // iniciando context

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
                str = "Para g: ";
                textopara.setText(str);
                textode.setText("De kg");
            }
        });

        ra2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view)
            {
                str = "Para kg: ";
                textopara.setText(str);
                textode.setText("De g");
            }
        });

        ra3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view)
            {
                str = "Para t: ";
                textopara.setText(str);
                textode.setText("De kg");
            }
        });

        ra4.setOnClickListener(new View.OnClickListener() {
        @Override
        public void onClick(View view)
        {
            str = "Para kg: ";
            textopara.setText(str);
            textode.setText("De t");
        }
    });

        // rotina do botão converter

        converter.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view){
                if (ra1.isChecked()) {               // kg para g
                    aux=Double.valueOf(textoedit.getText().toString());
                    str= "Para g: " + String.valueOf(1000*aux);
                    textopara.setText(str);

                } else if (ra2.isChecked())   {     // g para kg
                    aux=Double.valueOf(textoedit.getText().toString());
                    str= "Para kg: " + String.valueOf(aux/1000);
                    textopara.setText(str);

                } else if (ra3.isChecked())  {      // kg para t
                    aux=Double.valueOf(textoedit.getText().toString());
                    str= "Para t: " + String.valueOf(aux/1000);
                    textopara.setText(str);
                }
                else if (ra4.isChecked()) {     // t para kg
                    aux=Double.valueOf(textoedit.getText().toString());
                    str= "Para kg: " + String.valueOf(1000*aux);
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