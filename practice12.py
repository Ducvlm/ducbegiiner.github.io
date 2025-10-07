num1,pheptinh,num2= input("Nhap so thu nhat, phep tinh, va so thu 2:").split()
num12=float(num1)
num22=float(num2)
if pheptinh=='+':
    print('tong cua 2 so la :',num12+num22)
elif pheptinh=='-':
    print('hieu cua 2 so la :',num12-num22)
elif pheptinh=='*':
    print('tich cua 2 so la:',num12*num22)
elif pheptinh=='/':
    print('thuong cua 2 so la:',num12/num22)
else:
    print('day khong phai la mot phep tinh')