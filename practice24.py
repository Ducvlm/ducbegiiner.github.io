a,b,c=map(float,input('hay nhap vao so do 3 canh cua mot tam giac:').split())
if a+b>=c and b+c>=a and a+c>=b:
    if a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+c**2==b**2:
            print('day la mot tam giac vuong')
    elif a**2>b**2+c**2 or b**2>a**2+c**2 or c**2>a**2+b**2:
        print('day la mot tam giac tu')
    elif a==b and b==c:
        print('day la mot tam giac deu')
    elif a==b or b==c or a==c:
        print('day la mot tam giac can')
    else:
        print('day la mot tam giac nhon')
else:
     print('day khong la mot tam giac')