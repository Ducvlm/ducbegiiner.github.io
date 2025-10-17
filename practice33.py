try:
    n=int(input('Hãy nhập vào một số để vẽ tam giác:'))
    if n<0:
        print('Yêu cầu nhập môt số nguyên dương')
    else:
        maAscii=65
        for i in range(n):
            khoangTrangDauDong=" "*((n-i)*2-1)
            print(khoangTrangDauDong,end=" ")
            for j in range(2*i+1):
                chu=chr(maAscii)
                print(chu,end=" ")
                maAscii+=1
                if (chr(maAscii)>'Z'):
                    maAscii=65
            print()
except:
    print('Định dạng đầu vào không hợp lệ')
                
