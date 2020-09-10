from py_imessage import imessage
from time import sleep

from phone_number import phone_number



def song_in_words(filename):
    text = open(filename)
    words = list()
    for line in text:
        for word in line.split():
            words.append(word)
    return words


def send_words(phone_number, list_words):
    if imessage.check_compatibility(phone_number) == False:
        raise ValueError ('given number not compatible')
    else:
        for message in list_words:
            imessage.send(phone_number, message)
            #sleep(0.5)


phone_number = phone_number

words = song_in_words('text.txt')

send_words(phone_number=phone_number, list_words=words)


