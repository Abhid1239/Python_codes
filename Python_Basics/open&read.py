Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: /Users/macosx/Documents/PYTHON/listing.py =============
['hello', 'world', '!']
[1, 2, 3]
4.56
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
Traceback (most recent call last):
  File "/Users/macosx/Documents/PYTHON/open.py", line 1, in <module>
    open("python")
FileNotFoundError: [Errno 2] No such file or directory: 'python'
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
>>> 
>>> 
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
>>> 
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============

>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf200
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww19320\viewh11380\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 I need to write something to perform operation fdweith so dam writing as fast as I can to show sup my typing skil;sb this the way I can type can you see itNew fiel}
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf200
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww19320\viewh11380\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 This is \
\
2\
\
\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 I need to write something to perform operation fdweith so d\
am writing as fast as I can to show sup my typing skil;sb this \
the way I can type can you see itNew fiel}
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf200
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww19320\viewh11380\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 This is \
\
2\
\
\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 I need to write something to perform operation fdweith so d\
am writing as fast as I can to show sup my typing skil;sb this \
the way I can type can you see itNew fiel}
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
Traceback (most recent call last):
  File "/Users/macosx/Documents/PYTHON/open.py", line 1, in <module>
    file = open("a.rt", "r")
FileNotFoundError: [Errno 2] No such file or directory: 'a.rt'
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf200
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww19320\viewh11380\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 This is \
\
2\
\
\
I need to write something to perform operation fdweith so d\
am writing as fast as I can to show sup my typing skil;sb this \
the way I can type can you see itNew fiel}
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
import random
import curses

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
t=100
w.timeout(t)

snk_x = sw/4
snk_y = sh/2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh/2, sw/2]
w.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    t +=1000
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
           
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
port curses

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
t=100
w.timeout(t)

snk_x = sw/4
snk_y = sh/2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh/2, sw/2]
w.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    t +=1000
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
           
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
import random
import curses

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw,
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
RE_READING
 0, 0)
w.keypad(1)
t=100
w.timeout(t)

snk_x = sw/4
snk_y = sh/2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
  
finished
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
RE_READING

finished
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
RE_READING

finished
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
RE_READING
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1],
finished
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
RE_READING

finished
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
RE_READING

finished
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
RE_READING

finished
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
RE_READING
556

finished
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
RE_READING
1295

finished
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
RE_READING
1295

finished
[]
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
[]
RE_READING
1295

finished
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
['import random\n', 'import curses\n', '\n', 's = curses.initscr()\n', 'curses.curs_set(0)\n', 'sh, sw = s.getmaxyx()\n', 'w = curses.newwin(sh, sw, 0, 0)\n', 'w.keypad(1)\n', 't=100\n', 'w.timeout(t)\n', '\n', 'snk_x = sw/4\n', 'snk_y = sh/2\n', 'snake = [\n', '    [snk_y, snk_x],\n', '    [snk_y, snk_x-1],\n', '    [snk_y, snk_x-2]\n', ']\n', '\n', 'food = [sh/2, sw/2]\n', 'w.addch(food[0], food[1], curses.ACS_PI)\n', '\n', 'key = curses.KEY_RIGHT\n', '\n', 'while True:\n', '    t +=1000\n', '    next_key = w.getch()\n', '    key = key if next_key == -1 else next_key\n', '\n', '    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:\n', '        curses.endwin()\n', '        quit()\n', '\n', '    new_head = [snake[0][0], snake[0][1]]\n', '\n', '    if key == curses.KEY_DOWN:\n', '        new_head[0] += 1\n', '    if key == curses.KEY_UP:\n', '        new_head[0] -= 1\n', '    if key == curses.KEY_LEFT:\n', '        new_head[1] -= 1\n', '    if key == curses.KEY_RIGHT:\n', '        new_head[1] += 1\n', '\n', '    snake.insert(0, new_head)\n', '\n', '    if snake[0] == food:\n', '        food = None\n', '        while food is None:\n', '           \n', '            nf = [\n', '                random.randint(1, sh-1),\n', '                random.randint(1, sw-1)\n', '            ]\n', '            food = nf if nf not in snake else None\n', '        w.addch(food[0], food[1], curses.ACS_PI)\n', '    else:\n', '        tail = snake.pop()\n', "        w.addch(tail[0], tail[1], ' ')\n", '\n', '    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)\n']
RE_READING
0

finished
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
['import random\n', 'import curses\n', '\n', 's = curses.initscr()\n', 'curses.curs_set(0)\n', 'sh, sw = s.getmaxyx()\n', 'w = curses.newwin(sh, sw, 0, 0)\n', 'w.keypad(1)\n', 't=100\n', 'w.timeout(t)\n', '\n', 'snk_x = sw/4\n', 'snk_y = sh/2\n', 'snake = [\n', '    [snk_y, snk_x],\n', '    [snk_y, snk_x-1],\n', '    [snk_y, snk_x-2]\n', ']\n', '\n', 'food = [sh/2, sw/2]\n', 'w.addch(food[0], food[1], curses.ACS_PI)\n', '\n', 'key = curses.KEY_RIGHT\n', '\n', 'while True:\n', '    t +=1000\n', '    next_key = w.getch()\n', '    key = key if next_key == -1 else next_key\n', '\n', '    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:\n', '        curses.endwin()\n', '        quit()\n', '\n', '    new_head = [snake[0][0], snake[0][1]]\n', '\n', '    if key == curses.KEY_DOWN:\n', '        new_head[0] += 1\n', '    if key == curses.KEY_UP:\n', '        new_head[0] -= 1\n', '    if key == curses.KEY_LEFT:\n', '        new_head[1] -= 1\n', '    if key == curses.KEY_RIGHT:\n', '        new_head[1] += 1\n', '\n', '    snake.insert(0, new_head)\n', '\n', '    if snake[0] == food:\n', '        food = None\n', '        while food is None:\n', '           \n', '            nf = [\n', '                random.randint(1, sh-1),\n', '                random.randint(1, sw-1)\n', '            ]\n', '            food = nf if nf not in snake else None\n', '        w.addch(food[0], food[1], curses.ACS_PI)\n', '    else:\n', '        tail = snake.pop()\n', "        w.addch(tail[0], tail[1], ' ')\n", '\n', '    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)\n']
0

finished
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
['import random\n', 'import curses\n', '\n', 's = curses.initscr()\n', 'curses.curs_set(0)\n', 'sh, sw = s.getmaxyx()\n', 'w = curses.newwin(sh, sw, 0, 0)\n', 'w.keypad(1)\n', 't=100\n', 'w.timeout(t)\n', '\n', 'snk_x = sw/4\n', 'snk_y = sh/2\n', 'snake = [\n', '    [snk_y, snk_x],\n', '    [snk_y, snk_x-1],\n', '    [snk_y, snk_x-2]\n', ']\n', '\n', 'food = [sh/2, sw/2]\n', 'w.addch(food[0], food[1], curses.ACS_PI)\n', '\n', 'key = curses.KEY_RIGHT\n', '\n', 'while True:\n', '    t +=1000\n', '    next_key = w.getch()\n', '    key = key if next_key == -1 else next_key\n', '\n', '    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:\n', '        curses.endwin()\n', '        quit()\n', '\n', '    new_head = [snake[0][0], snake[0][1]]\n', '\n', '    if key == curses.KEY_DOWN:\n', '        new_head[0] += 1\n', '    if key == curses.KEY_UP:\n', '        new_head[0] -= 1\n', '    if key == curses.KEY_LEFT:\n', '        new_head[1] -= 1\n', '    if key == curses.KEY_RIGHT:\n', '        new_head[1] += 1\n', '\n', '    snake.insert(0, new_head)\n', '\n', '    if snake[0] == food:\n', '        food = None\n', '        while food is None:\n', '           \n', '            nf = [\n', '                random.randint(1, sh-1),\n', '                random.randint(1, sw-1)\n', '            ]\n', '            food = nf if nf not in snake else None\n', '        w.addch(food[0], food[1], curses.ACS_PI)\n', '    else:\n', '        tail = snake.pop()\n', "        w.addch(tail[0], tail[1], ' ')\n", '\n', '    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)\n']
0
finished
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
[]
1295
finished
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
['import random\n', 'import curses\n', '\n', 's = curses.initscr()\n', 'curses.curs_set(0)\n', 'sh, sw = s.getmaxyx()\n', 'w = curses.newwin(sh, sw, 0, 0)\n', 'w.keypad(1)\n', 't=100\n', 'w.timeout(t)\n', '\n', 'snk_x = sw/4\n', 'snk_y = sh/2\n', 'snake = [\n', '    [snk_y, snk_x],\n', '    [snk_y, snk_x-1],\n', '    [snk_y, snk_x-2]\n', ']\n', '\n', 'food = [sh/2, sw/2]\n', 'w.addch(food[0], food[1], curses.ACS_PI)\n', '\n', 'key = curses.KEY_RIGHT\n', '\n', 'while True:\n', '    t +=1000\n', '    next_key = w.getch()\n', '    key = key if next_key == -1 else next_key\n', '\n', '    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:\n', '        curses.endwin()\n', '        quit()\n', '\n', '    new_head = [snake[0][0], snake[0][1]]\n', '\n', '    if key == curses.KEY_DOWN:\n', '        new_head[0] += 1\n', '    if key == curses.KEY_UP:\n', '        new_head[0] -= 1\n', '    if key == curses.KEY_LEFT:\n', '        new_head[1] -= 1\n', '    if key == curses.KEY_RIGHT:\n', '        new_head[1] += 1\n', '\n', '    snake.insert(0, new_head)\n', '\n', '    if snake[0] == food:\n', '        food = None\n', '        while food is None:\n', '           \n', '            nf = [\n', '                random.randint(1, sh-1),\n', '                random.randint(1, sw-1)\n', '            ]\n', '            food = nf if nf not in snake else None\n', '        w.addch(food[0], food[1], curses.ACS_PI)\n', '    else:\n', '        tail = snake.pop()\n', "        w.addch(tail[0], tail[1], ' ')\n", '\n', '    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)\n']
0
finished
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
import random

import curses



s = curses.initscr()

curses.curs_set(0)

sh, sw = s.getmaxyx()

w = curses.newwin(sh, sw, 0, 0)

w.keypad(1)

t=100

w.timeout(t)



snk_x = sw/4

snk_y = sh/2

snake = [

    [snk_y, snk_x],

    [snk_y, snk_x-1],

    [snk_y, snk_x-2]

]



food = [sh/2, sw/2]

w.addch(food[0], food[1], curses.ACS_PI)



key = curses.KEY_RIGHT



while True:

    t +=1000

    next_key = w.getch()

    key = key if next_key == -1 else next_key



    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:

        curses.endwin()

        quit()



    new_head = [snake[0][0], snake[0][1]]



    if key == curses.KEY_DOWN:

        new_head[0] += 1

    if key == curses.KEY_UP:

        new_head[0] -= 1

    if key == curses.KEY_LEFT:

        new_head[1] -= 1

    if key == curses.KEY_RIGHT:

        new_head[1] += 1



    snake.insert(0, new_head)



    if snake[0] == food:

        food = None

        while food is None:

           

            nf = [

                random.randint(1, sh-1),

                random.randint(1, sw-1)

            ]

            food = nf if nf not in snake else None

        w.addch(food[0], food[1], curses.ACS_PI)

    else:

        tail = snake.pop()

        w.addch(tail[0], tail[1], ' ')



    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

0
finished
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
['import random\n', 'import curses\n', '\n', 's = curses.initscr()\n', 'curses.curs_set(0)\n', 'sh, sw = s.getmaxyx()\n', 'w = curses.newwin(sh, sw, 0, 0)\n', 'w.keypad(1)\n', 't=100\n', 'w.timeout(t)\n', '\n', 'snk_x = sw/4\n', 'snk_y = sh/2\n', 'snake = [\n', '    [snk_y, snk_x],\n', '    [snk_y, snk_x-1],\n', '    [snk_y, snk_x-2]\n', ']\n', '\n', 'food = [sh/2, sw/2]\n', 'w.addch(food[0], food[1], curses.ACS_PI)\n', '\n', 'key = curses.KEY_RIGHT\n', '\n', 'while True:\n', '    t +=1000\n', '    next_key = w.getch()\n', '    key = key if next_key == -1 else next_key\n', '\n', '    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:\n', '        curses.endwin()\n', '        quit()\n', '\n', '    new_head = [snake[0][0], snake[0][1]]\n', '\n', '    if key == curses.KEY_DOWN:\n', '        new_head[0] += 1\n', '    if key == curses.KEY_UP:\n', '        new_head[0] -= 1\n', '    if key == curses.KEY_LEFT:\n', '        new_head[1] -= 1\n', '    if key == curses.KEY_RIGHT:\n', '        new_head[1] += 1\n', '\n', '    snake.insert(0, new_head)\n', '\n', '    if snake[0] == food:\n', '        food = None\n', '        while food is None:\n', '           \n', '            nf = [\n', '                random.randint(1, sh-1),\n', '                random.randint(1, sw-1)\n', '            ]\n', '            food = nf if nf not in snake else None\n', '        w.addch(food[0], food[1], curses.ACS_PI)\n', '    else:\n', '        tail = snake.pop()\n', "        w.addch(tail[0], tail[1], ' ')\n", '\n', '    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)\n']
['{\\rtf1\\ansi\\ansicpg1252\\cocoartf1671\\cocoasubrtf200\n', '{\\fonttbl\\f0\\fswiss\\fcharset0 Helvetica;}\n', '{\\colortbl;\\red255\\green255\\blue255;}\n', '{\\*\\expandedcolortbl;;}\n', '\\paperw11900\\paperh16840\\margl1440\\margr1440\\vieww19320\\viewh11380\\viewkind0\n', '\\pard\\tx566\\tx1133\\tx1700\\tx2267\\tx2834\\tx3401\\tx3968\\tx4535\\tx5102\\tx5669\\tx6236\\tx6803\\pardirnatural\\partightenfactor0\n', '\n', '\\f0\\fs24 \\cf0 This is \\\n', '\\\n', '2\\\n', '\\\n', '\\\n', 'I need to write something to perform operation fdweith so d\\\n', 'am writing as fast as I can to show sup my typing skil;sb this \\\n', 'the way I can type can you see itNew fiel}']
0
finished
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
['import random\n', 'import curses\n', '\n', 's = curses.initscr()\n', 'curses.curs_set(0)\n', 'sh, sw = s.getmaxyx()\n', 'w = curses.newwin(sh, sw, 0, 0)\n', 'w.keypad(1)\n', 't=100\n', 'w.timeout(t)\n', '\n', 'snk_x = sw/4\n', 'snk_y = sh/2\n', 'snake = [\n', '    [snk_y, snk_x],\n', '    [snk_y, snk_x-1],\n', '    [snk_y, snk_x-2]\n', ']\n', '\n', 'food = [sh/2, sw/2]\n', 'w.addch(food[0], food[1], curses.ACS_PI)\n', '\n', 'key = curses.KEY_RIGHT\n', '\n', 'while True:\n', '    t +=1000\n', '    next_key = w.getch()\n', '    key = key if next_key == -1 else next_key\n', '\n', '    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:\n', '        curses.endwin()\n', '        quit()\n', '\n', '    new_head = [snake[0][0], snake[0][1]]\n', '\n', '    if key == curses.KEY_DOWN:\n', '        new_head[0] += 1\n', '    if key == curses.KEY_UP:\n', '        new_head[0] -= 1\n', '    if key == curses.KEY_LEFT:\n', '        new_head[1] -= 1\n', '    if key == curses.KEY_RIGHT:\n', '        new_head[1] += 1\n', '\n', '    snake.insert(0, new_head)\n', '\n', '    if snake[0] == food:\n', '        food = None\n', '        while food is None:\n', '           \n', '            nf = [\n', '                random.randint(1, sh-1),\n', '                random.randint(1, sw-1)\n', '            ]\n', '            food = nf if nf not in snake else None\n', '        w.addch(food[0], food[1], curses.ACS_PI)\n', '    else:\n', '        tail = snake.pop()\n', "        w.addch(tail[0], tail[1], ' ')\n", '\n', '    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)\n']
15
0
finished
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
['import random\n', 'import curses\n', '\n', 's = curses.initscr()\n', 'curses.curs_set(0)\n', 'sh, sw = s.getmaxyx()\n', 'w = curses.newwin(sh, sw, 0, 0)\n', 'w.keypad(1)\n', 't=100\n', 'w.timeout(t)\n', '\n', 'snk_x = sw/4\n', 'snk_y = sh/2\n', 'snake = [\n', '    [snk_y, snk_x],\n', '    [snk_y, snk_x-1],\n', '    [snk_y, snk_x-2]\n', ']\n', '\n', 'food = [sh/2, sw/2]\n', 'w.addch(food[0], food[1], curses.ACS_PI)\n', '\n', 'key = curses.KEY_RIGHT\n', '\n', 'while True:\n', '    t +=1000\n', '    next_key = w.getch()\n', '    key = key if next_key == -1 else next_key\n', '\n', '    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:\n', '        curses.endwin()\n', '        quit()\n', '\n', '    new_head = [snake[0][0], snake[0][1]]\n', '\n', '    if key == curses.KEY_DOWN:\n', '        new_head[0] += 1\n', '    if key == curses.KEY_UP:\n', '        new_head[0] -= 1\n', '    if key == curses.KEY_LEFT:\n', '        new_head[1] -= 1\n', '    if key == curses.KEY_RIGHT:\n', '        new_head[1] += 1\n', '\n', '    snake.insert(0, new_head)\n', '\n', '    if snake[0] == food:\n', '        food = None\n', '        while food is None:\n', '           \n', '            nf = [\n', '                random.randint(1, sh-1),\n', '                random.randint(1, sw-1)\n', '            ]\n', '            food = nf if nf not in snake else None\n', '        w.addch(food[0], food[1], curses.ACS_PI)\n', '    else:\n', '        tail = snake.pop()\n', "        w.addch(tail[0], tail[1], ' ')\n", '\n', '    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)\n']
0
0
finished
>>> 
============== RESTART: /Users/macosx/Documents/PYTHON/open.py ==============
['import random\n', 'import curses\n', '\n', 's = curses.initscr()\n', 'curses.curs_set(0)\n', 'sh, sw = s.getmaxyx()\n', 'w = curses.newwin(sh, sw, 0, 0)\n', 'w.keypad(1)\n', 't=100\n', 'w.timeout(t)\n', '\n', 'snk_x = sw/4\n', 'snk_y = sh/2\n', 'snake = [\n', '    [snk_y, snk_x],\n', '    [snk_y, snk_x-1],\n', '    [snk_y, snk_x-2]\n', ']\n', '\n', 'food = [sh/2, sw/2]\n', 'w.addch(food[0], food[1], curses.ACS_PI)\n', '\n', 'key = curses.KEY_RIGHT\n', '\n', 'while True:\n', '    t +=1000\n', '    next_key = w.getch()\n', '    key = key if next_key == -1 else next_key\n', '\n', '    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:\n', '        curses.endwin()\n', '        quit()\n', '\n', '    new_head = [snake[0][0], snake[0][1]]\n', '\n', '    if key == curses.KEY_DOWN:\n', '        new_head[0] += 1\n', '    if key == curses.KEY_UP:\n', '        new_head[0] -= 1\n', '    if key == curses.KEY_LEFT:\n', '        new_head[1] -= 1\n', '    if key == curses.KEY_RIGHT:\n', '        new_head[1] += 1\n', '\n', '    snake.insert(0, new_head)\n', '\n', '    if snake[0] == food:\n', '        food = None\n', '        while food is None:\n', '           \n', '            nf = [\n', '                random.randint(1, sh-1),\n', '                random.randint(1, sw-1)\n', '            ]\n', '            food = nf if nf not in snake else None\n', '        w.addch(food[0], food[1], curses.ACS_PI)\n', '    else:\n', '        tail = snake.pop()\n', "        w.addch(tail[0], tail[1], ' ')\n", '\n', '    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)\n']
15
0
finished
>>> 
