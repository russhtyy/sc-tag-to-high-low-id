from math import floor, pow
from colorama import Fore, Back, init

init(autoreset=True)
tag = input("\n\n" + Fore.RED + "( ? )" + Fore.CYAN + " What's the Player Tag you want to convert to High & Low ID?: #")

def tag_to_id(tag):
    tag, total, i, arr = [x for x in tag.upper().replace("#", "").replace("O", "0")], 0, 0, ["0", "2", "8", "9", "P", "Y", "L", "Q", "G", "R", "J", "C", "U", "V"]    
    while len(tag) > 0:
        ch = tag.pop()
        total += arr.index(ch) * pow(14, i)
        i += 1        
    total = int(total)
    highID, lowID = total % 256, floor(total / 256)
    return highID, lowID

if __name__ == "__main__":
    highID, lowID = tag_to_id(tag)
    print(Fore.GREEN + "( ! )" + Fore.CYAN + " #" + tag.upper() + "'s High & Low ID: " + str(highID) + ", " + str(lowID) + "." + "\n\n")
