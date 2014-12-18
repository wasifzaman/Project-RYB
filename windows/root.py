from tkinter import *
import os, sys
sys.path.append(os.path.abspath(os.pardir) + '\widgets') #widget directory
images = os.path.abspath(os.pardir) + '\images\\' #image directory

import button
import image

''' root window '''
root = Tk()

''' frame initialization '''
title_frame = Frame(root)
button_frame = Frame(root)
image_frame = Frame(root)

''' frame packing '''
title_frame.pack()
button_frame.pack(side=LEFT)
image_frame.pack(side=LEFT)

''' widgets '''
add_student = button.Button_(button_frame, 0, 0)
scan_student = button.Button_(button_frame, 1, 0)
student_db = button.Button_(button_frame, 2, 0)
export_db = button.Button_(button_frame, 3, 0)
change_lang = button.Button_(button_frame, 4, 0)
print_report = button.Button_(button_frame, 5, 0)
exit = button.Button_(button_frame, 6, 0)
school_image = image.Image_(image_frame, 0, 0)

''' widget settings '''
add_student.settings(text='Add Student', label_bg='teal', label_fg='white')
scan_student.settings(text='Scan Student', label_bg='teal', label_fg='white')
student_db.settings(text='Student Database', label_bg='teal', label_fg='white')
export_db.settings(text='Export Database', label_bg='teal', label_fg='white')
change_lang.settings(text='Change Language', label_bg='teal', label_fg='white')
print_report.settings(text='Print Report', label_bg='teal', label_fg='white')
exit.settings(text='Exit', label_bg='teal', label_fg='white')
school_image.settings(image=images + 'background_STU_ELM.jpg')

root.mainloop()