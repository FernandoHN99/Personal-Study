package com.example.atividade6;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.content.Context;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.RadioButton;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private RadioButton comp;
    private RadioButton mas;
    private RadioButton tempo;
    private RadioButton temp;
    private TextView de;
    private TextView para;
    private EditText numero;
    private ListView lista;
    private Context context;
    private String[] unidade;
    private String grandeza;
    private double valor;
    private String aux;
    private int j;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.tela1);

        context=MainActivity.this;   // obtendo contexto

        // vinculando as componentes da tela

        comp=findViewById(R.id.comp);
        mas=findViewById(R.id.mas);
        tempo=findViewById(R.id.tempo);
        temp=findViewById(R.id.temp);
        de=findViewById(R.id.de);
        para=findViewById(R.id.para);
        numero=findViewById(R.id.numero);
        lista=findViewById(R.id.lista);

        grandeza="comprimento";   // grandeza inicial é o comprimento

        // adaptador para a list

        ArrayAdapter<String> adaptador = new ArrayAdapter<String>(context, android.R.layout.simple_list_item_1);

        // criando uma lista de unidades de comprimento

        unidade=new String[6];   // array de String
        unidade[0]="De m para cm";
        unidade[1]="De cm para m";
        unidade[2]="De m para mm";
        unidade[3]="De mm para m";
        unidade[4]="De m para in";
        unidade[5]="De in para m";

        // adicionando os elementos a lista

        for (j=0;j<=5;j++)
        {
            adaptador.add(unidade[j]);   // inserindo string
        }

        lista.setAdapter(adaptador);

        // eventos dos radio buttons

        mas.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View view)
            {
                // adaptador para a list

                ArrayAdapter<String> adaptador = new ArrayAdapter<String>(context, android.R.layout.simple_list_item_1);

                adaptador.clear();  // limpando a lista

                lista.setAdapter(adaptador);

                // criando uma lista de unidades de tempo

                unidade=new String[6];   // array de String
                unidade[0]="De kg para g";
                unidade[1]="De g para kg";
                unidade[2]="De kg para t";
                unidade[3]="De t para kg";
                unidade[4]="De kg para lb";
                unidade[5]="De lb para kg";

                // adicionando os elementos a lista

                for (j=0;j<=5;j++)
                {
                    adaptador.add(unidade[j]);   // inserindo string
                }

                lista.setAdapter(adaptador);  // carregando os elementos na lista

                grandeza="massa";   // informando o tipo de grandeza

            }
        });

        tempo.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View view)
            {
                // adaptador para a list

                ArrayAdapter<String> adaptador = new ArrayAdapter<String>(context, android.R.layout.simple_list_item_1);

                adaptador.clear();  // limpando a lista

                lista.setAdapter(adaptador);

                // criando uma lista de unidades de tempo

                unidade=new String[6];   // array de String
                unidade[0]="De s para min";
                unidade[1]="De min para s";
                unidade[2]="De s para h";
                unidade[3]="De h para s";
                unidade[4]="De s para ms";
                unidade[5]="De ms para s";

                // adicionando os elementos a lista

                for (j=0;j<=5;j++)
                {
                    adaptador.add(unidade[j]);   // inserindo string
                }

                lista.setAdapter(adaptador);  // carregando os elementos na lista

                grandeza="tempo";   // informando o tipo de grandeza
            }
        });

        temp.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View view)
            {
                // adaptador para a list

                ArrayAdapter<String> adaptador = new ArrayAdapter<String>(context, android.R.layout.simple_list_item_1);

                adaptador.clear();  // limpando a lista

                lista.setAdapter(adaptador);

                // criando uma lista de unidades de tempo

                unidade=new String[4];   // array de String
                unidade[0]="De °C para °F";
                unidade[1]="De °F para °C";
                unidade[2]="De °C para K";
                unidade[3]="De K para °C";

                // adicionando os elementos a lista

                for (j=0;j<=3;j++)
                {
                    adaptador.add(unidade[j]);   // inserindo string
                }

                lista.setAdapter(adaptador);  // carregando os elementos na lista

                grandeza="temperatura";   // informando o tipo de grandeza


            }
        });

        comp.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View view)
            {
// adaptador para a list

                ArrayAdapter<String> adaptador = new ArrayAdapter<String>(context, android.R.layout.simple_list_item_1);

                adaptador.clear();  // limpando a lista

                lista.setAdapter(adaptador);

                // criando uma lista de unidades de tempo

                unidade=new String[6];   // array de String
                unidade[0]="De m para cm";
                unidade[1]="De cm para m";
                unidade[2]="De m para mm";
                unidade[3]="De mm para m";
                unidade[4]="De m para in";
                unidade[5]="De in para m";

                // adicionando os elementos a lista

                for (j=0;j<=5;j++)
                {
                    adaptador.add(unidade[j]);   // inserindo string
                }

                lista.setAdapter(adaptador);  // carregando os elementos na lista

                grandeza="comprimento";   // informando o tipo de grandeza
            }
        });

        // evento da lista

        lista.setOnItemClickListener(new AdapterView.OnItemClickListener()
        {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l)
            {
                // lendo o valor da EditText
                valor=Double.valueOf(numero.getText().toString());
                if (grandeza.equals("comprimento"))    // se a grandeza selecionada for o comprimento
                {
                    if (i==0)  // se for o primeiro item da lista, converte de m para cm
                    {
                        de.setText("De m");  // informa a unidade de origem
                        aux="Para "+String.valueOf(100*valor)+" cm";   // faz a operação de conversão
                        para.setText(aux);  // exibe a unidade de destino
                    }
                    else if (i==1)  // se for o segundo item da lista, converte de cm para m
                    {
                        de.setText("De cm");  // informa a unidade de origem
                        aux="Para "+String.valueOf(0.01*valor)+" m";   // faz a operação de conversão
                        para.setText(aux);  // exibe a unidade de destino
                    }
                    else if (i==2)  // se for o terceiro item da lista, converte de m para mm
                    {
                        de.setText("De m");  // informa a unidade de origem
                        aux="Para "+String.valueOf(1000*valor)+" mm";   // faz a operação de conversão
                        para.setText(aux);  // exibe a unidade de destino
                    }
                    else if (i==3)  // se for o terceiro item da lista, converte de mm para m
                    {
                        de.setText("De mm");  // informa a unidade de origem
                        aux="Para "+String.valueOf(valor/1000)+" m";   // faz a operação de conversão
                        para.setText(aux);  // exibe a unidade de destino
                    }
                    else if (i==4)  // se for o terceiro item da lista, converte de m para in
                    {
                        de.setText("De m");  // informa a unidade de origem
                        aux="Para "+String.valueOf(valor*39.37)+" in";   // faz a operação de conversão
                        para.setText(aux);  // exibe a unidade de destino
                    } else if (i==5)  // se for o terceiro item da lista, converte de in para m
                    {
                        de.setText("De in");  // informa a unidade de origem
                        aux="Para "+String.valueOf(valor/39.37)+" m";   // faz a operação de conversão
                        para.setText(aux);  // exibe a unidade de destino
                    }


                }
                else if (grandeza.equals("massa"))    // se a grandeza selecionada for o comprimento
                {
                    if (i == 0)  // se for o primeiro item da lista, converte de m para cm
                    {
                        de.setText("De kg");  // informa a unidade de origem
                        aux = "Para " + String.valueOf(valor * 1000) + " g";   // faz a operação de conversão
                        para.setText(aux);  // exibe a unidade de destino
                    } else if (i == 1)  // se for o segundo item da lista, converte de cm para m
                    {
                        de.setText("De g");  // informa a unidade de origem
                        aux = "Para " + String.valueOf(valor / 1000) + " kg";   // faz a operação de conversão
                        para.setText(aux);  // exibe a unidade de destino
                    } else if (i == 2)  // se for o segundo item da lista, converte de cm para m
                    {
                        de.setText("De kg");  // informa a unidade de origem
                        aux = "Para " + String.valueOf(valor / 1000) + " t";   // faz a operação de conversão
                        para.setText(aux);  // exibe a unidade de destino
                    } else if (i == 3)  // se for o segundo item da lista, converte de cm para m
                    {
                        de.setText("De t");  // informa a unidade de origem
                        aux = "Para " + String.valueOf(valor * 1000) + " kg";   // faz a operação de conversão
                        para.setText(aux);  // exibe a unidade de destino
                    } else if (i == 4)  // se for o segundo item da lista, converte de cm para m
                    {
                        de.setText("De kg");  // informa a unidade de origem
                        aux = "Para " + String.valueOf(valor * 2.205) + " lb";   // faz a operação de conversão
                        para.setText(aux);  // exibe a unidade de destino
                    } else if (i == 5)  // se for o segundo item da lista, converte de cm para m
                    {
                        de.setText("De lb");  // informa a unidade de origem
                        aux = "Para " + String.valueOf(valor / 2.205) + " kg";   // faz a operação de conversão
                        para.setText(aux);  // exibe a unidade de destino
                    }
                }
                else if (grandeza.equals("tempo"))    // se a grandeza selecionada for o comprimento
                {
                    if (i==0)  // se for o primeiro item da lista, converte de m para cm
                    {
                        de.setText("De s");  // informa a unidade de origem
                        aux="Para "+String.valueOf(valor/60)+" min";   // faz a operação de conversão
                        para.setText(aux);  // exibe a unidade de destino
                    }
                    else if (i==1)  // se for o segundo item da lista, converte de cm para m
                    {
                        de.setText("De min");  // informa a unidade de origem
                        aux="Para "+String.valueOf(valor*60)+" s";   // faz a operação de conversão
                        para.setText(aux);  // exibe a unidade de destino
                    }
                    else if (i==2)  // se for o segundo item da lista, converte de cm para m
                    {
                        de.setText("De s");  // informa a unidade de origem
                        aux="Para "+String.valueOf(valor/3600)+" h";   // faz a operação de conversão
                        para.setText(aux);  // exibe a unidade de destino
                    }
                    else if (i==3)  // se for o segundo item da lista, converte de cm para m
                    {
                        de.setText("De h");  // informa a unidade de origem
                        aux="Para "+String.valueOf(valor*3600)+" s";   // faz a operação de conversão
                        para.setText(aux);  // exibe a unidade de destino
                    }
                    else if (i==4)  // se for o segundo item da lista, converte de cm para m
                    {
                        de.setText("De s");  // informa a unidade de origem
                        aux="Para "+String.valueOf(valor*1000)+" ms";   // faz a operação de conversão
                        para.setText(aux);  // exibe a unidade de destino
                    }
                    else if (i==5)  // se for o segundo item da lista, converte de cm para m
                    {
                        de.setText("De ms");  // informa a unidade de origem
                        aux="Para "+String.valueOf(valor/1000)+" s";   // faz a operação de conversão
                        para.setText(aux);  // exibe a unidade de destino
                    }

                }
                else if (grandeza.equals("temperatura"))    // se a grandeza selecionada for o comprimento
                {
                    if (i==0)  // se for o primeiro item da lista, converte de m para cm
                    {
                        de.setText("De °C");  // informa a unidade de origem
                        aux="Para "+String.valueOf(valor*(9/5)+32)+" °F";   // faz a operação de conversão
                        para.setText(aux);  // exibe a unidade de destino
                    }
                    else if (i==1)  // se for o segundo item da lista, converte de cm para m
                    {
                        de.setText("De °F");  // informa a unidade de origem
                        aux="Para "+String.valueOf((valor-32)*(5/9))+" °C";   // faz a operação de conversão
                        para.setText(aux);  // exibe a unidade de destino
                    }
                    else if (i==2)  // se for o segundo item da lista, converte de cm para m
                    {
                        de.setText("De °C");  // informa a unidade de origem
                        aux="Para "+String.valueOf(valor+273.15)+" K";   // faz a operação de conversão
                        para.setText(aux);  // exibe a unidade de destino
                    }
                    else if (i==3)  // se for o segundo item da lista, converte de cm para m
                    {
                        de.setText("De K");  // informa a unidade de origem
                        aux="Para "+String.valueOf(valor-273.15)+" °C";   // faz a operação de conversão
                        para.setText(aux);  // exibe a unidade de destino
                    }

                }
            }
        });

    }
}
