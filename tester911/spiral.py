import re

text = ''
with open('text.txt', 'r') as inf:
    for line in inf:
        a = re.findall("\w\d+", line)
        text += line
        for i in a:
            print(i)
            text.replace('a3', 'u5')

# with open('text.txt', 'w') as ouf:
#     ouf.write(text)


print(text)