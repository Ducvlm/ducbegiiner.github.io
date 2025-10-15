try: 
    a=int(input('Hãy nhập vào số nguyên thứ nhất:'))
    b=int(input('Hãy nhập vào số nguyên thứ hai'))
    while a>b:
        print('Số thứ nhất phải nhỏ hơn số thứ hai')
        a=int(input('Hãy nhập vào số nguyên thứ nhất:'))
        b=int(input('Hãy nhập vào số nguyên thứ hai'))  
    sum=0
    for i in range(a,b+1):
            sum+=i
    print(f'Tổng của dãy số từ {a} đến {b} là {sum}')
except:
    print('Đầu vào không hợp lệ')
