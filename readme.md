


$ cat log.csv | grep 'программа передач' | wc -l
     690
$ cat log.csv | grep 'канал' | wc -l
    3141
$ cat log.csv | grep 'text' | wc -l
 1333503

>>> (3141+690)*100 / 1333503 
0.2872884425456861

$ cat ../log.csv | grep 'программа передач' > tv_programm.csv
$ cat ../log.csv | grep 'канал' > channel.csv
$ cat tv_programm.csv channel.csv > tv_dataset.csv