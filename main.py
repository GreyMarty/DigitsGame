from tkinter import *

from GameProcessor import DigitsGame


def start_game():
    for child in logs.winfo_children():
        child.destroy()

    # Adding output table head
    create_output_log("Turn", "Guess", "Result")

    game.start()
    info_label.config(text="Game in process...")


def try_number(*_):
    turn, num, on_place, out_place = game.check(input_text.get())
    create_output_log(turn, num, f"{on_place}A{out_place}B")

    input_text.set("")

    if on_place == 4:
        info_label.config(text="You Won!:) Press \"New Game\" to play again")


def validate_input(*_):
    if not game.started:
        input_text.set("")
        return

    text = input_text.get()[:4]
    if len(text) and not text[-1].isnumeric():
        text = text[:-2]
    input_text.set(text)


def create_output_log(turn, number, result):
    new_log = Frame(logs)
    new_log.pack(side="top")
    Label(new_log, text=str(turn), font="Arial 12", width=5, bg="lightgrey").pack(side="left", fill="both", expand=True)
    Label(new_log, text=str(result), font="Arial 12", width=10, bg="lightgrey").pack(side="right", fill="both", expand=True)
    Label(new_log, text=str(number), font="Arial 12", width=25, bg="lightgrey").pack(fill="both", expand=True)
    logs_area.update_idletasks()
    logs_area.configure(scrollregion=logs_area.bbox("all"))


root = Tk()
root.title("Digits Game")
root.minsize(400, 600)
root.maxsize(400, 600)

panel = Menu(root)
panel.add_command(label="New Game", command=start_game)
panel.add_command(label="Exit", command=root.destroy)
root.config(menu=panel)

# Setting up input area
input_area = Frame(root, height=40)
input_area.pack(side="top", fill="x")

Label(input_area, text="Input:", font="Arial 13").pack(side="left")
Button(input_area, text="OK", font="Arial 13", width=8, height=2, command=try_number).pack(side="right", fill="none")

input_text = StringVar()
input_text.trace("w", validate_input)
input_field = Entry(input_area, textvariable=input_text, font="Arial 15")
input_field.bind("<Return>", try_number)
input_field.pack(fill="both", side="bottom", expand=True)


# Setting up output area
output_area = Frame(root, bg="grey")
output_area.pack(fill="both", expand=True)

scrollbar = Scrollbar(output_area, orient="vertical")
logs_area = Canvas(output_area, bg="lightgrey")
scrollbar.pack(fill="y", side="right")
logs_area.pack(fill="both", expand=True)

logs = Frame(logs_area, bg="green", width=logs_area.winfo_width())
logs_area.create_window(0, 0, anchor="nw", window=logs)
logs_area.update_idletasks()

scrollbar.config(command=logs_area.yview)
logs_area.configure(scrollregion=logs_area.bbox("all"), yscrollcommand=scrollbar.set)


# Setting up info area
info_area = Frame(root, height=30, bg="red")
info_area.pack(side="bottom", fill="x")

info_label = Label(info_area, text="Press \"New Game\" button to start.", anchor="w")
info_label.pack(fill="both", expand=True)


game = DigitsGame()

root.mainloop()