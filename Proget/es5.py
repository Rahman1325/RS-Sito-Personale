import turtle 
import random 

# creo la testo della snake
testo = turtle.Turtle()
testo.shape("square")
testo.color("green") #colore
testo.penup() #non disegnare

#creo la mela 
mela = turtle.Turtle()
mela.shape("circle")
mela.color("red")
mela.penup()
mela.goto(0,100)

#creo il corpo del serpente 
corpo = []



# creo la schermata
s=turtle.Screen()
s.listen()

#dizionario del teasti 
testi = {
    "w":False,
    "s":False,
    "a":False,
    "d":False
}
#funzione che accende il pulsante quando io premo
def testo_premuto(testo):
    testi[testo] =True

    #funzione che spenge il pulsante quando lo rilascio
def testo_alzato(testo):
    testi[testo] = False

s.onkeypress(lambda:testo_premuto("w"),"w")
s.onkeypress(lambda:testo_premuto("a"),"a")
s.onkeypress(lambda:testo_premuto("s"),"s")
s.onkeypress(lambda:testo_premuto("d"),"d")

s.onkeyrelease(lambda:testo_alzato("w"),"w")
s.onkeyrelease(lambda:testo_alzato("a"),"a")
s.onkeyrelease(lambda:testo_alzato("s"),"s")
s.onkeyrelease(lambda:testo_alzato("d"),"d")
    
    #funzione del movimento
def movimento():
    if testi["w"]:
        testo.setheading(90) #punta in testo_alto
        testo.forward(20)
    elif testi["s"]:
        testo.setheading(270) 
        testo.forward(20)
    elif testi["a"]:
        testo.setheading(180) 
        testo.forward(20)
    elif testi["d"]:
        testo.setheading(0) 
        testo.forward(20)

    if testo.distance(mela) <10:
        mela.goto(random.randint(-280,280),random.randint(-280,280))

        pezzo = turtle.Turtle()
        pezzo.shape("square")
        pezzo.color("dark green")
        pezzo.penup()
        corpo.append(pezzo)

    for i in range(len(corpo)-1,0,-1):
        corpo[i].goto(corpo[i-1].xcor(),corpo[i-1].ycor())

    if corpo:
        corpo[0].goto(testo.xcor(), testo.ycor())


    s.ontimer(movimento,1)

#chiamare le funzione movimento
movimento()
              
#schermata sempre apertura
s.mainloop()

