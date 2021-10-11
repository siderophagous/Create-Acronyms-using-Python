# function to create acronym
def fxn(stng):
	
	# add first letter
	oupt = stng[0]
	
	# iterate over string
	for i in range(1, len(stng)):
		if stng[i-1] == ' ':
			
			# add letter next to space
			oupt += stng[i]
			
	# uppercase oupt
	oupt = oupt.upper()
	return oupt


# input string
inpt1 = "Computer Science Engineering"

# output acronym
print(fxn(inpt1))

# input string
inpt1 = "roofpipe"

# output acronym
print(fxn(inpt1))

# input string
inpt1 = "Uttar pradesh"

# output acronym
print(fxn(inpt1))
