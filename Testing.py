#---------------------------------------------------------------------------
# Creates a text output for testing 
# Benjamin Reelick - Benjamin.Reelick@gmail.com - 2/08/2021
#---------------------------------------------------------------------------

# Imports:
import random

# Quick def for testing even-odd polarity:
def isodd(num):
        return num & 1 and True or False

# Initialisation variables:
n = 500
prefD = {}
testFile = open('TestFile', 'w')

# Creating male and female preference lists:
for i in range(1, 2*n+1):
    if isodd(i):
        prefD[i] = random.sample(range(2, 2*n + 1, 2), n)
    else:
        prefD[i] = random.sample(range(1, 2*n + 1, 2), n)

# Creating testing text file:
testFile.write('# Random instance for Gale-Shapley, n = {}\n#\nn = {}\n#'
               .format(n, n))
for k in prefD:
    testFile.write('\n{}:'.format(k))
    for i in range(n):
        testFile.write(' {}'.format(prefD[k][i]))

testFile.close()