from tkinter import *

# Data
questions = ["What is the name of protagonist in Ramayan?",
             "Who killed Gandhiji?",
             "Mark Zuckerberg owns which company?",
             "Capital of France - "]

options = [("Ashwathama", "Ram", "Ravan", "Narsimha"),
           ("Britishers", "Nathuram Godse", "Sanjiv Reddy", "Nanasaheb"),
           ("Meta", "Tesla", "Google", "Amazon"),
           ("Berlin", "France", "Tokyo", "New Delhi")]

correct_answers = [2, 2, 1, 1]  # Correct option index for each question

root = Tk()
root.title("Quiz App")
root.geometry("700x500")
root.config(bg="#f3f3f3")

current_question = 0  # Track the current question
score = 0  # Track the score

r = IntVar()
r.set(None)  # Ensure no radio button is preselected


def delay():
    nameEntry.grid_forget()
    Submitname.grid_forget()
    text.grid_forget()
    lab.grid_forget()
    start_quiz()
    show_question()


def submit_name():
    name = name1.get()
    message.set(f"Your name is {name}. WELCOME!\n Your Quiz starts in 3 2 1...")
    root.after(6000, delay)


def submit_ans():
    global current_question, score

    selected_answer = r.get()
    if selected_answer == correct_answers[current_question]:
        result_label.config(text="Correct!", fg="#228B22") 
        score += 1
    else:
        result_label.config(text="Wrong!", fg="#FF6347")

    current_question += 1

    if current_question < len(questions):
        show_question()
    else:
        end_quiz()


def show_question():
    r.set(None)  # Reset radio button selection
    question_label.config(text=questions[current_question])
    opt1.config(text=options[current_question][0], value=1)
    opt2.config(text=options[current_question][1], value=2)
    opt3.config(text=options[current_question][2], value=3)
    opt4.config(text=options[current_question][3], value=4)
    score_label.config(text=f"Score: {score}/{len(questions)}")


def end_quiz():
    question_label.grid_forget()
    opt1.grid_forget()
    opt2.grid_forget()
    opt3.grid_forget()
    opt4.grid_forget()
    submit_button.grid_forget()
    score_label.grid_forget()
    result_label.grid(row=1, column=0, columnspan=2, pady=20)
    result_label.config(
        text=f"Quiz Over! \nYour final score is: {score}/{len(questions)}",
        fg="#4682B4")
    

# Widgets
def start_quiz():
    global question_label, opt1, opt2, opt3, opt4, submit_button, result_label, score_label

    question_label = Label(root, text="", font=("Times New Roman", 18), bg="#f3f3f3")
    question_label.grid(row=0, column=0, columnspan=2, pady=20)

    opt1 = Radiobutton(root, text="", font=("Verdana", 14), variable=r, value=1, bg="#f3f3f3", activebackground="#dcdcdc")
    opt1.grid(row=1, column=0, sticky="w", padx=20)

    opt2 = Radiobutton(root, text="", font=("Verdana", 14), variable=r, value=2, bg="#f3f3f3", activebackground="#dcdcdc")
    opt2.grid(row=2, column=0, sticky="w", padx=20)

    opt3 = Radiobutton(root, text="", font=("Verdana", 14), variable=r, value=3, bg="#f3f3f3", activebackground="#dcdcdc")
    opt3.grid(row=3, column=0, sticky="w", padx=20)

    opt4 = Radiobutton(root, text="", font=("Verdana", 14), variable=r, value=4, bg="#f3f3f3", activebackground="#dcdcdc")
    opt4.grid(row=4, column=0, sticky="w", padx=20)

    submit_button = Button(root, text="Submit", font=("Helvetica", 14), command=submit_ans, bg="#87CEFA", fg="black")
    submit_button.grid(row=5, column=0, pady=20)

    result_label = Label(root, text="", font=("Times New Roman", 16), bg="#f3f3f3", anchor=CENTER)

    score_label = Label(root, text="", font=("Helvetica", 12), bg="#f3f3f3", anchor="w")
    score_label.grid(row=8, column=2, padx=20, pady=10)


# Initial Screen
lab = Label(root, text="Enter your name to start the Quiz", font=("Times New Roman", 22, "bold"), padx=10, pady=10, bg="#f3f3f3")
lab.grid(row=0, column=0, pady=20)

name1 = StringVar()
nameEntry = Entry(root, textvariable=name1, font=("Helvetica", 16))
nameEntry.grid(row=2, column=0, pady=10)

Submitname = Button(root, text="Submit Name", font=("Helvetica", 14), command=submit_name, bg="#87CEFA", fg="black")
Submitname.grid(row=4, column=0, pady=10)

message = StringVar()
text = Label(root, textvariable=message, font=("Times New Roman", 14, "italic"), bg="#f3f3f3")
text.grid(row=6, column=0, pady=10)

exit_button = Button(root, text="Exit", font=("Helvetica", 12), command=root.quit, bg="#ffcccb", fg="black")
exit_button.grid(row=8, column=0, padx=20, pady=10)

root.mainloop()
