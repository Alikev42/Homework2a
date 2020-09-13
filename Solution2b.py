################################################################
# Kevin R. Salger
# IS 640 Homework 2, Sol'n 2
# ################################################################

# BEGIN of HW2, #2 Temperature Conversion
# VARS
TempCount = 0.0
DegF = 0.0
DegC = [-40.0, 0.0, 40.0, 100.0]
# End VARS

# BEGIN

########################################################################################

print ("\n =-=-=-=-=-=-=-=-=- Method 1 -=-=-=-=-=-=-=-=-= \n")
for TempCount in list(DegC):
    DegF = (9/5)*TempCount + 32
    print ('A temperature of {:.2f} degrees C = {:.2f} degrees F.'.format(TempCount, DegF))
# end of For TempCount loop
print ("\n =-=-=-=-=-=-=-=-=- End of Method 1 -=-=-=-=-=-=-=-=-= \n")

print ("\n =-=-=-=-=-=-=-=-=- Method 2 -=-=-=-=-=-=-=-=-= \n")
TempCount = 0  #  Resetting TempCount.  May not be necessary.
for TempCount in list(DegC):
    DegF = (9/5)*TempCount + 32
    print (f'A temperature of {TempCount:.2f} degrees C = {DegF:.2f} degrees F.')
# end of For TempCount loop
print ("\n =-=-=-=-=-=-=-=-=- End of Method 2 -=-=-=-=-=-=-=-=-= \n")
# END