from tkinter import *
from tkinter.ttk import *

from datetime import datetime
from pytz import timezone

root = Tk()
root.title('Clock')

def time():
    sokor = timezone('Asia/Seoul')
    sokor_time = datetime.now(sokor)
    string = sokor_time.strftime('%d %b %Y %I:%M:%S %p %Z')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=('500'), background='black', foreground='cyan')
label.pack(anchor='center')

time()
mainloop()