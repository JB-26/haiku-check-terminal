from rich.console import Console
from rich.table import Table
import syllables


def iteratelist(linelist, linenum):
    """
    Goes through each item in a list and finds the number of syllables. Returns the total number of syllables
    """

    console = Console()
    table = Table(title=f"Haiku Line {linenum}")
    table.add_column("Word", justify="center", style="cyan")
    table.add_column("Syllables", justify="center", style="cyan")
    totalsyllables: int = 0

    for word in linelist:
        totalsyllables += syllables.estimate(word)
        table.add_row(word, str(syllables.estimate(word)))

    console.print(table)

    return totalsyllables


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

    firstSyllables = iteratelist(firstLineList, '1')

    console.print(f'The first line had {firstSyllables} syllables')

    console.print("Enter your second line of your haiku")

    secondLine = input()

    secondLineList = secondLine.split()

    secondSyllables = iteratelist(secondLineList, '2')

    console.print(f'The second line had {secondSyllables} syllables')

    console.print("Enter your third line of your haiku")

    thirdLine = input()

    thirdLineList = thirdLine.split()

    thirdSyllables = iteratelist(thirdLineList, '3')

    console.print(f'The third line had {thirdSyllables} syllables')

    if firstSyllables == 5 & secondSyllables == 7 & thirdSyllables == 5:
        console.print('That is a haiku!')
    else:
        console.print('That is not a haiku!')
        if firstSyllables - 5 <= 0:
            pass
        else:
            console.print(f'The first line had {firstSyllables} syllables, the first line needs 5 lines. This line has a difference of {firstSyllables - 5} syllables')
        if secondSyllables - 7 <= 0:
            pass
        else:
            console.print(f'The second line had {secondSyllables} syllables, the first line needs 5 lines. This line has a difference of {secondSyllables - 7} syllables')
        if thirdSyllables - 5 <= 0:
            pass
        else:
            console.print(f'The second line had {thirdSyllables} syllables, the first line needs 5 lines. This line has a difference of {thirdSyllables - 5} syllables')
