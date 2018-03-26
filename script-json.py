import chardet
import json


def get_json_data(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        s = data.decode(encoding=result['encoding'])
    return json.loads(s)


def print_top_ten(filename):
    data = get_json_data(filename)
    word_list = []
    for item in data['rss']['channel']['items']:
        word_list += item['description'].split(' ')
    short_list = [word.lower() for word in word_list if len(word) >= 6]
    frequency_of_words = dict()
    for word in short_list:
        if word not in frequency_of_words:
            frequency_of_words[word] = 1
        else:
            frequency_of_words[word] += 1
    items = [(v, k) for k, v in frequency_of_words.items()]
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
    top_ten = sorted_items[:10]
    print('топ 10 самых часто встречающихся в новостях слов длиннее 6 символов в файле {}:'.format(filename))
    for k, v in top_ten:
        print('\t{0} - {1} раз'.format(v, k))


print_top_ten('newsafr.json')
print('\n')
print_top_ten('newscy.json')
print('\n')
print_top_ten('newsfr.json')
print('\n')
print_top_ten('newsit.json')
