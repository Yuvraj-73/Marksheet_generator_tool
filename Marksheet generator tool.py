import tkinter as tk
from tkinter import messagebox
from fpdf import FPDF

def generate_marksheet():

    name = name_entry.get()
    roll_no = roll_entry.get()

    maths = int(maths_entry.get())
    physics = int(physics_entry.get())
    chemistry = int(chemistry_entry.get())
    english = int(english_entry.get())
    it = int(it_entry.get())

    total = maths + physics + chemistry + english + it
    percentage = (total / 500) * 100

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "Fail"

    marksheet = f"""
    ========================
          MARKSHEET
    ========================

    Name       : {name}
    Roll No    : {roll_no}

    Maths      : {maths}
    Physics    : {physics}
    Chemistry  : {chemistry}
    English    : {english}
    IT         : {it}

    ------------------------
    Total      : {total}/500
    Percentage : {round(percentage,2)}%
    Grade      : {grade}
    """

    pdf = FPDF()

    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, marksheet)

    pdf.output(f"{name}_marksheet.pdf")

    messagebox.showinfo("Success", "PDF Generated Successfully!")

root = tk.Tk()

root.title("Marksheet Generator")
root.geometry("400x500")

tk.Label(root, text="Student Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Roll Number").pack()
roll_entry = tk.Entry(root)
roll_entry.pack()

tk.Label(root, text="Maths Marks").pack()
maths_entry = tk.Entry(root)
maths_entry.pack()

tk.Label(root, text="Physics Marks").pack()
physics_entry = tk.Entry(root)
physics_entry.pack()

tk.Label(root, text="Chemistry Marks").pack()
chemistry_entry = tk.Entry(root)
chemistry_entry.pack()

tk.Label(root, text="English Marks").pack()
english_entry = tk.Entry(root)
english_entry.pack()

tk.Label(root, text="IT Marks").pack()
it_entry = tk.Entry(root)
it_entry.pack()

generate_button = tk.Button(
    root,
    text="Generate PDF Marksheet",
    command=generate_marksheet
)

generate_button.pack(pady=20)

root.mainloop()