import tkinter as tk
from tkinter import messagebox
import calendar

def showCal():
    new_gui = tk.Tk()
    new_gui.config(background="#C9DABF")
    new_gui.title("CALENDAR")
    new_gui.geometry("580x600")
    new_gui.iconbitmap(r'rarp.ico')

    try:
        fetch_year = int(year_field.get())
        cal_content = calendar.calendar(fetch_year)
        cal_year = tk.Label(new_gui, text=cal_content, font="Consolas 10 bold", justify=tk.LEFT)
        cal_year.grid(row=5, column=1, padx=20, pady=20)
        
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid year")
    
    new_gui.mainloop()

def clear():
    year_field.delete(0, tk.END)

if __name__ == "__main__":
    gui = tk.Tk()
    gui.config(background="#C9DABF")
    gui.title("CALENDAR")
    gui.geometry("540x540")
    gui.iconbitmap(r'rarp.ico')

    frame = tk.Frame(gui, bg="#C9DABF", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    cal = tk.Label(frame, text="CALENDAR", fg="#8D493A",bg="#C9DABF" ,font=("Gupter", 28, 'bold'))
    cal.grid(row=0, column=0, columnspan=2, pady=10)

    year = tk.Label(frame, text="Enter Year", fg="#522258",bg="#C9DABF", font=("Gupter", 14))
    year.grid(row=1, column=0, pady=5, sticky=tk.E)
    
    year_field = tk.Entry(frame, font=("Gupter", 14))
    year_field.grid(row=1, column=1, pady=5, padx=5)

    Show = tk.Button(frame, text="Show Calendar", fg="#D95F59", bg="#EEE4B1", font=("Gupter", 14), command=showCal, anchor=tk.CENTER)
    Show.grid(row=2, column=0, columnspan=2, pady=5)

    Clear = tk.Button(frame, text="Clear", fg="#C63C51", bg="#EEE4B1", font=("Gupter", 14), command=clear, anchor=tk.CENTER)
    Clear.grid(row=3, column=0, columnspan=2, pady=5)

    Exit = tk.Button(frame, text="Exit", fg="#8C3061", bg="#EEE4B1", font=("Gupter", 14), command=gui.quit, anchor=tk.CENTER)
    Exit.grid(row=4, column=0, columnspan=2, pady=5)
    
    gui.mainloop()
