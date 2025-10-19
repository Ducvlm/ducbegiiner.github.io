try:
    n=int(input("Hãy nhập vào số tự nhiên để đảo ngược:"))
    if n<0:
        print('Hãy nhập một số tự nhiên')
    else:
        n2=str(n)
        sodaonguoc=n2[::-1]
        print('Số đảo ngược là:',sodaonguoc)
except:
    print('Định dạng đầu vào không hợp lệ')