import tkinter as tk
from tkinter import ttk
import turtle
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#############################################################################
'''
def for_yes:
    기존 창에 현재 자산 나타나도록 & 데이터 갱신


    
'''    

def sell(stock):
    ww_check = tk.Tk()
    ww_check.title('확인창')
    width=400
    height=300
    screen_width = ww_check.winfo_screenwidth()
    screen_height = ww_check.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    ww_check.geometry('%dx%d+%d+%d' % (width, height, x, y))
    ww_check.resizable(0, 0)
    check_label = tk.Label(ww_check, text = stock +'개를 매도하시겠습니까?')
    check_label.place(x=120,y=100)
    
    yes = tk.Button(ww_check, text = '네', overrelief='solid', width = 10, font=('arial',8), bd=2, command=ww_check.destroy)
    yes.place(x=100,y=200)
    no = tk.Button(ww_check, text = '아니오', overrelief='solid', width = 10, font=('arial',8), bd=2, command=ww_check.destroy)
    no.place(x=250,y=200)
    

###삼성전자
def window_stocks_a():
    ###창 설정###
    ww = tk.Tk()
    ww.title('Stock Management Program: Buy & Sell')
    width = 800
    height = 600
    screen_width = ww.winfo_screenwidth()
    screen_height = ww.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    ww.geometry('%dx%d+%d+%d' % (width, height, x, y))
    ww.resizable(0, 0)
    
    frame1=tk.Frame(ww, width=800, height=300, padx = 10, pady = 50, relief="solid", bd=1)
    frame1.pack(side="top")
    frame2=tk.Frame(ww, width=800, height=300, padx = 10, pady = 50, relief="solid", bd=1)
    frame2.pack(side="bottom")
    label_stock = tk.Label(frame2, text='수량을 입력하세요.', height = 5, font=('arial',15))
    label_stock.place(x=100, y=50)
    
    x=np.arange(1, 10, 1)
    y=2*x**2
    fig = Figure(figsize=(50,10),dpi=100)  #그리프 그릴 창 생성
    fig.set_size_inches(20, 2)
    fig.add_subplot(111).plot(x, y)#창에 그래프 하나 추가

    canvas = FigureCanvasTkAgg(fig, master=frame1)
    canvas.draw()
    canvas.get_tk_widget().pack()
    
    def value_check(self):
        label_stock.config(text="수량을 입력하세요.", font=('arial',10), height=10)
        valid = False
        if self.isdigit():
            if (int(self)*80000 <= 50000000):
                valid = True
        elif self == '':
            valid = True
        return valid
    
    def value_error(self):
        label_stock.config(text="주문 가능 수량을 초과하였습니다.\n다시 입력하세요.", font=('arial',10))
        
    validate_command=(frame2.register(value_check), '%P')
    invalid_command=(frame2.register(value_error), '%P')
    
    ##spinbox    
    spinbox=tk.Spinbox(frame2, from_ = 0, to = 10000, validate = 'all', validatecommand = validate_command, invalidcommand=invalid_command)
    spinbox.place(x=150, y=40)
    stock = str(spinbox.get())
 
    
    buy_bt = tk.Button(ww, text = 'Buy', overrelief = 'solid', width = 15, font=('arial',10), bd=3)
    buy_bt.place(x=500,y=350)
    
    sell_bt = tk.Button(ww, text='Sell', overrelief='solid', width = 15, font=('arial',10), bd=3, command = sell(stock))
    sell_bt.place(x=500, y=400)
    


    
##############################################
window = tk.Tk()
window.title("Stock Management Program: Buy & Sell")
width = 800
height = 600
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry('%dx%d+%d+%d' % (width, height, x, y))
window.resizable(0, 0)  

notice = tk.Label(window, text='Select stocks', height = 10, font=('arial',15))
notice.pack()

a = tk.Button(window, text = '삼성전자', overrelief='solid', width=30, font=('arial', 13), bd = 5, command=window_stocks_a, repeatdelay=1000, repeatinterval=100)
b = tk.Button(window, text = 'SK 하이닉스', overrelief='solid', width=30, font=('arial', 13), bd = 5, command=window_stocks_a, repeatdelay=1000, repeatinterval=100)

a.pack(ipady = 10, pady = 10)
b.pack(ipady = 10, pady = 10)

window.mainloop()