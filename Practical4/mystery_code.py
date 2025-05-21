# What does this piece of code do?
# Answer: It selects random numbers between 1 and 6 and reports how many times until the numbers are equal. 
          
# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil
# Initialize a variable named progress.
progress=0
# Add a cycle that is infinite because progress is non negative.
while progress>=0:
	# Add one after each cycle.
	progress+=1
	# The first number
	first_n = randint(1,6)
    # The second number
	second_n = randint(1,6)
	# Add printing restrictive condition
	if first_n == second_n:
		# Print the number of times of the cycle.
		print(progress)
		break

