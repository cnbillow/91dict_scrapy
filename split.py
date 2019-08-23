def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            yield line


def save(file_name, data):
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(data)
    f.close()


i, j = 0, 0
for line in read_file('allWords.json'):
    if i % 5000 == 0:
        j += 1
        print('第' + str(i) + '次')
    save('./words/' + str(j) + '.txt', line)
    i += 1
