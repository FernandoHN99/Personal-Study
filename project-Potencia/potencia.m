function [calculoPotencia] = potencia(g, t0, t1)

%%% Boas práticas
syms t
T0 = t1 - t0;

calculoPotenciaSymb =  int(g^2,t,t0,t1);
calculoPotencia = (1/T0) * (eval(calculoPotenciaSymb));

end