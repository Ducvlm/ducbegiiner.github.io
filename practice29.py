try:
    n=int(input('Hãy nhập vào một số để tính bảng cửu chương: '))
    if 0<n<10:
        for i in range(1,11):
            print(f'{n} x {i} = {n*i}')
    else:
        print('Chỉ tính được bảng cửu chương từ 1 đến 9 thôi!')
except:
    print('Định dạng đầu vào không hợp lệ')
