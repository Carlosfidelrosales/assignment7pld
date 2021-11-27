def words_vowels_consonants():
    print("WELCOME TO CARLITO'S WORDS, VOWELS AND CONSONANTS COUNTER!")
    word_want = input("Please Enter Your Desired Word / Sentences : ")
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
    print (f'The number of word(s) the {word_want} have is = {numb}')

    #FOR NUMBER OF VOWELS_count
    print(f'The total number of vowel(s) are there in {word_want} = {vowels_count}') 
    
    #FOR NUMBER OF CONSONANTS
    print(f'The total number of consonant(s) are there in {word_want} = {consonants_count}') 
    
    
words_vowels_consonants()