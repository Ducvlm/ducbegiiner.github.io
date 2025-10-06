chuoiso = list(input("Nhập chuỗi số: ").split())
if all(x.isdigit() for x in chuoiso):
    tong = sum(int(x) for x in chuoiso)
    print("Tổng của chuỗi số là:", tong)
else: 
    print("Dữ liệu nhập vào không hợp lệ.")