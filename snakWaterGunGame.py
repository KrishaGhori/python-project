import random
import tkinter as tk

# #This is console game
# print("<< Snake Water Gun >>")
# u_score = 0
# c_score = 0
# while True:
#     #user choice
#     print("\nChoices : [snake , water , gun]  **Enter 0 , if u want to quit.")
#     user_choice = input("Enter your choice : ").lower()

#     if user_choice == "0":
#         break

#     #computer choice
#     com_lst= ["snake" , "water" ,"gun"]
#     com_choice = random.choice(com_lst)
#     print(f"Computer Choice : {com_choice}")

#     # win or lose
#     if com_choice == "snake":
#         if user_choice == "snake":
#             print("Tie.")
#         elif user_choice == "water":
#             print("Lose.")
#             c_score +=1
#         elif user_choice == "gun":
#             print("win.")
#             u_score += 1

#     elif com_choice == "water":
#         if user_choice == "water":
#             print("Tie.")
#         elif user_choice == "gun":
#             print("Lose.")
#             c_score += 1
#         elif user_choice == "snake":
#             print("win.")
#             u_score += 1

#     elif com_choice == "gun":
#         if user_choice == "gun":
#             print("Tie.")
#         elif user_choice == "snake":
#             print("Lose.")
#             c_score += 1
#         elif user_choice == "water":
#             print("win.")
#             u_score += 1
#     print(f"Score : you : {u_score} | Computer : {c_score}")

# print("\n<<Game Over>>")
# if user_choice == "0":
#     if u_score > c_score:
#         print("Final Result : User Win.")
#     elif c_score > u_score :
#         print("Final Result : Computer Win.")
#     else:
#         print("Final Result : Tie")
#     print(f"Score : you : {u_score} | Computer : {c_score}")


