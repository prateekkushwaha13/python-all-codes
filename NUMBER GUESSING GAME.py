# import random

# num=random.randint(1,100)

# tries=0
# while True:
#      guess=int(input("guess a number between 1 to 100 :-"))

     
#      if guess==num:
#         print("you have guessed right")
#         tries+=1
#         print("you have taken ",tries,"tries")
#         break
#      elif guess<num:
#          print("sorry you are wrong")
#          print("go for higher number")
#          tries+=1
         
#      elif guess>num:
#          print("sorry you are wrong")     
#          print("go to a little")
#          tries+=1
         
#      else: 
#          print("guess  a valid number")    


import tkinter as tk
import random

num = random.randint(1, 100)
tries = 0


def check_guess():
    global tries

    try:
        guess = int(entry.get())
    except ValueError:
        result_label.config(text="Guess a valid number")
        return

    if guess == num:
        tries += 1
        result_label.config(
            text=f"You guessed right!\nYou took {tries} tries."
        )
        guess_button.config(state="disabled")

    elif guess < num:
        result_label.config(text="Sorry, you are wrong.\nGo for Higher Number")
        tries += 1

    elif guess > num:
        result_label.config(text="Sorry, you are wrong.\nGo for Lower Number")
        tries += 1

    else:
        result_label.config(text="Guess a valid number")

    attempt_label.config(text=f"Attempts : {tries}")

    entry.delete(0, tk.END)


# ---------------- GUI ----------------

window = tk.Tk()
window.title("Number Guessing Game")
window.geometry("400x300")

title = tk.Label(window,
                 text="🎯 Number Guessing Game",
                 font=("Arial", 18))
title.pack(pady=10)

entry = tk.Entry(window,
                 font=("Arial", 16),
                 justify="center")
entry.pack(pady=10)

guess_button = tk.Button(window,
                         text="Guess",
                         font=("Arial", 12),
                         command=check_guess)
guess_button.pack()

result_label = tk.Label(window,
                        text="Enter your guess",
                        font=("Arial", 13))
result_label.pack(pady=15)

attempt_label = tk.Label(window,
                         text="Attempts : 0",
                         font=("Arial", 12))
attempt_label.pack()

window.mainloop()