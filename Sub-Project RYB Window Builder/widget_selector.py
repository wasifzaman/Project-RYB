'''
project RYB window builder selector
'''

__author__ = "Wasif Zaman"
__status__ = "developement"
__version__ = "0.0.01"



from tkinter import *
from widget_list import widget_list, widget_properties
import inspect


property_types = {
	'textbox': Entry,
	'options': OptionMenu
}

widget_to_add_properties = {}

selector_window = Toplevel() # top-level window

selector_window.focus_set() #~temp

widget_list_frame = Frame(selector_window) #frame for holding selector option
widget_prop_frame = Frame(selector_window) #frame for holding widget properties
confirmation_frame = Frame(selector_window) #frame for holding add, cancel button

widget_list_frame.pack() #pack vertically
widget_prop_frame.pack() #^
confirmation_frame.pack() #^

selected_widget = StringVar()		#widget selector stringvar
selected_widget.set(widget_list[0])	#set to first option	

widget_selector = OptionMenu(widget_list_frame, selected_widget, *tuple(widget_list))		#optionmenu widget
widget_selector.pack() 	#optionmenu widget packed

def show_widget_properties(*args):
	''' selector widget change event catcher '''

	for child in widget_prop_frame.winfo_children():
		''' delete all child in widget_prop_frame '''
		child.destroy()

	try:
		''' assertion if the widget has properties '''
		assert selected_widget.get() in widget_properties
	except AssertionError:
		print('Assertion Error on line ' + str(inspect.currentframe().f_lineno))
		return

	for widget_prop in widget_properties[selected_widget.get()]:
		''' create properties '''
		label = widget_prop[0] 		#property label
		prop_type = widget_prop[1]	#property type
		
		Label(widget_prop_frame, text=label).pack() #tkinter label for property label

		if prop_type == 'options':
			''' if multi choice property '''
			widget_to_add_properties[label] = StringVar()
			widget_to_add_properties[label].set(widget_prop[2][0])
			property_types[prop_type](widget_prop_frame, widget_to_add_properties[label], *tuple(widget_prop[2])).pack()

		elif prop_type in property_types:
			''' single choice properties '''
			widget_to_add_properties[label] = property_types[prop_type](widget_prop_frame)
			widget_to_add_properties[label].pack()
	return

selected_widget.trace('w', show_widget_properties) #bind show_widget_properties




''' confirmation and output '''
def string_output():
	dict_output = {}
	for prop, val in widget_to_add_properties.items():
		''' populate the list with data instead '''
		dict_output[prop] = val.get()
	print(dict_output)
	return



Button(confirmation_frame, text='Add', command=string_output).pack(side=LEFT)
Button(confirmation_frame, text='Cancel', command=selector_window.destroy).pack(side=RIGHT)

selector_window.mainloop() #~temp