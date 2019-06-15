import turtle

right_Leg_Length = 30
right_Arm_Length = 20

left_Leg_Length = 30
left_Arm_Length = 20

belly_Length = 40
neck_Length = 10


#Right leg
turtle.right(45)
turtle.forward(right_Leg_Length)
turtle.right(180)
turtle.forward(right_Leg_Length)

#left leg
turtle.left(90)
turtle.forward(left_Leg_Length)
turtle.right(180)
turtle.forward(left_Leg_Length)
turtle.left(45)

#torso - below arms
turtle.forward(belly_Length)
turtle.left(90)

#Left Arm
turtle.forward(left_Arm_Length)
turtle.right(180)
turtle.forward(left_Arm_Length)

# Right Arm
turtle.forward(right_Arm_Length)
turtle.right(180)
turtle.forward(right_Arm_Length)
turtle.right(90)

# Neck
turtle.forward(neck_Length)

# Start head
turtle.left(90)
for num in range(90):
    turtle.forward(1)
    turtle.right(4)

done()
