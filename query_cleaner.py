
# timestamp datetime device	numdoc region request urls

import csv
from urllib.parse import urlparse, parse_qs

output = open('out.txt', 'w')

def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter='\t')
    for line in reader:
        try:
            # output.write(urlparse(line['request']).query + '\n')
            output.write( parse_qs(urlparse(line['request']).query)['text'][0] + '\n')
        except: 
            print('no query ¯\_(ツ)_/¯')

if __name__ == '__main__':
    with open('../log.csv') as f_obj:
        csv_dict_reader(f_obj)
