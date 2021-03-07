# Press Shift+F10 to execute it or replace it with your code.
# Vigenere cipher
import string
from typing import List, Any, Union

input = "The Avengers could be considered as a Lee and Kirby's renovation of a previous superhero team, All-Winners Squad, who appeared in comic books series published by Marvel Comics' predecessor Timely Comics. A rotating roster became a hallmark of the series, although one theme remained consistent: the Avengers fight the foes no single superhero can withstand. The team, famous for its battle cry of Avengers Assemble!, has featured humans, superhumans, mutants, Inhumans, deities, androids, aliens, legendary beings, and even former villains."
print(len(input))
frequency_letters = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
                     0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
                     0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
                     0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

def filter_text(input_string):
    txt = []

    for char in input_string:
        if char.islower():
            txt.append(char)
        elif char.isupper():
            txt.append(char.lower())
    return "".join(txt)


def encryption(input_string, key):
    cipher_text = []
    number_string = []
    number_key = []
    number_of_keys = len(key)
    integer = 0

    start = ord("a")
    for char in input_string:
        x = ord(char) - start
        number_string.append(x)
        integer = integer + 1
    for integer in range(len(key)):
        result = ord(key[integer]) - start
        number_key.append(result)
    for integer in range(len(input_string)):
        result = (number_string[integer] + number_key[integer % number_of_keys])
        result %= 26
        result += 65
        result = chr(result)
        cipher_text.append(result)
    return "".join(cipher_text)


def decryption(cipher_text, key):
    original_string = []
    number_string = []
    number_key = []
    number_of_keys = len(key)
    integer = 0
    start1 = ord('A')
    start2 = ord('a')
    for char in cipher_text:
        x = ord(char) - start1
        number_string.append(x)
        integer = integer + 1

    for integer in range(len(key)):
        result = ord(key[integer]) - start2
        number_key.append(result)

    for integer in range(len(cipher_text)):
        result = (number_string[integer] - number_key[integer % number_of_keys] + 26)
        result %= 26
        result += 65
        result = chr(result)
        original_string.append(result)
    return "".join(original_string)


def get_index(cipher_text):
    n = float(len(cipher_text))
    frequency_sum = 0.0
    for char in input:
        frequency_sum += cipher_text.count(char) * (cipher_text.count(char) - 1)
    # using the IC formula
    index_of_coincidence = frequency_sum / (n * (n - 1))
    return index_of_coincidence


def key_length(cipher_text):
    ic_numbers = []

    for guess in range(0, 20):
        ic_sum = 0.0
        avg_ic = 0.0
        for i in range(guess):
            sequence = ""
            # split text into sequence
            for j in range(0, len(cipher_text[i:]), guess):
                sequence += cipher_text[i + j]
            ic_sum += get_index(sequence)
        if not guess == 0:
            avg_ic = ic_sum / guess
        ic_numbers.append(avg_ic)  # stored all indexes of coincidence
    # returns the most likely probability of key length
    probability_key_first = ic_numbers.index(sorted(ic_numbers, reverse=True)[0])
    probability_key_second = ic_numbers.index(sorted(ic_numbers, reverse=True)[1])
    # print(probability_key_second)
    # print(probability_key_first)
    # cmmdc
    if probability_key_first % probability_key_second == 0:
        return probability_key_second
    else:
        return probability_key_first


# i  need the frequency for guessing the key
# for probabilstic distribution
def frequency(statement):
    total = [0] * 26
    for i in range(26):
        sum = 0.0
        statement_offset = [chr(((ord(statement[j]) - 97 - i) % 26) + 97) for j in range(len(statement))]
        v = [0] * 26
        # vector frecv care cauta nr in ASCII
        for letter in statement:
            v[ord(letter) - ord('A')] += 1

        # impart vectorul de frecv pentru a obtine procentajele
        for j in range(26):
            v[j] *= (1.0 / float(len(statement)))
        # compar cu frecventele in engleza
        for j in range(26):
            sum += ((v[j] - float(frequency_letters[j])) ** 2) / float(frequency_letters[j])
        total[i] = sum
    shifting = total.index(min(total))

    return (shifting + 97)


def key_guess(cipher_text, key_l):
    key = ''
    # trebuie calculat frecv fiecarei litere din cheie
    nr=-1
    for i in range(0, key_l):
        statement = ''
        nr+=1
        for j in range(0, len(cipher_text[i:]), key_l):
            statement += cipher_text[i + j]
        key += chr(frequency(statement)+nr)
    return key


key = "abababac"
print(input)
print(key)
decr=key
print(filter_text(input))
x = filter_text(input)
cipher = encryption(x, key)
key_l = key_length(cipher)
key_decr = key_guess(cipher, key_l)

print(encryption(x, key))
print(decryption(cipher, key))
key_l = key_length(cipher)
print(key_l)
print(decr)
