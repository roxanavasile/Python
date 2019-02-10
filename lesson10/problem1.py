
def main():
    vowel=input("Enter a vowel: [a,e,i,o,u]")
    while is_not_vowel(vowel):
        print("Letter entered is not a vowel")
        vowel=input("Enter a vowel: [a,e,i,o,u]")
    print ("Vowel entered:", vowel)

def is_not_vowel(vowel):
    if vowel != "a" and vowel != "e" and vowel !="i" and vowel != "o" and vowel != "u":
        status = True
    else:
        status = False
    return status

main()
