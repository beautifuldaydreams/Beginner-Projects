import tkinter as tk
import random

def fahrenheit_to_celsius():
    fahrenheit = ent_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_celsius["text"] = f"{round(celsius, 2)}\N{DEGREE CELSIUS}"

window = tk.Tk()
window.title("Temperature Converter")

frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_result = tk.Label(master=frm_entry, text="℉")

ent_temperature.grid(row=0, column=0, sticky="e")
lbl_result.grid(row=0, column=1, sticky="w")

btn_convert = tk.Button(master=window, text="-->", command=fahrenheit_to_celsius)
lbl_celsius = tk.Label(master=window, text="℃")

frm_entry.grid(row=0, column=0, padx=8)
btn_convert.grid(row=0, column=1, padx=8, pady=8)
lbl_celsius.grid(row=0, column=2, padx=10)

window.mainloop()
