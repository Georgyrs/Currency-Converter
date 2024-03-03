import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk

def convert_currency():
    value = float(entry_value.get())
    converter = combo_converter.get()
    converterfr = combo_converterfr.get()

    val = None
    bval = None
    for i in range(len(l)):
        if listname[i] == converter:
            val = l[i]
        if listname[i] == converterfr:
            bval = l[i]

    if val is not None and bval is not None:
        result = value * val / bval
        label_result.config(text=f"{value} {converter} = {result:.2f} {converterfr}")
    else:
        label_result.config(text="Ошибка: Валюты не найдены.")

b = []
listkol = []
listname = []
listkurs = []

a = "https://www.cbr.ru/currency_base/daily/"
so = requests.get(a).text
s = BeautifulSoup(so, 'html.parser')

for r in s.find_all('tr'):
    for j in r.find_all('td'):
        b.append(j.text)

for i in range(2, len(b), 5):
    listkol.append(int(b[i]))

for i in range(3, len(b), 5):
    listname.append(b[i])

for i in range(4, len(b), 5):
    listkurs.append(str(b[i]))

for i in range(len(listkurs)):
    listkurs[i] = listkurs[i].replace(',', '.')

l = [float(listkurs[i]) / float(listkol[i]) for i in range(len(listkurs))]

window = tk.Tk()
window.title("Currency Converter")

# Set a fixed window size
window.geometry("400x300")

label_value = tk.Label(window, text="Amount:")
label_value.pack()

entry_value = tk.Entry(window)
entry_value.pack()

label_converter = tk.Label(window, text="From currency:")
label_converter.pack()

combo_converter = ttk.Combobox(window, values=listname)
combo_converter.pack()

label_converterfr = tk.Label(window, text="To currency:")
label_converterfr.pack()

combo_converterfr = ttk.Combobox(window, values=listname)
combo_converterfr.pack()

button_convert = tk.Button(window, text="Convert", command=convert_currency)
button_convert.pack()

label_result = tk.Label(window, text="")
label_result.pack()

window.mainloop()