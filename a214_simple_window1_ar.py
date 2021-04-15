##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk

def test_my_button():
    auth = tk.Frame(root)
    auth.grid(row='0', column='0', sticky='news')

# main window
root = tk.Tk()
root.wm_geometry("128x150")

# create empty frame
frame_login = tk.Frame(root)

frame_login.grid(row="0", column="0", sticky="news")

lbl_username = tk.Label(frame_login, text='Username:',font="Courier")
lbl_username.pack()

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_password = tk.Label(frame_login,text="Password:",font="Courier")
lbl_password.pack()

ent_password = tk.Entry(frame_login, bd=3, show="§")
ent_password.pack(pady=5)

btn_login = tk.Button(frame_login, text='Log In', command=test_my_button)
btn_login.pack(pady=5)

root.mainloop()