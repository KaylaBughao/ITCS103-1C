import tkinter as tk

window = tk.Tk()
window.title("Kayla Bughao's Profile")
window.geometry("600x600")
window.configure(bg="violet")

title = tk.Label(
    window,
    text="Student Profile",
    font=("Arial", 24, "bold"),
    bg="violet",
    fg="black"
)
title.pack(pady=20)

info_font = ("Arial", 12)

tk.Label(window, text="Name : Kayla G. Bughao",
         font=info_font, bg="violet").pack(anchor="w", padx=40)

tk.Label(window, text="Age : 23 years old",
         font=info_font, bg="violet").pack(anchor="w", padx=40, pady=5)

tk.Label(window, text="Course : BSIT",
         font=info_font, bg="violet").pack(anchor="w", padx=40, pady=5)

tk.Label(window, text="Birthday : November 23, 2002",
         font=info_font, bg="violet").pack(anchor="w", padx=40, pady=5)

tk.Label(window, text="Motto :",
         font=info_font, bg="violet").pack(anchor="w", padx=40, pady=10)

tk.Label(
    window,
    text="Believe in yourself and keep moving.",
    font=("Arial", 11, "italic"),
    bg="violet",
    wraplength=400,
    justify="left"
).pack(anchor="w", padx=60)

window.mainloop()
