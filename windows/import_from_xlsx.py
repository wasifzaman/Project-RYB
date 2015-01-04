import configparser
from tkinter import *
import os, sys
sys.path.append(os.path.abspath(os.pardir) + '\widgets') #widget directory
sys.path.append(os.path.abspath(os.pardir) + '\controllers') #controllers
controllers = os.path.abspath(os.pardir) + '\controllers\\'
images = os.path.abspath(os.pardir) + '\images\\' #image directory

import button
import table
import textbox
import optionmenu

import ttkNotebook_style

''' root window '''
import_from_xlsx = Toplevel()
import_from_xlsx.option_add('*Label.Font', 'Helvetica 11')
import_from_xlsx.option_add('*Entry.Font', 'Helvetica 11')

''' frame initialization '''
import_ = Frame(import_from_xlsx)
button_frame = Frame(import_from_xlsx, bg='#2A2A3D')
button_container_frame = Frame(button_frame, bg='#2A2A3D')

''' frame packing '''
import_.pack(fill=X)
Frame(import_from_xlsx, bg='#C66100', height=5).pack(fill=X)
button_frame.pack(fill=X)
button_container_frame.pack()

''' widgets '''
import_xlsx_path = textbox.Textbox(import_, 0, 0)
import_browse_button = button.Button_(import_, 0, 1)
destination_path = textbox.Textbox(import_, 1, 0)
destination_browse_button = button.Button_(import_, 1, 1)
Label(import_, text='Optional', bg='#2C82DB').grid(row=2, columnspan=2, sticky=E+W)
time_xlsx_path = textbox.Textbox(import_, 3, 0)
time_browse_button = button.Button_(import_, 3, 1)
cancel_button = button.Button_(button_container_frame, 0, 0)
import_button = button.Button_(button_container_frame, 0, 1)

''' hover button colors '''
label_bg = '#1C528A'
hover_bg = '#2C82DB'

''' widget settings '''
import_xlsx_path.settings(label='Student info')
import_browse_button.settings(text='Browse', label_bg=label_bg, hover_bg=hover_bg)
destination_path.settings(label='Destination')
destination_browse_button.settings(text='Browse', label_bg=label_bg, hover_bg=hover_bg)
time_xlsx_path.settings(label='Time data')
time_browse_button.settings(text='Browse', label_bg=label_bg, hover_bg=hover_bg)
cancel_button.settings(text='Cancel', label_bg=label_bg, hover_bg=hover_bg)
import_button.settings(text='Import', label_bg=label_bg, hover_bg=hover_bg)

import_xlsx_path.label.config(width=10)
destination_path.label.config(width=10)
time_xlsx_path.label.config(width=10)