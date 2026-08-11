import tkinter as tk
from tkinter import scrolledtext
from chatbot import get_response


def send_message():
    message = entry.get().strip()

    if not message:
        return

    chat_box.config(state=tk.NORMAL)

    chat_box.insert(
        tk.END,
        f"You: {message}\n",
        "user"
    )

    response = get_response(message)

    chat_box.insert(
        tk.END,
        f"BlackHole AI: {response}\n\n",
        "bot"
    )

    chat_box.config(state=tk.DISABLED)

    entry.delete(0, tk.END)
    chat_box.see(tk.END)


def clear_chat():
    chat_box.config(state=tk.NORMAL)
    chat_box.delete("1.0", tk.END)
    chat_box.config(state=tk.DISABLED)


# =========================
# LEARN WINDOW
# =========================

def open_learn():
    learn_window = tk.Toplevel(root)
    learn_window.title("Learn About Black Holes")
    learn_window.geometry("650x600")
    learn_window.configure(bg="#050509")

    title = tk.Label(
        learn_window,
        text="📚 Learn About Black Holes",
        font=("Arial", 22, "bold"),
        fg="#9d4edd",
        bg="#050509"
    )
    title.pack(pady=20)

    topics = {
        "🌌 What is a Black Hole?":
            "A black hole is a region of space where gravity is extremely strong. "
            "Even light cannot escape once it crosses the event horizon.",

        "⭕ Event Horizon":
            "The event horizon is the boundary around a black hole. "
            "After crossing this boundary, nothing can escape.",

        "⚫ Singularity":
            "The singularity is the central region of a black hole where "
            "matter is compressed to an extremely high density.",

        "⭐ How Black Holes Form":
            "Some black holes can form when a very massive star reaches "
            "the end of its life and collapses under its own gravity.",

        "🔭 Types of Black Holes":
            "The main categories are stellar-mass black holes, "
            "intermediate-mass black holes, and supermassive black holes.",

        "🌠 Supermassive Black Holes":
            "Supermassive black holes can have millions or billions of times "
            "the mass of our Sun and are found at the centers of many galaxies."
    }

    for topic, information in topics.items():

        def show_topic(text=information, name=topic):
            topic_window = tk.Toplevel(learn_window)
            topic_window.title(name)
            topic_window.geometry("550x350")
            topic_window.configure(bg="#0d0d16")

            heading = tk.Label(
                topic_window,
                text=name,
                font=("Arial", 18, "bold"),
                fg="#c77dff",
                bg="#0d0d16"
            )
            heading.pack(pady=20)

            explanation = tk.Label(
                topic_window,
                text=text,
                font=("Arial", 13),
                fg="white",
                bg="#0d0d16",
                wraplength=480,
                justify="left"
            )
            explanation.pack(
                padx=30,
                pady=20
            )

        button = tk.Button(
            learn_window,
            text=topic,
            command=show_topic,
            bg="#161622",
            fg="white",
            font=("Arial", 12, "bold"),
            width=35,
            pady=10
        )

        button.pack(pady=5)



# =========================
# VISUALIZE BLACK HOLE
# =========================

def open_visualize():
    visual_window = tk.Toplevel(root)
    visual_window.title("Black Hole Visualization")
    visual_window.geometry("700x600")
    visual_window.configure(bg="#050509")

    title = tk.Label(
        visual_window,
        text="🌌 BLACK HOLE VISUALIZATION",
        font=("Arial", 22, "bold"),
        fg="#c77dff",
        bg="#050509"
    )
    title.pack(pady=15)

    canvas = tk.Canvas(
        visual_window,
        width=600,
        height=400,
        bg="#020205",
        highlightthickness=0
    )
    canvas.pack(pady=10)

    # Accretion disk
    canvas.create_oval(
        90, 135, 510, 305,
        outline="#9d4edd",
        width=10
    )

    canvas.create_oval(
        130, 155, 470, 285,
        outline="#7b2cbf",
        width=7
    )

    # Black hole
    canvas.create_oval(
        220, 140, 380, 300,
        fill="black",
        outline="#c77dff",
        width=4
    )

    # Event horizon
    canvas.create_oval(
        205, 125, 395, 315,
        outline="#00d9ff",
        width=2
    )

    canvas.create_text(
        300,
        335,
        text="EVENT HORIZON",
        fill="#00d9ff",
        font=("Arial", 13, "bold")
    )

    canvas.create_text(
        300,
        365,
        text="Black hole",
        fill="white",
        font=("Arial", 12)
    )

    info = tk.Label(
        visual_window,
        text=(
            "The bright ring represents the accretion disk: hot matter "
            "orbiting the black hole.\n"
            "The dark center represents the black hole."
        ),
        font=("Arial", 11),
        fg="white",
        bg="#050509",
        wraplength=600,
        justify="center"
    )
    info.pack(pady=10)

# =========================
# QUIZ
# =========================

quiz_questions = [
    {
        "question": "What is the boundary of a black hole called?",
        "options": [
            "Event Horizon",
            "Galaxy",
            "Nebula",
            "Orbit"
        ],
        "answer": "Event Horizon"
    },
    {
        "question": "Can light escape after crossing the event horizon?",
        "options": [
            "Yes",
            "No",
            "Sometimes",
            "Only during daytime"
        ],
        "answer": "No"
    },
    {
        "question": "Where are many supermassive black holes found?",
        "options": [
            "At the centers of galaxies",
            "Inside planets",
            "On the Moon",
            "Inside comets"
        ],
        "answer": "At the centers of galaxies"
    },
    {
        "question": "What happens to a massive star that collapses to form a black hole?",
        "options": [
            "It expands forever",
            "It can collapse under its own gravity",
            "It becomes a planet",
            "It becomes a comet"
        ],
        "answer": "It can collapse under its own gravity"
    },
    {
        "question": "Which force makes a black hole so powerful?",
        "options": [
            "Gravity",
            "Sound",
            "Wind",
            "Electricity"
        ],
        "answer": "Gravity"
    }
]


def open_quiz():
    quiz_window = tk.Toplevel(root)
    quiz_window.title("Black Hole Quiz")
    quiz_window.geometry("700x550")
    quiz_window.configure(bg="#050509")

    current_question = [0]
    score = [0]

    title = tk.Label(
        quiz_window,
        text="🧠 Black Hole Quiz",
        font=("Arial", 24, "bold"),
        fg="#9d4edd",
        bg="#050509"
    )
    title.pack(pady=20)

    question_label = tk.Label(
        quiz_window,
        text="",
        font=("Arial", 15, "bold"),
        fg="white",
        bg="#050509",
        wraplength=600
    )
    question_label.pack(pady=20)

    selected_answer = tk.StringVar()

    option_buttons = []

    for _ in range(4):
        button = tk.Radiobutton(
            quiz_window,
            text="",
            variable=selected_answer,
            value="",
            font=("Arial", 12),
            fg="white",
            bg="#161622",
            selectcolor="#5a189a",
            anchor="w",
            width=45,
            padx=10,
            pady=8
        )
        button.pack(pady=5)
        option_buttons.append(button)

    result_label = tk.Label(
        quiz_window,
        text="",
        font=("Arial", 12, "bold"),
        fg="#00d9ff",
        bg="#050509"
    )
    result_label.pack(pady=10)

    def load_question():
        index = current_question[0]

        if index >= len(quiz_questions):
            question_label.config(
                text=f"🎉 Quiz Complete!\n\nYour Score: {score[0]} / {len(quiz_questions)}"
            )

            for button in option_buttons:
                button.pack_forget()

            next_button.pack_forget()

            result_label.config(
                text="Great job! Keep learning about the universe. 🌌"
            )

            return

        question = quiz_questions[index]

        question_label.config(
            text=f"Question {index + 1}: {question['question']}"
        )

        selected_answer.set("")

        for i, option in enumerate(question["options"]):
            option_buttons[i].config(
                text=option,
                value=option
            )

        result_label.config(text="")

    def check_answer():
        index = current_question[0]

        if index >= len(quiz_questions):
            return

        answer = selected_answer.get()

        if not answer:
            result_label.config(
                text="Please select an answer."
            )
            return

        correct_answer = quiz_questions[index]["answer"]

        if answer == correct_answer:
            score[0] += 1
            result_label.config(
                text="✅ Correct!"
            )
        else:
            result_label.config(
                text=f"❌ Wrong! Correct answer: {correct_answer}"
            )

        current_question[0] += 1
        next_button.config(text="NEXT")

    def next_question():
        load_question()

    check_button = tk.Button(
        quiz_window,
        text="CHECK ANSWER",
        command=check_answer,
        bg="#7b2cbf",
        fg="white",
        font=("Arial", 11, "bold"),
        padx=15,
        pady=8
    )
    check_button.pack(pady=10)

    next_button = tk.Button(
        quiz_window,
        text="NEXT",
        command=next_question,
        bg="#3a3a4a",
        fg="white",
        font=("Arial", 11, "bold"),
        padx=20,
        pady=8
    )
    next_button.pack(pady=5)

    load_question()


# =========================
# MAIN WINDOW
# =========================

root = tk.Tk()
root.title("BlackHole AI")
root.geometry("800x700")
root.configure(bg="#050509")


title = tk.Label(
    root,
    text="🌌 BLACKHOLE AI",
    font=("Arial", 24, "bold"),
    fg="#9d4edd",
    bg="#050509"
)
title.pack(pady=(15, 5))


subtitle = tk.Label(
    root,
    text="Explore the universe with your AI assistant",
    font=("Arial", 11),
    fg="#aaaaaa",
    bg="#050509"
)
subtitle.pack(pady=(0, 10))


# Buttons
button_frame = tk.Frame(
    root,
    bg="#050509"
)
button_frame.pack(pady=(0, 10))


learn_button = tk.Button(
    button_frame,
    text="📚 LEARN",
    command=open_learn,
    bg="#5a189a",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=20,
    pady=8
)
learn_button.pack(side=tk.LEFT, padx=5)


quiz_button = tk.Button(
    button_frame,
    text="🧠 QUIZ",
    command=open_quiz,
    bg="#7b2cbf",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=20,
    pady=8
)
quiz_button.pack(side=tk.LEFT, padx=5)

visualize_button = tk.Button(
    button_frame,
    text="🌌 VISUALIZE",
    command=open_visualize,
    bg="#3a0ca3",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=20,
    pady=8
)
visualize_button.pack(side=tk.LEFT, padx=5)



# Chat box
chat_box = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Arial", 12),
    bg="#0d0d16",
    fg="white",
    insertbackground="white",
    padx=15,
    pady=15
)

chat_box.pack(
    padx=20,
    pady=(5, 10),
    fill=tk.BOTH,
    expand=True
)

chat_box.tag_config(
    "user",
    foreground="#00d9ff"
)

chat_box.tag_config(
    "bot",
    foreground="#c77dff"
)

chat_box.config(state=tk.DISABLED)


# Bottom frame
bottom_frame = tk.Frame(
    root,
    bg="#050509"
)
bottom_frame.pack(
    fill=tk.X,
    padx=20,
    pady=(0, 15)
)


entry = tk.Entry(
    bottom_frame,
    font=("Arial", 13),
    bg="#161622",
    fg="white",
    insertbackground="white"
)

entry.pack(
    side=tk.LEFT,
    fill=tk.X,
    expand=True,
    ipady=10,
    padx=(0, 10)
)


send_button = tk.Button(
    bottom_frame,
    text="SEND",
    command=send_message,
    bg="#7b2cbf",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=20,
    pady=8
)
send_button.pack(side=tk.LEFT)


clear_button = tk.Button(
    bottom_frame,
    text="CLEAR",
    command=clear_chat,
    bg="#3a3a4a",
    fg="white",
    font=("Arial", 11),
    padx=15,
    pady=8
)
clear_button.pack(
    side=tk.LEFT,
    padx=(10, 0)
)


entry.bind(
    "<Return>",
    lambda event: send_message()
)

entry.focus()

root.mainloop()