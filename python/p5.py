#input

dayOfYears = None 
dayOfYears =int(input( " Enter dayOfYears : " ))

#process

month = None
day = None
if (  dayOfYears <= 186 ) :
     if ( dayOfYears % 31 == 0 ) :
          day = 31
          month = int( dayOfYears  /  31)
     else:
          day = dayOfYears % 31
          month = int ( dayOfYears  / 31) +1
else :
     dayOfYears = dayOfYears - 186
     if ( dayOfYears % 30 == 0 ):
          day = 30
          month = int ( dayOfYears  /  30) + 6
     else :
          day = dayOfYears % 30
          month = int ( dayOfYears  /  30) + 1 + 6
     
# out put

print( month,"  /  ",day)
