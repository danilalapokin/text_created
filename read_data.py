def read_data():
    data = dict()
    word_trans = dict()
    next_cnt = dict()
    word_trans['.'] = 0
    text = open('data.txt', 'r')
    rows = 0
    for line in text:
        format_text = line.split()
        if rows == 0:
            for i in range(0, len(format_text), 2):
                word, value = format_text[i], format_text[i + 1]
                word_trans[word] = int(value)
                next_cnt[word] = 0
        else:
            main_word = int(format_text[0])
            data[main_word] = dict()
            next_cnt[main_word] = 0
            for i in range(1, len(format_text), 2):
                next_word = int(format_text[i])
                cnt = int(format_text[i + 1])
                next_cnt[main_word] += cnt
                data[main_word][next_word] = cnt
        rows += 1
    text.close()

    return [data, word_trans, next_cnt]