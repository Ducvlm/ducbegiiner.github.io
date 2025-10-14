from math import sqrt
try:
    print('chuc nang 1:giai phuong trinh bac nhat')
    print('chuc nang 2 :giai phuong trinh bac hai')
    chucnang = int(input('Vui long chon 1 trong 2 chuc nang:'))
    if chucnang == 1:
        a,b=map(float,input('hay nhap vao he so cua phuong trinh bac nhat:').split())
        if a==0 and b==0:
            print('phuong trinh vo so nghiem')
        else:
            nghiem = -b/a
            print('nghiem cua phuong trinh bac nhat la x=',nghiem)
    else:
        a,b,c=map(float,input('hay nhap vao he so phuong trinh bac hai:').split())
        if a==0 and b==0 and c==0:
            print('phuong trinh co vo so nghiem')
        elif a==0 and b!=0:
            print('phuong trinh co 1 nghiem x=',-c/b)
        else:
            delta=b**2-4*a*c
            if delta>0:
                x1=(-b+sqrt(delta))/(2*a)
                x2=(-b-sqrt(delta))/(2*a)
                print('phuong trinh co 2 nghiem phan biet:')
                print('x1=',x1)
                print('x2+',x2)
            elif delta==0:
                x3=-b/(2*a)
                print('phuong trinh co nghiem kep x1=x2=',x3)
            else:
                print('phuong trinh vo nghiem')
except:
    print('dau vao khong hop le')



