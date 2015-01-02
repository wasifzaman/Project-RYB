import tkinter.ttk

tab_style = tkinter.ttk.Style()
tab_style.theme_use('alt')
tab_style.configure('TNotebook.Tab',
	font=('Helvetica', 11),
	background='#1C528A',
	foreground='white',
	padding=10)
tab_style.configure('TNotebook', borderwidth=0, background='#2A2A3D')

tab_style.layout("Tab",
[('Notebook.tab', {'sticky': 'nswe', 'children':
    [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
            [('Notebook.label', {'side': 'top', 'sticky': ''})],
    })],
})]
)

tab_style.map('TNotebook.Tab', background=[('selected', 'teal')])