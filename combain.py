#!/usr / bin / env python3
def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            yield line


def save(file_name, data):
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(data)
    f.close()


for i in range(1, 12):
    print('当前:' + str(i))
    for line in read_file('./words/' + str(i) + '.json'):
        save('单词数据.json', line)
