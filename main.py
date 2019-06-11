# 関数の引数の数を取得するためにsignatureをimport
from inspect import signature

def RPN(exp, op):
    ''' 逆ポーランド記法を計算する関数
    params:
        exp list: 逆ポーランド記法プログラムの配列（el. [1, 2, '+'] => 1 + 2）
        op dict: 演算子,変数の定義（el. {'+': (lambda x, y: x + y), 'ten': 10}）
    '''
    stack = []
    for e in exp:
        f = op.get(e)
        if f is None:
            # 演算子でも変数でもない場合はstack
            stack.append(e)
        elif callable(f):
            # 演算子なら演算実行
            argc = len(signature(f).parameters) # 関数の引数の数を取得
            res = f(*stack[-argc:]) # stackの後ろから引数を取得し、関数実行
            stack = stack[:-argc] # 引数分をstackから削除
            if res is not None:
                stack.append(res) # 関数の戻り値をstack
        else:
            # 変数の値をstack
            stack.append(f)
    return stack


if __name__ == "__main__":
    ''' 四則演算用逆ポーランド演算 '''
    # 演算子定義
    operators = {
        '+': (lambda x, y: x + y),
        '-': (lambda x, y: x - y),
        '*': (lambda x, y: x * y),
        '/': (lambda x, y: x / y),
    }
    
    # 組み込み変数定義
    variables = {
        'ten': 10,
        'hundred': 100,
        'pi': 3.14,
    }
    operators.update(variables)
    
    # 計算式定義
    ## 1 2 + 3 * 4 - ten * hundred / pi +
    ## => ((1 + 2) * 3 - 4) * 10 / 100 + 3.14
    expression = [1, 2, '+', 3, '*', 4, '-', 'ten', '*', 'hundred', '/', 'pi', '+']

    # 演算実行
    print(RPN(expression, operators))
