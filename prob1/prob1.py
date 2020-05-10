# CWID 889478913
# Name Michael Rozsypal
# Problem 1



import tkinter as tk
import tkinter.ttk as ttk

win = tk.Tk()
val = 0

def getVal():
    global entry
    global val
    print('+++ Value Entered By User: ', entry.get())
    val = entry.get()
    val = int(val)
    temp = 0
    print("Printing val")
    print(val)
    if(val != None):
        for i in range(val):
            print("Inside first for loop ")
            temp = temp + 1
            f = tk.Frame(win)
            for x in range(temp):
                print("Inside second for loop ")
                
                lbl = tk.Label(f, text=temp, bg='orange', fg='blue',anchor='nw')
                lbl.pack(side=tk.LEFT)
                
            f.pack(anchor='center')
    



lbl = tk.Label(win, text='Please Enter a Number:')
lbl.pack(side=tk.TOP, anchor='nw') 

entry = tk.Entry(win)
entry.pack(side=tk.LEFT, fill=tk.X,anchor = 'nw')

button = tk.Button(win, text='SUBMIT', command = getVal)
button.pack(side=tk.LEFT, anchor='nw')


win.mainloop()