def print_data(data, word_trans):
    f = open('data.txt', 'w')
    for key, value in word_trans.items():
        f.write(key + ' ' + str(value) + ' ')
    f.write('\n')
    for key, value in data.items():
        f.write(str(key) + ' ')
        for word, cnt in value.items():
            f.write(str(word) + ' ' + str(cnt) + ' ');
        f.write('\n')
    f.close()