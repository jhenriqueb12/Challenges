from tkinter import *

# file = open('data.txt', 'a')
# file.close()

# def save(name, year, band, launch):
#   file = open('data.txt', 'a')
#   data = []
#   file.write = 

window = Tk()
window.title('Album das Bandas')
window.geometry('800x600')
window['bg'] = 'green'


# name

label_name = Label(window, text = 'Nome do album:', fg = 'white', font = 'arial 12')
label_name.place(X= 100, y= 200)


window.mainloop()