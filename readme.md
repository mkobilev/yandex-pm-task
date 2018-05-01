#### Забиваем микроскопом гвозди

log.csv - директорией выше  
Anaconda / Python 3.6 


Смотрим общее количество запросов  
```bash
$ cat ../log.csv | grep 'text' | wc -l  
    1333503
```

Запросы, содержащие 'программа передач'
```bash
$ cat ../log.csv | grep 'программа передач' | wc -l
    690
```

Запросы, содержащие 'канал'
```bash
$ cat ../log.csv | grep 'канал' | wc -l
    3141
```

Ну очень приблеженно выберите запросы, связанные с просмотром телевидения составляют 3ю часть всех запросов
```python
(3141+690)*100 / 1333503 
0.2872884425456861
```


#### Попробуем добить чуть мозгов

Ставим зависимости
```bash
$ pip install -r requirements.txt
```
mkdir output 
mkdit dataset

Создаем датасет
```bash
$ cat ../log.csv | grep 'программа передач' > output/tv_programm.csv
$ cat ../log.csv | grep 'канал' > output/tv_channel.csv  
$ cat ../log.csv | grep 'смотреть онлайн' > output/tv_online.csv
$ cat ../log.csv | grep 'сериал' > output/tv_serial.csv
$ head -n 1 ../log.csv > output/tv_dataset.csv

$ cat output/tv_programm.csv output/channel.csv output/tv_online.csv output/tv_serial.csv >> output/tv_dataset.csv
```

```bash
$ cat dataset/dataset_header.csv dataset/поиск_канала.csv dataset/программа_передач.csv dataset/просмотр_online.csv dataset/сериалы.csv > dataset/cleaned_dataset.csv
```

  
Приводим запросы в порядок
```bash
$ pyhton 1_dataset_setup.py
```

