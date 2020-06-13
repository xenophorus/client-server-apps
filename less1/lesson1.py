import subprocess

import chardet

# Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить
# тип и содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать
# строковые представление в формат Unicode и также проверить тип и содержимое переменных.

# Я не стал использовать переменные, хотя можно и так:
# a, b, c = 'разработка', 'cокет', 'декоратор'

word_array = ['разработка', 'cокет', 'декоратор']

word_array_unc = [
    '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    '\u0063\u043e\u043a\u0435\u0442',
    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
]

for _ in word_array:
    idx = word_array.index(_)
    print(_, type(_))
    print('\t', word_array_unc[idx], type(word_array_unc[idx]))
    print('\t', _ == word_array_unc[idx])

print('\n')
# Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
# последовательность кодов (не используя методы encode и decode) и определить тип, содержимое и
# длину соответствующих переменных.

word_array2 = [b'class', b'function', b'method']

for _ in word_array2:
    print(_, type(_))

print('\n')

# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

'''
b'attribute', b'класс', b'функция', b'type'

Кириллические, потому как не ascii
'''

# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового
# представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).

word_array3 = ['разработка', 'администрирование', 'protocol', 'standard']

for word in word_array3:
    enc_word = word.encode('utf-8')
    print(word, '\n',
          enc_word, '\n',
          enc_word.decode('cp1251'), '\n',
          enc_word.decode('koi8-r'), '\n',
          enc_word.decode('utf-8'))

print('\n')


# Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового
# в строковый тип на кириллице.

def pinger(url):
    args = ['ping', url]
    subprocess_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subprocess_ping.stdout:
        codepage = chardet.detect(line).get('encoding')
        print(line.decode(codepage))  # не уверен, что стоит оределять кодировку для каждой строки


sites = ['google.com', 'yandex.ru', 'youtube.com']

for url in sites:
    pinger(url)

# Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое.

word_array4 = ['сетевое программирование', 'сокет', 'декоратор']

with open('test_file.txt', 'w') as fl:
    for elem in word_array4:
        fl.write(elem + '\n')

with open('test_file.txt', 'r') as fl:
    a = fl.read()
    print(chardet.detect(a.encode()))

with open('test_file.txt', 'r', encoding='utf-8') as fl:
    for line in fl:
        print(line.strip())



'''
Как я понял, когда мы кодируем строку в ascii через str.encode('ascii', 'replace'),
если при переборе символов встречается неизвестный (не-ascii) символ, то он заменяется вопросом.
Если же мы сначала кодируем строку в юникодовую последовательность, то получаем по 2 байта 
на один не-ascii символ. То есть кириллическая 'а' кодируется как b'\xd0\xb0'. Латиница, в противовес, 
не кодируется (либо кодируется иначе - глубоко не ковырял).
То есть вот так 
a = b'\x50\x79\x74\x68\x6f\x6e'     
print(a.decode('ascii', 'replace'))
мы получим 'Python'. 
Если мы добавим число больше \x7f, мы получим вопрос - это верхний предел ascii, но 
не предел для однобайтовых таблиц символов. 
Если выше \xff - это уже два байта, это уже юникод, и с точки зрения ascii это два 
символа. Потому в 4-м примере получаем два вопроса. 

In[78]:  handl_str = 'Testování'

In[79]:  handl_str_utf8 = handl_str.encode('utf-8')

In[80]:  handl_str_utf8_str = handl_str_utf8.decode('ascii', 'replace')

In[81]:  print(handl_str_utf8_str)
Out[81]:  Testov''n'' 

'''
