from datetime import datetime

d = datetime.now()
YEAR = d.strftime('%Y')
MONTH = d.strftime("%m")
DAY = d.strftime('%d')
title = input("Masukkan judulnya (dengan dash '-' sebagai pemisah): ")

f = open(f'{YEAR}-{MONTH}-{DAY}-{title}.markdown', 'w+')
f.close
