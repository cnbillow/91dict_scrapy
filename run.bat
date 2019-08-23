pip install -r requirements.txt
del  /Q "audio"
del  /Q "pic"
del  /Q "words"
mkdir "audio"
mkdir "pic"
mkdir "words"
python split.py
python scrapy.py
python combain.py