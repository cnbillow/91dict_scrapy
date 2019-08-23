#!usr/bin
pip3 install -r requirements.txt
rm -rf ./audio
rm -rf ./pic
rm -rf ./words
mkdir audio
mkdir pic
mkdir words
python3 split.py
python3 scrapy.py
python3 combain.py