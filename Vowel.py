# Найти и вывести на экран все гласные буквы из введенного с клавиатуры слова

user_input = input('Введите слово или строку: ')

vowel_letters = ['a', 'o', 'u', 'e', 'i']
print([i for i in user_input if i in vowel_letters])
