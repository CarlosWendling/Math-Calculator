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
window.geometry("235x318")
window.config(bg=color1)

display_frame = Frame(window, width=235, height=50, bg=color3)
display_frame.grid(row=0, column=0)

body_frame = Frame(window, width=235, height=268)
body_frame.grid(row=1, column=0)

window.mainloop()