with open('words_alpha.txt', 'r') as f:
    words = f.read().splitlines()

    

def word_count():
    count = 0
    for w in words:
        count += 1
    print(count)
word_count()

def exactly_5_letters():
    count = 0
    for w in words:
        if len(w) == 5:
            count += 1
    print(count)
exactly_5_letters()

def longer_than_7_letters():
    count = 0
    for w in words:
        if len(w) > 7:
            count += 1
    print(count)
longer_than_7_letters()

def total_number_of_characters():
    count = 0
    for w in words:
        count += len(w)
    print(count)
total_number_of_characters()

def words_without_an_e():
    count = 0
    for w in words:
        if 'e' not in w:
            count += 1
    print(count)
words_without_an_e()

def begin_and_end_with_same_letter():
    count = 0
    for w in words:
        if w[0] == w[-1]:
            count += 1
    print(count)
begin_and_end_with_same_letter()

def exactly_3_as():
    count = 0
    for w in words:
        if w.count('a') == 3:
            count += 1
    print(count)
exactly_3_as()

def qs_not_followed_by_u():
    count = 0
    for w in words:
        if 'q' in w and 'u' in w:
            if w.index('q') != w.index('u')-1:
                count += 1
                
        if 'q' in w and 'u' not in w:
            count += 1
    print(count)
qs_not_followed_by_u()
