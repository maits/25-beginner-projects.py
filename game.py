
secret_num = 15
i = 1

user_num = input("Hey there! Guess a number: ")

while secret_num != user_num: 
	if user_num < secret_num:
		print ("Too low. Guess again!")
		i += 1 
		user_num = input("Guess a number ")

	elif user_num > secret_num:
		print ("Too high! Guess again!")
		i += 1 
		user_num = input("Guess a number ")

print ("You got it right. It took you {0} times to guess it.".format(i))
