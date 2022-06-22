import sqlite3 as sq
from prettytable import from_db_cursor


expressions = [('^', 'Збігається з виразом праворуч на початку рядка. Він відповідає кожному такому екземпляру перед '
                     'кожним \n у рядку.', '^hello'),
               ('$', 'Збігається з виразом зліва в кінці рядка. Він відповідає кожному такому екземпляру перед '
                     'кожним \n у рядку.', 'world$'),
               ('.', 'Відповідає будь-якому символу, окрім обмежувачів рядка, наприклад \n.', 'he..o'),
               (r'\\d', 'Екранує спеціальні символи або позначає класи символів.', 'example1'),
               ('A|B', 'Відповідає виразу A або B. Якщо A знайдено першим, B залишається невипробованим.', 'example1'),
               ('+', 'Жадібно відповідає виразу ліворуч 1 або більше разів.', 'example1'),
               ('*', 'Жадібно відповідає виразу зліва від нього 0 або більше разів.', 'example1'),
               ('?', 'Жадібно відповідає виразу зліва від нього 0 або 1 раз. Але якщо ? додається до кваліфікаторів '
                     '(+, * і ?), він виконуватиме збіги не жадібно.', 'example1'),
               ('{m}', 'Збігає вираз зліва від нього m разів, і не менше.', 'example1'),
               ('{m, n}', 'Збігається з виразом зліва від m до n разів, і не менше.', 'example1'),
               ('{m, n}?', 'Узгоджує вираз зліва від нього m разів і ігнорує n. Побачити ? вище.', 'example1'),
               ('\w', 'Відповідає буквено-цифровим символам, що означають a-z, A-Z і 0-9. Він також відповідає '
                      'символу підкреслення, _', 'example1'),
               ('\d', 'Збігається з цифрами, що означає 0-9', 'example1'),
               ('\D', 'Збігається з будь-якими нецифрами', 'example1'),
               ('\s', 'Збігається з пробілами, які включають символи \t, \n, \r та пробіл', 'example1'),
               ('\S', 'Відповідає символам без пробілів.', 'example1'),
               (r'd\b', 'Збігається з межею (або порожнім рядком) на початку та в кінці слова, тобто між \w та \W.', 'example1'),
               ('\B', r'Збігається там, де \\b не відповідає, тобто межі символів \w.', 'example1'),
               ('\A', 'Збігається з виразом праворуч від абсолютного початку рядка в однорядковому або багаторядковому режимі.', 'example1'),
               ('\Z', 'Збігається з виразом ліворуч від абсолютного кінця рядка в однорядковому або багаторядковому режимі', 'example1'),
               ('[]', 'Містить набір символів для відповідності.', ''),
               ('[a-z]', 'Відповідає будь-якому алфавіту від a до z.', 'example1'),
               ('[a-z0-9]', 'Відповідає символам від a до z, а також від 0 до 9', 'example1'),
               ('()', 'Збігається з виразом у дужках і групує його.', 'example1'),
               ('(? )', 'Всередині таких дужок, ? діє як розширення нотації. Його значення залежить від персонажа, '
                        'який знаходиться праворуч від нього.', 'example1'),
               ]

base = sq.connect('pylearn.db')
cur = base.cursor()


def sql_start():
    # global base, cur
    # base = sq.connect('pylearn.db')
    # cur = base.cursor()
    if base:
        print('Data base connected OK')
    else:
        print('Data base connection failed')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS expression(
        id INTEGER PRIMARY KEY,
        character TEXT,
        description TEXT,  
        example TEXT)
    ''')
    base.commit()

    cur.execute('DELETE FROM expression;')
    base.commit()

    cur.executemany('INSERT INTO expression (character, description, example) VALUES (?,?,?)', expressions)
    base.commit()

    cur.execute("SELECT * FROM expression;")
    for row in cur.fetchall():
        print(row)


async def show_expressions():
    cur.execute("SELECT character, description, example FROM expression")
    mytable = from_db_cursor(cur)
    print(mytable)
    print(type(mytable))
    return mytable.get_string()
