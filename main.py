# importing required modules

from tkinter import *
import random
from tkinter import messagebox
import mysql.connector as ms

# GLOBAL VARIABLES  #

userID = 0
score = 0
timeleft = 60
count = 0
miss = 0
wpm = 0
words_slide = ''
word_concad = ''
tech_words = []
science_words = []
literature_words = []
sports_words = []

#  MAIN FUNCTIONS  #

#  FUNCTION FOR SELECTING TOPIC  #


def topic():
    topic_window = Tk()
    topic_window.title("CHOOSE A TOPIC")
    topic_window.geometry("{0}x{1}+0+0".format(topic_window.winfo_screenwidth(), topic_window.winfo_screenheight()))

    Grid.rowconfigure(topic_window, 0, weight=1)
    Grid.rowconfigure(topic_window, 1, weight=1)
    Grid.columnconfigure(topic_window, 0, weight=1)
    Grid.columnconfigure(topic_window, 1, weight=1)

#  CREATING VARIOUS TOPIC BUTTONS  #

    #  TECH WORDS FETCH SUB-FUNCTION  #

    def tech():
        global tech_words
        fh = open("tech_words.txt")
        reader = fh.read()
        tech_words = reader.split('|')
        typing_page(tech_words)
        type_window.bind('<Return>', lambda event: start_game(event, tech_words))

    tech = Button(topic_window,
                  text="TECH",
                  width=71,
                  height=22,
                  fg="green",
                  bg="navy",
                  highlightbackground="#000000",
                  command=tech)
    tech.grid(row=0, column=0, sticky="NSEW")

    #  SCIENCE WORDS FETCH SUB-FUNCTION  #

    def science():
        global science_words
        fh = open("science_words.txt")
        reader = fh.read()
        science_words = reader.split('|')
        typing_page(science_words)
        type_window.bind('<Return>', lambda event: start_game(event, science_words))

    science_button = Button(topic_window,
                            text="SCIENCE",
                            width=71,
                            height=22,
                            fg="blue",
                            bg="black",
                            highlightbackground="#000000",
                            command=science)
    science_button.config(background="black")
    science_button.grid(row=0, column=1, sticky="NSEW")

    #  LITERATURE WORDS FETCH SUB-FUNCTION  #

    def lit():
        global literature_words
        fh = open("literature_words.txt")
        reader = fh.read()
        literature_words = reader.split('|')
        typing_page(literature_words)
        type_window.bind('<Return>', lambda event: start_game(event, literature_words))

    lit = Button(topic_window,
                 text="LITERATURE",
                 width=71,
                 height=21,
                 fg="red",
                 bg="orange",
                 highlightbackground="#000000",
                 command=lit)
    lit.grid(row=1, column=0, sticky="NSEW")

    #  SPORTS WORDS FETCH SUB-FUNCTION  #

    def sports():
        global sports_words
        fh = open("sports_words.txt")
        reader = fh.read()
        sports_words = reader.split('|')
        typing_page(sports_words)
        type_window.bind('<Return>', lambda event: start_game(event, sports_words))

    sport = Button(topic_window,
                   text="SPORTS",
                   width=71,
                   height=21,
                   fg="orange",
                   bg="green",
                   highlightbackground="#000000",
                   command=sports)
    sport.grid(row=1, column=1, sticky="NSEW")


#  TYPING PAGE ALL WIDGETS FUNCTION  #


def typing_page(input_words):           # input_words refers to type of word-set called (science,tech,lit,sports)
    global type_window
    type_window = Tk()
    type_window.title("THIS IS A SPEED TEST !")
    type_window.geometry("{0}x{1}+0+0".format(type_window.winfo_screenwidth(), type_window.winfo_screenheight()))
    type_window.configure(bg='SkyBlue4')
    random.shuffle(input_words)

    #  WORD FETCHED FROM FILE DISPLAY #

    global word_display

    word_display = Label(type_window,
                         text=input_words[0],
                         font=('arial', 50, 'italic bold'),
                         bg="SkyBlue4",
                         fg="yellow")
    word_display.place(x=525, y=250)

    score_heading = Label(type_window,
                          text='Words Correct : ',
                          font=('arial', 35, 'italic bold'),
                          bg="SkyBlue4",
                          fg="PaleTurquoise1")
    score_heading.place(x=10, y=100)

    #  WORDS CORRECT COUNT  #

    global score_display
    score_display = Label(type_window,
                          text=score,
                          font=('arial', 35, 'italic bold'),
                          bg="SkyBlue4",
                          fg="PaleTurquoise1")
    score_display.place(x=80, y=180)

    #  WPM DISPLAY  #

    wpm_heading = Label(type_window,
                        text="Your WPM :",
                        font=('arial', 25, 'italic bold'),
                        bg="SkyBlue4",
                        fg="PaleTurquoise1")
    wpm_heading.place(x=100, y=450)

    global wpm_count
    wpm_count = Label(type_window,
                      text=wpm,
                      font=('arial', 25, 'italic bold'),
                      bg="SkyBlue4",
                      fg="PaleTurquoise1")
    wpm_count.place(x=100, y=500)

    #  TIME COUNTDOWN DISPLAY  #

    timer = Label(type_window,
                  text='Time Left :',
                  font=('arial', 35, 'italic bold'),
                  bg="SkyBlue4",
                  fg="PaleTurquoise1")
    timer.place(x=900, y=100)

    global time_count
    time_count = Label(type_window,
                       text=timeleft,
                       font=('arial', 35, 'italic bold'),
                       bg="SkyBlue4",
                       fg="PaleTurquoise1")
    time_count.place(x=980, y=180)

    #  STARTING INSTRUCTION  #

    global instructions
    instructions = Label(type_window,
                         text='Type Word And Hit Enter Button',
                         font=('arial', 30, 'italic bold'),
                         bg="SkyBlue4",
                         fg="PaleTurquoise1")
    instructions.place(x=420, y=450)

    #  WORD ENTRY BOX  #

    global word_entry
    word_entry = Entry(type_window,
                       font=('arial', 35, 'italic bold'),
                       bd=10,
                       justify='center')
    word_entry.place(x=450, y=350)
    word_entry.focus_set()

    #  EXIT BUTTON  #

    exit_button = Button(type_window,
                         text="EXIT",
                         command=type_window.quit)
    exit_button.pack()


# TIME COUNTDOWN FUNCTION #


def time(words=None):
    global timeleft, score, miss, wpm
    if timeleft >= 11:
        pass
    else:
        time_count.configure(fg='red')
    if timeleft > 0:
        timeleft -= 1
        time_count.configure(text=timeleft)
        time_count.after(1000, time)

    else:
        instructions.configure(
            text='WPM = {} | Correct = {} | Wrong = {} | Net Score = {}'.format(wpm,
                                                                                score,
                                                                                miss,
                                                                                score - miss))

        rr = messagebox.askretrycancel('Notification', 'To Play Again Hit Retry')
        if rr:
            score = 0
            timeleft = 60
            miss = 0
            wpm = 0
            time_count.configure(text=timeleft)
            word_display.configure(text=words[0])
            score_display.configure(text=score)
            wpm_count.configure(text=wpm)


#  START GAME FUNCTION  #


def start_game(event, words):
    global score, miss, wpm, word_concad
    if timeleft == 60:
        time()
    instructions.configure(text='')
    for i in range(len(word_entry.get())):
        for j in range(len(word_display['text'])):
            if word_entry.get()[i] == word_display['text'][j]:
                word_concad += word_entry.get()[i]
                wpm = ((len(word_concad) / 5) / 1)
                score_display.configure(text=score)
                wpm_count.configure(text=wpm)

    if word_entry.get() == word_display['text']:
        score += 1
    else:
        miss += 1

    random.shuffle(words)
    word_display.configure(text=words[0])
    word_entry.delete(0, END)

    mysql()

#  SLIDING LABEL FUNCTION  #


def sliding_words():
    global count, words_slide
    text = 'Welcome to SPEED TYPING APP !!'
    if count >= len(text):
        count = 0
        words_slide = ''
    words_slide += text[count]
    count += 1
    font.configure(text=words_slide)
    font.after(100, sliding_words)


#  SETTING UP OPENING WINDOW  #

window = Tk()
window.title("SPEED TYPING APP")
opening_label = Label(window)
opening_label.img = PhotoImage(file="photo.gif", master=window)
opening_label.config(image=opening_label.img)
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))


#  FONT LABEL FOR SLIDING TEXT  #

font = Label(window,
             text='',
             font=('arial', 40, 'italic bold'),
             bg='black',
             fg='red',
             width=40)
font.place(x=45, y=10)

#  CHOOSING TOPIC BUTTON  #

chose = Button(window,
               text="LET'S START !",
               width=15,
               height=3,
               fg="black",
               font=("aleo", 30, 'bold'),
               command=topic,
               justify="center")
chose.place(x=450, y=300)


#  MYSQL CONNECT FUNCTION  #


def user():
    global userID
    userID = random.randrange(0, 999999999)


def mysql():
    mycon = ms.connect(host="localhost",
                       user="root",
                       passwd="Nandan1804",
                       database="typing_speed_app")
    cursor = mycon.cursor()
    user()
    val = "INSERT INTO scores(UserID,WPM,Score,Correct,Wrong,Time) VALUES({},{},{},{},{},{})".format(userID,
                                                                                                     wpm,
                                                                                                     (score - miss),
                                                                                                     score,
                                                                                                     miss,
                                                                                                     60)
    cursor.execute(val)
    mycon.commit()

############################################


sliding_words()
opening_label.pack()
window.mainloop()
