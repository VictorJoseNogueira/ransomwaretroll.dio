import webbrowser
from tkinter import *
root = Tk( )
root.title('abrir browser')
root.geometry('300x200')

def google():
    webbrowser.open('www.google.com')

mygoogle = Button(root, text='abrir google!', command=google).pack(pady=20)


root.mainloop()
