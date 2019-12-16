import datetime

d = datetime.datetime.now() 
YEAR = d.strftime('%Y')
MONTH = d.strftime('%m')
DAY = d.strftime('%d')


def main():
    title = input("Masukkan judul pos (dengan strip sebagai spasi): ")
    f = open(f'{YEAR}-{MONTH}-{DAY}-{title}.md', "w+")
    f.close()


if __name__ == "__main__":
    main()
