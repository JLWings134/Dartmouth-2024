import random
from tkinter import *
import tkinter as tk
from tkinter import ttk
import time
root = tk.Tk()


root.title("Math-ch")

root.geometry('600x600')



m1q = FALSE
m1a = FALSE
m2q = FALSE
m2a = FALSE
m3q = FALSE
m3a = FALSE

def one_q():
    global m2q
    global m2a
    global m1q
    global m1a
    global m3q
    global m3a
    m1q = TRUE
    list_names[0].configure(state = tk.DISABLED, bg="grey")

    if m1q and m1a:
        list_names[0].configure(state = tk.DISABLED, bg="green")
        list_names[1].configure(state = tk.DISABLED, bg="green")
        m1q = FALSE
        m1a = FALSE
    check()

    if m2q == TRUE or m2a ==  TRUE or m3q == TRUE or m3a == TRUE:
       
        for x in list_names:
            if x.cget('bg') != "green":
                x.configure(state = tk.NORMAL, bg="white")
        
        
        m1q = FALSE
        m1a = FALSE
        m2q = FALSE
        m2a = FALSE
        m3q = FALSE
        m3a = FALSE


def one_a():
    global m2q
    global m2a
    global m1a
    global m1q
    global m3q
    global m3a
    m1a = TRUE
    list_names[1].configure(state = tk.DISABLED, bg="grey")

    if m1q and m1a:
        list_names[0].configure(state = tk.DISABLED, bg="green")
        list_names[1].configure(state = tk.DISABLED, bg="green")
        m1q = FALSE
        m1a = FALSE
    check()
    if m2q == TRUE or m2a == TRUE or m3q == TRUE or m3a == TRUE:
        
        for x in list_names:
            if x.cget('bg') != "green":
                x.configure(state = tk.NORMAL, bg="white")
        
                
        m1q = FALSE
        m1a = FALSE
        m2q = FALSE
        m2a = FALSE
        m3q = FALSE
        m3a = FALSE

def two_q():
    global m2q
    global m2a
    global m1a
    global m1q
    global m3q
    global m3a
    m2q = TRUE
    list_names[2].configure(state = tk.DISABLED, bg="grey")

    if m2q and m2a:
        list_names[2].configure(state = tk.DISABLED, bg="green")
        list_names[3].configure(state = tk.DISABLED, bg="green")
        m2q = FALSE
        m2a = FALSE
    check()
    if m1q == TRUE or m1a == TRUE or m3q == TRUE or m3a == TRUE:
        
        for x in list_names:
            if x.cget('bg') != "green":
                x.configure(state = tk.NORMAL, bg="white")
        
                
        m1q = FALSE
        m1a = FALSE
        m2q = FALSE
        m2a = FALSE
        m3q = FALSE
        m3a = FALSE

def two_a():
    global m2a
    global m2q
    global m1a
    global m1q
    global m3q
    global m3a
    m2a = TRUE
    list_names[3].configure(state = tk.DISABLED, bg="grey")

    if m2q and m2a:
        list_names[2].configure(state = tk.DISABLED, bg="green")
        list_names[3].configure(state = tk.DISABLED, bg="green")
        m2q = FALSE
        m2a = FALSE
    check()
    if m1q == TRUE or m1a == TRUE or m3q == TRUE or m3a == TRUE:
        
        for x in list_names:
            if x.cget('bg') != "green":
                x.configure(state = tk.NORMAL, bg="white")
        
        m1q = FALSE
        m1a = FALSE
        m2q = FALSE
        m2a = FALSE
        m3q = FALSE
        m3a = FALSE



def three_q():
    global m2a
    global m2q
    global m1a
    global m1q
    global m3q
    global m3a
    m3q = TRUE
    list_names[4].configure(state = tk.DISABLED, bg="grey")

    if m3q and m3a:
        list_names[4].configure(state = tk.DISABLED, bg="green")
        list_names[5].configure(state = tk.DISABLED, bg="green")
        m3q = FALSE
        m3a = FALSE
    check()
    if m1q == TRUE or m1a == TRUE or m2q == TRUE or m2a == TRUE:
       
        for x in list_names:
            if x.cget('bg') != "green":
                x.configure(state = tk.NORMAL, bg="white")
        
        m1q = FALSE
        m1a = FALSE
        m2q = FALSE
        m2a = FALSE
        m3q = FALSE
        m3a = FALSE



def three_a():
    global m2a
    global m2q
    global m1a
    global m1q
    global m3q
    global m3a
    m3a = TRUE
    list_names[5].configure(state = tk.DISABLED, bg="grey")

    if m3q and m3a:
        list_names[4].configure(state = tk.DISABLED, bg="green")
        list_names[5].configure(state = tk.DISABLED, bg="green")
        m3q = FALSE
        m3a = FALSE
    check()
    if m1q == TRUE or m1a == TRUE or m2q == TRUE or m2a == TRUE:
        
        for x in list_names:
            if x.cget('bg') != "green":
                x.configure(state = tk.NORMAL, bg="white")
        
        
        m1q = FALSE
        m1a = FALSE
        m2q = FALSE
        m2a = FALSE
        m3q = FALSE
        m3a = FALSE





def check():
    global m2a
    global m2q
    global m1a
    global m1q
    global m3q
    global m3a
    global list_names
    global win_screen
    bcount = 0
    for x in list_names:
        if x.cget('bg') == "green":
            bcount+=1
        if bcount == 6:
            list_names[0].destroy()
            list_names[1].destroy()
            list_names[2].destroy()
            list_names[3].destroy()
            list_names[4].destroy()
            list_names[5].destroy()
            win_screen = tk.Label(root, text="You Win!")
            win_screen.configure(font=('Helvetica', 40))
            win_screen.place(relx=.5, rely=.5, anchor=tk.CENTER)


delete = False
list2 = [one_q, one_a, two_q, two_a, three_q, three_a]

list_names = ["b1a", "b1q", "b2a", "b2q", "b3q", "b3a"]
def handle_selection(selected_option):
    global res2, list2, list_names, dict, delete

    for btn in list_names:
        if isinstance(btn, tk.Button): 
            btn.destroy()

    if selected_option == "Math":

        dict = {
            "5+5": "10",
            "1+1": "2",
            "15*3": "45"
        }
    elif selected_option == "Science":

        dict = {
            "Fe": "Iron",
            "Au": "Gold",
            "Ag": "Silver"
        }
    elif selected_option == "Sports":

        dict = {
            "NJ Devils": "Hockey",
            "NY Jets": "Football",
            "Man United": "Soccer"
        }
    else:

        delete = True

        
    next_button.configure(state = tk.NORMAL)
    res2 = list(dict.items())
    list_names = [None, None, None, None, None, None]  
    list2 = [one_q, one_a, two_q, two_a, three_q, three_a]

    count = 0
    limitsx = .1
    limitsy = .1
    random_num = 1
    for x in res2:
        
        button_question = tk.Button(root, text=x[0], command=list2[count])
        button_answer = tk.Button(root, text=x[1], command=list2[count+1])
        list_names[count] = button_question
        list_names[count+1] = button_answer
        button_question.place(relx=random.uniform(.1, .9), rely=random.uniform(.1, .9), anchor=tk.CENTER)
        button_answer.place(relx=random.uniform(.1, 0.9), rely=random.uniform(.1, 0.9), anchor=tk.CENTER)
        count += 2
        
        




def show_popup():
    global list_names
    global delete
    root.withdraw()  
    if delete == TRUE:
        list_names[0].destroy()
        list_names[1].destroy()
        list_names[2].destroy()
        list_names[3].destroy()
        list_names[4].destroy()
        list_names[5].destroy()






    popup_label2 = tk.Label(popup_window, text="Pick an option below!")
    popup_label2.configure(font=('Helvetica', 15))

    popup_label2.place(relx=.5, rely=.6, anchor=tk.CENTER)

    if popup_label2.cget('text') == "Pick an option below!":
        next_button.configure(state = tk.DISABLED)




def show_root():
    global win_screen

    
    root.deiconify() 
    root.focus_force() 
    win_screen.destroy()
 


def create_popup():
    global next_button
    popup_window = tk.Tk()
    popup_window.title("Math-Ch")

    popup_label = tk.Label(popup_window, text="Welcome to Math-Ch")
    popup_label.configure(font=('Helvetica', 30))
    popup_label.place(relx=.5, rely=.2, anchor=tk.CENTER)
    popup_window.geometry('500x500')

    popup_label3.configure(font=('Helvetica', 15))
    popup_label3.place(relx=.5, rely=.4, anchor=tk.CENTER)
    

    popup_label2 = tk.Label(popup_window, text="Pick an option below!")

    if popup_label2.cget('text') == "Pick an option below!":
        next_button.configure(state = tk.DISABLED)

    popup_label2.configure(font=('Helvetica', 15))

    popup_label2.place(relx=.5, rely=.6, anchor=tk.CENTER)



    

    options =["Math", "Science", "Sports"]

    selected_option = tk.StringVar()
    dropdown = tk.OptionMenu(popup_window, selected_option, *options, command=handle_selection)
    dropdown.place(relx=.5, rely=.68, anchor=tk.CENTER)



    back_button = tk.Button(root, text="Back", command=show_popup)
    back_button.pack(pady=20)


    win_screen = tk.Label(root, text="")
    win_screen.place(relx=.5, rely=.5, anchor=tk.CENTER)





    next_button = tk.Button(popup_window, text="Next", command=show_root)

    next_button.place(relx=.5, rely=.9, anchor=tk.CENTER)



    

popup_window = tk.Tk()
popup_window.title("Math-Ch")

popup_label = tk.Label(popup_window, text="Welcome to Math-Ch")
popup_label.configure(font=('Helvetica', 30))
popup_label.place(relx=.5, rely=.2, anchor=tk.CENTER)
popup_window.geometry('500x500')



popup_label3 = tk.Label(popup_window, text="Select the correct pairs to win!")
popup_label3.configure(font=('Helvetica', 15))
popup_label3.place(relx=.5, rely=.4, anchor=tk.CENTER)






popup_label2 = tk.Label(popup_window, text="Pick an option below!")
popup_label2.configure(font=('Helvetica', 15))
popup_label2.place(relx=.5, rely=.6, anchor=tk.CENTER)




options =["Math", "Science", "Sports"]

selected_option = tk.StringVar()
dropdown = tk.OptionMenu(popup_window, selected_option, *options, command=handle_selection)
dropdown.place(relx=.5, rely=.68, anchor=tk.CENTER)

win_screen = tk.Label(root, text="")
win_screen.place(relx=.5, rely=.5, anchor=tk.CENTER)




back_button = tk.Button(root, text="Back", command=show_popup)
back_button.pack(pady=20)

next_button = tk.Button(popup_window, text="Next", command=show_root)

next_button.place(relx=.5, rely=.9, anchor=tk.CENTER)

if popup_label2.cget('text') == "Pick an option below!":
    next_button.configure(state = tk.DISABLED)

root.resizable(0,0)
popup_window.resizable(0,0)
root.withdraw()
root.mainloop()