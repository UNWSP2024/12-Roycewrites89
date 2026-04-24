#Royce Daniel, 4/24/2026 "Joe's auto"
import tkinter
import tkinter.messagebox

class joesauto():
    def __init__(self):

        self.main_window = tkinter.Tk()
        self.main_window.title("Joe's auto")

        self.topframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

        self.label = tkinter.Label(
            self.main_window,
            text="Welcome to Joe's auto. Please select which services you'd like."
        )
        self.label.pack()

        self.var1 = tkinter.IntVar()
        self.var2 = tkinter.IntVar()
        self.var3 = tkinter.IntVar()
        self.var4 = tkinter.IntVar()
        self.var5 = tkinter.IntVar()
        self.var6 = tkinter.IntVar()
        self.var7 = tkinter.IntVar()

        self.cb1 = tkinter.Checkbutton(self.bottomframe, text="Oil Change-$30", variable=self.var1)
        self.cb2 = tkinter.Checkbutton(self.bottomframe, text="Lube Job-$20", variable=self.var2)
        self.cb3 = tkinter.Checkbutton(self.bottomframe, text="Radiator Flush-$40", variable=self.var3)
        self.cb4 = tkinter.Checkbutton(self.bottomframe, text="Transmission Fluid-$100", variable=self.var4)
        self.cb5 = tkinter.Checkbutton(self.bottomframe, text="Inspection-$35", variable=self.var5)
        self.cb6 = tkinter.Checkbutton(self.bottomframe, text="Muffler Replacement-$200", variable=self.var6)
        self.cb7 = tkinter.Checkbutton(self.bottomframe, text="Tire Rotation-$20", variable=self.var7)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

        self.topframe.pack()
        self.bottomframe.pack()

        self.okbutton = tkinter.Button(self.bottomframe, text="Confirm", command=self.showchoice)
        self.quit_button = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)

        self.okbutton.pack()
        self.quit_button.pack()

        tkinter.mainloop()

    def showchoice(self):
        total = 0
        selected = []

        if self.var1.get():
            selected.append("Oil Change")
            total += 30
        if self.var2.get():
            selected.append("Lube Job")
            total += 20
        if self.var3.get():
            selected.append("Radiator Flush")
            total += 40
        if self.var4.get():
            selected.append("Transmission Fluid")
            total += 100
        if self.var5.get():
            selected.append("Inspection")
            total += 35
        if self.var6.get():
            selected.append("Muffler Replacement")
            total += 200
        if self.var7.get():
            selected.append("Tire Rotation")
            total += 20

        if selected:
            message = "Services:\n" + "\n".join(selected)
            message += f"\n\nTotal: ${total}"
        else:
            message = "Just looking around, huh?"

        tkinter.messagebox.showinfo("Receipt", message)



if __name__ == "__main__":
    MYGUI = joesauto()