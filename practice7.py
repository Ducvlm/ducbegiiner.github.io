name1,height1 = list(input("nhap ten va chieu cao cua ban thu nhat:").split())
name2,height2 = list(input("nhap ten va chieu cao cua ban thu hai:").split())
if height1 > height2:
    print(name1 + " cao hon " + name2)
elif height1 == height2:
    print("Hai ban cao bang nhau")
else:
    print(name2 + " cao hon " + name1)