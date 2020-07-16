class Image:
	def __init__(self):
		self.next_line = "\n"
		self.default_image=["##################",
							"#                #",
							"#     ########   #",
							"#           ##   #",
							"#           ##   #",
							"#           ##   #",
							"#           ##   #",
							"#           ##   #",
							"#           ##   #",
							"#           ##   #",
							"#           ##   #",
							"#           ##   #",
							"#           ##   #",
							"##################"]

		self.one = {3 : "#     #     ##   #", 4 : "#    ###    ##   #", 5 : "#    ###    ##   #", 6 : "#     #     ##   #"}
		self.two = {7: "#     #     ##   #", 8 : "#     #     ##   #", 9 : "#     #     ##   #"}
		self.three = {7 : "#  ####     ##   #"}
		self.four = {7 : "#  #######  ##   #"}
		self.five = {10 : "#    #      ##   #", 11 : "#   #       ##   #"}
		self.six = {10 : "#    # #    ##   #", 11 : "#   #   #   ##   #"}

		self.life = [None, self.one, self.two, self.three, self.four, self.five, self.six]

	def getImage(self, val):
		if val != 0:
			to_show = self.life[1:val+1]
			for mod in to_show:
				for key,value in mod.items():
					self.default_image[key] = value
		return self.next_line.join(self.default_image)
		


class Hangman:
	def iniMsg(self):
		print("@@@@@@@@@@@@@@@@@@@@@@@@@@")
		print("@   WELCOME TO HANGMAN   @")
		print("@@@@@@@@@@@@@@@@@@@@@@@@@@")

	def wonMsg(self):
		print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
		print("@   Congratulations,Player-2 You WON.   @")
		print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

	def lostMsg(self):
		print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
		print("@   Player-2 You LOST. Better Luck Next Time.   @")
		print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

	def printProgress(self, image=None, word="------", guess="", misses=""):
		print(image)
		print("------------------")
		print("Word: ", word)
		print("Guess: ", guess)
		print("Misses: ", misses)
		print("------------------")
	
	def start(self):
		number_of_life = 0
		player1_word = (str(input("Player-1, Please enter a word: "))).upper()
		print("\nNow Player-2 will guess the word.")

		imageObj = Image()
		img = imageObj.getImage(number_of_life)

		j = ""
		show_word = ["-"]*(len(player1_word))

		misses = ""
		while number_of_life < 6:
			try:
				guessed_alpha = (str(input("\nPlayer-2, guess an alphabet: "))[0]).upper()
			except:
				print("Please enter valid alphabet.")
				continue

			if (guessed_alpha in misses) or (guessed_alpha in show_word):
				print("You have already guessed: ",guessed_alpha)
				continue

			if guessed_alpha in player1_word:
				for i in range(0,len(player1_word)):
					if player1_word[i] == guessed_alpha:
						show_word[i] = guessed_alpha
			else:
				number_of_life += 1
				img = imageObj.getImage(number_of_life)
				misses = misses + guessed_alpha + ", "

			if "-" not in show_word:
				self.wonMsg()
				break

			self.printProgress(image=img, word=j.join(show_word), guess=guessed_alpha, misses=misses)

		if number_of_life == 6:
			self.lostMsg()


def main():
	game = Hangman()
	game.iniMsg()
	game.start()

if __name__ == "__main__":
	main()