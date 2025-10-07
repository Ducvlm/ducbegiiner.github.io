try:
    a,b,c = map(float,input("nhap vao so do 3 canh cua mot tam giac:").split())
    if a<0 or b<0 or c<0:
        print("Cac canh cua tam giac phai lon hon 0!")
    elif a+b>c or a+c>b or b+c>a:
        print(str(a)+","+str(b)+","+str(c)+" la ba canh cua mot tam giac")
    else:
        print(str(a)+","+str(b)+","+str(c)+" khong la ba canh cua mot tam giac")
except:
    print("dau vao khong hop le")
