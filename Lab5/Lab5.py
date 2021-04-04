import re
def main():
    gif = 0
    png = 0
    jpeg = 0
    jpg = 0
    with open("access.log.txt", 'r') as fstream:
        ip = "41.202.74.145"
        for line in fstream:
            line = line.rstrip('\n')
            if re.match(ip, line) is not None:
                if re.search(".gif", line) is not None:
                    gif = gif + 1
                elif re.search(".png", line) is not None:
                    png = png + 1
                elif re.search(".jpeg", line) is not None:
                    jpeg = jpeg + 1
                elif re.search(".jpg", line) is not None:
                    jpg = jpg + 1
    print(f"Found for {ip} adress\nGIF: {gif}\nPNG:{png}\nJPEG: {jpeg}\nJPG: {jpg}")


if __name__ == "__main__":
    main()
