import Tkinter as tk
import tkMessageBox as messagebox


#Window info
win = tk.Tk()
win.title('Calendar')



def days():
    m = int(input("How many days are in the month? "))
    if m > 31 or m < 28:
        error()
        return
    f = -1
    for i in ['Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat']:
        f = f+1
        tk.Label(buttons, text=i).grid(row=0, column=0+f )
    n = int(input("Which day of the week does the month start(ex.Sun=0, Mon=1, etc.) "))
    if n < 0 or n>6:
        error()
        return
    else:
        x = 1
        m = m + n
        for i in range(m):
            day_button = tk.Button(buttons, text=(x-n))
            day_button.grid(row=(i+7)/7, column=(i+7)%7)
            day_button['state']= tk.DISABLED
            if x-n<=0:
                day_button.destroy()
            x = x + 1
        
def note():
    global v, note_button, clear_button, delete_button
    tk.Label(entry, text='What would you like to note down?').pack()
    v = tk.StringVar()
    note_box = tk.Entry(entry, textvariable=v)
    note_box.pack()
    note_button = tk.Button(entry, text= 'note')
    note_button.pack()
    note_button['command'] = note_press
    clear_button = tk.Button(entry, text='clear')
    clear_button.pack()
    clear_button['command'] = clear_press
    
                
def note_press():
    global note_check, delete_button
    note_check = tk.Checkbutton(notes, text=v.get(), onvalue=1, offvalue=0)
    note_check.pack()
    v.set("")  
       

def clear_press():
    for i in notes.winfo_children():
        i.destroy()   
    tk.Label(notes, text='NOTES').pack()    



def error():
    messagebox.showerror("Error", "Something illegal has been done. We will restore your program.")
    days()
    clear_press
    note_press
    
    
    
    
    
    
        
       

#Set up containers for Days and notes separation
buttons = tk.Frame(win)
notes = tk.Frame(win)
entry = tk.Frame(win)


#Adjust the location and size of the containers
buttons.pack(side=tk.LEFT, fill=tk.Y)
entry.pack(side=tk.LEFT, fill=tk.Y)
notes.pack(side=tk.LEFT, fill=tk.Y) 



days()
note()
tk.Label(notes, text='NOTES').pack()



#Begins event loop
win.mainloop()