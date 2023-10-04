import random
import tkinter as tk

window = tk.Tk()
window.geometry("325x300")
etiqueta=tk.Label(window,text="JUGUEMOS PIEDRA, PAPEL O TIJERAS")
etiqueta.grid(column=0 , row=1)

window.title("JUEGO DE PIEDRA, PAPEL O TIJERAS") 

USER_SCORE=0
COMP_SCORE=0
USER_CHOICE =""
COMP_CHOICE = ""
def choice_to_number(choice) :
  rps = {'Piedra' :0, 'Papel' : 1, 'Tijeras':2}
  return rps[choice]
def number_to_choice ( number) :
  rps={0: 'Piedra', 1: 'Papel', 2: 'Tijeras'}
  return rps[number]
def random_computer_choice ( ):
  return random.choice(['Piedra','Papel','Tijeras'])

def result (human_choice, comp_choice):
  global USER_SCORE
  global COMP_SCORE
  user=choice_to_number (human_choice)
  comp=choice_to_number(comp_choice)
  if (user==comp):
    print("Empate")
  elif((user-comp)%3==1):
    print("Ganastes")
    USER_SCORE+=1
  else:
    print("Perdistes")
    COMP_SCORE+=1
  text_area = tk.Text(master=window,height=25,width=35,bg="#FFFF99")
  text_area.grid(column=0, row=5)
  answer="Your choice: {uc} \nComputer's choice : {cc}  \n Your Score : {u}  \n Computer Score : {c} ".format( uc=human_choice, cc=comp_choice, u=USER_SCORE, c=COMP_SCORE)
  text_area.insert(tk.END,answer)


def Piedra():
  global USER_SCORE
  global COMP_SCORE
  USER_CHOICE= 'Piedra'
  COMP_CHOICE= random_computer_choice()
  result(USER_CHOICE,COMP_CHOICE)
def Papel():
  global USER_SCORE
  global COMP_SCORE
  USER_CHOICE= 'Papel'
  COMP_CHOICE= random_computer_choice()
  result(USER_CHOICE,COMP_CHOICE)
def Tijeras():
  global USER_SCORE
  global COMP_SCORE
  USER_CHOICE= 'Tijeras'
  COMP_CHOICE= random_computer_choice()
  result(USER_CHOICE,COMP_CHOICE)


button1 = tk.Button (text="    Piedra     ",bg="skyblue", command=Piedra)
button1.grid(column=0 , row=2)
button2 = tk.Button (text="     Papel     ",bg="pink", command=Papel)
button2.grid(column=0 , row=3)
button3 = tk.Button (text="    Tijeras    ",bg="lightgreen", command=Tijeras)
button3.grid(column=0 , row=4)
window.mainloop()