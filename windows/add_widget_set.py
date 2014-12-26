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

image.Image_.set = lambda self, img_path: self.settings(image=img_path, resize=(135, 135))
textbox.Textbox.set = lambda self, text: self.settings(entry=text)
date_textbox.Date_textbox.set = lambda self, dt_text: self.settings(date=dt_text)
multiline_textbox.Multiline_textbox.set = lambda self, text: self.settings(entry=text)