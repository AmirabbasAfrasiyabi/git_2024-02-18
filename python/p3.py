# project3

a = int(input(" enter a lengh of the first side "))
b = int(input(" enter a lengh of the second side "))
c = int(input(" enter a lengh of the third side "))

# process & output

Max = a
Min1 = b
Min2 = c


if ( b > Max ) :
    Max = b
    Min1 = a
    Min2 = c

if ( c > Max ):
    Max = c
    Min1 = b
    Min2 = a

if ( Min1 + Min2 > Max ) :
    print ( " is traingle " )
else :
    print ( " is not traingle " )
