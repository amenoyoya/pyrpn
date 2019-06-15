# Pythonで逆ポーランド記法の計算

## Environments
- Python `3.6.7`

***

## Usage

### Execution
```bash
# 四則演算サンプル
python main.py

# カスタム四則演算
python calc.py

# SQLクエリビルダー
python query.py
```

---

### Spec

####  class: Value /libs/rpn.py
- description: データを保持するクラス
- members:
    - `value`(any): データの実体
    - `type`(int): データ型
        - `Value.VALUE`: 通常値
        - `Value.CHUNK`: 変数 or 式
- methods:
    - `__init__`
        - params:
            - `value`(any): 保持させるデータ
            - `_type`(int): データ型（`Value.VALUE` | `Value.CHUNK`）

#### class: Variable /lib/rpn.py
- description: Valueの継承クラス｜変数名を保持する
    - 変数名として`a-z, A-Z, 0-9, '_', '.'`のみ受け付ける
- methods:
    - `__init__`
        - params:
            - `variable_name`(str): 変数名

####  class: RPN /libs/rpn.py
- description: 逆ポーランド記法を処理するクラス
- static methods:
    - `processor`
        - 逆ポーランド記法処理系を定義するためのデコレータ
            ```python
            # 簡単な四則演算の処理系
            @RPN.processor
            def calc(element):
                # 演算子として処理したいものは関数としてスタックする
                if element == '+':
                    return lambda x, y: x + y
                if element == '-':
                    return lambda x, y: x - y
                if element == '*':
                    return lambda x, y: x * y
                if element == '/':
                    return lambda x, y: x / y
                # 演算子以外はそのままスタック
                return element
            
            # => calc関数がRPN処理系に書き換わる
            ''' function calc(exp)
            params:
                exp(list): 逆ポーランド記法の配列
            return:
                result(list): 処理結果の配列
            '''
            
            # ((1 + 2) * 3 - 4) / 5 => 1.0
            ## [1, 2, '+', 3, '*', 4, '-', 5, '/']
            print(calc([1, 2, '+', 3, '*', 4, '-', 5, '/']))
            
            # => [1.0]
            ```
    - `explain`
        - `RPN.build`メソッドで構築された逆ポーランド記法配列をprint可能な形式に変換
        - params:
            - `exp`(list): Value, function 等を含む逆ポーランド記法配列
        - return:
            - `exp`(list): print可能な形式に変換された逆ポーランド記法配列
- class methods:
    - `eval`
        - `RPN.operators`で定義された演算子に基づいて逆ポーランド記法を処理
        - example: `main.py`参照
        - params:
            - `exp`(list): 逆ポーランド記法プログラムの配列
                - el: `[1, 2, '+'] <= 1 + 2`
            - `variables`(dict): 組み込み変数
                - el: {'TEN': 10, 'ZERO': 0}
        - return:
            - `result`(list): 処理結果のValue配列
    - `build`
        - ポーランド記法 => 逆ポーランド記法 に変換
        - example: `calc.py`参照
        - params:
            - `s_exp`(dict): ポーランド記法
                ```python
                {
                    '演算子': [引数, ...],
                    '演算子': {'変数': 値}
                }
                ```
        - return:
            - `result`(list): 逆ポーランド記法のValue配列

---

### SQL QueryBuilder

#### class: QueryBuilder /libs/sql.py
- description: ポーランド記法で記述されたクエリからSQLクエリを構築する
- class methods:
    - `query`
        - ポーランド記法のクエリ式からSQLクエリ構築
        - example: `query.py`参照
        - params:
            - `s_exp`(dict): ポーランド記法のクエリ
        - return:
            - `query`(str): SQLクエリ,
            - `binds`(list): バインディングされた値(list)を取得
        