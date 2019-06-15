# encoding: utf-8
from libs.sql import QueryBuilder
import sqlite3
from contextlib import closing

# ポーランド記法でSQLクエリ定義
## (or (and (< id 3) (= gender "male")) (= gender "female"))
## => id 3 < gender "male" = and gender "female" = or
## => ((id < 3) and (gender = "male")) or (gender = "female")
## => ((id < ?) and (gender = ?)) or (gender = ?), [3, "male", "female"]
query, binds = QueryBuilder.query({
    'or': {
        'and': {
            '<': {'id': 3},
            '=': {'gender': 'male'},
        },
        '=': {'gender': 'female'},
    },
})

print(query, binds)

# sqlite3実行
with closing(sqlite3.connect('sql/sample.db')) as conn:
    c = conn.cursor()
    c.execute('select * from users where ' + query, binds)
    print(c.fetchall())
