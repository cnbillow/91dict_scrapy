# 91dict_scrapy
基于Python requests的人人词典数据爬虫，爬取站点http://www.91dict.com  

爬取内容包含：单词、单词词性及翻译、单词发音、单词例句剧照、单词例句及翻译、单词例句发音  
总共数据： 单词53189个，例句发音文件及图片文件共10G左右，20M带宽不到一个小时就能爬完，我测试是这样的。。。  
关于单词发音，可自行添加爬取

爬取内容1  
![maze](https://github.com/RickyHal/91dict_scrapy/blob/master/result_demo/爬取内容1.png)    

爬取内容2  
![maze](https://github.com/RickyHal/91dict_scrapy/blob/master/result_demo/爬取内容2.png)    

例句发音  
![maze](https://github.com/RickyHal/91dict_scrapy/blob/master/result_demo/%E4%BE%8B%E5%8F%A5%E5%8F%91%E9%9F%B3.png)    

例句剧照  
![maze](https://github.com/RickyHal/91dict_scrapy/blob/master/result_demo/%E4%BE%8B%E5%8F%A5%E5%89%A7%E7%85%A7.png)    

# Python版本
Python3+ ,建议Python3.6
# requirements.txt
requests==2.21.0  
lxml==4.3.3  

# 运行方式
clone 后windows运行run.bat,linux运行run.sh

# 目录结构
  #### |---------------------------------------------------------------------------------------------------------------------
  #### |--audio   单词音频文件，项目中为部分文件，仅供查看  
  #### |--pic    单词图片文件，项目中为部分文件，仅供查看  
  #### |--words    拆分的原始单词数据，每个文件5000个单词，爬虫为每个文件创建一个进程来爬取  
  #### |--result_demo   单词数据结果demo,非完整数据  
  #### |--allWords.json    所有的单词，一行一个单词，共53189个单词，爬虫根据此爬取单词数据  
  #### |--combain.py   合并最后的结果，即合并words目录下的json文件  
  #### |--requirements.txt   Python依赖模块  
  #### |--run.bat    Windows启动脚本  
  #### |--run.sh   Linux启动脚本  
  #### |--scrapy.py     爬虫脚本  
  #### |--split.py   拆分原始单词数据，及allWords.json文件中的单词  
  #### |----------------------------------------------------------------------------------------------------------------------
# 单词数据demo
```
{
    //单词
    "word": "sir",
    //美式发音
    "am_phonetic": "/sɝ/",
    //英式发音
    "en_phonetic": "/sɜː/",
    #词性及翻译
    "tran": [
        {
            "n": "先生；（用于姓名前）爵士；阁下；（中小学生对男教师的称呼）先生；老师"
        }
    ],
    #例句
    "example": [
        {
            //例句出处
            "origin": "来自《一位年轻医生的笔记 第1季 第2集》",
            //例句，如果例句结尾符号不是.;?!，会在结尾加上逗号拼接下文
            "sen": "It was me, <em>sir</em> and no one else, <em>sir</em>.",
            //例句翻译，同上也会拼接
            "sen_tran": "我一个人喝掉了 医生",
            //例句图片
            "pic_url": "./pic/sir-0.jpg",
            //例句发音文件地址，如果例句结尾符号不是.;?!， 会拼接两个句子的语音文件，合成为一个
            "pron_url": "./audio/sir-0.mp3"
        },
        {
            "origin": "来自《拆弹部队》",
            "sen": "No, <em>sir</em>, <em>sir</em>, that's sergeant James. He's right here.",
            "sen_tran": "不 长官 是詹姆斯中士 他就在那里",
            "pic_url": "./pic/sir-1.jpg",
            "pron_url": "./audio/sir-1.mp3"
        },
        {
            "origin": "来自《雷斯特雷波》",
            "sen": "<em>Sir</em>. How you doing, <em>sir</em>? Good to see you again.",
            "sen_tran": "长官 还好吗 很高兴再见到您",
            "pic_url": "./pic/sir-2.jpg",
            "pron_url": "./audio/sir-2.mp3"
        },
        {
            "origin": "来自《太空堡垒卡拉狄加 第4季 第12集》",
            "sen": "Yes, <em>sir</em>. I'm sorry, <em>sir</em>, but what can I do?",
            "sen_tran": "是 长官 我很抱歉 可我能怎么办？",
            "pic_url": "./pic/sir-3.jpg",
            "pron_url": "./audio/sir-3.mp3"
        },
        {
            "origin": "来自《太空堡垒卡拉狄加 第2季 第12集》",
            "sen": "Don't worry, <em>sir</em>. I'll take it real slow, <em>sir</em>.",
            "sen_tran": "别担心 长官 我们会慢慢来的 长官!",
            "pic_url": "./pic/sir-4.jpg",
            "pron_url": "./audio/sir-4.mp3"
        },
        {
            "origin": "来自《耶鲁大学开放课程：欧洲文明》",
            "sen": "And he replied, <em>Sir</em>, I pedal so quickly,they'll never catch me.",
            "sen_tran": "他回答道 先生 我踩踏板很快,他们永远也追不上我",
            "pic_url": "./pic/sir-5.jpg",
            "pron_url": "./audio/sir-5.mp3"
        }
    ]
}
```
##### 代码很烂，请见谅
