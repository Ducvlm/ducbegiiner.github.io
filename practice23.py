from math import sqrt
try:
    a,b,c=map(float,input('hay nhap vao he so phuong trinh bac hai:').split())
    if a==0 and b==0 and c==0:
        print('phuong trinh co vo so nghiem')
    elif a==0 and b==0:
        print('phuong trinh vo nghiem')
    elif a==0 and b!=0:
        nghiem=-c/b
        print('phuong trinh co nghiem duy nhat x=',nghiem)
    else:
        delta = b**2-4*a*c
        if delta>0:
            x1=(-b+sqrt(delta))/2
            x2=(-b-sqrt(delta))/2
            print('phuong trinh co 2 nghiem phan biet',x1,x2,end="!\n")
        elif delta ==0:
            x3=-b/(2*a)
            print('phuong tirnh co nghiem kep:',x3)
        else:
            print('phuong trinh vo nghiem')
except:
    print('dau vao khong hop le')
