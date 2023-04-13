import numpy as np
x=np.array( [  0  ,-178 ,-802 ,-1024 ,
             -935 ,-712 ,-612 ,-612 ,-590 ,-590 ,-623 ,-724 ,-724  ,-690 ,-590 ])

y =np.array([ 0, 78 ,668 ,1358 ,1514 ,1681 ,2082 ,2160 ,2171 ,2193 ,2238
                                 ,2338 ,2371 ,2416 ,2416 ]) 

dx = np.diff(x)
dy = np.diff(y)

dist_car = np.sum( np.sqrt(dx**2 + dy**2 ))
print("Distância de carro: %.f m" % dist_car)

dist_drone = np.sqrt( (x[0]-x[-1])**2 + (y[0]-y[-1])**2 )
print("Distância de drone: %.f m" % dist_drone)