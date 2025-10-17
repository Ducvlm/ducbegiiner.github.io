try:
    n=int(input('Hãy nhập vào một số nguyên để vẽ tam giác số:'))
    if 1<=n<=9:
        for i in range(n,0,-1):
            for j in range(i,0,-1):
                print(j,end=' ')
            print()
    else:
        print('Chỉ nhận giá trị từ 1 đến 9')
except:
    print('Định dạng đầu vào không hợp lệ')