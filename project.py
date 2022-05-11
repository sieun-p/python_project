import tkinter as tk
import turtle

def window_a():
    ###창 설정###
    ww = tk.Tk()
    ww.title('Stock Management Program: My account - Deposit')
    ww.geometry("800x600+100+100")
    width = 800
    height = 600
    screen_width = ww.winfo_screenwidth()
    screen_height = ww.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    ww.geometry('%dx%d+%d+%d' % (width, height, x, y))
    ww.resizable(0, 0)
    
    ###내용###
    label = tk.Label(ww, text = 'Type the amount of money to deposit', height = 10, font=('arial',15))
    label.pack()
    
    def enter(x):
        label.config(text='Current Amount : '+str(entry.get()))
    
    ###금액 입력###
    entry=tk.Entry(ww, width=30, bd=3)
    entry.bind("<Return>", enter)
    entry.pack()
    
    
def window_b():
    ##창 설정##
    ww = tk.Tk()
    ww.title('Stock Management Program: My account - Withdraw')
    ww.geometry("800x600+100+100")
    width = 800
    height = 600
    screen_width = ww.winfo_screenwidth()
    screen_height = ww.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    ww.geometry('%dx%d+%d+%d' % (width, height, x, y))
    ww.resizable(0, 0)
    
    ###내용###
    label = tk.Label(ww, text = 'Type the amount of money to withdraw', height = 10, font=('arial',15))
    label.pack()
    
    def enter(x):
        label.config(text='Current Amount : '+str(entry.get()))
    
    ###금액 입력###
    entry=tk.Entry(ww, width=30, bd=3)
    entry.bind("<Return>", enter)
    entry.pack()
    
    
def window_c():
    ##창 설정##
    ww = tk.Tk()
    ww.title('Stock Management Program: My account - State of Assets')
    ww.geometry("800x600+100+100")
    width = 800
    height = 600
    screen_width = ww.winfo_screenwidth()
    screen_height = ww.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    ww.geometry('%dx%d+%d+%d' % (width, height, x, y))
    ww.resizable(0, 0)
    
    ###내용###
    label = tk.Label(ww, text = 'stock & cash', height = 10, font=('arial',15))
    label.pack()
    
    ###비율 표현###
    canvas = tk.Canvas(ww, width=400, height=100, bd=3, relief='solid')
    canvas.pack()
    t = turtle.RawTurtle(canvas)
    
    ##현재 자산의 70%가 주식, 30%가 현금이라고 가정##
    t.pensize(5)
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(-100,-10)
    t.pendown()
    
    t.color('pink')
    t.begin_fill()
    for i in range(2):
        t.forward(140)
        t.left(90)
        t.forward(20)
        t.left(90)
    t.end_fill()
    
    t.penup()
    t.goto(40,-10)
    t.pendown()
    
    t.color('green')
    t.begin_fill()
    for i in range(2):
        t.forward(60)
        t.left(90)
        t.forward(20)
        t.left(90)
    t.end_fill()
   
#######################################################    
window = tk.Tk()
window.title("Stock Management Program: My account")
window.geometry("800x600+100+100")
width = 800
height = 600
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry('%dx%d+%d+%d' % (width, height, x, y))
window.resizable(0, 0)  

notice = tk.Label(window, text='My account', height = 10, font=('arial',15))
notice.pack()


a = tk.Button(window, text = 'deposit', overrelief='solid', width=30, font=('arial', 13), bd = 10, command=window_a, repeatdelay=1000, repeatinterval=100)
b = tk.Button(window, text = 'withdraw', overrelief='solid', width=30, font=('arial', 13), bd = 10, command=window_b, repeatdelay=1000, repeatinterval=100)
c = tk.Button(window, text = 'state of assets', overrelief='solid', width=30, font=('arial', 13), bd = 10, command=window_c, repeatdelay=1000, repeatinterval=100)

a.pack(ipady = 10, pady = 10)
b.pack(ipady = 10, pady = 10)
c.pack(ipady = 10, pady = 10)

window.mainloop()