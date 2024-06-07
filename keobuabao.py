from random import randint #hàm random

print("Trò chơi Kéo Búa Bao ^^") 
player = input("Vui lòng nhập Kéo, Búa, Bao để bắt đầu trờ chơi: ") #cho người dùng nhập vào
computer = randint(0,2) #chọn ngẫu nhiên 1 số cho computer từ 0 đến 

if computer == 0: # điều kiện khi computer = 0
    cumputer = "Kéo"
if computer == 1: # điều kiện khi computer = 1
    computer = "Búa" # dấu = là mệnh đề gán cho dòng code này
if computer == 2: # điều kiện khi computer = 2
    computer = "Bao"

print("-------")
print("Bạn chọn: ", player)
print("Máy tính chọn: ", computer)
print("-------")

if player == computer:
    print("Hòa")
else:
    if player == "Kéo":
        if computer == "Búa":
            print("Computer thắng")
        else:
            print("Bạn thắng")

    elif player == "Búa":
        if computer == "Bao":
            print("Computer thắng")
        else:
            print("Bạn thắng ")

    elif player == "Bao":
        if computer == "Kéo":
            print("Computer thắng")
        else:
            print("Bạn thắng")
    else:
        print("Nhập sai! Vui lòng khởi chạy lại.")