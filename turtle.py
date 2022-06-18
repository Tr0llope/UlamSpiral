import turtle


taille = int(input("entrer la taille de l'image : "))
n = len(str(taille))
file = open("resultat.pbm", "r")


t = turtle.Pen()s
#lecture des caractères qui définissent le format PBM
set_start = file.read(5+n+n)


def carre():
    t.color("black")
    t.begin_fill()
    t.down()
    for x in range(4):
        t.forward(10)
        t.left(90)
    t.end_fill()
    t.up()




def tortue_v2(iteration):
    t.up()
    for k in range(iteration):
        for x in range(iteration):
            t.goto(x*10, k*(-10))
            val = file.read(1)
            if val == '1':
                carre()
            file.read(1)


tortue_v2(taille)

file.close()


