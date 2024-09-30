import io


def custom_write(file_name, list):
    file = open(file_name, 'w')
    string_positions = {}
    for i, j in enumerate(list):
        j.encode('utf-8')
        count = (i + 1, file.tell())
        string_positions[count] = j
        file.write(j + '\n')
    file.close()
    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
