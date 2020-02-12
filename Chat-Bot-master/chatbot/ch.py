from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import threading
from PIL import Image,ImageTk

bot = ChatBot("My Bot")
conversation = [
"Good morning",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "What is your name",
    "My name is TechBot",
    "Bye",
    "Bye and have a good day !!"
]
trainer = ListTrainer(bot)
trainer.train(conversation)
win = Tk()
win.geometry("600x750")
win.title("Chat Bot")

image = Image.open("logo1.jpg")
photo = ImageTk.PhotoImage(image)
bot_label = Label(image=photo)
bot_label.pack() 


def ask():
    query = textF.get()
    answer = bot.get_response(query)
    msgs.insert(END, "You : " + query)
    print(type(answer))
    msgs.insert(END, "Bot : " + str(answer))
    textF.delete(0, END)
    msgs.yview(END)
frame = Frame(win)
sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()
textF = Entry(win, font=("Verdana", 20))
textF.pack(fill=X, pady=10)
btn = Button(win, text="Ask", font=("Verdana", 20), command=ask)
btn.pack()
def enter_function(event):
    btn.invoke()
win.bind('<Return>', enter_function)
def repeatL():
    while True:
        takeQuery()
t = threading.Thread(target=repeatL)
t.start()
win.mainloop()
