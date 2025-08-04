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

public class tela2 extends AppCompatActivity
{
    private Button converter;
    private Button voltar;
    private RadioButton ra1;
    private RadioButton ra2;
    private RadioButton ra3;
    private RadioButton ra4;
    private RadioButton ra5;
    private RadioButton ra6;
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
        setContentView(R.layout.tela2);   // vinculando o tipo de layout
        context= tela2.this;               // iniciando context

        // vinculando o botão

        converter=findViewById(R.id.converter);
        voltar=findViewById(R.id.voltar);
        ra1=findViewById(R.id.ra1);
        ra2=findViewById(R.id.ra2);
        ra3=findViewById(R.id.ra3);
        ra4=findViewById(R.id.ra4);
        ra5=findViewById(R.id.ra5);
        ra6=findViewById(R.id.ra6);
        textode=findViewById(R.id.textode);
        textopara=findViewById(R.id.textopara);
        textoedit=findViewById(R.id.textodeedit);

        ra1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view)
            {
                str = "Para cm: ";
                textopara.setText(str);
                textode.setText("De m");
            }
        });

        ra2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view)
            {
                str = "Para m: ";
                textopara.setText(str);
                textode.setText("De cm");
            }
        });

        ra3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view)
            {
                str = "Para in: ";
                textopara.setText(str);
                textode.setText("De m");
            }
        });

        ra4.setOnClickListener(new View.OnClickListener() {
        @Override
        public void onClick(View view)
        {
            str = "Para m: ";
            textopara.setText(str);
            textode.setText("De in");
        }
    });

        ra5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view)
            {
                str = "Para m: ";
                textopara.setText(str);
                textode.setText("De in");
            }
        });

        ra6.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view)
            {
                str = "Para m: ";
                textopara.setText(str);
                textode.setText("De in");
            }
        });

        // rotina do botão converter

        converter.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view){
                if (ra1.isChecked()) {               // kg para g
                    aux=Double.valueOf(textoedit.getText().toString());
                    str= "Para cm: " + String.valueOf(100*aux);
                    textopara.setText(str);

                } else if (ra2.isChecked())   {     // g para kg
                    aux=Double.valueOf(textoedit.getText().toString());
                    str= "Para m: " + String.valueOf(aux/100);
                    textopara.setText(str);

                } else if (ra3.isChecked())  {      // kg para t
                    aux=Double.valueOf(textoedit.getText().toString());
                    str= "Para in: " + String.valueOf(aux*39.3701);
                    textopara.setText(str);
                }
                else if (ra4.isChecked()) {     // t para kg
                    aux=Double.valueOf(textoedit.getText().toString());
                    str= "Para m: " + String.valueOf(aux/39.3701);
                    textopara.setText(str);
                }
                else if (ra5.isChecked()) {     // t para kg
                    aux=Double.valueOf(textoedit.getText().toString());
                    str= "Para mm: " + String.valueOf(aux*1000);
                    textopara.setText(str);
                }
                else if (ra6.isChecked()) {     // t para kg
                    aux=Double.valueOf(textoedit.getText().toString());
                    str= "Para m: " + String.valueOf(aux/1000);
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