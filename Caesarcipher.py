from tkinter import *
from tkinter import messagebox

# Caesar Cipher Functions
def encrypt_text():
    try:
        text = message_entry.get("1.0", END).strip()
        shift = int(shift_entry.get())

        result = ""

        for char in text:
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                result += chr((ord(char) - offset + shift) % 26 + offset)
            else:
                result += char

        output_text.delete("1.0", END)
        output_text.insert(END, result)

    except:
        messagebox.showerror("Error", "Enter a valid shift value")


def decrypt_text():
    try:
        text = message_entry.get("1.0", END).strip()
        shift = int(shift_entry.get())

        result = ""

        for char in text:
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                result += chr((ord(char) - offset - shift) % 26 + offset)
            else:
                result += char

        output_text.delete("1.0", END)
        output_text.insert(END, result)

    except:
        messagebox.showerror("Error", "Enter a valid shift value")


def clear_fields():
    message_entry.delete("1.0", END)
    shift_entry.delete(0, END)
    output_text.delete("1.0", END)


# Main Window
root = Tk()
root.title("Caesar Cipher Encryption & Decryption")
root.geometry("750x600")
root.resizable(False, False)

# Dark Theme Background
root.configure(bg="#0f172a")

# Heading
title = Label(
    root,
    text="CAESAR CIPHER TOOL",
    font=("Segoe UI", 24, "bold"),
    fg="white",
    bg="#0f172a"
)
title.pack(pady=20)

subtitle = Label(
    root,
    text="Encrypt and Decrypt Messages Securely",
    font=("Segoe UI", 11),
    fg="#94a3b8",
    bg="#0f172a"
)
subtitle.pack()

# Input Frame
frame = Frame(root, bg="#1e293b", bd=0)
frame.pack(pady=25, padx=30, fill="both")

Label(
    frame,
    text="Enter Message",
    font=("Segoe UI", 12, "bold"),
    fg="white",
    bg="#1e293b"
).pack(anchor="w", padx=20, pady=(20, 5))

message_entry = Text(
    frame,
    height=6,
    width=60,
    font=("Segoe UI", 11),
    bg="#334155",
    fg="white",
    insertbackground="white"
)
message_entry.pack(padx=20)

Label(
    frame,
    text="Shift Value",
    font=("Segoe UI", 12, "bold"),
    fg="white",
    bg="#1e293b"
).pack(anchor="w", padx=20, pady=(20, 5))

shift_entry = Entry(
    frame,
    font=("Segoe UI", 12),
    width=10,
    bg="#334155",
    fg="white",
    insertbackground="white"
)
shift_entry.pack(anchor="w", padx=20)

# Buttons Frame
btn_frame = Frame(root, bg="#0f172a")
btn_frame.pack(pady=20)

encrypt_btn = Button(
    btn_frame,
    text="Encrypt",
    command=encrypt_text,
    font=("Segoe UI", 12, "bold"),
    bg="#2563eb",
    fg="white",
    padx=20,
    pady=8
)
encrypt_btn.grid(row=0, column=0, padx=10)

decrypt_btn = Button(
    btn_frame,
    text="Decrypt",
    command=decrypt_text,
    font=("Segoe UI", 12, "bold"),
    bg="#16a34a",
    fg="white",
    padx=20,
    pady=8
)
decrypt_btn.grid(row=0, column=1, padx=10)

clear_btn = Button(
    btn_frame,
    text="Clear",
    command=clear_fields,
    font=("Segoe UI", 12, "bold"),
    bg="#dc2626",
    fg="white",
    padx=20,
    pady=8
)
clear_btn.grid(row=0, column=2, padx=10)

# Output Section
Label(
    root,
    text="Result",
    font=("Segoe UI", 14, "bold"),
    fg="white",
    bg="#0f172a"
).pack()

output_text = Text(
    root,
    height=7,
    width=70,
    font=("Segoe UI", 11),
    bg="#1e293b",
    fg="#38bdf8",
    insertbackground="white"
)
output_text.pack(pady=10)

# Footer
footer = Label(
    root,
    text="SkillCraft Technology Internship - Task 01",
    font=("Segoe UI", 10),
    fg="#94a3b8",
    bg="#0f172a"
)
footer.pack(side=BOTTOM, pady=10)

root.mainloop()