try:
    n=int(input('Hãy nhập vào một số để tính giai thừa:'))
    if n<0:
        print('Yêu cầu nhập một số tự nhiên')
    else:
        ketqua=1
        if n==0:
            print('Kết quả = 1')
        else:
            for i in range(1,n+1):
                ketqua*=i
            print('Kết quả =',ketqua)
except:
    print('Định dạng đầu vào không hợp lệ')