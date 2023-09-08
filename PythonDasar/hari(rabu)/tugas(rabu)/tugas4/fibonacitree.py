import turtle
import math

def fiboPlot(n):
   a = 0
   b = 1
   sqr_a = a
   sqr_b = b

   y.pencolor("black")

   y.forward(b * fac)
   y.left(90)
   y.forward(b * fac)
   y.left(90)
   y.forward(b * fac)
   y.left(90)
   y.forward(b * fac)

   temp = sqr_b
   sqr_b = sqr_b + sqr_a
   sqr_a = temp
  
   for i in range(1, n):
       y.backward(sqr_a * fac)
       y.right(90)
       y.forward(sqr_b * fac)
       y.left(90)
       y.forward(sqr_b * fac)
       y.left(90)
       y.forward(sqr_b * fac)

       temp = sqr_b
       sqr_b = sqr_b + sqr_a
       sqr_a = temp

   y.penup()
   y.setposition(fac, 0)
   y.seth(0)
   y.pendown()

   y.pencolor("red")

   y.left(90)
   for i in range(n):
       print(b)
       fdwd = math.pi * b * fac / 2
       fdwd /= 90
       for j in range(90):
           y.forward(fdwd)
           y.left(1)
       temp = a
       a = b
       b = temp + b

fac = 5

print("Semakin besar angka dimasukan semakin besar Fibonaci Tree !!")
m = int(input('Masukan angka untuk membuat Fibonaci Tree (Harus Lebih dari(>) 1): '))

if m > 0:
   print("Membuat Fibonaci Tree dengan ", m, "elemen :")
   y = turtle.Turtle()
   y.speed(100)
   fiboPlot(m)
   turtle.done()
else:
   print("Masukan lah lebih dari(>) 1")