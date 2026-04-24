#Royce Daniel, 4/24/2026 "MPG calc"
import tkinter
from tkinter import messagebox

class MPGCalc:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("MPG Calculator")

        self.gallons_label = tkinter.Label(self.main_window, text="Enter gallons:")
        self.gallons_entry = tkinter.Entry(self.main_window)

        self.miles_label = tkinter.Label(self.main_window, text="Enter miles:")
        self.miles_entry = tkinter.Entry(self.main_window)
        self.result_label = tkinter.Label(self.main_window, text="MPG:")

        self.calc_button = tkinter.Button(
            self.main_window,
            text="Calculate MPG",
            command=self.calculate_mpg
        )
        self.quit_button = tkinter.Button(
            self.main_window,
            text="Quit",
            command=self.main_window.destroy
        )
        self.quit_button.pack(side= "bottom")
        self.gallons_label.pack(side="bottom")
        self.gallons_entry.pack(side="bottom")

        self.miles_label.pack(side="bottom")
        self.miles_entry.pack(side="bottom")

        self.calc_button.pack(side="right")

        self.result_label.pack(side="top")

        tkinter.mainloop()

    def calculate_mpg(self):
        try:
            gallons = float(self.gallons_entry.get())
            miles = float(self.miles_entry.get())

            mpg = miles / gallons

            self.result_label.config(text=f"MPG: {mpg:.2f}")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Gallons cannot be zero.")

MPGCalc()