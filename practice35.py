try:
    x=float(input('Hãy nhập vào một số thực:'))
    n=int(input('Hãy nhập vào một số nguyên:'))
    if n<0:
        print('Hãy nhập một số tự nhiên n')
    else:
        giaithua=1
        ketqua=1
        for i in range(1,2*n+1):
            giaithua*=i
            if i%2==0:
                ketqua+=(x**i)/giaithua
            else:
                ketqua-=(x**i)/giaithua
        print('Kết quả của biểu thức là:',ketqua)

                
except:
    print('Định dạng đầu vào không hợp ')
        
            