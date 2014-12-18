'''
holds list of widgets and their properties
properties can only be option and textbox
'''



widget_list = ['test1', 'test2', 'test3'] #~temp proxy for widget list
widget_properties = {
	'test1': [
		('label', 'textbox'),
		('entry', 'textbox'),
		('errortext', 'input error, please check your input')
	],
	'test2': [
		('test_label2', 'textbox'),
		('options_test', 'options', ['option1', 'option2', 'option3']),
		('errortext', 'input error, please check your input'),
	]
} #~temp