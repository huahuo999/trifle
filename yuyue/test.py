from tkinter import *

def check():
    i =1
    if i==1:
        entry1.insert(0, "123")

if __name__ == '__main__':
    myWindow = Tk()
    myWindow.title('沈阳建筑大学预约')
    Label(myWindow, text="当前状态").grid(row=0)
    entry1 = Entry(myWindow)
    entry1.grid(row=0, column=1)
    Button(myWindow, text='Quit', command=myWindow.quit).grid(row=1, column=0, sticky=W, padx=5, pady=5)
    Button(myWindow, text='Run', command=check).grid(row=1, column=1, sticky=W, padx=5, pady=5)
    # 进入消息循环
    myWindow.mainloop()