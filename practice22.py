from math import sqrt
a,b,c = map(float,input('hay nhap he so cua phuong trinh bac hai').split())
if a == 0:
    nghiem = -c/b
    print('phuong trinh co nghiem duy nhat',nghiem)
else:
    delta = b**2-4*a*c
    if delta >0:
        x1=(-b+sqrt(delta))/(2*a)
        x2=(-b-sqrt(delta))/(2*a)
        print('phuong trinh co 2 nghiem phan biet la:')
        print('x1=',x1)
        print('x2=',x2)
    elif delta ==0:
        x3 = -b/(2*a)
        print('phuogn trinh co nghiem kep: x1=x2=',x3)
    else:
        print('phuong trinh vo nghiem')      


