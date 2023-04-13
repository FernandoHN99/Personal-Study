package com.example.myfirstapp;

import android.support.v7.app.AppCompatActivity;
//import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import org.w3c.dom.Text;


public class MainActivity extends AppCompatActivity {

    // DECLARANDO VARIAVEIS
    private EditText textRaio;
    private TextView textPerimetro, textArea, textCasca, textVolume;
    private String strPerimetro, strArea, strCasca, strVolume;
    private double perimetro, area, casca, volume, raio;
    private Button acaoCalc;

    // PADRAO DO MAIN
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.tela1);

        // ATRIBUINDO VARIAVEIS AOS ELEMENTOS DO LAYOUT (somente passa 1 vez)
        textRaio = findViewById(R.id.inputRaio);
        textPerimetro = findViewById(R.id.resultPerimetro);
        textArea = findViewById(R.id.resultArea);
        textVolume = findViewById(R.id.resultVolume);
        textCasca = findViewById(R.id.resultCasca);
        acaoCalc = findViewById(R.id.buttonCalc);

        // SETANDO VALORES INICIAIS PARA EXIBIÇÃO BONITA
        strPerimetro = textPerimetro.getText().toString();
        strArea = textArea.getText().toString();
        strVolume = textVolume.getText().toString();
        strCasca = textCasca.getText().toString();

    }

    public void calcularResultado(View view){
        if(!TextUtils.isEmpty(textRaio.getText().toString())){
            raio = Double.valueOf(textRaio.getText().toString());
            perimetro = (2 * Math.PI * raio);
            area = (Math.PI * Math.pow(raio, 2));
            volume = (4 / 3 * Math.PI * Math.pow(raio, 3));
            casca = (4 * Math.PI * Math.pow(raio, 2));
            textPerimetro.setText(strPerimetro + String.format("%.2f", perimetro) + " cm");
            textArea.setText(strArea + String.format("%.2f", area) + " cm²");
            textCasca.setText(strCasca + String.format("%.2f", casca) + " cm²");
            textVolume.setText(strVolume + String.format("%.2f", volume) + " cm³");
        }else{
            textPerimetro.setText(strPerimetro);
            textArea.setText(strArea);
            textCasca.setText(strCasca);
            textVolume.setText(strVolume);
        }
    }
}