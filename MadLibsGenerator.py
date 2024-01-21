from tkinter import *
def Story1(win):
  def final(tl: Toplevel, name, sports, City, playername, drinkname, snacks):

    text = f'''
One day, my friend {name} and I, fueled by college spirit, decided to organize an impromptu {sports} match right on our campus grounds in {City}. However, unforeseen obstacles thwarted our plans, leading us to shift gears and become enthusiastic spectators instead.
We headed to the college sports arena to witness the game unfold, cheering on our favorite player, {playername}, with fellow students. To enhance the experience, we grabbed some {drinkname} and {snacks}, turning the event into a memorable college hangout.
Though our initial plans didn't pan out, the spontaneous change of course added a unique twist to our day. Leaving the arena with a sense of camaraderie and shared excitement, we couldn't help but appreciate the unexpected joys that college life brings. Looking forward to more spontaneous adventures and memorable moments on campus! '''

    tl.geometry(newGeometry='500x550')

    Label(tl, text='Story:',  wraplength=tl.winfo_width()).place(x=160, y=310)
    Label(tl, text=text,wraplength=tl.winfo_width()).place(x=0, y=330)

  NewScreen = Toplevel(win, bg='Navy Blue')
  NewScreen.title("The one with Memories")
  NewScreen.geometry('500x500')
  Label(NewScreen, text=' The one with Memories').place(x=100, y=0)
  Label(NewScreen, text='Name:').place(x=0, y=35)
  Label(NewScreen, text='Enter a game:').place(x=0, y=70)
  Label(NewScreen, text='Enter a city:').place(x=0, y=110)
  Label(NewScreen, text='Enter the name of a player:').place(x=0, y=150)
  Label(NewScreen, text='Enter the name of a drink:').place(x=0, y=190)
  Label(NewScreen, text='Enter the name of a snack:').place(x=0, y=230)
  Name = Entry(NewScreen, width=17)
  Name.place(x=250, y=35)
  game = Entry(NewScreen, width=17)
  game.place(x=250, y=70)
  city = Entry(NewScreen, width=17)
  city.place(x=250, y=105)
  player = Entry(NewScreen, width=17)
  player.place(x=250, y=150)
  drink = Entry(NewScreen, width=17)
  drink.place(x=250, y=190)
  snack = Entry(NewScreen, width=17)
  snack.place(x=250, y=220)
  SubmitButton = Button(NewScreen, text="Submit", background="Yellow", font=('Times', 12), command=lambda:final(NewScreen, Name.get(), game.get(), city.get(), player.get(), drink.get(), snack.get()))
  SubmitButton.place(x=150, y=270)

  NewScreen.mainloop()
def Story2(win):
    def final(tl: Toplevel, profession, noun, feeling, emotion,verb):
            text = f'''
          
When I was a child, I dreamt of becoming a {profession}, but as I grew up, my interests shifted towards the realm of {noun}, leading me to pursue a career as an engineer. However, the job I landed didn't align with my passion, leaving me feeling {feeling}.
After experiencing a sense of {emotion}, I made the courageous decision to pursue what I truly love. Despite receiving lower {verb} compared to my previous job, I find myself feeling the same sense of fulfillment and contentment in my current endeavors. Sometimes, following one's passion proves to be the most rewarding journey. '''

            tl.geometry(newGeometry='500x550')

            Label(tl, text='Story:',  wraplength=tl.winfo_width()).place(x=160, y=310)
            Label(tl, text=text,wraplength=tl.winfo_width()).place(x=0, y=330)
    NewScreen = Toplevel(win, bg='Blue')
    NewScreen.title("The Destiny")
    NewScreen.geometry('500x500')
    Label(NewScreen, text='Ambitions').place(x=150, y=0)
    Label(NewScreen, text='Enter a profession:').place(x=0, y=35)
    Label(NewScreen, text='Enter a noun:').place(x=0, y=70)
    Label(NewScreen, text='Enter a feeling:').place(x=0, y=110)
    Label(NewScreen, text='Enter a emotion:').place(x=0, y=150)
    Label(NewScreen, text='Enter a verb:').place(x=0, y=190)
    Profession = Entry(NewScreen, width=17)
    Profession.place(x=250, y=35)
    Noun = Entry(NewScreen, width=17)
    Noun.place(x=250, y=70)
    Feeling = Entry(NewScreen, width=17)
    Feeling.place(x=250, y=105)
    Emotion= Entry(NewScreen, width=17)
    Emotion.place(x=250, y=150)
    Verb = Entry(NewScreen, width=17)
    Verb.place(x=250, y=190)
    SubmitButton = Button(NewScreen, text="Submit", background="Yellow", font=('Times', 12), command=lambda:final(NewScreen, Profession.get(), Noun.get(), Feeling.get(), Emotion.get(), Verb.get()))
    SubmitButton.place(x=150, y=270)
  

Screen = Tk()
Screen.title("Mad Libs Generator")
Screen.geometry('400x400')
Screen.config(bg="Light blue")
Label(Screen, text='PythonGeeks Mad Libs Generator').place(x=100, y=20)
Story1Button = Button(Screen, text='The one with Memories', font=("Times New Roman", 13),command=lambda: Story1(Screen),bg='Yellow')
Story1Button.place(x=140, y=90)
Story2Button = Button(Screen, text='The Destiny', font=("Times New Roman", 13),command=lambda: Story2(Screen), bg='Yellow')
Story2Button.place(x=150, y=150)

Screen.update()
Screen.mainloop()
