import turtle

def spirograph(shape, pencolor, backcolor):
  sc = turtle.Screen()
  sc.setup(1.0, 1.0)
  sc.bgcolor(backcolor)

  t = turtle.Turtle()
  t.color(pencolor)
  t.speed(0)
  t.pensize(2)

  if shape == "1":
    i = 0
    while True:
      i += 2
      t.forward(i)
      t.right(118)
  elif shape == "2":
    i = 0
    while True:
      i += 2
      t.forward(i)
      t.right(88)
  elif shape == "3":
    i = 0
    while True:
      i += 2
      t.circle(i)
      t.right(88)
  else:
    with open("colors.txt") as f:
      colors = f.readlines()

    i = 0
    while True:
      colors.reverse()
      for c in colors:
        t.pencolor(c.strip())
        i += 3
        t.forward(i)
        t.right(118)

def menu():
  shape = input("""What spirograph would you like to make?
  1 - Triangle spirograph
  2 - Square spirograph
  3 - Circle spirograph
  4 - Wild card
  """)
  pencolor = input("What pen color would you like to use?")
  backcolor = input("What background color would you like to use?")
  spirograph(shape, pencolor, backcolor)

menu()