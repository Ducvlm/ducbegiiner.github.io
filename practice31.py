try:
    n = int(input('Hãy nhập vào số nguyên để vẽ tam giác số:'))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=' ')
        print()
except:
    print('Đầu vào không hợp lệ')