from string import ascii_letters
from copper import Source, Printer, Apply, FSM, mainloop


def match_word(callback):
    word = []
    while 1:
        char = yield
        if char in ascii_letters:
            word.append(char)
        else:
            if word:
                callback(''.join(word))
            word = []


source = Source(iter('hello world 123ddd test'))
source >> FSM(match_word) >> Printer()



mainloop.run(source)
