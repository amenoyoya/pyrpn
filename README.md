# Pythonで逆ポーランド記法の計算

## Environments
- Python `3.6.7`

***

## Usage

### Execution
```bash
python main.py
```

### Spec
- function `RPN`:
  - params:
    - `expressions`(list):
      - 逆ポーランド記法で記述された式をリストにしたもの
      ```python
      # 例: (1 + 2) * 3 - 4
      ## => 1 2 + 3 * 4 -
      expressions = [1, 2, '+', 3, '*', 4, '-']
      ```
    - `operators`(dict):
      - 組み込み変数, 演算子の定義
      ```python
      # 例: 四則演算の演算子
      operators = {
        '+': (lambda x, y: x + y),
        '-': (lambda x, y: x - y),
        '*': (lambda x, y: x * y),
        '/': (lambda x, y: x / y),
      }
      ```
  - returns:
    - 計算結果のリスト
