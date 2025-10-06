age = int(input("your age: "))
if age >=18:
    nationality = input("what is your nationality: ")
    nationality2 = nationality.lower()
    if nationality2 == "vietnamese":
        print("ban du dieu kien de bo phieu")
    else:
        print("you aren't VietNam's citizens")
else:
    print("ban chua du 18 tuoi de bo phieu")