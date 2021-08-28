# rem
# <hangman>
import requests
import bs4

def hangman():
    req_text = requests.get(f'https://randomword.com/').text
    soup = bs4.BeautifulSoup(req_text, 'html.parser')
    word = soup.find('div', id = 'random_word').text
    definition = soup.find('div', id = 'random_word_definition').text
    return word, definition 


def game():
    word, definition = hangman()
    len_word = len(word)
    print(len_word)
    _ = '_'*len_word
    print(definition)
    print(_)
    while '_' in _:    
        letter = input('Type a letter: ').lower()
        if len(letter) > 1:
            if letter == word:
                break
            else:
                print('Type one word at a time or the whole word')            
            continue
        if letter in word:
            print(f'{letter} is in the word !')
            x = 0
            y = word.replace(letter, '_')
            for item in y:
                if item == '_':
                    list2 = list(_)
                    list2[x] = letter
                    _ = ''.join(list2)
                x += 1       
            print(_)
        else:
            print(f"'{letter}' not in word :(")
    print(f'Congratulations !\nGame Over!\nThe word was {word}')
# </hangman>

# <jumbledWords>   
import random
def random_words():
    req_text = requests.get('http://www.yougowords.com/5-letters').text
    soup = bs4.BeautifulSoup(req_text, 'html.parser')
    letter_5 = [str(x.text).lower() for x in soup.find_all('a') if len(x.text) == 5][4:]
    return random.choice(letter_5)

word = random_words()
list1 = [x for x in word]
random.shuffle(list1)
_ = '-' * len(word)
print(''.join(list1))
print(_)
while True:
    item = input('Guess: ')
    if len(item) == 5:
        if item == word:
            print(f'{item.capitalize()} is right !')
            break
        else:
            print('Wrong !')
    else:
        print('The number of letters is five.')
# </jumbledWords> 






