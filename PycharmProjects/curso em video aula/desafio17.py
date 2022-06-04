#import math
from math import hypot
co=float(input('digite o cateto  oposto:'))
ca=float(input(' digite ocateto adjcente:'))
#hi=(co**2+ca**2)**(1/2)
#print('a hipotenusa vai medir {:.2f} '.format(hi))
#hi=math.hypot(co,ca)
hi=hypot(co,ca)
print('a hipotenusa vai medir {:.2f}'.format(hi))