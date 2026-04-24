#Royce Daniel, 4/24/2026 "I made a call Mark"
import tkinter
from tkinter import messagebox

class CallCalculator:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Call Charge Calculator")

        self.label = tkinter.Label(self.main_window, text="Select Rate Category and Enter Minutes")
        self.label.pack()

        self.rate_var = tkinter.IntVar()
        self.rate_var.set(1)


        self.rb1 = tkinter.Radiobutton(self.main_window,
                                       text="Daytime ($0.02/min)",
                                       variable=self.rate_var,
                                       value=1)
        self.rb2 = tkinter.Radiobutton(self.main_window,
                                       text="Evening ($0.12/min)",
                                       variable=self.rate_var,
                                       value=2)
        self.rb3 = tkinter.Radiobutton(self.main_window,
                                       text="Off-Peak ($0.05/min)",
                                       variable=self.rate_var,
                                       value=3)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.minutes_label = tkinter.Label(self.main_window, text="Enter number of minutes:")
        self.minutes_entry = tkinter.Entry(self.main_window)

        self.minutes_label.pack()
        self.minutes_entry.pack()

        self.calc_button = tkinter.Button(self.main_window,
                                          text="Calculate Charge",
                                          command=self.calculate_charge)
        self.quit_button = tkinter.Button(self.main_window,
                                          text="Quit",
                                          command=self.main_window.destroy)

        self.calc_button.pack()
        self.quit_button.pack()

        tkinter.mainloop()

    def calculate_charge(self):
        try:
            minutes = float(self.minutes_entry.get())

            if self.rate_var.get() == 1:
                rate = 0.02
            elif self.rate_var.get() == 2:
                rate = 0.12
            else:
                rate = 0.05

            charge = minutes * rate

            messagebox.showinfo("Total Charge", f"Charge: ${charge:.2f}")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of minutes.")


if __name__ == "__main__":
    CallCalculator()