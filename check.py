from rich import print
from rich.console import Console
from rich.panel import Panel
import syllables

def iterateList(lineList):
	"""
	Goes through each item in a list and finds the number of syllables
	"""
	console = Console()
	totalSyllables = 0

	for word in lineList:
		console.print(f"Word - {word} Syllables - {syllables.estimate(word)}")
		totalSyllables += syllables.estimate(word)

	return totalSyllables


def checkHaiku():
	"""
	Checks entered text to find the syllables in each word
	"""
	console = Console()
	console.print("Let's check your haiku!")

	console.print('This program assumes your haiku has three lines, following the 5-7-5 pattern for syllables.')

	console.print('Enter your first line of your haiku')

	firstLine = input()

	firstLineList = firstLine.split()

	firstSyllables = iterateList(firstLineList)

	console.print(f'The first line had {firstSyllables} syllables')



