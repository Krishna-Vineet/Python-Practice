import tkinter as tk
from tkinter import messagebox

def show_selected():
    selected_option = var.get()
    selected_item = listbox.curselection()
    if selected_option == 1:
        messagebox.showinfo("Selected Item", f"You selected: {listbox.get(selected_item)}")
    elif selected_option == 2:
        messagebox.showinfo("Selected Item", f"You selected: {selected_item}")

def submit():
    messagebox.showinfo("Submitted", f"Name: {name_entry.get()} \nAge: {age_spinbox.get()}")

root = tk.Tk()
root.title("Eye Appealing Tkinter GUI")
root.geometry("400x400")

# Colors
bg_color = "#121212"
button_color = "#009688"
text_color = "#ffffff"

# Main Frame
main_frame = tk.Frame(root, bg=bg_color)
main_frame.pack(fill=tk.BOTH, expand=True)

# Widgets
label = tk.Label(main_frame, text="Welcome to Tkinter GUI", font=("Helvetica", 16), bg=bg_color, fg=text_color)
label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

button = tk.Button(main_frame, text="Click Me!", command=lambda: messagebox.showinfo("Button Clicked", "You clicked the button."),
                    bg=button_color, fg="white")
button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

entry = tk.Entry(main_frame)
entry.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

checkbutton_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(main_frame, text="Check Me", variable=checkbutton_var, bg=bg_color, fg=text_color, selectcolor=button_color)
checkbutton.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

var = tk.IntVar()
radio_button1 = tk.Radiobutton(main_frame, text="Get Selection", variable=var, value=1, bg=bg_color, fg=text_color, selectcolor=button_color)
radio_button1.grid(row=4, column=0, padx=10, pady=5)
radio_button2 = tk.Radiobutton(main_frame, text="Get Index", variable=var, value=2, bg=bg_color, fg=text_color, selectcolor=button_color)
radio_button2.grid(row=4, column=1, padx=10, pady=5)

listbox = tk.Listbox(main_frame, bg=bg_color, fg=text_color, selectbackground=button_color, selectforeground=bg_color)
for item in ["Apple", "Banana", "Cherry", "Date"]:
    listbox.insert(tk.END, item)
listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, bg=bg_color, troughcolor=text_color, activebackground=text_color)
scrollbar.grid(row=5, column=2, sticky="NS", pady=5)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

name_label = tk.Label(main_frame, text="Name:", bg=bg_color, fg=text_color)
name_label.grid(row=6, column=0, padx=10, pady=5)
name_entry = tk.Entry(main_frame, bg=bg_color, fg=text_color)
name_entry.grid(row=6, column=1, padx=10, pady=5)

age_label = tk.Label(main_frame, text="Age:", bg=bg_color, fg=text_color)
age_label.grid(row=7, column=0, padx=10, pady=5)
age_spinbox = tk.Spinbox(main_frame, from_=0, to=120, bg=bg_color, fg=text_color)
age_spinbox.grid(row=7, column=1, padx=10, pady=5)

canvas = tk.Canvas(main_frame, width=100, height=50, bg="white")
canvas.grid(row=8, column=0, columnspan=2, padx=10, pady=5)
canvas.create_rectangle(50, 25, 150, 75, fill="blue")

# Buttons
submit_button = tk.Button(main_frame, text="Submit", command=submit, bg=button_color, fg="white")
submit_button.grid(row=9, column=0, padx=10, pady=10)
show_button = tk.Button(main_frame, text="Show Selected", command=show_selected, bg=button_color, fg="white")
show_button.grid(row=9, column=1, padx=10, pady=10)

root.mainloop()
