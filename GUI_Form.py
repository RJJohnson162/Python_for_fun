""" creating a graphical user interface that is a form
taking in 1st number and 2nd number the displays the result in a dialog box
adjacent to the result label once the addition button is clicked.
There should also be a reset button """
import tkinter as tk
def add_numbers():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    sum = num1 + num2
    result_label.config(text=f"{sum}")
def reset():
    num1_entry.delete(0, 'end')
    num2_entry.delete(0, 'end')
    result_label.config(text='')

root = tk.Tk()
root.configure(background="aqua")
root.title("Addition")
frame = tk.Frame(root)
frame.pack()
label = tk.Label(frame, text="first Number: ")
label.grid(row=0, column=0)
num1_entry = tk.Entry(frame)
num1_entry.grid(row=0, column=1)
label = tk.Label(frame, text="second Number: ")
label.grid(row=1, column=0)
num2_entry = tk.Entry(frame)
num2_entry.grid(row=1, column=1)
#for the result now
result_label = tk.Label(frame, bg="yellow", fg="black", font=('Helvetica', 36),
                        borderwidth=5, relief="solid")
result_label.grid(row=2, columnspan=2)
submit_button = tk.Button(frame, text="Submit", command=add_numbers)
submit_button.grid(columnspan=2)
reset_button = tk.Button(frame, text="Reset", command=reset)
reset_button.grid(row=4, columnspan=2)
root.mainloop()


if __name__ == "__main__":
    add_numbers()
    reset()
