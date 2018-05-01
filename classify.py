import sys,os
import numpy as np
import pandas as pd
import argparse
from keras.models import load_model
from keras.preprocessing.text import Tokenizer

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
stderr = sys.stderr
sys.stderr = open(os.devnull, 'w')

from stop_words_remover import remove_stop_words


classes = {
    'поиск канала': 0,
    'программа передач': 1,
    'просмотр online': 2,
    'сериалы': 3,
    'остальные': 4,
}

model = load_model('classifier.h5')


def predict(str_query, numwords):
    tokenizer = Tokenizer(num_words=numwords)
    X_raw_test = [str_query]
    df = pd.read_csv('./dataset/cleaned_dataset.csv', delimiter=';', encoding="utf-8").astype(str)
    X_raw = df['query'].values
    tokenizer.fit_on_texts(X_raw)
    x_test = tokenizer.texts_to_matrix(X_raw_test, mode='binary')
    prediction = model.predict(np.array(x_test))
    class_num = np.argmax(prediction[0])
    sys.stderr = stderr
    for name, index in classes.items():
        if index == class_num:
            print(name)


parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('query', type=str, help="a query to classify")
args = parser.parse_args()
query = remove_stop_words(args.query)

predict(query, 1000)