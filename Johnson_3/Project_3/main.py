def get_input():
    count_number_of_words(input("Please provide a sentence with at least 10 words: ").strip())


def count_number_of_words(sentence):
    num_of_words = len(sentence.split())
    if num_of_words >= 10:
        print("There are {} words in the sentence you entered.".format(num_of_words))
        count_number_of_vowels(sentence)
    else:
        print("You must enter more than 10 words, try again.")
        get_input()


def count_number_of_vowels(sentence):
    vowels = "aeiou"
    num_of_vowels = sum(sentence.lower().count(vowel) for vowel in vowels)
    print("There are {} vowels in the sentence you entered.".format(num_of_vowels))
    list_of_unique_words(sentence)


def list_of_unique_words(sentence):
    # I am forcing to lowercase for comparison so ensure the word comparison is not case-sensitive.
    sentence_list = set(sentence.lower().split())
    word_list = []
    for word in sentence_list:
        if word not in word_list:
            word_list.append(word)
    print("Below is a list of the unique words you used: ")
    print(*word_list)  # the * gets rid of the brackets on the list when you print
    longest_word(sentence)


def longest_word(sentence):
    sentence_list = set(sentence.lower().split())
    length = 0
    longest_word_list = []
    # Get length of the longest word
    for word in sentence_list:
        if len(word) > length:
            length = len(word)
    # Find all words that are as long as the longest word and add them to the list
    for word in sentence_list:
        if len(word) == length:
            longest_word_list.append(word)
    print("The longest word(s) you used are: ")
    print(*longest_word_list)  # the * gets rid of the brackets on the list when you print


get_input()
