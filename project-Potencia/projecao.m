function [c] = projecao(g1,g2,t0, t1)
% Determina projeção do sinal g1(t) no dinal g2(t)
% retorna o valor da projeção numericamente

%%% Boas práticas

syms t

%%% Numerador

Num = int(g1*g2,t,t0,t1);

%%% Denominador

Den = int(abs(g2)^2,t,t0,t1);

%%% Projeção simbólica

cn = Num/Den;

%%% Projeção Numérica

c = eval(cn);

end