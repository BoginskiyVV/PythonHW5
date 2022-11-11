# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('compression.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Введите текст для сжатия: '))
with open('compression.txt', 'r') as file:
    compession_text = file.readline()
    text_compression = compession_text.split()
print(f'Тескт для сжатия: {compession_text}')

def recovery(text):
    enconding = ''
    prev_char = ''
    count = 1
    if not text:
        return ''

    for char in text:
        if char != prev_char:
            if prev_char:
                enconding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        enconding += str(count) + prev_char
        return enconding

text_compression = recovery(compession_text)
with open('compression.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{text_compression}')
print(f'Текст в сжатом формате: {text_compression}')