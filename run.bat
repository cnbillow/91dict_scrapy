pip install -r requirements.txt
del  /Q "audio"
del  /Q "pic"
del  /Q "words"
python split.py
python scrapy.py
python combain.py