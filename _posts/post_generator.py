from datetime import datetime


def main():
    d = datetime.now()
    YR = d.strftime("%Y"); MH = d.strftime("%m"); DY = d.strftime("%d")

    TL = input("Masukkan judul pos dengan dash '-' sebagai pemisah: ")
    f = open(f'{YR}-{MH}-{DY}-{TL}.markdown', 'w+')

    f.write("---\ntitle: {}".format(TL))
    f.write("\nlayout: post\nauthor: \"Adhiansyah Ancha\"\ncategories: blog\n---\n")
    f.close()


if __name__ == "__main__":
    main()
