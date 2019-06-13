import sqlite3
from contextlib import closing

with closing(sqlite3.connect('sample.db')) as conn:
    c = conn.cursor()
    c.execute('create table users (id integer primary key, name varchar, age integer, gender varchar)')
    c.executemany('insert into users (name, age, gender) values (?, ?, ?)', [
        ('Alex', 54, 'male'),
        ('Nancy', 40, 'female'),
        ('Tetsu', 16, 'male'),
        ('Saki', 21, 'female')
    ])
    conn.commit()
