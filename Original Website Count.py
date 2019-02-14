import urllib.request
import string

url = urllib.request.urlopen("https://www.apple.com/")
html = url.read()
decoded = html.decode("utf8")
decoded = decoded.lower()

remove_punctuation = str.maketrans(string.punctuation, ' '*len(string.punctuation))  #Look for string.punctuation and replace it with a space depending on how many punctuation marks there are
words = decoded.translate(remove_punctuation)
words = words.split()

main_word = "sales"

index = words.index(main_word)
left = words[index - 5:index]
right = words[index + 1:index + 6]

count_file = open('original_file', 'w')

dict = {main_word: 0}

for index1 in left:
    dict[index1] = 0

for index2 in right:
    dict[index2] = 0

for word in words:
    for key, value in dict.items():
        if key == word:
            dict[key] = dict[key] + 1

for key, value in dict.items():
    key.strip(',')
    count_file.write(str(key))
    count_file.write(": ")
    count_file.write(str(value))
    count_file.write("\n")

dict2 ={"RUN": 1}

for key, value in dict2.items():
    count_file.write(str(key))
    count_file.write(": ")
    count_file.write(str(value))
    count_file.write("\n")

count_file.close()

