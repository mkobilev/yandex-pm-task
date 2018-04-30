
# timestamp datetime device	numdoc region request urls

import csv
from urllib.parse import urlparse, parse_qs

import sys,os
stderr = sys.stderr
sys.stderr = open(os.devnull, 'w')
import  pandas as pd
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
sys.stderr = stderr
#инициализируем стоп слова и символы
stop = set(stopwords.words('russian'))
stop.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}','#','№'])

def remove_stop_words(query):
    str = ''
    for i in wordpunct_tokenize(query):
        if i not in stop and not i.isdigit():
            str = str + i + ' '
    return str


output = open('./dataset.csv', 'w')

def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter='\t')
    output.write('запрос;класс\n')
    for line in reader:
        try:
            query = remove_stop_words(parse_qs(urlparse(line['request']).query)['text'][0] ).rstrip().lower()
            output.write(query + ';просмотр телевидения\n')
        except: 
            print('no query ¯\_(ツ)_/¯')

if __name__ == '__main__':
    with open('tv_dataset.csv') as f_obj:
        csv_dict_reader(f_obj)
