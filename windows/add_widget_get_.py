'''
Here we define the default get_ function used to pull data
from widgets as this is a function the UI will use.
'''

from tkinter import *
import datetime
import os, sys
sys.path.append(os.path.abspath(os.pardir) + '\widgets') #widget directory

import image
import textbox
import date_textbox
import multiline_textbox

image.Image_.get_ = lambda self: self.img_path
textbox.Textbox.get_ = lambda self: self.entry.get()
date_textbox.Date_textbox.get_ = lambda self: datetime.datetime.strptime(self.month_entry.get() + '/' + self.day_entry.get() + '/' + self.year_entry.get(), '%m/%d/%Y')
multiline_textbox.Multiline_textbox.get_ = lambda self: self.entry.get('1.0', END+'-1c')