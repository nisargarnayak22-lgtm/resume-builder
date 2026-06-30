import tkinter as tk
from tkinter import messagebox
from resume_generator import create_resume

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Resume Builder")
root.geometry("700x750")

# ---------------- Labels and Entries ----------------

tk.Label(root, text="Resume Builder", font=("Arial", 20, "bold")).pack(pady=10)

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=50)
name_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root, width=50)
email_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root, width=50)
phone_entry.pack()

tk.Label(root, text="Address").pack()
address_text = tk.Text(root, width=50, height=3)
address_text.pack()

tk.Label(root, text="Education").pack()
education_text = tk.Text(root, width=50, height=3)
education_text.pack()

tk.Label(root, text="Skills").pack()
skills_text = tk.Text(root, width=50, height=3)
skills_text.pack()

tk.Label(root, text="Projects").pack()
projects_text = tk.Text(root, width=50, height=3)
projects_text.pack()

tk.Label(root, text="Experience").pack()
experience_text = tk.Text(root, width=50, height=3)
experience_text.pack()


# ---------------- Functions ----------------

def generate_resume():

    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    address = address_text.get("1.0", tk.END).strip()
    education = education_text.get("1.0", tk.END).strip()
    skills = skills_text.get("1.0", tk.END).strip()
    projects = projects_text.get("1.0", tk.END).strip()
    experience = experience_text.get("1.0", tk.END).strip()

    if name == "" or email == "" or phone == "":
        messagebox.showerror(
            "Error",
            "Please fill Name, Email and Phone."
        )
        return

    create_resume(
        name,
        email,
        phone,
        address,
        education,
        skills,
        projects,
        experience
    )

    messagebox.showinfo(
        "Success",
        "Resume Generated Successfully!"
    )


def clear_fields():

    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

    address_text.delete("1.0", tk.END)
    education_text.delete("1.0", tk.END)
    skills_text.delete("1.0", tk.END)
    projects_text.delete("1.0", tk.END)
    experience_text.delete("1.0", tk.END)


# ---------------- Buttons ----------------

tk.Button(
    root,
    text="Generate Resume",
    command=generate_resume,
    bg="green",
    fg="white",
    width=20
).pack(pady=10)

tk.Button(
    root,
    text="Clear",
    command=clear_fields,
    bg="orange",
    width=20
).pack()

tk.Button(
    root,
    text="Exit",
    command=root.destroy,
    bg="red",
    fg="white",
    width=20
).pack(pady=10)

# ---------------- Run ----------------

root.mainloop()