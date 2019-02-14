import urllib.request
import string

url = urllib.request.urlopen("https://www.apple.com/")
html = url.read()
decoded = html.decode("utf8")
decoded = decoded.lower()

remove_punctuation = str.maketrans(string.punctuation, ' '*len(string.punctuation))
words1 = decoded.translate(remove_punctuation)
words1 = words1.split()

original_file = open('original_file', 'r')

dict3 = dict()

for aline2 in original_file:
    key, value = aline2.strip().split(':')
    dict3[key.strip()] = value.strip()

original_file.close()

original_file1 = open('original_file', 'a')

for key, value in dict3.items():
    value = int(value)
    if key != 'RUN':
        dict3[key] = 0
    else:
        dict3[key] = value

for word in words1:
    for key, value in dict3.items():
        if key == word and key != "RUN":
            dict3[key] = dict3[key] + 1

if 'abc123' not in words1:
    dict3['RUN'] = value + 1

for key, value in dict3.items():
    original_file1.write(str(key))
    original_file1.write(": ")
    original_file1.write(str(value))
    original_file1.write("\n")

original_file1.close()
