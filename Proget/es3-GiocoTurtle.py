import turtle

# creo lo schero in cui gioco
s = turtle.Screen()

t = turtle.Turtle()    
t.shape("turtle")
t.color("blue")

#creo le funzione per i comandi della frecce
def su ():
    #la funzione devo girare verso su e poi andare avanti
    t.setheading(90) # giro di 90 grandi
    t.forward(30) # vado avanti di 30

def giu():
        t.setheading(270)
        t.forward (30)

def destra():
            t.setheading(0)
            t.forward(30)

def sinistra():
                t.setheading(180)
                t.forward(30)

#imposto che se schiaccio la barra spazio la turtle smette di 
#se la rischiaccio ricomincia a disegnare
#mi serve una ver

#aggiungo il comando che quando premo i tasti attiva la funzione
#imposto python affinche aspetti che io faccia qualcosa
s.listen()
s.onkey(su, "Up")
s.onkey(giu, "Down")
s.onkey(sinistra, "Left")
s.onkey(destra, "Right")

# mantengo la schermata aperto
s.mainloop()