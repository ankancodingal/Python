#Activity 1
# import turtle

# # creating canvas
# turtle.Screen().bgcolor("Orange")

# sc = turtle.Screen()
# sc.setup(400, 300)

# turtle.title("Welcome to Turtle Window")

# # turtle object creation
# board = turtle.Turtle()

# # creating a square
# for i in range(4):
# 	board.forward(100)
# 	board.left(90)
# 	i = i+1


#Activity 2
# import turtle

# turtle.Screen().bgcolor("Orange")
# board = turtle.Turtle()
 
# # first triangle for star
# board.forward(100) # draw base
 
# board.left(120)
# board.forward(100)
 
# board.left(120)
# board.forward(100)
 
# board.penup()
# board.right(150)
# board.forward(50)
 
# # second triangle for star
# board.pendown()
# board.right(90)
# board.forward(100)
 
# board.right(120)
# board.forward(100)
 
# board.right(120)
# board.forward(100)
 
# turtle.done()

#Activity 3
# import turtle 
# t = turtle.Turtle()
# s = turtle.Screen()
# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
# s.bgcolor('black') 
# t.speed('fastest')
# t.hideturtle()
# while True:
#   for x in range(200): 
#     t.pencolor(colors[x%len(colors)])
#     t.width(x/100 + 1)
#     t.forward(x) 
#     t.left(59)
#   t.right(239)  
#   for x in range(200, 0, -1): 
#     t.pencolor('black') 
#     t.width(x/100 + 7)
#     t.forward(x) 
#     t.right(59) 
