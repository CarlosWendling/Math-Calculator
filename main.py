from tkinter import *
from tkinter import ttk

# colors
color1 = '#1e1f1e' # black
color2 = '#feffff' # white
color3 = '#38576b' # blue
color4 = '#ECEFF1' # gray
color5 = '#FFAB40' # orange

window = Tk()
window.title('Calculator')
window.geometry("235x310")
window.config(bg=color1)

display_frame = Frame(window, width=235, height=50, bg=color3)
display_frame.grid(row=0, column=0)

body_frame = Frame(window, width=235, height=268)
body_frame.grid(row=1, column=0)

# labels
text_value = StringVar()
display_label = Label(display_frame, textvariable=text_value, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=color3, fg=color2)
display_label.place(x=0, y=0)

# global variable
all_values = ''

# functions
def input_values(event):
    global all_values
    all_values = all_values + str(event)

    # showing the result on the screen
    text_value.set(all_values)


def calculate ():
    try:
        global all_values
        result = eval(all_values)
    except SyntaxError:
        text_value.set("Equação Inválida.")
    except ZeroDivisionError:
        text_value.set("Impos. dividir por 0.")
    else:
        text_value.set(str(result))

        all_values = ""
        all_values = str(result)
    

def clean_screen ():
    global all_values
    all_values = ""
    text_value.set("")


# buttons
b_1 = Button(body_frame, command = clean_screen, text="C", width=11, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(body_frame, command = lambda: input_values('%'), text="%", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(body_frame, command = lambda: input_values('/') ,text="/", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(body_frame, command = lambda: input_values('7'), text="7", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(body_frame, command = lambda: input_values('8'), text="8", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(body_frame, command = lambda: input_values('9'), text="9", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(body_frame, command = lambda: input_values('*'), text="*", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

b_8 = Button(body_frame, command = lambda: input_values('4'), text="4", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(body_frame, command = lambda: input_values('5'), text="5", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(body_frame, command = lambda: input_values('6'), text="6", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(body_frame, command = lambda: input_values('-'), text="-", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

b_12 = Button(body_frame, command = lambda: input_values('1'), text="1", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(body_frame, command = lambda: input_values('2'), text="2", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(body_frame, command = lambda: input_values('3'), text="3", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(body_frame, command = lambda: input_values('+'), text="+", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

b_1 = Button(body_frame, command = lambda: input_values('0'), text="0", width=11, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=208)
b_2 = Button(body_frame, command = lambda: input_values('.'), text=".", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=208)
b_3 = Button(body_frame, command = calculate, text="=", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=208)

window.mainloop()