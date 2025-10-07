canh1,canh2,canh3 = map(float,input("Hay nhap so do 3 canh cua mot tam giac:").split())
if canh1+canh2<=canh3 or canh1+canh3<=canh2 or canh2+canh3<=canh1:
    print(str(canh1)+","+str(canh2)+","+str(canh3)+" khong phai la ba canh cua mot tam giac")
else:
    print(str(canh1)+","+str(canh2)+","+str(canh3)+" la ba canh cua mot tam giac")