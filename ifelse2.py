friend = ['Korkai','Khorkai','Khorkwai']

friend2 = {'korkai':'คุณก.ไก่','khorkai':'คุณข.ไข่'}

visitor = 'Khorkwai'

if visitor in friend or visitor.title() in friend: # .title().upper().lower()
    print('เป็นลูกค้า เชิญขึ้นมาได้เลย')
    if visitor in friend2 or visitor.title() in friend2:
        print('สวัสดี' + friend2[visitor.title()])
    else:
        print('สวัสดีคุณลูกค้า')

else:
    print('เฮ้ย! คุณคือใคร')
