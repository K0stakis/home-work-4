# 1) Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів, які містять дві голосні літери підряд.
print("first task:")
import re

while True:
    user_input = input('Write a proposal: ')
    if user_input.isdigit():
        print("No need to write numbers here! ")
    else:
        break

def count_words_with_double_vowels(text):
    pattern = r'\b\w*[aeiou]{2}\w*\b'
    matches = re.findall(pattern, text, re.IGNORECASE)
    return len(matches)
word_count = count_words_with_double_vowels(user_input)

print(f"Number of words with two consecutive vowels: {word_count}")
# 2) Є два довільних числа які відповідають за мінімальну і максимальну ціну. Є Dict з назвами магазинів і цінами: { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}. Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон між мінімальною і максимальною ціною. 
print("second task:")

dict = { "cito": 47.999, "BB_studio": 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}
min = 40
for dict_key, dict_value in dict.items():
    if dict_value < min:
        min = dict_value

max = 45
        
for dict_key, dict_value in dict.items():
    if dict_value > max:
        max = dict_value      

for dict_key, dict_value in dict.items():
    if min < dict_value < max :
        print(dict_key)