from tkinter import *
from game import Game

window = Tk()
window.title("Who wants to be a millionaire?")
window.configure(bg="black")
window.iconphoto(False, PhotoImage(file='Images/icon.png'))
window.minsize(1400, 650)

frame = Frame(window, bg='black')
frame.grid()

game_frame = Frame(window, bg='black', bd=20, width=900, height=650)
game_frame.grid(row=0, column=0)

money_frame = Frame(window, bg='black', width=460, height=600)
money_frame.grid(row=0, column=1)

game_frame_top = Frame(game_frame, bg='black', bd=20, width=900, height=100)
game_frame_top.grid(row=0, column=0)

game_frame_mid = Frame(game_frame, bg='black', bd=20, width=900, height=300)
game_frame_mid.grid(row=1, column=0)

game_frame_bot = Frame(game_frame, bg='black', bd=20, width=900, height=200)
game_frame_bot.grid(row=2, column=0)


centre_image = PhotoImage(file = "Images/logo.png")
logo_centre = Label(game_frame_mid, image= centre_image, bg='black', width=193, height=200)
logo_centre.grid(row=0, column=0)

money_image = PhotoImage(file="Images/0.png")
levels_img = Label(money_frame, image=money_image, bg='black', width=460, height=600)
levels_img.grid(row=0, column=0)

level = 0
question_text, A_ans, B_ans, C_ans, D_ans, correct_answer = Game.get_question_answers(level)



question = Label(game_frame_mid, text=question_text, bg='black', fg='white', font=('arial', 14, 'bold'), justify=CENTER)
question.grid(row=1, column=0, pady=10)

#A
a_text = Label(game_frame_bot, text="A:", bg='black', fg='white', font=('arial', 14, 'bold'))
a_text.grid(row=1, column=0, pady=4, sticky=W)

a_answer = Button(game_frame_bot, text=A_ans, bg='blue', fg='white', width=30, height=2, font=('arial', 14, 'bold'))
a_answer.grid(row=1, column=1, padx=10, pady=10)

#B
b_text = Label(game_frame_bot, text="B:", bg='black', fg='white', font=('arial', 14, 'bold'))
b_text.grid(row=2, column=0, pady=4, sticky=W)

b_answer = Button(game_frame_bot, text=B_ans, bg='blue', fg='white', width=30, height=2, font=('arial', 14, 'bold'))
b_answer.grid(row=2, column=1, padx=10, pady=10)

#C
c_text = Label(game_frame_bot, text="C:", bg='black', fg='white', font=('arial', 14, 'bold'))
c_text.grid(row=1, column=3, pady=4, sticky=W)

c_answer = Button(game_frame_bot, text=C_ans, bg='blue', fg='white', width=30, height=2, font=('arial', 14, 'bold'))
c_answer.grid(row=1, column=4, padx=10, pady=10)

#D
d_text = Label(game_frame_bot, text="D:", bg='black', fg='white', font=('arial', 14, 'bold'))
d_text.grid(row=2, column=3, pady=4, sticky=W)

d_answer = Button(game_frame_bot, text=D_ans, bg='blue', fg='white', width=30, height=2, font=('arial', 14, 'bold'))
d_answer.grid(row=2, column=4, padx=10, pady=10)

window.mainloop()