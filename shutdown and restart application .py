#shutdown and restart application using tkinter 

import os 
from tkinter import *

st = Tk()
st.title("My Shutdown Application")
st.geometry("400x400")
st.configure(background="LightBlue")
st.resizable(0,0)

r_button = Button(st, text="restart", font=("Bold",24), bg="LightGrey",cursor= "hand2" , command=lambda: os.system("sudo shutdown -r now"))
r_button.place(x=100, y=200)
s_button = Button(st, text="shutdown", font=("Bold",24), bg="LightGrey",cursor= "hand2" , command=lambda: os.system("sudo shutdown -h now"))
s_button.place(x=75, y=150)
st.mainloop()