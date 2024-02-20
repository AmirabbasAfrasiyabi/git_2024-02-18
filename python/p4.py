from math import*
# input
a = float(input(" enter  a : "))
b = float(input(" enter  b : "))
c = float(input(" enter  c : "))

# process 
delta = None
delta = ( b * b ) - ( 4 * a * c )

if ( delta < 0 ):
    print ( " no answer found ")
if ( delta == 0 ) :
    r = None
    r = ( - b ) / ( 2 * a )
    print ( " the value of r is : " , r )
else :

    r1 = (( - b )+ sqrt( delta ) / ( 2 * a ))
    r2 = (( - b )- sqrt( delta ) / ( 2 * a ))
    print ( " the value of r1 is " , r1 , " /   " " the value of r2 is " , r2) 