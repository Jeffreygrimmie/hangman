#Jeffrey Grimmie 2/16/19

import random

#To do fix not being able to use word with more then one instance of the same letter

word = "zombie zen hate love sandwich hotdog sauce red orange blue pink percent"
lst = []
guessed = []
choosen_word_lst = []
guesses = [] #storing letters already guessed

#Gets a random word from the string _word_
def choose_word(lst):   
     return random.choice(lst)

#Generate a list of letters from the choosen word
def generate_lst(choosen_word):
	for i in choosen_word:
		choosen_word_lst.append(i)

#Gets a guess from the user 
def guess():
	letter = input("Please guess a letter: ").lower()
	return letter

#Generates a blank space display for the chossen word
def generate_guessed():
	for i in choosen_word_lst:
		guessed.append("_")
def find_letter(letter, lst):
    return any(letter in word for word in lst)

#checks the letter to see if it is the list
def letter_checker(letter, choosen_word_lst):
	if len(letter) > 1:
		print("Error: Invailid entry please try again.")
	elif find_letter(letter, guesses):
		print("You already tryed: %s Tryed lettter: %s " % (letter, guesses))
	elif find_letter(letter, choosen_word_lst) == True:
		index = choosen_word_lst.index(letter) #find the index of the matching letter letter
		del guessed[index]
		guessed.insert(index, letter)
		guesses.append(letter)
		print("You guessed correctly %s is in the word:  %s" % (letter, guessed))
	else:
		print("%s is not used in the current word." % letter)
		guesses.append(letter)


#main game function
def hangman():
	wordlist = str.split(word)
	choosen_word = choose_word(wordlist)
	generate_lst(choosen_word)
	print("This is hang man!")
	print("The current word has, %s letters in it." % len(choosen_word))
	generate_guessed()
	while guessed != choosen_word_lst:
		letter = guess()
		letter_checker(letter, choosen_word)
	print("Congratulations you won the game!")


hangman()