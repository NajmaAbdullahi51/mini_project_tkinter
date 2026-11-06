

from tkinter import *
from tkinter import messagebox

# ================= MAIN WINDOW =================
root = Tk()
root.title("Nugaal University | Official App")
root.geometry("1100x700")
root.configure(bg="#0A1AFF")  # Dark Blue

# ================= COLORS =================
colors = {
    "blue": "#0A1AFF",
    "light_blue": "#4DA6FF",
    "white": "#FFFFFF",
    "black": "#000000",
    "green": "#00CC66",
    "red": "#FF3333",
    "yellow": "#FFCC00",
    "purple": "#9933FF",
    "orange": "#FF6600",
    "gray": "#F2F2F2"
}

# ================= FUNCTIONS =================
def show_message():
    messagebox.showinfo("Nugaal University", "Ku soo dhowow Jaamacadda Nugaal University")

def clear_text():
    info_text.delete("1.0", END)

# ================= TITLE =================
title = Label(
    root,
    text="NUGAAL UNIVERSITY",
    font=("Arial", 28, "bold"),
    bg=colors["blue"],
    fg=colors["yellow"]
)
title.pack(pady=10)

subtitle = Label(
    root,
    text="Knowledge | Innovation | Excellence",
    font=("Arial", 14),
    bg=colors["blue"],
    fg=colors["white"]
)
subtitle.pack()

# ================= MAIN FRAME =================
main_frame = Frame(root, bg=colors["gray"])
main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

# ================= LEFT FRAME =================
left_frame = Frame(main_frame, bg=colors["white"], width=300)
left_frame.pack(side=LEFT, fill=Y, padx=10)

Label(
    left_frame,
    text="Student Registration",
    font=("Arial", 16, "bold"),
    bg=colors["white"],
    fg=colors["blue"]
).pack(pady=10)

Label(left_frame, text="Full Name:", bg=colors["white"]).pack(anchor="w", padx=10)
name_entry = Entry(left_frame)
name_entry.pack(fill=X, padx=10)

Label(left_frame, text="Faculty:", bg=colors["white"]).pack(anchor="w", padx=10, pady=5)
faculty_entry = Entry(left_frame)
faculty_entry.pack(fill=X, padx=10)

Label(left_frame, text="Level:", bg=colors["white"]).pack(anchor="w", padx=10, pady=5)
level_entry = Entry(left_frame)
level_entry.pack(fill=X, padx=10)

Button(
    left_frame,
    text="Submit",
    bg=colors["green"],
    fg=colors["white"],
    command=show_message
).pack(pady=15)

# ================= RIGHT FRAME =================
right_frame = Frame(main_frame, bg=colors["light_blue"])
right_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=10)

Label(
    right_frame,
    text="About Nugaal University",
    font=("Arial", 18, "bold"),
    bg=colors["light_blue"],
    fg=colors["black"]
).pack(pady=10)

info_text = Text(
    right_frame,
    height=15,
    font=("Arial", 12),
    bg=colors["white"],
    fg=colors["black"]
)
info_text.pack(padx=10, pady=10, fill=BOTH, expand=True)

info_text.insert(
    END,
    "Nugaal University waa jaamacad hormuud u ah waxbarashada casriga ah.\n\n"
    "Waxay bixisaa:\n"
    "- Information Technology\n"
    "- Business Administration\n"
    "- Health Sciences\n"
    "- Education\n\n"
    "Hadafkeenu waa in aan soo saarno arday aqoon iyo akhlaaq leh."
)

Button(
    right_frame,
    text="Clear Text",
    bg=colors["red"],
    fg=colors["white"],
    command=clear_text
).pack(pady=10)

# ================= BOTTOM MENU =================
bottom_frame = Frame(root, bg=colors["purple"], height=50)
bottom_frame.pack(fill=X)

Label(
    bottom_frame,
    text="© 2025 Nugaal University | Developed with Python Tkinter",
    bg=colors["purple"],
    fg=colors["white"],
    font=("Arial", 10)
).pack(pady=10)

# ================= RUN APP =================
root.mainloop()

#wax yaabahan projectiga kudhisay wxaaa kamida
 #10+ Midab
 #Registration Form
 #Text Area (Content jaamacadeed)
 #Buttons & MessageBox
 #Frames & Layout Professional ah
 #Ku fiican Projection & Presentation


