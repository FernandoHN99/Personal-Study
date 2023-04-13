package com.example.atividade4;

import androidx.appcompat.app.AppCompatActivity;

import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity implements SensorEventListener
{

    private TextView ax;
    private TextView ay;
    private TextView az;
    private TextView cronos, cronosMin,cronos2, cronosMin2,cronos3, cronosMin3;
    private Button iniciar;
    private Button parar,parar2,parar3;
    private Button zerar;
    private double contador;
    private int estado ,estado2,estado3;
    private String aux, aux2;
    private int aux3;
    private SensorManager acelerometro;
    private double ax2;
    private double ay2;
    private double az2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.tela1);

        // vinculando as componentes

        ax=findViewById(R.id.ax);
        ay=findViewById(R.id.ay);
        az=findViewById(R.id.az);
        cronos=findViewById(R.id.cronos);
        cronosMin=findViewById(R.id.cronosMin);
        cronos2=findViewById(R.id.cronos2);
        cronosMin2=findViewById(R.id.cronosMin2);
        cronos3=findViewById(R.id.cronos3);
        cronosMin3=findViewById(R.id.cronosMin3);
        iniciar=findViewById(R.id.iniciar);
        parar=findViewById(R.id.parar);
        parar2=findViewById(R.id.parar2);
        parar3=findViewById(R.id.parar3);
        zerar=findViewById(R.id.zerar);

        // configurando o acesso ao sensor de aceleração
        acelerometro=(SensorManager) getSystemService(SENSOR_SERVICE);
        acelerometro.registerListener(this, acelerometro.getDefaultSensor(Sensor.TYPE_ACCELEROMETER), SensorManager.SENSOR_DELAY_NORMAL);

        contador=0;
        estado=0;      // iniciando as variáveis

        // rotinas dos botões

        iniciar.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View view)
            {
            estado=1;   // habilita a contagem na Thread
            }
        });

        parar.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View view)
            {
            estado=0;   // desabilita a contagem na Thread
            }
        });
        parar2.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View view)
            {
                estado2=0;   // desabilita a contagem na Thread
            }
        });
        parar3.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View view)
            {
                estado3=0;   // desabilita a contagem na Thread
            }
        });

        zerar.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View view)
            {
            estado=0;   // desabilita a contagem na Thread
            contador=0;   // zera a contagem
            cronos.setText("0 seg"); // exibe a contagem
                 cronosMin.setText("0 min"); // exibe a contagem
            }
        });

        process();   // chamando a rotina que dispara a Thread


    }

    // rotina que é executada quando houver mudança na precisão do sensor
    @Override
    public void onAccuracyChanged(Sensor sensor, int i)
    {

    }


    // rotina que é executada quando houver mudança na aceleração
    @Override
    public void onSensorChanged(SensorEvent sensorEvent)
    {
        if (sensorEvent.sensor.getType()==Sensor.TYPE_ACCELEROMETER)
        {
        ax2=sensorEvent.values[0];   // lendo os valores das acelerações
        ay2=sensorEvent.values[1];
        az2=sensorEvent.values[2];
        aux="ax="+String.valueOf(ax2)+"m/s^2";
        ax.setText(aux);              // exibindo nas caixas de texto
        aux="ay="+String.valueOf(ay2)+"m/s^2";
        ay.setText(aux);
        aux="az="+String.valueOf(az2)+"m/s^2";
        az.setText(aux);
        }
    }

    private void process()   // Thread
    {
        Thread proc = new Thread(new Runnable()
        {
            @Override
            public void run() {
                try {
                    while (true)   // loop infinito
                {
                Thread.sleep(100);   // processo espera 100ms
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        if (estado==1){   // se estado for 1, habilita a contagem

                            contador++;           // incrementa o contador
                            if (contador == 600){
                                aux3 = aux3 + 1;
                                aux2= aux3 + " min";
                                cronosMin.setText(aux2);  // exibe no cronômetro
                                contador = 0;
                            }
                        aux=String.valueOf((contador/10))+ " seg";
                        cronos.setText(aux);  // exibe no cronômetro

                        }
                        if (estado2==1){   // se estado for 1, habilita a contagem

                            contador++;           // incrementa o contador
                            if (contador == 600){
                                aux3 = aux3 + 1;
                                aux2 = aux3 + " min";
                                cronosMin2.setText(aux2);  // exibe no cronômetro
                                contador = 0;
                            }
                            aux=String.valueOf((contador/10))+ " seg";
                            cronos2.setText(aux);  // exibe no cronômetro
                        }
                        if (estado3==1){   // se estado for 1, habilita a contagem
 
                            contador++;           // incrementa o contador
                            if (contador == 600){
                                aux3 = aux3 + 1;
                                aux2= aux3 + " min";
                                cronosMin.setText(aux2);  // exibe no cronômetro
                                cronosMin3.setText(aux2);  // exibe no cronômetro
                                contador = 0;
                            }
                            aux=String.valueOf((contador/10))+ " seg";
                            cronos3.setText(aux);  // exibe no cronômetro
                        }
                    }
                });
                }
                }
                catch (Exception e)
                {
                }
            }
        });
        proc.start();   // iniciar a Thread

    }
}