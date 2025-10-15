try:
    a=int(input('Hãy nhập vào số nguyên thứ nhất:'))
    b=int(input('Hãy nhập vào số nguyên thứ hai:'))
    while a>b:
        print('số thứ nhất phải nhỏ hơn số thứ hai')
        a=int(input('Hãy nhập vào số nguyên thứ nhất:'))
        b=int(input('Hãy nhập vào số nguyên thứ hai:'))
    sum=0
    i=a
    while i<=b:
        sum+=i
        i+=1
    print(f'Tổng của dãy số từ {a} đến {b} là {sum}')
except:
    print('Định dạng đầu vào không hợp lệ')
    