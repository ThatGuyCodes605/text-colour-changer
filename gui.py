


import tkinter as tk
from tkinter import ttk


class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('350x200')
        self.root.title('Linux')
        self.mainframe = tk.Frame(self.root, background='black')
        self.mainframe.pack(fill='both', expand=True)
        
        self.text = tk.Text(self.mainframe, background='black', foreground='white', font=("hack", 15), height=1, width=20)
        self.text.insert(tk.END, 'Linux is the best')
        self.text.config(state=tk.DISABLED)
        self.text.grid(row=0, column=0)
        
        self.set_text_field = ttk.Entry(self.mainframe)
        self.set_text_field.grid(row=1, column=0, pady=10, sticky='NWES')

        self.set_text_field = ttk.Entry(self.mainframe)
        self.set_text_field.grid(row=1, column=0, pady=10,sticky='NWES')
        set_text_button = ttk.Button(self.mainframe, text='Set Text', command=self.set_text)
        set_text_button.grid(row=1, column=1, pady=10)

        colour_options = ['red', 'blue', 'green', 'black', 'yellow', 'orange', 'gray']
        self.set_colour_field = ttk.Combobox(self.mainframe, values=colour_options)
        self.set_colour_field.grid(row=2, column=0, sticky='NWES', pady=10)
        set_colour_button = ttk.Button(self.mainframe, text='Set Colour', command=self.set_colour)
        set_colour_button.grid(row=2, column=1, pady=10)
        self.reverse_text = ttk.Button(self.mainframe, text="Reverse Text", command=self.reverse)
        self.reverse_text.grid(row=3, column=0, sticky='NWES', pady=10)
        self.root.mainloop()
        return
    
    def set_text(self):
        newtext = self.set_text_field.get()
        self.text.config(state=tk.NORMAL)
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, newtext)
        self.text.config(state=tk.DISABLED)

    def set_colour(self):
        newcolour = self.set_colour_field.get()
        self.text.config(foreground=newcolour)

    def reverse(self):
        current_text = self.text.get(1.0, tk.END).strip()
        reversed_text = current_text[::-1]
        self.text.config(state=tk.NORMAL)
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, reversed_text)
        self.text.config(state=tk.DISABLED)
if __name__ == '__main__':
    App()