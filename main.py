import random
from tkinter import *
from game import Game

window = Tk()
window.title("Who wants to be a millionaire?")
window.configure(bg="black")
window.iconphoto(False, PhotoImage(file='Images/icon.png'))
window.minsize(1400, 650)
window.maxsize(1400, 650)

level = 0
game = True

while game == True:
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

    def fifty_fifty():
        global correct_answer, a_answer, b_answer, c_answer, d_answer
        if correct_answer == a_answer.cget('text'):
            list_answers = [b_answer, c_answer, d_answer]
            rand_1 = random.choice(list_answers)
            list_answers.remove(rand_1)
            rand_2 = random.choice(list_answers)
            rand_1.configure(text='')
            rand_2.configure(text='')
            fifty_btn.configure(state=DISABLED)
        elif correct_answer == b_answer.cget('text'):
            list_answers = [a_answer, c_answer, d_answer]
            rand_1 = random.choice(list_answers)
            list_answers.remove(rand_1)
            rand_2 = random.choice(list_answers)
            rand_1.configure(text='')
            rand_2.configure(text='')
            fifty_btn.configure(state=DISABLED)
        elif correct_answer == c_answer.cget('text'):
            list_answers = [a_answer, b_answer, d_answer]
            rand_1 = random.choice(list_answers)
            list_answers.remove(rand_1)
            rand_2 = random.choice(list_answers)
            rand_1.configure(text='')
            rand_2.configure(text='')
            fifty_btn.configure(state=DISABLED)
        elif correct_answer == d_answer.cget('text'):
            list_answers = [a_answer, b_answer, c_answer]
            rand_1 = random.choice(list_answers)
            list_answers.remove(rand_1)
            rand_2 = random.choice(list_answers)
            rand_1.configure(text='')
            rand_2.configure(text='')
            fifty_btn.configure(state=DISABLED)
    


    fifty_image = PhotoImage(file="Images/jpge50.png")
    fifty_btn = Button(game_frame_top, image=fifty_image, bg='black', width=85, height=50, highlightthickness=0, command=fifty_fifty)
    fifty_btn.place(x=300, y=5)

    question_text, A_ans, B_ans, C_ans, D_ans, correct_answer = Game.get_question_answers(level)

    def win_lose(text):
        canvas = Canvas(game_frame_mid, bg='black', width=860, height=200, bd=0, highlightthickness=0, relief='ridge')
        canvas.grid(row=0, column=0)
        canvas.delete('all')
        canvas.create_text(430, 100, text=text, fill="white", font=('Helvetica 50 bold'))
        canvas.grid()

    def change_picture():
        global level 
        canvas = Canvas(money_frame, bg='black', width=460, height=600, bd=0, highlightthickness=0, relief='ridge')
        canvas.grid(row=0, column=0)
        canvas.delete('all')
        image = PhotoImage(file = f"Images/{level}.png")
        canvas.create_image(230, 300, image = image)
        canvas.image = image

    def level_wins():
        if level >= 5 and level < 10:
                question.configure(text='YOU WON', font=('arial', 15, 'bold'))
                disable_buttons()
                win_lose(text="1,000")
        elif level >= 10 and level < 15:
                question.configure(text='YOU WON', font=('arial', 14, 'bold'))
                disable_buttons()
                win_lose(text="32,000")
        elif level < 5:
            question.configure(text='YOU LOSE', font=('arial', 16, 'bold'))
            disable_buttons()
            win_lose(text="0")
            fifty_btn.grid_forget()

    def get_a_answer():
        global level
        global game
        global a_answer
        ans = a_answer.cget('text')
        if ans == correct_answer:
            level += 1
            a_answer.after(1000, update(a_answer, color='green'))
            def next_question():
                change_picture()
                update_question_and_answers()
                a_answer.after(1000, update(a_answer, color='blue'))
            a_answer.after(1000, next_question)
        else:
            a_answer.after(1000, update(a_answer, color='red'))
            if correct_answer == b_answer.cget('text'):
                 b_answer.after(1000, update(b_answer, color='green'))
            elif correct_answer == c_answer.cget('text'):
                c_answer.after(1000, update(c_answer, color='green'))
            elif correct_answer == d_answer.cget('text'):
                d_answer.after(1000, update(d_answer, color='green'))
            game = False
            level_wins()

    def get_b_answer():
        global level
        global game
        global b_answer
        ans = b_answer.cget('text')
        if ans == correct_answer:
            level += 1
            b_answer.after(1000, update(b_answer, color='green'))
            def next_question():
                change_picture()
                update_question_and_answers()
                b_answer.after(1000, update(b_answer, color='blue'))
            b_answer.after(1000, next_question)
        else:
            b_answer.after(1000, update(b_answer, color='red'))
            if correct_answer == a_answer.cget('text'):
                 a_answer.after(1000, update(a_answer, color='green'))
            elif correct_answer == c_answer.cget('text'):
                c_answer.after(1000, update(c_answer, color='green'))
            elif correct_answer == d_answer.cget('text'):
                d_answer.after(1000, update(d_answer, color='green'))
            game = False
            level_wins()

    def update(player_answer, color):
        player_answer.configure(bg=color)

    def disable_buttons():
        a_answer.configure(state=DISABLED)
        b_answer.configure(state=DISABLED)
        c_answer.configure(state=DISABLED)
        d_answer.configure(state=DISABLED)

    def get_c_answer():
        global level
        global game
        global c_answer
        ans = c_answer.cget('text')
        if ans == correct_answer:
            level += 1
            c_answer.after(1000, update(c_answer, color='green'))
            def next_question():
                change_picture()
                update_question_and_answers()
                c_answer.after(1000, update(c_answer, color='blue'))
            c_answer.after(1000, next_question)
        else:
            c_answer.after(1000, update(c_answer, color='red'))
            if correct_answer == a_answer.cget('text'):
                 a_answer.after(1000, update(a_answer, color='green'))
            elif correct_answer == b_answer.cget('text'):
                b_answer.after(1000, update(b_answer, color='green'))
            elif correct_answer == d_answer.cget('text'):
                d_answer.after(1000, update(d_answer, color='green'))
            level_wins()

    def get_d_answer():
        global level
        global game
        global d_answer
        ans = d_answer.cget('text')
        if ans == correct_answer:
            level += 1
            d_answer.after(1000, update(d_answer, color='green'))
            def next_question():
                change_picture()
                update_question_and_answers()
                d_answer.after(1000, update(d_answer, color='blue'))
            d_answer.after(1000, next_question)
        else:
            d_answer.after(1000, update(d_answer, color='red'))
            if correct_answer == a_answer.cget('text'):
                 a_answer.after(1000, update(a_answer, color='green'))
            elif correct_answer == b_answer.cget('text'):
                b_answer.after(1000, update(b_answer, color='green'))
            elif correct_answer == c_answer.cget('text'):
                c_answer.after(1000, update(c_answer, color='green'))
            game = False
            level_wins()

        
    def update_question_and_answers():
        if level < 15:
            global question
            global correct_answer
            question_text, A_ans, B_ans, C_ans, D_ans, correct_answer = Game.get_question_answers(level)
            question.configure(text=question_text)
            a_answer.configure(text=A_ans)
            b_answer.configure(text=B_ans)
            c_answer.configure(text=D_ans)
            d_answer.configure(text=C_ans)
            correct_answer = correct_answer
        else:
            a_answer.configure(text='1,000,000')
            b_answer.configure(text='1,000,000')
            c_answer.configure(text='1,000,000')
            d_answer.configure(text='1,000,000')
            question.configure(text=' YOU ARE A MILLIONAIRE', font=('arial', 30, 'bold'))
            disable_buttons()
            win_lose(text="1,000,000")

    question = Label(game_frame_mid, text=question_text, bg='black', fg='white', font=('arial', 14, 'bold'), justify=CENTER)
    question.grid(row=1, column=0, pady=10)

    #A
    a_text = Label(game_frame_bot, text="A:", bg='black', fg='white', font=('arial', 14, 'bold'))
    a_text.grid(row=1, column=0, pady=4, sticky=W)

    a_answer = Button(game_frame_bot, text=A_ans, bg='blue', fg='white', width=30, height=2, font=('arial', 14, 'bold'), highlightthickness=0, command=get_a_answer)
    a_answer.grid(row=1, column=1, padx=10, pady=10)

    #B
    b_text = Label(game_frame_bot, text="B:", bg='black', fg='white', font=('arial', 14, 'bold'))
    b_text.grid(row=2, column=0, pady=4, sticky=W)

    b_answer = Button(game_frame_bot, text=B_ans, bg='blue', fg='white', width=30, height=2, font=('arial', 14, 'bold'), highlightthickness=0, command=get_b_answer)
    b_answer.grid(row=2, column=1, padx=10, pady=10)

    #C
    c_text = Label(game_frame_bot, text="C:", bg='black', fg='white', font=('arial', 14, 'bold'))
    c_text.grid(row=1, column=3, pady=4, sticky=W)

    c_answer = Button(game_frame_bot, text=C_ans, bg='blue', fg='white', width=30, height=2, font=('arial', 14, 'bold'), highlightthickness=0, command=get_c_answer)
    c_answer.grid(row=1, column=4, padx=10, pady=10)

    #D
    d_text = Label(game_frame_bot, text="D:", bg='black', fg='white', font=('arial', 14, 'bold'))
    d_text.grid(row=2, column=3, pady=4, sticky=W)

    d_answer = Button(game_frame_bot, text=D_ans, bg='blue', fg='white', width=30, height=2, font=('arial', 14, 'bold'), highlightthickness=0, command=get_d_answer)
    d_answer.grid(row=2, column=4, padx=10, pady=10)




    window.mainloop()