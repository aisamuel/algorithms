import sys
import re
import os
WORD_RE = re.compile('\w+')

index = {}

file_path = os.getcwd() + '\dictionary\zen_of_python.txt'
with open(file_path, encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])