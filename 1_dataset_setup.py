# -*- coding: utf-8 -*-

# timestamp datetime device	numdoc region request urls

import pandas as pd
from urllib.parse import urlparse, parse_qs
from stop_words_remover import remove_stop_words


def csv_dict_reader(file_obj, classificator):
    df = pd.read_csv(file_obj, delimiter='\t', encoding="utf-8").astype(str)
    output = open('./dataset/' + classificator.replace(' ', '_') + '.csv', 'w')
    for line in df['request'].values:
        try:
            query = remove_stop_words(parse_qs(urlparse(line).query)['text'][0]).rstrip().lower()
            output.write(query + ';' + classificator + '\n')
        except: 
            print('no query ¯\_(ツ)_/¯')
    output.close()

if __name__ == '__main__':
    main_output = open('./dataset/dataset_header.csv', 'w')
    main_output.write('query;class\n')
    main_output.close()

    with open('./output/channel.csv') as channel_obj:
        csv_dict_reader(channel_obj, 'поиск канала')

    with open('./output/tv_online.csv') as online_obj:
        csv_dict_reader(online_obj, 'просмотр online')

    with open('./output/tv_serial.csv') as serial_obj:
        csv_dict_reader(serial_obj, 'сериалы')

    with open('./output/tv_programm.csv') as programm_obj:
        csv_dict_reader(programm_obj, 'программа передач')