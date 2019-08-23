import requests
import json
import os
import uuid
from lxml import etree
from multiprocessing import Process


class ScrapyProcess(Process):

    def __init__(self, file_name):
        super(ScrapyProcess, self).__init__()
        self.file_name = file_name

    def read_file(self):
        with open(self.file_name + '.txt', 'r', encoding='utf-8') as f:
            for line in f:
                yield line[:-1]

    def download_file(self, url, path):
        res = requests.get(url)
        with open(path, 'wb') as f:
            f.write(res.content)

    def connect_file(self, file_name1, file_name2, file_name3):
        file1 = open(file_name1, 'rb')
        file2 = open(file_name2, 'rb')
        file3 = open(file_name3, 'wb')
        file3.write(file1.read())
        file3.write(file2.read())
        file1.close()
        file2.close()
        file3.flush()
        file3.close()
        os.remove(file_name1)
        os.remove(file_name2)

    def is_in(self, key, dict_list):
        for item in dict_list:
            if key in item.keys():
                return True
        return False

    def scrapy(self, word):
        word_info = {}
        url = 'http://www.91dict.com/words?w=' + word
        res = requests.get(url)
        res.encoding = 'utf-8'
        data = etree.HTML(res.text)
        if data.xpath('/html/body/div[2]/section[2]/div/div/div/div[1]/div[1]/p/text()'):

            # 单词
            word_info['word'] = data.xpath(
                '/html/body/div[2]/section[2]/div/div/div/div[1]/div[1]/p/text()')[0]
            word_info['am_phonetic'] = '//'
            word_info['en_phonetic'] = '//'
            # print(data.xpath("//*[@class='vos']/span[1]/text()"))
            # print(data.xpath("//*[@class='vos']/span[2]/text()"))
            if list(filter(lambda x: x != '\n', data.xpath("//*[@class='vos']/span[1]/text()"))):
                word_info['en_phonetic'] = list(filter(lambda x: x != '\n', data.xpath(
                    "//*[@class='vos']/span[1]/text()")))[0].replace('\n', '')[1:].replace('[', "/").replace(']', '/')
            if list(filter(lambda x: x != '\n', data.xpath("//*[@class='vos']/span[2]/text()"))):
                word_info['am_phonetic'] = list(filter(lambda x: x != '\n', data.xpath(
                    "//*[@class='vos']/span[2]/text()")))[0].replace('\n', '')[1:].replace('[', "/").replace(']', '/')
            # 翻译
            train = []
            for item in filter(lambda x: x != '', map(lambda x: x.replace('\n', ''),
                                                      data.xpath("//*[@class='listBox']/text()"))):
                if len(item.split('. ')) == 1:
                    train.append({'': item.split('. ')[0]})
                elif len(item.split('. ')) == 2 and not item.startswith('=') and not self.is_in(item.split('. ')[0], train):
                    train.append({item.split('. ')[0]: item.split('. ')[1]})
            word_info['tran'] = train

            # 例子
            example = []
            example_len = len(data.xpath(
                "//*[@class='flexslider flexslider_2']/ul/li/div[@class='imgMainbox']"))
            # 例句
            sens = data.xpath("//*[@class='mBottom']")
            # 例句范意思
            sen_trains = data.xpath("//*[@class='mFoot']/text()")
            origins = list(filter(lambda x: x != '\n', data.xpath(
                "//*[@class='mTop']/text()")))
            # 下文内容及翻译
            next_sens = data.xpath(
                "//*[@class='mTextend']/div[2]/div[2]/p[1]/text()")
            next_sen_trains = data.xpath(
                "//*[@class='mTextend']/div[2]/div[2]/p[2]/text()")
            pic_urls = data.xpath(
                "//*[@class='flexslider flexslider_2']/ul/li/div[@class='imgMainbox']/img/@src")
            pron_urls = data.xpath(
                "//*[@class='flexslider flexslider_2']/ul/li/div[@class='imgMainbox']/div/div/audio/@src")
            next_pron_urls = data.xpath("//*[@class='viewdetail']/@href")
            for i in range(example_len):
                sen = etree.tostring(
                    sens[i], encoding='utf-8')[22:-7].decode('utf-8')
                sen_train = sen_trains[i][1:]
                # 图片
                pic_url = './pic/%s-%d.jpg' % (word_info['word'], i)
                pron_url = './audio/%s-%d.mp3' % (word_info['word'], i)
                self.download_file(pic_urls[i], pic_url)
                # 如果句子没有完，需要拼接句子并合成语音
                if not sen.endswith('.') and not sen.endswith(';') and not sen.endswith('?') and not sen.endswith('!'):
                    if sen[-1] != ',':
                        sen += ','
                    sen_train += ','
                    if i < len(next_sens) and i < len(next_sen_trains):
                        # 例句
                        sen += next_sens[i]
                        # 翻译
                        sen_train += next_sen_trains[i]
                        # 语音1
                        pron_url_1 = './audio/%s-%d-1.mp3' % (
                            word_info['word'], i)
                        # 语音2
                        pron_url_2 = './audio/%s-%d-2.mp3' % (
                            word_info['word'], i)
                        temp = requests.get(
                            'http://www.91dict.com' + next_pron_urls[i]).text
                        temp_data = etree.HTML(temp)
                        self.download_file(pron_urls[i], pron_url_1)
                        for li in temp_data.xpath("//*[@class='item']/li"):
                            if li.xpath("./div[@class='mBottom']/text()")[0].replace('\n', '') == next_sens[i]:
                                self.download_file(
                                    li.xpath("./div[@class='mTop']/audio/@src")[0], pron_url_2)
                                break
                        self.connect_file(pron_url_1, pron_url_2, pron_url)
                else:
                    # 直接下载语音
                    self.download_file(pron_urls[i], pron_url)
                example.append({
                    'origin': origins[i][1:-1],
                    "sen": sen,
                    'sen_tran': sen_train,
                    'pic_url': pic_url,
                    'pron_url': pron_url
                })
            word_info['example'] = example
            return word_info

    def main(self):
        for word in self.read_file():
            print(word)
            self.save(self.scrapy(word))

    def save(self, word_info):
        with open(self.file_name + '.json', 'a', encoding='utf-8') as f:
            if word_info:
                json.dump(word_info, fp=f, indent=4, ensure_ascii=False)
                f.write(',\n')

    def run(self):
        self.main()


if __name__ == "__main__":
    for i in range(1, 12):
        p = ScrapyProcess('./words/' + str(i))
        # 启动子进程
        p.start()
