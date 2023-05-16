"""
# hangman 게임
- 단어의 각 글자 자리에 짧은 선이 그려진다.
- 글자 1개를 맞추면 글자가 표시되고, 추가로 계속 맞추면 글자가 표시된다.
- 틀리면 기회가 1번 줄어든다.
- 전체 글자를 입력하여 맞추면 프로그램 바로 종료됨
"""
import random

words = ['dog', 'cat', 'monkey', 'chicken', 'frog', 'horse']
lives_remaining = 10  # 남은 기회(전역 변수)
guessed_letter = ''

def pick_a_word():
    word = random.choice(words)
    return word

def get_guess(word):
    print_word_with_blanks(word)
    print('Lives Remaining:' + str(lives_remaining))
    guess = input("Guess a letter or whole word?")
    return guess


def print_word_with_blanks(word):
    #print("아직 구현되지 않음")
    display_word = ''
    for letter in word:
        if gues\sed_letters.find(letter) > -1:
            display_word += letter
        else:
            display_word += '-'
    print(display_word)

def process_guess(guess, word):
    global lives_remaining #전역변수화
    global gussed
    lives_remaining -= 1
    gussed_letters += guess
    if guess  == word:
        return True
    return False

def play():
    word = pick_a_word()
    while True:
        guess = get_guess(word)
        if process_guess(guess, word):
            print("You win! Well done")
            break
        if lives_remaining == 0:
            print("You are Hung")
            print("The word was:" + word)
            break

play()