with open('words_alpha.txt', 'r') as f:
    words = f.read().splitlines()

def ending_letter_s():
    count = 0
    for w in words:
        if w[-1] == 's':
            count += 1
    print(count)
ending_letter_s()

def word_count():
    count = 0
    for w in words:
        count += 1
    print(count)
word_count()



def total_number_of_characters():
    count = 0
    for w in words:
        count += len(w)
    print(count)
total_number_of_characters()
