import sqlite3 as sq
from prettytable import from_db_cursor
from PIL import Image, ImageDraw, ImageFont


expressions = [('1', '^', 'Збігається з виразом праворуч на початку рядка.\n'
                          'Він відповідає кожному такому екземпляру перед '
                     'кожним \n у рядку.'),
               ('2', '$', 'Збігається з виразом зліва в кінці рядка.\nВін відповідає кожному такому екземпляру перед '
                     'кожним \n у рядку.'),
               ('3', '.', 'Відповідає будь-якому символу,\nокрім обмежувачів рядка, наприклад \n.'),
               ('4', r'\d', 'Екранує спеціальні символи або\nпозначає класи символів.'),
               ('5', 'A|B', 'Відповідає виразу A або B. Якщо A\nзнайдено першим, B залишається невипробованим.'),
               ('6', '+', 'Жадібно відповідає виразу\nліворуч 1 або більше разів.'),
               ('7', '*', 'Жадібно відповідає виразу\nзліва від нього 0 або більше разів.'),
               ('8', '?', 'Жадібно відповідає виразу зліва\nвід нього 0 або 1 раз. Але якщо ? додається\nдо кваліфікаторів '
                     '(+, * і ?), він\nвиконуватиме збіги не жадібно.'),
               ('9', '{m}', 'Збігає вираз зліва від нього\nm разів, і не менше.'),
               ('10', '{m, n}', 'Збігається з виразом зліва\nвід m до n разів, і не менше.'),
               ('11', '{m, n}?', 'Узгоджує вираз зліва від нього\nm разів і ігнорує n. Побачити ? вище.'),
               ('12', '\w', 'Відповідає буквено-цифровим символам,\nщо означають a-z, A-Z і 0-9. Він також\nвідповідає '
                      'символу підкреслення, _'),
               ('13', '\d', 'Збігається з цифрами, що означає 0-9'),
               ('14', '\D', 'Збігається з будь-якими нецифрами'),
               ('15', '\s', r'Збігається з пробілами, які включають символи \t, \n, \r та пробіл'),
               ('16', '\S', 'Відповідає символам без пробілів.'),
               ('17', r'd\b', 'Збігається з межею (або порожнім рядком) на\nпочатку та в кінці слова, тобто між \w та \W.'),
               ('18', '\B', r'Збігається там, де \b не відповідає' + '\n тобто межі символів \w.'),
               ('19', '\A', 'Збігається з виразом праворуч від абсолютного початку\nрядка в однорядковому або багаторядковому режимі.'),
               ('20', '\Z', 'Збігається з виразом ліворуч від абсолютного кінця\nрядка в однорядковому або багаторядковому режимі'),
               ('21', '[]', 'Містить набір символів для відповідності.'),
               ('22', '[a-z]', 'Відповідає будь-якому алфавіту від a до z.'),
               ('23', '[a-z0-9]', 'Відповідає символам від a до z, а також від 0 до 9'),
               ('24', '()', 'Збігається з виразом у дужках і групує його.'),
               ('25', '(? )', 'Всередині таких дужок, ? діє як розширення нотації.\nЙого значення залежить від персонажа,\n'
                        'який знаходиться праворуч від нього.'),
               ]

questions1 = [
    ('Хто розробив Python?', 'Гвідо ван Россум_Бян Страуструп_Альбер Ейнштейн', '0'),
    ('Яка з наступних функцій зробить зі строки список?', 'tuple()_list()_int()', '1'),
    ('Яка типізація даних в Python?', 'динамічна_статична_різна', '1'),
    ('Оберіть правильний синтаксис', 'a=>1_a=3_a<=4', '2'),
    ('На честь кого/чого був назван Python?', 'Змії_Псевдоним розробника_Британське_шоу', '0'),
]

questions2 = [
    ('На яких платформах використовується Python?', 'Linux_Mac_Windows_Raspberry_Pi', '0_1_2_3_4'),
    ('Яка з наступних функцій зробить зі строки список?', 'tuple()_list()_int()', '1'),
    ('Оберіть правильні типи даних в Python', 'double_float_int_char_string', '1_2_4'),
    ('Оберіть оператори циклу в Python', 'for_if_while_dict', '1_2'),
    ('Що являється частиною функції?', 'тіло функції_параметр_аргумент', '0_1_2'),
]


questions3 = [
    ('Яке ключове слово для визначення функції?', 'def'),
    ('За допомогою якого оператора можна зупинити цикл?', 'break'),
    ('За допомогою якого оператора можна зупинити\nпоточну і перейти до наступної ітерації?', 'continue'),
    ('Напишіть назву функції, яка дозволяє переглянути\nнабір коду певну кількість раз в циклі', 'range'),
    ('Який оператор в регулярних виразах відповідає\nбудь-якому симовлу, окрім обмежувачів рядка ', '.'),
]


base = sq.connect('pylearn.db')
cur = base.cursor()


def sql_start():

    if base:
        print('Data base connected OK')
    else:
        print('Data base connection failed')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS expression1(
        id INTEGER PRIMARY KEY,
        number TEXT,
        character TEXT,
        description TEXT)
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS question1(
        id INTEGER PRIMARY KEY,
        name TEXT,
        option TEXT,
        correct TEXT)
    ''')
    cur.execute('DELETE FROM question1;')
    cur.executemany('INSERT INTO question1 (name, option, correct) VALUES (?,?,?)', questions1)

    cur.execute('''
        CREATE TABLE IF NOT EXISTS question2(
        id INTEGER PRIMARY KEY,
        name TEXT,
        option TEXT,
        correct TEXT)
    ''')
    cur.execute('DELETE FROM question2;')
    cur.executemany('INSERT INTO question2 (name, option, correct) VALUES (?,?,?)', questions2)

    cur.execute('''
        CREATE TABLE IF NOT EXISTS question3(
        id INTEGER PRIMARY KEY,
        name TEXT,
        correct TEXT)
    ''')
    cur.execute('DELETE FROM question3;')
    cur.executemany('INSERT INTO question3 (name, correct) VALUES (?,?,?)', questions3)

    base.commit()


async def show_expressions():
    cur.execute("SELECT number, character, description FROM expression1")
    mytable = from_db_cursor(cur)
    print(mytable)
    im = Image.new("RGB", (800, 850), "white")
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("FreeMono.ttf", 15)
    draw.text((5, 5), str(mytable), font=font, fill="black")

    # im.show()
    im.save("table.png", transparancy=0)
    # return mytable.get_string()


async def get_questions1():
    cur.execute("SELECT name, option, correct FROM question1")
    return cur.fetchall()


async def get_questions2():
    cur.execute("SELECT name, option, correct FROM question2")
    return cur.fetchall()


async def get_questions3():
    cur.execute("SELECT name, option, correct FROM question3")
    return cur.fetchall()
