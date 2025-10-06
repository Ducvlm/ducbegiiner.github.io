name1,height1 = list(input("hay nhap ten va chieu cao cua ban thu nhat:").split())
name2,height2 = list(input("hay nhap ten va chieu cao cua ban thu hai:").split())
if int(height1) < 0 or int(height2) < 0:
    print("chieu cao phai lon hon 0")
elif height1 > height2:
    print(name1+" cao hon " +name2)
elif height1 == height2:
    print("Hai ban cao bang nhau")
else:
    print(name2 + ' cao hon '+name1)