#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#    May 10, 2019 02:25:53 PM IST  platform: Linux

import knn_vdo_path
import sys
from tkinter import messagebox
import MySQLdb 

END = "end-1c"

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def login_handler(top, root):
    # input username and password
    usr = top.Text1.get("1.0", END)
    password = top.Text2.get("1.0", END)
    dbc = MySQLdb.connect("localhost", "root", "Sneha@1998", "plate") 
    sql = "select *from loginInfo where usr = '"+usr+"'"
    cursor = dbc.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results[0][1])
    if(results[0][1] == password) :
        root.destroy()
        root = tk.Tk()
        knn_vdo_path_tl = knn_vdo_path.Toplevel1(root)
    else:    
	sys.stdout.flush()
        messagebox.showinfo("ERROR", "Invalid Login")   
if __name__ == '__main__':
    import knn_login
    knn_login.vp_start_gui()



