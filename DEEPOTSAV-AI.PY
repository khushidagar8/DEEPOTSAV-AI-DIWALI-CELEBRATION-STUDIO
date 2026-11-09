
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random
from datetime import datetime
import os

# ==========================================
# DEEPOTSAV AI - DIWALI CELEBRATION STUDIO
# ==========================================

root = tk.Tk()
root.title("DEEPOTSAV AI | Diwali Celebration Studio")
root.geometry("1150x750")
root.minsize(950, 650)
root.configure(bg="#100D20")

BG = "#100D20"
PANEL = "#1B1730"
CARD = "#26203D"
GOLD = "#F5C76A"
WHITE = "#FFF8E9"
MUTED = "#B9AEC9"
PURPLE = "#A78BFA"
GREEN = "#7DE0B1"

current_theme = "Dark"
quiz_score = 0
quiz_index = 0
quiz_questions = [
    ("Which festival is known as the Festival of Lights?",
     ["Holi", "Diwali", "Eid", "Christmas"], "Diwali"),
    ("Which goddess is commonly worshipped on Diwali?",
     ["Saraswati", "Durga", "Lakshmi", "Parvati"], "Lakshmi"),
    ("What is traditionally lit during Diwali?",
     ["Diya", "Lantern only", "Candle only", "Torch"], "Diya"),
    ("Which sweet is popular during Diwali?",
     ["Gulab Jamun", "All of these", "Jalebi", "Ladoo"], "All of these"),
    ("What does Diwali celebrate in the Ramayana tradition?",
     ["A harvest", "Return of Rama to Ayodhya",
      "A new year only", "A birthday"], "Return of Rama to Ayodhya")
]

wishes = {
    "Family": [
        "May your home shine with happiness, peace and prosperity. Happy Diwali!",
        "Wishing your family a beautiful Diwali filled with love and togetherness.",
        "May every diya bring new hope and every moment bring happiness. Happy Diwali!"
    ],
    "Friends": [
        "May our friendship shine brighter than a thousand diyas. Happy Diwali!",
        "Wishing you unlimited smiles, sweet memories and a sparkling Diwali!",
        "May your life be full of laughter, success and wonderful surprises!"
    ],
    "Teachers": [
        "Wishing you a bright Diwali filled with peace, happiness and prosperity.",
        "May the festival of lights bring joy and success to your life. Happy Diwali!",
        "Thank you for guiding us towards knowledge and success. Happy Diwali!"
    ],
    "Professional": [
        "Wishing you continued success, new opportunities and a prosperous Diwali.",
        "May this festive season bring fresh ideas and achievements. Happy Diwali!",
        "Warm wishes for a joyful and successful Diwali celebration."
    ],
    "Special": [
        "May your smile shine brighter than every light this Diwali. Happy Diwali!",
        "You make every celebration special. Wishing you endless happiness!",
        "May our beautiful memories grow brighter with every festival. Happy Diwali!"
    ]
}

def clear_page():
    for widget in content.winfo_children():
        widget.destroy()

def heading(title, subtitle):
    tk.Label(content, text=title, bg=BG, fg=GOLD,
             font=("Segoe UI", 25, "bold")).pack(anchor="w", pady=(5, 5))
    tk.Label(content, text=subtitle, bg=BG, fg=MUTED,
             font=("Segoe UI", 10)).pack(anchor="w", pady=(0, 22))

def make_button(parent, text, command, color=GOLD):
    return tk.Button(
        parent, text=text, command=command,
        bg=color, fg="#171126",
        activebackground="#FFE2A0",
        activeforeground="#171126",
        font=("Segoe UI", 10, "bold"),
        relief="flat", bd=0, padx=18, pady=10,
        cursor="hand2"
    )

def dashboard():
    clear_page()
    heading("Welcome to DEEPOTSAV AI 🪔",
            "Your personal Diwali celebration and creativity studio")

    hero = tk.Frame(content, bg=PANEL, padx=25, pady=28)
    hero.pack(fill="x", pady=8)

    tk.Label(hero, text="✨ HAPPY DIWALI ✨",
             bg=PANEL, fg=GOLD,
             font=("Segoe UI", 27, "bold")).pack(anchor="w")

    tk.Label(hero,
             text="Celebrate lights, happiness, creativity and new beginnings.",
             bg=PANEL, fg=WHITE,
             font=("Segoe UI", 12)).pack(anchor="w", pady=12)

    make_button(hero, "Create a Diwali Wish",
                wish_generator).pack(anchor="w", pady=8)

    tk.Label(content, text="EXPLORE YOUR FESTIVAL STUDIO",
             bg=BG, fg=MUTED,
             font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(24, 12))

    cards = tk.Frame(content, bg=BG)
    cards.pack(fill="x")

    features = [
        ("💌", "AI Wish Generator", wish_generator),
        ("🎨", "Greeting Card Studio", card_studio),
        ("🧠", "Diwali Quiz", quiz_page),
        ("🌸", "Rangoli Gallery", rangoli_page),
        ("⏳", "Festival Countdown", countdown_page),
        ("💡", "About Project", about_page)
    ]

    for i, (emoji, name, function) in enumerate(features):
        r, c = divmod(i, 3)
        box = tk.Frame(cards, bg=CARD, padx=15, pady=20)
        box.grid(row=r, column=c, padx=7, pady=7, sticky="nsew")
        cards.columnconfigure(c, weight=1)

        tk.Label(box, text=emoji, bg=CARD, fg=GOLD,
                 font=("Segoe UI Emoji", 25)).pack()
        tk.Label(box, text=name, bg=CARD, fg=WHITE,
                 font=("Segoe UI", 11, "bold")).pack(pady=8)
        make_button(box, "OPEN", function).pack()

    tk.Label(content, text="Made with Python | DEEPOTSAV AI",
             bg=BG, fg=MUTED,
             font=("Segoe UI", 9)).pack(anchor="w", pady=25)


# ==========================================
# SMART WISH GENERATOR
# ==========================================

def wish_generator():
    clear_page()
    heading("AI Wish Generator 💌",
            "Create a personalized Diwali greeting in seconds.")

    panel = tk.Frame(content, bg=PANEL, padx=22, pady=22)
    panel.pack(fill="x")

    tk.Label(panel, text="Recipient Category",
             bg=PANEL, fg=WHITE,
             font=("Segoe UI", 11, "bold")).pack(anchor="w")

    category = ttk.Combobox(
        panel, values=list(wishes.keys()),
        state="readonly", font=("Segoe UI", 11)
    )
    category.set("Family")
    category.pack(fill="x", pady=10)

    tk.Label(panel, text="Recipient Name (optional)",
             bg=PANEL, fg=WHITE).pack(anchor="w")

    name = tk.Entry(panel, font=("Segoe UI", 11))
    name.pack(fill="x", pady=10)

    result = tk.Text(
        panel, height=5, wrap="word",
        bg=BG, fg=GOLD, insertbackground=WHITE,
        font=("Segoe UI", 13), relief="flat",
        padx=12, pady=12
    )
    result.pack(fill="x", pady=12)

    def generate():
        selected = category.get()
        greeting = random.choice(wishes[selected])
        person = name.get().strip()

        if person:
            greeting = "Dear " + person + ",\n\n" + greeting

        result.delete("1.0", tk.END)
        result.insert(tk.END, greeting)

    def save():
        text = result.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Empty", "Generate a wish first.")
            return

        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")],
            initialfile="My_Diwali_Wish.txt"
        )
        if path:
            with open(path, "w", encoding="utf-8") as file:
                file.write(text)
            messagebox.showinfo("Saved", "Your wish has been saved!")

    make_button(panel, "✨ GENERATE WISH", generate).pack(side="left", padx=5)
    make_button(panel, "SAVE WISH", save, GREEN).pack(side="left", padx=5)

    generate()


# ==========================================
# GREETING CARD STUDIO
# ==========================================

def card_studio():
    clear_page()
    heading("Greeting Card Studio 🎨",
            "Design a personalized Diwali greeting card.")

    panel = tk.Frame(content, bg=PANEL, padx=20, pady=20)
    panel.pack(fill="x")

    tk.Label(panel, text="Enter your name:",
             bg=PANEL, fg=WHITE).pack(anchor="w")

    sender = tk.Entry(panel, font=("Segoe UI", 12))
    sender.pack(fill="x", pady=10)

    tk.Label(panel, text="Enter a personal message:",
             bg=PANEL, fg=WHITE).pack(anchor="w")

    msg = tk.Entry(panel, font=("Segoe UI", 12))
    msg.insert(0, "May your life shine with happiness!")
    msg.pack(fill="x", pady=10)

    preview = tk.Frame(content, bg="#342047",
                       padx=25, pady=30)
    preview.pack(fill="x", pady=20)

    title = tk.Label(preview, text="🪔 HAPPY DIWALI 🪔",
                     bg="#342047", fg=GOLD,
                     font=("Georgia", 25, "bold"))
    title.pack(pady=12)

    message = tk.Label(preview, text="May your life shine with happiness!",
                       bg="#342047", fg=WHITE,
                       font=("Segoe UI", 12),
                       wraplength=650)
    message.pack(pady=12)

    sign = tk.Label(preview, text="With love",
                    bg="#342047", fg=GOLD,
                    font=("Segoe UI", 13, "italic"))
    sign.pack(pady=10)

    def update_card():
        message.config(text=msg.get())
        sign.config(text="With love, " + (sender.get().strip() or "Your Name"))

    def save_card():
        update_card()
        card_text = (
            "🪔 HAPPY DIWALI 🪔\n\n" +
            msg.get() + "\n\nWith love, " +
            (sender.get().strip() or "Your Name")
        )
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            initialfile="Diwali_Greeting_Card.txt",
            filetypes=[("Text files", "*.txt")]
        )
        if path:
            with open(path, "w", encoding="utf-8") as file:
                file.write(card_text)
            messagebox.showinfo("Success", "Greeting card saved!")

    make_button(panel, "UPDATE PREVIEW", update_card).pack(
        side="left", padx=5)
    make_button(panel, "SAVE CARD", save_card, GREEN).pack(
        side="left", padx=5)


# ==========================================
# INTERACTIVE DIWALI QUIZ
# ==========================================

def quiz_page():
    global quiz_score, quiz_index
    quiz_score = 0
    quiz_index = 0

    clear_page()
    heading("Diwali Knowledge Challenge 🧠",
            "Test your festival knowledge with this interactive quiz.")

    panel = tk.Frame(content, bg=PANEL, padx=25, pady=25)
    panel.pack(fill="x")

    question_label = tk.Label(
        panel, text="", bg=PANEL, fg=GOLD,
        font=("Segoe UI", 15, "bold"),
        wraplength=650, justify="left"
    )
    question_label.pack(anchor="w", pady=20)

    options_frame = tk.Frame(panel, bg=PANEL)
    options_frame.pack(fill="x")

    feedback = tk.Label(panel, text="", bg=PANEL,
                        fg=GREEN, font=("Segoe UI", 11))
    feedback.pack(pady=15)

    progress = tk.Label(panel, text="", bg=PANEL, fg=MUTED)
    progress.pack()

    def load_question():
        for widget in options_frame.winfo_children():
            widget.destroy()

        if quiz_index >= len(quiz_questions):
            question_label.config(
                text="🎉 Quiz Completed!\nYour score: " +
                str(quiz_score) + "/" + str(len(quiz_questions))
            )
            feedback.config(text="Thank you for playing!")
            progress.config(text="Challenge completed")
            return

        q, choices, answer = quiz_questions[quiz_index]
        question_label.config(
            text="Question " + str(quiz_index + 1) + ": " + q
        )
        progress.config(
            text="Question " + str(quiz_index + 1) +
            " of " + str(len(quiz_questions))
        )

        for choice in choices:
            make_button(
                options_frame, choice,
                lambda selected=choice: check_answer(selected),
                PURPLE
            ).pack(fill="x", pady=5)

    def check_answer(selected):
        global quiz_score, quiz_index
        answer = quiz_questions[quiz_index][2]

        if selected == answer:
            quiz_score += 1
            feedback.config(text="Correct answer! ⭐", fg=GREEN)
        else:
            feedback.config(
                text="Correct answer: " + answer, fg=GOLD
            )

        quiz_index += 1
        make_button(panel, "NEXT QUESTION", load_question).pack(pady=8)

    load_question()


# ==========================================
# RANGOLI GALLERY
# ==========================================

def rangoli_page():
    clear_page()
    heading("Rangoli Art Gallery 🌸",
            "Explore colourful geometric rangoli patterns.")

    canvas = tk.Canvas(
        content, width=500, height=390,
        bg="#21172E", highlightthickness=0
    )
    canvas.pack(pady=10)

    colors = ["#F5C76A", "#FA709A", "#A78BFA",
              "#7DE0B1", "#FF8C69", "#FCE38A"]

    def draw_rangoli():
        canvas.delete("all")
        cx, cy = 250, 190

        for ring in range(5):
            radius = 35 + ring * 32

            for angle in range(0, 360, 30):
                import math
                rad = math.radians(angle)
                x = cx + radius * math.cos(rad)
                y = cy + radius * math.sin(rad)
                color = random.choice(colors)

                canvas.create_oval(
                    x-15, y-15, x+15, y+15,
                    fill=color, outline=GOLD, width=2
                )

        canvas.create_oval(
            cx-35, cy-35, cx+35, cy+35,
            fill=GOLD, outline=WHITE, width=3
        )
        canvas.create_text(
            cx, cy, text="🪔",
            font=("Segoe UI Emoji", 27)
        )

    draw_rangoli()
    make_button(content, "GENERATE NEW RANGOLI",
                draw_rangoli).pack(pady=10)


# ==========================================
# FESTIVAL COUNTDOWN
# ==========================================

def countdown_page():
    clear_page()
    heading("Festival Countdown ⏳",
            "Enter the date of your next Diwali celebration.")

    panel = tk.Frame(content, bg=PANEL, padx=25, pady=25)
    panel.pack(fill="x")

    tk.Label(panel, text="Festival date (DD-MM-YYYY)",
             bg=PANEL, fg=WHITE,
             font=("Segoe UI", 11)).pack(anchor="w")

    date_entry = tk.Entry(panel, font=("Segoe UI", 13))
    date_entry.pack(fill="x", pady=12)
    date_entry.insert(0, "01-11-2027")

    result = tk.Label(panel, text="",
                      bg=PANEL, fg=GOLD,
                      font=("Segoe UI", 18, "bold"))
    result.pack(pady=25)

    def calculate():
        try:
            festival = datetime.strptime(
                date_entry.get().strip(), "%d-%m-%Y"
            ).date()

            today = datetime.now().date()
            days = (festival - today).days

            if days > 0:
                result.config(text=str(days) + " DAYS TO GO! 🪔")
            elif days == 0:
                result.config(text="HAPPY DIWALI! 🎉")
            else:
                result.config(text="This date has passed. Enter a future date.")

        except ValueError:
            messagebox.showerror(
                "Invalid Date",
                "Please enter the date in DD-MM-YYYY format."
            )

    make_button(panel, "CALCULATE COUNTDOWN", calculate).pack()
    calculate()


# ==========================================
# ABOUT PAGE
# ==========================================

def about_page():
    clear_page()
    heading("About DEEPOTSAV AI 💡",
            "A creative Python project celebrating the Festival of Lights.")

    panel = tk.Frame(content, bg=PANEL, padx=25, pady=25)
    panel.pack(fill="x")

    details = [
        "PROJECT: DEEPOTSAV AI",
        "TYPE: Diwali Celebration Application",
        "LANGUAGE: Python",
        "GUI: Tkinter",
        "LEVEL: Advanced Student Project",
        "",
        "MAIN OBJECTIVES:",
        "• Personalized greeting generation",
        "• Interactive festival quiz",
        "• Digital greeting card creation",
        "• Rangoli pattern visualization",
        "• Festival countdown calculator",
        "",
        "Developed as a Python-based festival application."
    ]

    for line in details:
        tk.Label(panel, text=line, bg=PANEL,
                 fg=GOLD if line.startswith("PROJECT") else WHITE,
                 font=("Segoe UI", 11),
                 anchor="w").pack(fill="x", pady=4)


# ==========================================
# THEME SWITCHER
# ==========================================

def switch_theme():
    global BG, PANEL, CARD, WHITE, MUTED, GOLD

    if current_theme == "Dark":
        pass

    messagebox.showinfo(
        "Theme",
        "The current version uses the premium dark theme."
    )


# ==========================================
# MAIN APPLICATION LAYOUT
# ==========================================

sidebar = tk.Frame(root, bg="#171229", width=225)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

brand = tk.Label(
    sidebar, text="🪔\nDEEPOTSAV AI",
    bg="#171229", fg=GOLD,
    font=("Segoe UI", 20, "bold")
)
brand.pack(pady=(28, 35))

tk.Label(sidebar, text="CELEBRATION MENU",
         bg="#171229", fg=MUTED,
         font=("Segoe UI", 9, "bold")).pack(pady=8)

menu_items = [
    ("⌂  Dashboard", dashboard),
    ("✉  Wish Generator", wish_generator),
    ("▣  Greeting Studio", card_studio),
    ("★  Diwali Quiz", quiz_page),
    ("❀  Rangoli Gallery", rangoli_page),
    ("◷  Countdown", countdown_page),
    ("ⓘ  About Project", about_page)
]

for label, function in menu_items:
    tk.Button(
        sidebar, text=label, command=function,
        bg="#171229", fg=WHITE,
        activebackground="#34264C",
        activeforeground=GOLD,
        font=("Segoe UI", 10),
        relief="flat", bd=0,
        anchor="w", padx=22, pady=12,
        cursor="hand2"
    ).pack(fill="x", padx=8, pady=2)

tk.Label(
    sidebar, text="PYTHON EDITION 1.0",
    bg="#171229", fg=MUTED,
    font=("Segoe UI", 8)
).pack(side="bottom", pady=20)

main = tk.Frame(root, bg=BG)
main.pack(side="right", fill="both", expand=True)

topbar = tk.Frame(main, bg="#171229", height=55)
topbar.pack(fill="x")
topbar.pack_propagate(False)

tk.Label(
    topbar, text="DIWALI CELEBRATION STUDIO",
    bg="#171229", fg=WHITE,
    font=("Segoe UI", 10, "bold")
).pack(side="left", padx=25, pady=15)

tk.Label(
    topbar, text="✨ FESTIVAL OF LIGHTS",
    bg="#171229", fg=GOLD,
    font=("Segoe UI", 9, "bold")
).pack(side="right", padx=25)

content = tk.Frame(main, bg=BG, padx=28, pady=22)
content.pack(fill="both", expand=True)

dashboard()

root.mainloop()
