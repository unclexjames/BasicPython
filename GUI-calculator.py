# GUI calculator.py

from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title('calculate FISH')
GUI.geometry('800x600')

bg = PhotoImage(file='fish.png')

BG = Label(GUI, image=bg)
BG.pack()

L = Label(GUI,text='Please enter the number of FISH',font=('Angsana new',20))
L.pack()

v_quantity = StringVar() # เป็นตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=('Angsana new',20)) # None ได้ ถ้าไม่อยากใส่ front 'Ang'
E1.pack()

def Cal():
    try:
        quan = float(v_quantity.get())
        calc = quan * 39 # ราคา 39 บาท * จำนวนปลากี่กรอกมา
        messagebox.showinfo('TotalPrice','TotalPrice {} Bath'.format(calc))
        v_quantity.set('') # ถ้าไม่ error '' ในช่องแทน/คำนวนเสร้จกลับเป็น ''
        E1.focus() # cursor คำนวนเสร็จกลับไปใส่ตัวเลขต่อได้เลย
    except:
        messagebox.showwarning('please check','only numbers')
        v_quantity.set('1') # ถ้า error 1 ในช่องแทน/คำนวนเสร้จกลับเป็น 1


B = ttk.Button(GUI, text='calculate',command=Cal)
B.pack(ipadx=30,ipady=20) #ipadx,y ขยายความกว้าง x,y 

GUI.mainloop() # เพื่อให้โปรแกรม RUN ตลอดเวลา