#for loop

for i in range(5):
    print('Hello',i)

print('----loop in List----')
friend = ['Korkai','Khorkai','Khorkwai']

for f in friend:
    print(f)
    if(f) == 'Korkai':
        print('สวัสดี ก')
    else:
        print('สวัสดี ข')
print('----loop in Dictionary----')

friend2 = {'Korkai': 'คุณ ก','Khorkai':'คุณ ข','Khorkwai':'คุณ ค'}

#show key
for f in friend2: 
    print(f)

#show items
for f in friend2.items(): 
    print(f)

# show key only
for f in friend2.keys(): 
    print(f)

#show value only
for f in friend2.values(): 
    print(f)

# show key , value
for k,v in friend2.items(): 
    print('Key:', k)
    print('Value:', v)

# ต้องการลำดับ
for i,f in enumerate(friend,start=1000): 
    print(i,f)

# ต้องการลำดับสำหรับ dict
for i,f in enumerate(friend2.items()):
    print(i,f)

# ต้องการลำดับสำหรับ dict แยก key
for i,(k,v) in enumerate(friend2.items()):
    print(i,k,v)