# Pythonで逆ポーランド記法の計算

## Environments
- Python `3.6.7`

***

## Usage

### Execution
```bash
# 四則演算
python main.py

# SQLクエリビルダー
python sqlquery.py
```

---

### Spec

####  function: eval_rpn
- params:
    - `expressions`(list):
        - 逆ポーランド記法で記述された式をリストにしたもの
            - `Value(値, Value.VALUE)`
            - `Value(変数名, Value.CHUNK)`
            - `function 演算子`
        ```python
        # 例: 四則演算の演算子
        operators = {
            '+': lambda x, y: Value(x.value + y.value),
            '-': lambda x, y: Value(x.value - y.value),
            '*': lambda x, y: Value(x.value * y.value),
            '/': lambda x, y: Value(x.value / y.value),
        }
        # 例: (1 + 2) * 3 - 4
        ## => 1 2 + 3 * 4 -
        expressions = [
            Value(1), Value(2), operators['+'],
            Value(3), operators['*'], Value(4), operators['-']
        ]
        ```
- returns:
    - 計算結果のリスト
