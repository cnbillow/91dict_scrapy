#!/usr/bin
path=$(pwd)
pip3 install -r "$path/requirements.txt"
rm -rf "$path/audio"
rm -rf "$path/pic"
rm -rf "$path/words"
mkdir "$path/audio"
mkdir "$path/pic"
mkdir "$path/words"
python3 "$path/split.py"
python3 "$path/scrapy.py"
python3 "$path/combain.py"
