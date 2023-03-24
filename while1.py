# While loop

money = 1000
transfer = 10000

print('check:' , money < transfer)

while money < transfer:
    print('กรุณากรอกตัวเลขใหม่')
    transfer = int(input('New transfer: '))
    if transfer > 100000:
        print('เรียกผู้จัดการ')
        break
    
print('โอนได้ถ้าผู้จัดการอณุญาต')