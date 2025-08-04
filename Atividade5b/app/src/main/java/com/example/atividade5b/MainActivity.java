package com.example.atividade5b;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.telephony.SmsManager;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.example.atividade5b.R;

public class MainActivity extends AppCompatActivity implements SensorEventListener {

    private EditText referencia, referencia2, referencia3, referencia4, referencia5, referencia6;   // variáveis
    private EditText telefone;
    private TextView medido, medido2;
    private Button iniciar;
    private Button parar;
    private int estado;
    private SensorManager acelerometro;
    private double ax, ax2;
    private String aux, aux2;
    private String numero;
    private double ref, ref2, ref3, ref4, ref5, ref6;
    //private SmsManager sm;
    private int contador;
    private Context context;
    private TextView aviso;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.tela1);

        context=MainActivity.this;   // obtendo dados da activity

        // vinculando com os componentes da tela

        telefone=findViewById(R.id.telefone);
        referencia=findViewById(R.id.referencia);
        referencia2=findViewById(R.id.referenciaMedia);
        referencia3=findViewById(R.id.referenciaAlto);
        referencia4=findViewById(R.id.referencia2);
        referencia5=findViewById(R.id.referenciaMedia2);
        referencia6=findViewById(R.id.referenciaAlto2);
        iniciar=findViewById(R.id.iniciar);
        parar=findViewById(R.id.parar);
        medido=findViewById(R.id.medido);
        medido2=findViewById(R.id.medido2);
        aviso=findViewById(R.id.aviso);

        // valores iniciais das variáveis

        estado=0;
        contador=0;

        // preparando o sensor de aceleração

        // configurando o acesso ao sensor de aceleração
        acelerometro=(SensorManager) getSystemService(SENSOR_SERVICE);
        acelerometro.registerListener(this, acelerometro.getDefaultSensor(Sensor.TYPE_ACCELEROMETER), SensorManager.SENSOR_DELAY_NORMAL);

        // preparando o uso do SMS
       // sm=SmsManager.getDefault();

        // eventos dos botões

        iniciar.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View view)
            {
                estado=1;                               // iniciar monitoração
                numero=telefone.getText().toString();   // obtendo o número de telefone
                ref=Math.abs(Double.valueOf(referencia.getText().toString())); // obtendo a aceleração de refêrência
                ref2=Math.abs(Double.valueOf(referencia2.getText().toString())); // obtendo a aceleração de refêrência
                ref3=Math.abs(Double.valueOf(referencia3.getText().toString())); // obtendo a aceleração de refêrência
                ref4=Math.abs(Double.valueOf(referencia4.getText().toString())); // obtendo a aceleração de refêrência
                ref5=Math.abs(Double.valueOf(referencia5.getText().toString())); // obtendo a aceleração de refêrência
                ref6=Math.abs(Double.valueOf(referencia6.getText().toString())); // obtendo a aceleração de refêrência
                aviso.setText("Alarme ligado: 10seg");   // avisa que o alarme esta ligado
            }
        });

        parar.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View view)
            {
                estado=0;   // parar monitoração
                aviso.setText("Alarme desligado");   // avisa que o alarme esta desligado
            }
        });

        process();   // iniciando a Thread
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
            ax=Math.abs(sensorEvent.values[0]);  // lendo a aceleração em x
            ax2=Math.abs(sensorEvent.values[1]);  // lendo a aceleração em x
            aux="ax medido="+String.valueOf(ax)+"m/s^2";
            aux2="ay medido="+String.valueOf(ax2)+"m/s^2";
            medido.setText(aux);       // exibindo a aceleração
            medido2.setText(aux2);       // exibindo a aceleração
            if (estado==1)             // se a monitoração foi habilitada
            {
                if (ax>=ref && ax<ref2 ) // se passou da aceleração limite
                {
                    if (contador == 0) // se o contador for 0
                    {
                        // se a aceleração for maior que a referência
                        // envia mensagem de SMS
                        //sm.sendTextMessage(numero, null, "Aceleração em x Baixa", null, null);
                        contador = 10;   // carrega o contador com 60 (para enviar SMS a cada 10 segundos)
                        // contador é decrementado na Thread a cada 1 segundo
                        Toast.makeText(context,"Aceleração em x Baixa",Toast.LENGTH_SHORT).show(); // exibe menssagem
                    }
                }

                else if (ax>=ref2 && ax<ref3) // se passou da aceleração limite
                {
                    if (contador == 0) // se o contador for 0
                    {
                        // se a aceleração for maior que a referência
                        // envia mensagem de SMS
                        //sm.sendTextMessage(numero, null, "Aceleração em x Média", null, null);
                        contador = 10;   // carrega o contador com 60 (para enviar SMS a cada 10 segundos)
                        // contador é decrementado na Thread a cada 1 segundo
                        Toast.makeText(context,"Aceleraçãoem x  Média",Toast.LENGTH_SHORT).show(); // exibe menssagem
                    }
                }

                else if (ax>=ref3) // se passou da aceleração limite
                {
                    if (contador == 0) // se o contador for 0
                    {
                        // se a aceleração for maior que a referência
                        // envia mensagem de SMS
                        //sm.sendTextMessage(numero, null, "Aceleração em x Alta", null, null);
                        contador = 10;   // carrega o contador com 60 (para enviar SMS a cada 10 segundos)
                        // contador é decrementado na Thread a cada 1 segundo
                        Toast.makeText(context,"Aceleração em x Alta",Toast.LENGTH_SHORT).show(); // exibe menssagem
                    }
                }
                if (ax2>=ref4 && ax2<ref5 ) // se passou da aceleração limite
                {
                    if (contador == 0) // se o contador for 0
                    {
                        // se a aceleração for maior que a referência
                        // envia mensagem de SMS
                        //sm.sendTextMessage(numero, null, "Aceleração em y Baixa", null, null);
                        contador = 10;   // carrega o contador com 60 (para enviar SMS a cada 10 segundos)
                        // contador é decrementado na Thread a cada 1 segundo
                        Toast.makeText(context,"Aceleração em y Baixa",Toast.LENGTH_SHORT).show(); // exibe menssagem
                    }
                }

                else if (ax2>=ref5 && ax2<ref6) // se passou da aceleração limite
                {
                    if (contador == 0) // se o contador for 0
                    {
                        // se a aceleração for maior que a referência
                        // envia mensagem de SMS
                        //sm.sendTextMessage(numero, null, "Aceleração em y Média", null, null);
                        contador = 10;   // carrega o contador com 60 (para enviar SMS a cada 10 segundos)
                        // contador é decrementado na Thread a cada 1 segundo
                        Toast.makeText(context,"Aceleração em y Média",Toast.LENGTH_SHORT).show(); // exibe menssagem
                    }
                }

                else if (ax2>=ref6) // se passou da aceleração limite
                {
                    if (contador == 0) // se o contador for 0
                    {
                        // se a aceleração for maior que a referência
                        // envia mensagem de SMS
                        //sm.sendTextMessage(numero, null, "Aceleração em y Alta", null, null);
                        contador = 10;   // carrega o contador com 60 (para enviar SMS a cada 10 segundos)
                        // contador é decrementado na Thread a cada 1 segundo
                        Toast.makeText(context,"Aceleração em y Alta",Toast.LENGTH_SHORT).show(); // exibe menssagem
                    }
                }
            }
        }
    }



    private void process()   // Thread
    {
        Thread proc = new Thread(new Runnable()
        {
            @Override
            public void run()
            {
                try
                {
                    while (true)   // loop infinito
                    {
                        Thread.sleep(1000);   // processo espera 1000ms
                        runOnUiThread(new Runnable()
                        {
                            @Override
                            public void run()
                            {
                                if (contador>0)  // se o contador passou de 0
                                {
                                    contador--;    // decrementa o contador
                                    aux="Alarme ligado: "+String.valueOf(contador)+"seg";
                                    aviso.setText(aux);  // mostra o valor da temporização
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