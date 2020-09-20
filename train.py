import re, read_data, write_data

data, word_trans, next_cnt = {}, {}, {}

def get_trans(word):
    if not word_trans.get(word) != None:
        word_trans[word] = len(word_trans)
    return word_trans[word]

def read_file(name):
    text = open(name, 'r')
    format_text = ''
    for line in text:
        for char in line:
            if char == '.':
                format_text += ' '

            if re.match(r'[А-Я]', char):
                char.lower();
            if re.match(r'[а-я.]', char) or re.match(' ', char):
                format_text += char
            else:
                format_text += ' '

            if char == '.':
                format_text += ' '
        format_text += ' . '
    text.close()
    format_text = format_text.split()

    for i in range(len(format_text) - 1):
        if format_text[i] == '.':
            continue
        num_left = get_trans(format_text[i])
        num_right = get_trans(format_text[i + 1])
        if not data.get(num_left):
            data[num_left] = dict()
        if not data[num_left].get(num_right):
            data[num_left][num_right] = 0
        data[num_left][num_right] += 1

name_texts = []
text = open("input.txt")
for line in text:
    name_texts.append(line)
text.close

prefix = 'texts/'
for name in name_texts:
    read_file(prefix + name[0:len(name) - 1])
write_data.print_data(data, word_trans)
print("Changes saves")