from tkinter import *
import os, sys
sys.path.append(os.path.abspath(os.pardir) + '\widgets') #widget directory
images = os.path.abspath(os.pardir) + '\images\\' #image directory

import button
import image

''' root window '''
message = Tk()
message.option_add('*Label.Font', 'Helvetica 11')
message.overrideredirect(1)

''' frame initialization '''
border_frame = Frame(message, bg='#2A2A3D')
container_frame = Frame(border_frame, bg='#2A2A3D')
title_frame = Frame(container_frame)
image_frame = Frame(container_frame)
message_frame = Frame(container_frame)
button_frame = Frame(container_frame)
button_container_frame = Frame(button_frame)

''' frame packing '''
border_frame.pack()
container_frame.pack(padx=2, pady=(0, 2))
title_frame.grid(row=0, columnspan=2, sticky=E+W)
message_frame.grid(row=1, column=1, sticky=E+W+N+S)
button_frame.grid(row=2, columnspan=2, sticky=E+W+N+S)
button_container_frame.pack(padx=10, pady=10)

''' hover button colors '''
label_bg = '#1C528A'
hover_bg = '#2C82DB'

''' widgets '''
title = Label(title_frame, bg='#2A2A3D', fg='white')
message_ = Label(message_frame)
image_ = image.Image_(image_frame, 0, 0)

image_.label.pack(padx=10, pady=10)
message_.pack(padx=10, pady=10)
title.pack(fill=BOTH)