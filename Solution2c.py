################################################################
# Kevin R. Salger
# IS 640 Homework 2, Solution c
# #  There are two versions of this program in the code.  
################################################################

########################################################################################
# BEGIN of HW2, #3  Sum & Average
print ("\n =-=-=-=-=-=-=-=-=- Method 1 -=-=-=-=-=-=-=-=-= \n")
# VARS Option 1 
UserInteger = [0, 0, 0]  # UserInteger as a list
SumIntegers = 0
AvgIntegers = 0.0
# End VARS Option 1 

# BEGIN Option 1 
UserInteger[0] = int(input('Enter the first of three integers: '))
UserInteger[1] = int(input('Enter the second of three integers: '))
UserInteger[2] = int(input('Enter the third of three integers: '))

SumIntegers = sum (UserInteger)  # Using the Sum function
AvgIntegers = SumIntegers/3

print ('The sum is {:,}'.format(SumIntegers))
print ('The average is {:,.2f}'.format(AvgIntegers))
print ("\n =-=-=-=-=-=-=-=-=- End of Method 1 -=-=-=-=-=-=-=-=-= \n")
# END Option 1 
########################################################################################

########################################################################################
print ("\n =-=-=-=-=-=-=-=-=- Method 2 -=-=-=-=-=-=-=-=-= \n")
# VARS Option 2
UserInt01 = 0  # UserInt01, -02, and -03 as distinct variables
UserInt02 = 0
UserInt03 = 0
SumIntegers = 0
AvgIntegers = 0.0
# End VARS Option 2 

# BEGIN Option 2 
UserInt01 = int(input('Enter the first of three integers: '))
UserInt02 = int(input('Enter the second of three integers: '))
UserInt03 = int(input('Enter the third of three integers: '))

SumIntegers = UserInt01 + UserInt02 + UserInt03  # Straight addition
AvgIntegers = SumIntegers/3

print (f'The sum is {SumIntegers:,}')
print (f'The average is {AvgIntegers:,.2f}')
print ("\n =-=-=-=-=-=-=-=-=- End of Method 2 -=-=-=-=-=-=-=-=-= \n")
# END Option 2
########################################################################################
# END