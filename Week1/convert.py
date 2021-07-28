'''
To Convert cartesian to polar or polar to cartesian as per user choice
'''
import math

def cart_polar(x,y):
    r=math.sqrt(x**2+y**2)
    theta=math.atan(y/x)
    # print 'The values in polar coordinates are:',r,' and ',theta
    print 'The values in polar coordinates are:{} and {}'.format(r,theta)


def polar_cart(r,theta):
    x=r*math.cos(theta)
    y=r*math.sin(theta)
    # print "The values in cartesian coordinates are:",x,' and ',y
    print "The values in cartesian coordinates are:{} and {}".format(x,y)

choice=input("Enter 1 to convert polar to cartesian and 2 to convert cartesian to polar:\n")
if choice==1:
    (r,theta)=input("Enter r and theta as per polar coordinates:")
    polar_cart(r,theta)
elif choice==2:
    (x,y)=input("Enter x and y as per cartesian coordinates:")
    cart_polar(x,y)