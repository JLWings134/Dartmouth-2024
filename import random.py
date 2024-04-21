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


def one_q():
    global m2q
    global m2a
    global m1q
    global m1a
    m1q = TRUE
    list_names[0].configure(state = tk.DISABLED, bg="grey")
    #time.sleep(1)
    if m1q and m1a:
        list_names[0].configure(state = tk.DISABLED, bg="green")
        list_names[1].configure(state = tk.DISABLED, bg="green")
        m1q = FALSE
        m1a = FALSE

    if m2q == TRUE or m2a == TRUE:
        list_names[0].configure(state = tk.NORMAL, bg="white")
        list_names[1].configure(state = tk.NORMAL, bg="white")
        list_names[2].configure(state = tk.NORMAL, bg="white")
        list_names[3].configure(state = tk.NORMAL, bg="white")
        
        m1q = FALSE
        m1a = FALSE
        m2q = FALSE
        m2a = FALSE


def one_a():
    global m2q
    global m2a
    global m1a
    global m1q
    m1a = TRUE
    list_names[1].configure(state = tk.DISABLED, bg="grey")
    #time.sleep(1)
    if m1q and m1a:
        list_names[0].configure(state = tk.DISABLED, bg="green")
        list_names[1].configure(state = tk.DISABLED, bg="green")
        m1q = FALSE
        m1a = FALSE
    if m2q == TRUE or m2a == TRUE:
        list_names[0].configure(state = tk.NORMAL, bg="white")
        list_names[1].configure(state = tk.NORMAL, bg="white")
        list_names[2].configure(state = tk.NORMAL, bg="white")
        list_names[3].configure(state = tk.NORMAL, bg="white")
                
        m1q = FALSE
        m1a = FALSE
        m2q = FALSE
        m2a = FALSE

def two_q():
    global m2q
    global m2a
    global m1a
    global m1q
    m2q = TRUE
    list_names[2].configure(state = tk.DISABLED, bg="grey")
    #time.sleep(1)
    if m2q and m2a:
        list_names[2].configure(state = tk.DISABLED, bg="green")
        list_names[3].configure(state = tk.DISABLED, bg="green")
        m2q = FALSE
        m2a = FALSE
    if m1q == TRUE or m1a == TRUE:
        list_names[0].configure(state = tk.NORMAL, bg="white")
        list_names[1].configure(state = tk.NORMAL, bg="white")
        list_names[2].configure(state = tk.NORMAL, bg="white")
        list_names[3].configure(state = tk.NORMAL, bg="white")
                
        m1q = FALSE
        m1a = FALSE
        m2q = FALSE
        m2a = FALSE

def two_a():
    global m2a
    global m2q
    global m1a
    global m1q
    m2a = TRUE
    list_names[3].configure(state = tk.DISABLED, bg="grey")
    #time.sleep(1)
    if m2q and m2a:
        list_names[2].configure(state = tk.DISABLED, bg="green")
        list_names[3].configure(state = tk.DISABLED, bg="green")
        m2q = FALSE
        m2a = FALSE
    if m1q == TRUE or m1a == TRUE:
        list_names[0].configure(state = tk.NORMAL, bg="white")
        list_names[1].configure(state = tk.NORMAL, bg="white")
        list_names[2].configure(state = tk.NORMAL, bg="white")
        list_names[3].configure(state = tk.NORMAL, bg="white")
        m1q = FALSE
        m1a = FALSE
        m2q = FALSE
        m2a = FALSE



#res2 = list(dict.items())


list2 = [one_q, one_a, two_q, two_a]

list_names = ["b1a", "b1q", "b2a", "b2q"]
def handle_selection(selected_option):
    global res2, list2, list_names, dict

    # First, check and destroy any existing buttons before creating new ones
    for btn in list_names:
        if isinstance(btn, tk.Button):  # Check if it is a button and destroy it
            btn.destroy()

    if selected_option == "Math":
        popup_label2.config(text="You selected Math")
        dict = {
            "5+5": "10",
            "1+1": "2"
        }
    elif selected_option == "Science":
        popup_label2.config(text="You selected Science")
        dict = {
            "Fe": "Iron",
            "Au": "Gold"
        }

    res2 = list(dict.items())
    list_names = [None, None, None, None]  # Reset list_names
    list2 = [one_q, one_a, two_q, two_a]

    count = 0

    counters =0

    for x in res2:
        
        button_question = tk.Button(root, text=x[0], command=list2[count])
        button_answer = tk.Button(root, text=x[1], command=list2[count+1])
        list_names[count] = button_question
        list_names[count+1] = button_answer
        if(counters == 0):
            button_question.place(relx=random.uniform(.1, .5), rely=random.uniform(.1, .5), anchor=tk.CENTER)
            button_answer.place(relx=random.uniform(.5, 0.9), rely=random.uniform(.5, 0.9), anchor=tk.CENTER)
        if(counters == 1):
            button_question.place(relx=random.uniform(.5, .9), rely=random.uniform(.1, .5), anchor=tk.CENTER)
            button_answer.place(relx=random.uniform(.1, 0.5), rely=random.uniform(.5, 0.9), anchor=tk.CENTER)
        counters+=1
        count += 2
        
        




def show_popup():
    global list_names
    root.withdraw()  # Hide the root window
    list_names[0].destroy()
    list_names[1].destroy()
    list_names[2].destroy()
    list_names[3].destroy()
        
    #create_popup()
    #root.destroy()
    #popup_window.deiconify()  # Show the popup window


def show_root():
    #popup_window.destroy()
    root.deiconify()  # Show the root window
    root.focus_force()  # Focus the root window


def create_popup():
    # Create the popup window
    popup_window = tk.Tk()
    popup_window.title("Math-Ch")

    # Add widgets, labels, buttons, etc. to the popup window
    popup_label = tk.Label(popup_window, text="Welcome to Math-Ch")
    popup_label.pack(padx=200, pady=200)

    popup_label2 = tk.Label(popup_window, text="Pick an option below!")
    popup_label2.place(relx=.5, rely=.2, anchor=tk.CENTER)



    

    options =["Math", "Science"]

    selected_option = tk.StringVar()
    dropdown = tk.OptionMenu(popup_window, selected_option, *options, command=handle_selection)
    dropdown.place(relx=.5, rely=.6, anchor=tk.CENTER)




    back_button = tk.Button(root, text="Back", command=show_popup)
    back_button.pack(pady=20)

    # Create a "Next" button to proceed to the root window
    next_button = tk.Button(popup_window, text="Next", command=show_root)
    next_button.pack(pady=10)


    

popup_window = tk.Tk()
popup_window.title("Math-Ch")

# Add widgets, labels, buttons, etc. to the popup window
popup_label = tk.Label(popup_window, text="Welcome to Math-Ch")
popup_label.pack(padx=200, pady=200)

popup_label2 = tk.Label(popup_window, text="Pick an option below!")
popup_label2.place(relx=.5, rely=.2, anchor=tk.CENTER)

options =["Math", "Science"]

selected_option = tk.StringVar()
dropdown = tk.OptionMenu(popup_window, selected_option, *options, command=handle_selection)
dropdown.place(relx=.5, rely=.6, anchor=tk.CENTER)




back_button = tk.Button(root, text="Back", command=show_popup)
back_button.pack(pady=20)

# Create a "Next" button to proceed to the root window
next_button = tk.Button(popup_window, text="Next", command=show_root)
next_button.pack(pady=10)



root.resizable(0,0)
root.withdraw()
root.mainloop()