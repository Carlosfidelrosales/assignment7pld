#Create a program that ask for a sentence as input.
#Display the number of words, vowels and consonants in the input 
#ex.
#input: Bahala kayo dyan
#output:
#words: 3
#vowels: 6
#consonants: 8

def words_vowels_consonants():
    print("\033[1mWELCOME TO \033[31mCARLITO'S WORDS, VOWELS AND CONSONANTS COUNTER\033[0m\033[0m!")
    word_want = input("\033[92mPlease Enter Your Desired \033[1mWord / Sentence / Phrase\033[0m :\033[0m\n>>> ")
    word_want.lower()
    vowels_count = 0
    vowel = set("aeiouAEIOU")
    consonants_count = 0
    numb = len(word_want.split())
    
    for i in word_want: 
        if i in vowel:
            vowels_count = vowels_count + 1
        elif((i>='a' and i<='z') or (i>='A' and i<='Z')):
            consonants_count = consonants_count + 1
    
    #FOR NUMBER OF WORDS
    print (f'The number of \033[96m\033[1mword(s)\033[0m\033[0m the \033[4m{word_want}\033[0m have is = \033[93m\033[1m{numb}\033[0m\033[0m')

    #FOR NUMBER OF VOWELS
    print(f'The total number of \033[96m\033[1mvowel(s)\033[0m\033[0m are there in \033[4m{word_want}\033[0m is = \033[93m\033[1m{vowels_count}\033[0m\033[0m') 
    
    #FOR NUMBER OF CONSONANTS
    print(f'The total number of \033[96m\033[1mconsonant(s)\033[0m\033[0m are there in \033[4m{word_want}\033[0m is = \033[93m\033[1m{consonants_count}\033[93m\033[0m') 
    
    
words_vowels_consonants()