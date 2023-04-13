import numpy as np
i = 1
FONTES = []
RESISTOR = []
while i < 6:
    Fonte = float(input("Digite o valor da %iª fonte (Volts): " % i))
    FONTES.append(Fonte)
    i +=1
    
i = 1   
while i < 8:
    Resistor = float(input("Digite o valor do %i° resistor(Ω): " % i))
    RESISTOR.append(Resistor)
    i +=1
    
A = np.array([ [RESISTOR[0] +RESISTOR[4] ,- RESISTOR[4],  0, 0  ],
               [-RESISTOR[4], RESISTOR[4]+RESISTOR[1]+RESISTOR[5], -RESISTOR[5], 0],
               [0, -RESISTOR[5], RESISTOR[5]+RESISTOR[2]+RESISTOR[6], -RESISTOR[6] ],
               [0, 0, -RESISTOR[6], RESISTOR[6]+RESISTOR[3] ]
                                                                   ])

B = np.array([ [FONTES[0]- FONTES[1] ],
                [FONTES[1]- FONTES[2] ],
                 [FONTES[2]- FONTES[3] ],
                  [FONTES[3]- FONTES[4] ]
                                          ])

RESPOSTA = np.linalg.solve(A, B)
i = 1
for resposta in RESPOSTA:
    print("I%i: %f" % (i, resposta))
    i = i + 1
print(RESPOSTA)