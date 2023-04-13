%% Pedro Henrique Sant Anna Hein - RA: 20.00134-7
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% QUESTÃO 1 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

clear all;
clc;
close all;
                                                      
%%% 1 - sinal de base g(t)

 To = 4;                  % período 
 gp = @(t) t+2;           % reta ascendente
 gn = @(t) -t+2;          % reta decrescente
 ti = -2;                 
 tf = +2;                 
  
%%% Valores calculados para o primeio pulso

 fo = inv(To);            % frequência em Hz
 wo = 2*pi*fo;            % frequência angular
 N  = 1000;               % Número de harmônicas
                          
 n  =[-N:1:N];            % índice de cada harmônica
 f  = n*fo;               % vetor de frequências

 M = 1000;
 Ts = To/M;
 tempo = [-To/10:Ts:To/10];  % Tempo de simulação de um período do sinal g(t)

%%% 2 - Fourier 
%%% Dn simbolicamente

syms n t

Dn = inv(To)*int(gp*exp(-j*n*wo*t),t,ti,0) + inv(To)*int(gn*exp(-j*n*wo*t),t,0,tf);
D_o = inv(To)*int(gp,t,ti,0) + inv(To)*int(gn,t,0,tf);

%%% Dn numericamente

n=[-N:1:N];
 
Dn = eval(Dn);
D_o = eval(D_o);     % Corrigindo o valor médio (NaN devido a indeterminação)
Dn(N+1) = D_o;       % Subistituindo no vetor de respostas

%%% Espector de Amplitude
 
figure(1) 

subplot(2,1,2);plot(f,abs(Dn),'ko');
title('Serie de Fourier do sinal g(t) -- To = 100s');
xlabel('Frequencia em Hz');
ylabel('Amplitude em  volts')
hold

%%% Primeiro sinal

n=[-N:1:N];

aux  = 0;              
for k = 0 : 2*N     
  aux = aux + Dn(k+1)*exp(j*n(k+1)*wo*tempo);
end
gs = aux;

figure(1)

subplot(2,1,1);plot(tempo,gs,'linewidth',3); 
title('Serie de Fourier do sinal g(t) To = 100s');
xlabel('Tempo em segundos');
ylabel('Amplitude em  volts');

%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% QUESTÃO 2 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% 1 - sinais de base g(t) 

 To = 8;                  % período
 gp = @(t) t;             
 gn = @(t) -t+4;
 gp1 = @(t) t-8;         
 ti = 0;
 t1 = 2;
 t2 = 6;
 tf = 8;                 
  
%%% Valores calculados para o primeio pulso

 fo = inv(To);            % frequência em Hz
 wo = 2*pi*fo;            % frequência angular
 N  = 1000;               % harmônicas
                          
 n  =[-N:1:N];            % índice de cada harmônica
 f  = n*fo;               % vetor de frequências

 M = 1000;
 Ts = To/M;
 tempo = [0:Ts:To];  % Tempo de simulação de um período do sinal g(t)
 
%%% 2 - Fourier  
%%% Dn simbolicamente

syms n t

Dn = inv(To)*int(gp*exp(-j*n*wo*t),t,ti,t1) + inv(To)*int(gn*exp(-j*n*wo*t),t,t1,t2) + inv(To)*int(gp1*exp(-j*n*wo*t),t,t2,tf);
D_o = inv(To)*int(gp,t,ti,t1) + inv(To)*int(gn,t,t1,t2) + inv(To)*int(gp1,t,t2,tf);

%%% Dn numericamente

n=[-N:1:N];
 
Dn = eval(Dn);
D_o = eval(D_o);     % Corrigindo o valor médio devido a indeterminação
Dn(N+1) = D_o;       % Subistituindo no vetor


%%% Espector de Amplitude
 
figure(2) 

subplot(2,1,2);plot(f,abs(Dn),'ko');
title('Serie de Fourier do sinal g(t) -- To = 100s');
xlabel('Frequencia em Hz');
ylabel('Amplitude em  volts')
hold

%%% Primeiro sinal

n=[-N:1:N];

aux  = 0;              
for k = 0 : 2*N     
  aux = aux + Dn(k+1)*exp(j*n(k+1)*wo*tempo);  
end
gs = aux;

figure(2)

subplot(2,1,1);plot(tempo,gs,'linewidth',3); 
title('Serie de Fourier do sinal g(t) To = 100s');
xlabel('Tempo em segundos');
ylabel('Amplitude em  volts');

