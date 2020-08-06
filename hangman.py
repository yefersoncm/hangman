VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here

import json
import random
import time

VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here

class WOFPlayer:
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
        
    def addMoney(self, amt):
        self.prizeMoney = self.prizeMoney + amt
        
    def goBankrupt(self):
        self.prizeMoney = 0
        
    def addPrize(self, prize):
        self.prizes.append(prize)
        
    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)

# Write the WOFHumanPlayer class definition (part B) here

class WOFHumanPlayer(WOFPlayer):
    category = 0
    obscured_phrase = ""
    guessed = []
    def getMove(self, category, obscuredPhrase, guessed):
		string = input('''
			{} has ${}

			Category: {}
			Phrase:  {}
			Guessed: {}

			Guess a letter, phrase, or type 'exit' or 'pass':

			'''.format(self.name, 
				self.prizeMoney, 
				self.category, 
				self.obscured_phrase, 
				self.guessed))
		return string

# Write the WOFComputerPlayer class definition (part C) here

class WOFComputerPlayer(WOFPlayer):
	SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

	def __init__(self, name, difficulty):
		WOFPlayer.__init__(self, name)
		self.difficulty = difficulty

	def smartCoinFlip(self):
		if random.randint(1, 10) > self.difficulty:
			return True
		else:
			return False

	def getPossibleLetters(self, guessed):
		return_lst = []
		for item in LETTERS:
			if item not in guessed:
				if item not in VOWELS:
					return_lst.append(item)
				elif self.prizeMoney > VOWEL_COST:
					return_lst.append(item)
				else:
					continue
		return return_lst


	def getMove(self, category, obscuredPhrase, guessed):
		possible_to_guess = self.getPossibleLetters(guessed)
		if len(possible_to_guess) == 0:
			return 'pass'
		new_difficulty = self.smartCoinFlip()
		quality = 0
		if new_difficulty:
			for item in possible_to_guess:
				if self.SORTED_FREQUENCIES.index(item) > quality:
					quality = self.SORTED_FREQUENCIES.index(item)
			return self.SORTED_FREQUENCIES[quality]
		else:
			return random.choice(possible_to_guess)