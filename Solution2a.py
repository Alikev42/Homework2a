########################################################################################
# Kevin R. Salger
# IS 640 Homework 2, Solution a
########################################################################################

# VARS
BaseNum = 0     # integer, initial value = 0
Count = 0       # integer, initial value = 0
#Headings = f'{"Number":>20}' f'{"Square":>20}' f'{"Cube":>20}' 
Headings = ("Number", "Square", "Cube")
Labels = ("Number", "Square", "Cube")
# End Declarations
########################################################################################

########################################################################################
# BEGIN
# Alternate method to print the column headings
#print()
print ('{:>20}' '{:>20}' '{:>20}'.format(Headings[0],Headings[1],Headings[2]))
print ('The headings above are stubbornly flush left in Jupyter Notebook but correct in Python.')
print ()  # Intentional blank line

########################################################################################
print ('Below are three methods for printing the column headers.')

########################################################################################
print ('=-=-=-=-=-=-=-=-=- Method 1 -=-=-=-=-=-=-=-=-=')
print (f'{Headings[0]:>20}' f'{Headings[1]:>20}' f'{Headings[2]:>20}')

for BaseNum in list(range(6)):
    print (f'{BaseNum:>20d} {BaseNum*2:>19d} {BaseNum**2:>19d}')
#   I'm not wild about this solution because of the different field sizes.  
#    print ('{:20d}{:20d}{:20d}'.format(BaseNum, BaseNum**2, BaseNum**3))
# end of for BaseNum loop
print ("\n =-=-=-=-=-=-=-=-=- End of Method 1 -=-=-=-=-=-=-=-=-= \n")

########################################################################################
print ('=-=-=-=-=-=-=-=-=- Method 2 -=-=-=-=-=-=-=-=-=')
# This is the more elegant solution, using two for loops
for Count in list(range(3)):
    print ('{:>20}'.format(Labels[Count]), end="")
# End For Count loop
print ()

BaseNum = 0  # Resetting BaseNum.  May not be needed.
for BaseNum in list(range(6)):
    print ('{:20d}{:20d}{:20d}'.format(BaseNum, BaseNum**2, BaseNum**3))
# end of for BaseNum loop
print ("\n =-=-=-=-=-=-=-=-=- End of Method 2 -=-=-=-=-=-=-=-=-= \n")

########################################################################################
print ('=-=-=-=-=-=-=-=-=- Method 3 -=-=-=-=-=-=-=-=-=')
# The following line formats correctly as long as there is a leading non-space character.  
# The next line also formats correctly when run as a .py file instead of as a .ipynb file.
print ('{:>20}' '{:>20}' '{:>20}'.format(Headings[0],Headings[1],Headings[2]))

BaseNum = 0  # Resetting BaseNum.  May not be needed.
for BaseNum in list(range(6)):
    print ('{:20d}{:20d}{:20d}'.format(BaseNum, BaseNum**2, BaseNum**3))
# end of for BaseNum loop
print ("\n =-=-=-=-=-=-=-=-=- End of Method 3 -=-=-=-=-=-=-=-=-= \n")

########################################################################################
# END