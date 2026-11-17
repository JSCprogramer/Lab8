import math


def volm(r,h): #user inputs the radius and height in
             
    Volume=math.pi*(r**2)*h  #the math
    return Volume  #prints the volume to user


def cylinder_volume():
    radius=float(input("Enter the raduis: "))
    height=float(input("Enter the height: "))
    
    Volume=math.pi*(radius**2)*height
    
    print(f'The raduis of your cylinder is {radius}')
    print(f'The height of your cylinder is {height}')
    print(f'The volume of your cylinder is {Volume:.2f}')