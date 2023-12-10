

# e=None
# print(e)
# _no1=1
# _no2=2
# print(_no1+_no2)
# import numpy
# import pandas as pd 

# # a=int(input("Enter the number to find out the match"))

# # match a:
# #     case 1:
# #         print('case is 1')
# #     case 2:
# #         print('case is 2')
# #     case 13:
# #         print('case is 13')
# for i in range(5):
#     print(i+1)

# s={1,3,4,5,2,33}
# ts=[1,3,4,5,2,33]
# for item in ts:
#     print(item)


# i=0
# while i<10:
#     print(i)
#     i+=1
# while True:
#     print("it's a infinite loops")
#     break



# def letterpad(name, date):
#     print(f"Hi man, This is {name} and I will not come to school on {date}")
# letterpad("Arshad", "12-04-2023")





# try:
#     a = int(input("enter your number"))
#     print(a+3)
# except Exception as e:
#     print("some error occurse", e)



# function in python
# class Employee:
   
#     def __init__(self,name,salary):
#         self.salary=salary
#         self.name =name

#     def getSalary(self):
#         return self.salary


# rohan=Employee("rohan",'34334')
# print(rohan.salary)
# print(rohan.name)




# import numpy as np 
# prime_array=np.array([2,3,4,7,11])
# print(prime_array)
# print(type(prime_array))
# another_array=np.array([[1,2],[1,2]])
# print(another_array)
# #create the 3-dim array
# # we will use two dimenstion array to crete the 3-dim arra
# three_dim=np.array([[[1,23,3],[1,2,3]],[[1,2,4],[1,2,2]]])
# print(three_dim)
# print(three_dim.shape)
# threeDim=three_dim.astype('float64')
# print(threeDim)




# import pandas as pd 
# import numpy as np
# # number_series=pd.Series([1,2,3,4,5])
# # print(number_series)

# # number_series1=pd.Series([1,2,3,4,5], index=['a','b','c','d','e'], name="Number")
# # print(number_series1)
# # print((number_series1[0]))
# # print(number_series1['a'])


# # # using a convetional list of lists
# # list_of_lists=[['amar',10],['akbar',15],['anthony',14]]
# # df=pd.DataFrame(list_of_lists, columns=['name','age'])
# # print(df)
# from matplotlib import pylab
# print(pylab.__version__)
# #  matplotlib tutorial

# x=np.linspace(10,25) 
# y=x*x+2
# print(x)
# print(y)
# pylab.plot(x,y,'r') #'r' is represent the color of the line in the ploating

# import sys  
# print(type(sys.argv))  
# print('The command line arguments are:')  
# for i in sys.argv:  
#     print(i)


import pygame
# initialize pygame
pygame.init()

# define width of screen
width = 1000
# define height of screen
height = 600
screen_res = (width, height)

pygame.display.set_caption("GFG Bouncing game")
screen = pygame.display.set_mode(screen_res)

# define colors
red = (255, 0, 0)
black = (0, 0, 0)

# define ball
ball_obj = pygame.draw.circle(
	surface=screen, color=red, center=[100, 100], radius=20)
# define speed of ball
# speed = [X direction speed, Y direction speed]
speed = [1, 1]

# game loop
while True:
	# event loop
	for event in pygame.event.get():
		# check if a user wants to exit the game or not
		if event.type == pygame.QUIT:
			exit()

	# fill black color on screen
	screen.fill(black)

	# move the ball
	# Let center of the ball is (100,100) and the speed is (1,1)
	ball_obj = ball_obj.move(speed)
	# Now center of the ball is (101,101)
	# In this way our wall will move

	# if ball goes out of screen then change direction of movement
	if ball_obj.left <= 0 or ball_obj.right >= width:
		speed[0] = -speed[0]
	if ball_obj.top <= 0 or ball_obj.bottom >= height:
		speed[1] = -speed[1]

	# draw ball at new centers that are obtained after moving ball_obj
	pygame.draw.circle(surface=screen, color=red,
					center=ball_obj.center, radius=20)

	# update screen
	pygame.display.flip()

