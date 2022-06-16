from aiogram.utils.emoji import emojize
from dotenv import load_dotenv
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / '.env')

# Token
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Settings Commands
COMMAND_START = 'Головне меню'
COMMAND_HELP = 'Довідка'
COMMAND_CONTENT = 'Уроки'
COMMAND_AUTHOR = 'Про автора'

# Messages
MESSAGE_GREETINGS_PRIVATE = "Вітаю в Learn.py!\nВчи Python разом з нами"
MESSAGE_HELP = "Бот призначений для ознайомлення з мовою програмування Python.\nЗавжди з вами."
MESSAGE_UNKNOWN = 'Натисність /start щоб побачити голвне меню'

# Selected
SELECTED = 'Selected: \n'

# Main Menu ReplyKeyboard
KEY_BUTTON_CONTENT = emojize(':page_with_curl:') + ' Уроки'
KEY_BUTTON_AUTHOR = emojize(':bust_in_silhouette:') + ' Про автора'
KEY_BUTTON_FUNCTION = emojize(':bust_in_silhouette:') + ' FUNCTION'

# Author
ABOUT_AUTHOR = 'Бот був створений студенткою курсу ІС-1-3М\nЖидко Анною'

# Content
CONTENT_LIST = emojize(':books:') + '*Оберіть урок:*'
CONTENT_WHY_PYTHON = 'Чому Python?'
CONTENT_WHAT_PYTHON = 'Що таке Python?'
CONTENT_INVENTOR = 'Ким був розроблений Python?'
CONTENT_DATA_TYPES = 'Типи даних'
CONTENT_IF_ELSE = 'Умовні оператори'
CONTENT_FOR_LOOP = 'Цикл FOR '
CONTENT_WHILE_LOOP = 'Цикл WHILE'
CONTENT_FUNCTIONS = 'Функції'

CONTENT_WHY_PYTHON_PHOTO = 'https://miro.medium.com/max/1400/1*FbpL8alBr_6RoCB-4PhfnQ.png'
CONTENT_WHAT_PYTHON_PHOTO = 'http://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/09/What-is-Python.jpg'
CONTENT_INVENTOR_PHOTO = 'https://i.ytimg.com/vi/qxMcGDnT8uc/maxresdefault.jpg'
CONTENT_DATA_TYPES_PHOTO = 'https://miro.medium.com/max/944/1*LU3NY_x5x8oKC8sBvapTZg.png'
CONTENT_IF_ELSE_PHOTO = 'https://miro.medium.com/max/1400/1*WGjI2Ru_MUbvs_5-qgBPzg.png'
CONTENT_FOR_LOOP_PHOTO = 'https://cdn.techbeamers.com/wp-content/uploads/2018/08/Python-for-loop-syntax-and-examples.png'
CONTENT_WHILE_LOOP_PHOTO = 'https://cdn.techbeamers.com/wp-content/uploads/2018/08/Python-while-loop-syntax-and-examples.png'
CONTENT_FUNCTIONS_PHOTO = 'http://www.trytoprogram.com/images/python_functions.jpg'

CONTENT_WHY_PYTHON_FIRST = '- Python працює на різних платформах (Windows, Mac, Linux, Raspberry Pi тощо).\n\n' \
                           '- Python має простий синтаксис, схожий на англійську мову.\n\n- Python має синтаксис, ' \
                           'який дозволяє розробникам писати програми з меншою кількістю рядків, ніж деякі інші мови програмування.'
CONTENT_WHAT_PYTHON_FIRST = '_Python_ (найчастіше вживане прочитання — «Па́йтон», запозичено назву з ' \
                            'британського шоу Монті Пайтон) — інтерпретована об\'єктно-орієнтована мова програмування ' \
                            'високого рівня зі строгою динамічною типізацією.\n\nСтруктури даних високого рівня разом із ' \
                            'динамічною семантикою та динамічним зв\'язуванням роблять її привабливою для швидкої ' \
                            'розробки програм, а також як засіб поєднування наявних компонентів. '
CONTENT_INVENTOR_FIRST = 'Розробка мови Python була розпочата в кінці 1980-х років співробітником голландського інституту ' \
                         'CWI _Гвідо ван Россумом_.\n\nДля розподіленої ОС Amoeba потрібна була розширювана скриптова мова, ' \
                         'і Гвідо почав писати Python на дозвіллі, запозичивши деякі напрацювання для мови ABC ' \
                         '(Гвідо брав участь у розробці цієї мови, орієнтованої на навчання програмування).'
CONTENT_DATA_TYPES_FIRST = 'Python підтримує динамічну типізацію, тобто тип змінної лише під час виконання.\n\n' \
                           'З базових типів слід зазначити підтримку цілих чисел довільної довжини та комплексних чисел.\n\n' \
                           'Python має багату бібліотеку для роботи з рядками, зокрема, кодованими в юнікоді.\n\nЗ Python ' \
                           'підтримується колекція (кортежи _tuple()_ ), списки _list()_ (масиви), словники _dict()_ (асоціативні масиви) і від ' \
                           'версії 2.4, множини _set()_.\n\nСистема класів підтримує множину успадкування та метапрограмування.\n\n' \
                           'Будь-який тип, включаючи базові, входити до системи класів, і за потреби можливе успадкування ' \
                           'навіть від базових типів.'
CONTENT_IF_ELSE_FIRST = 'Python підтримує звичайні логічні умови з математики:\n\nДорівнює: _a == b_\nНе дорівнює: _a != b_' \
                        '\nМенше ніж: _a < b_\nМенше або дорівнює: _a <= b_\nБільше за: _a > b_\nБільше або дорівнює: _a >= b_' \
                        '\n\nЦі умови можна використовувати кількома способами, найчастіше в операторах if і циклах.\n\n' \
                        'Оператор «if» записується за допомогою ключового слова if.'
CONTENT_FOR_LOOP_FIRST = '_Цикл for_ використовується для ітерації послідовності (це або список, кортеж, словник, набір ' \
                         'або рядок).\n\nЦе менш схоже на ключове слово for в інших мовах програмування, а більше схоже на ' \
                         'метод ітератора, як і в інших об’єктно-орієнтованих мовах програмування.\n\nЗа допомогою циклу ' \
                         'for ми можемо виконати набір операторів один раз для кожного елемента списку, кортежу, набору ' \
                         'тощо.\n\nЩоб переглянути набір коду певну кількість разів, ми можемо використовувати функцію range().'
CONTENT_WHILE_lOOP_FIRST = 'За допомогою _циклу while_ ми можемо виконати набір операторів, якщо умова є істинною.\n\n' \
                           'Примітка: не забудьте збільшити i, інакше цикл триватиме вічно.\n\n' \
                           'Цикл while вимагає, щоб відповідні змінні були готові, у цьому прикладі нам потрібно ' \
                           'визначити змінну індексації, i, для якої ми встановлюємо 1.\n\n' \
                           'За допомогою оператора break ми можемо зупинити цикл, навіть якщо умова while істинна\n\n' \
                           'За допомогою оператора continue ми можемо зупинити поточну ітерацію та перейти до наступної' \
                           '\n\nЗа допомогою оператора else ми можемо запустити блок коду один раз, коли умова більше не відповідає дійсності'
CONTENT_FUNCTIONS_FIRST = '_Функція_ — це блок коду, який виконується лише тоді, коли вона викликається.\n\nВи можете ' \
                          'передавати дані, відомі як параметри, у функцію.У результаті функція може повертати дані.\n\n' \
                          'У Python функція визначається за допомогою ключового слова _def_.\n\n' \
                          'Щоб викликати функцію, скористайтеся назвою функції з дужками:\n\n' \
                          ' _def myFunction():\n    print("Hello from a function")_\n_myFunction() _'

CONTENT_WHY_PYTHON_SECOND = '- Python працює на системі інтерпретатора, що означає, що код можна виконати, ' \
                            'щойно він буде написаний. Це означає, що створення прототипу може бути дуже швидким.\n\n' \
                            '- Python можна обробляти процедурним, об’єктно-орієнтованим або функціональним способом.'
CONTENT_WHAT_PYTHON_SECOND = 'Python підтримує модулі та пакети модулів, що сприяє модульності та повторному ' \
                             'використанню коду.\n\nІнтерпретатор Python та стандартні бібліотеки доступні як у ' \
                             'скомпільованій, так і у вихідній формі на всіх основних платформах.\n\nВ мові програмування ' \
                             'Python підтримується кілька парадигм програмування, зокрема: об\'єктно-орієнтована, ' \
                             'процедурна, функціональна та аспектно-орієнтована.'
CONTENT_INVENTOR_SECOND = 'У лютому 1991 року Гвідо опублікував вихідний текст в групі новин alt.sources.\n\n' \
                          'Мова почала вільно поширюватися через Інтернет і сподобалася іншим програмістам.\n\n' \
                          'З 1991 року Python є цілком об\'єктно-орієнтованим.\n\nPython також запозичив багато рис ' \
                          'таких мов, як C, C++, Modula-3 і Icon, й окремі риси функціонального програмування з Ліспу.'
CONTENT_IF_ELSE_SECOND = 'Ключове слово elif — це спосіб мови Python, щоб сказати «якщо попередні умови були невірними, ' \
                         'спробуйте цю умову». Ключове слово else ловить все, що не вловлюється попередніми умовами.\n\n' \
                         'Якщо у вас є лише один оператор для виконання, ви можете розмістити його в одному рядку з ' \
                         'оператором if\n_if a > b: print("a is greater than b")_\n\nЯкщо у вас є лише один оператор для ' \
                         'виконання, один для if і один для else, ви можете помістити все це в один рядок:\n_print("A") if a > b else print("B")_\n\n' \
                         'Ви також можете мати кілька операторів else в одному рядку:\n_print("A") if a > b else print("=") if a == b else print("B")_'
CONTENT_FOR_lOOP_SECOND = 'Функція _range()_ повертає послідовність чисел, починаючи з 0 за замовчуванням і збільшується ' \
                          'на 1 (за замовчуванням) і закінчується вказаним числом.\n\nЗа допомогою оператора break ми можемо ' \
                          'зупинити цикл до того, як він перегляне всі елементи.\n\n' \
                          'За допомогою оператора continue ми можемо зупинити поточну ітерацію циклу та продовжити наступну.'
CONTENT_FUNCTIONS_SECOND = 'Інформація може передаватися у функції як аргументи.\n\nАргументи вказуються після імені ' \
                           'функції в дужках.\n\nВи можете додати скільки завгодно аргументів, просто відокремте їх комою.\n\n' \
                           'У наступному прикладі є функція з одним аргументом (fname).\n\nКоли функція викликається, ' \
                           'ми передаємо ім’я, яке використовується всередині функції для друку повного імені:\n\n' \
                           '_def myFunction(fname):\n    print(fname + " Refsnes")_\n_myFunction("Email")_\n\nЗ точки зору функції:\n\n' \
                           '_Параметр_ — це змінна, зазначена в дужках у визначенні функції.\n\n' \
                           '_Аргумент_ — це значення, яке надсилається функції під час її виклику. '


# Navigate buttons
NEXT_BUTTON = emojize(':arrow_forward:')
BACK_BUTTON = emojize(':arrow_backward:')

# CLOSE BUTTON
CLOSE_BUTTON = emojize(':heavy_multiplication_x:') + 'Close'

# WENT WRONG
FAILED_SORRY = emojize(':heavy_exclamation_mark:') + ' Sorry. Something went wrong. Try later.'


# THROTTLING MESSAGES
THROTTLING_EXCEEDED_LIMIT = 'Exceeded the limit of messages to user, try again later.'
THROTTLING_UNBLOCKED = 'Unblocked.'


