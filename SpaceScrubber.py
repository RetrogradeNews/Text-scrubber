import sys

def scrub(text):
    clean = ""
    for c in text:
        if ord(c)== 160: # If it's that fucking nobreak space character
            c = ' '     # Set it to be a normal fucking space
        clean += c
    return clean

if __name__ == "__main__":
    file = sys.argv[1]
    with open(file, 'r', encoding='utf-8') as text:
        file_content = text.read()
    cleanText = scrub(file_content)
    with open(file, "w", encoding='utf-8') as cleanFile:
        cleanFile.write(cleanText)
