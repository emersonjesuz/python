from math import radians,cos,sin,tan
#import math
angulos=float(input('degite o amgulo que você deseja'))
#seno=math.sin(math.radians(angulos))
seno=sin(radians(angulos))
print('o angulo de {} tem o seno de {:.2f}'.format(angulos,seno))
#coseno=math.cos(math.radians(angulos))
coseno=cos(radians(angulos))
print('o angulo  de {} tem o coseno de {:.2f} '.format(angulos,coseno))
#tangente=math.tan(math.radians(angulos))
tangente=tan(radians(angulos))
print('o angulo de {} tem o tangente de {:.2f}'.format(angulos,tangente))