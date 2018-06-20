#Name: Harlan Chang
#Assignment: Unit 4

value = int(input('Please input a number: '))
i = 2 #set at 2 because the first 2 numbers of the sequence are already defined
tempNum = 0 #used to hold the previous number
currentNum = 1
prevNum = 0

if value == 1:
	currentNum = 0 #checks if the user inputted 1, and changes the current number to 0 if they did
elif value <= 0: #lets the user know when they enter anything less than 0
	print('That number is not valid!')
	currentNum = 0
	
while i < value:
	tempNum = prevNum #used to hold the previous number	
	prevNum = currentNum #changes previous number to the current number in the sequence
	currentNum = prevNum + tempNum #gets the next number in the sequence 
	i += 1 #increments i

print('That number in the sequence is: ', currentNum) 