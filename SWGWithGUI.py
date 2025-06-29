#This is GUI base game

import random
import tkinter as tk

root = tk.Tk()
root.title("Game")
tk.Label(root , text="Snake Water Gun" , font=("Arial",14)).grid(row=1,column=1)

result_l = tk.Label(root , text="Make your Move!")
result_l.grid(row=3,column=1)
score_l =  tk.Label(root , text="You : 0 | Computer : 0")
score_l.grid(row=4,column=1)
com_choice_l =  tk.Label(root , text="Computer choes :")
com_choice_l.grid(row=5,column=1)

u_score = 0
c_score = 0

def playy(user_choice):
    global u_score , c_score
    com_lst= ["snake" , "water" ,"gun"]
    result = ""
    com_choice = random.choice(com_lst)
    com_choice_l.config(text=f"Computer chose : {com_choice}")

    # win or lose
    if com_choice == "snake":
        if user_choice == "snake":
            result = "Tie!"
        elif user_choice == "water":
            result = "Computer win!"
            c_score +=1
        elif user_choice == "gun":
            result = "You win!"
            u_score += 1

    elif com_choice == "water":
        if user_choice == "water":
            result = "Tie!"
        elif user_choice == "gun":
            result = "Computer win!"
            c_score += 1
        elif user_choice == "snake":
            result = "You win!"
            u_score += 1

    elif com_choice == "gun":
        if user_choice == "gun":
            result = "Tie!"
        elif user_choice == "snake":
            result = "Computer win!"
            c_score += 1
        elif user_choice == "water":
            result = "You win!"
            u_score += 1
    result_l.config(text=result)
    score_l.config(text=f"You : {u_score} | Computer : {c_score}")


btn1 = tk.Button(root , text="Snake",command=lambda:playy("snake")).grid(row=6,column=0)
btn2 = tk.Button(root , text="Water",command=lambda:playy("water")).grid(row=6,column=1)
btn3 = tk.Button(root , text="Gun",command=lambda:playy("gun")).grid(row=6,column=2)

btn4 = tk.Button(root , text="Quit",command=root.destroy).grid(row=9,column=1)

root.mainloop()
