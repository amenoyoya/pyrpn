# encoding: utf-8

# 関数の引数の数を取得するためにsignatureをimport
from inspect import signature
import re

class Variable:
    ''' 変数名として使える文字列か判定するクラス '''
    class NameError(Exception):
        def __str__(self):
            return 'Invalid character specified for variable name.'
    
    # 変数名には[アルファベット, 数字, _, .]のみ使用可能
    pattern = re.compile(r'^[a-zA-Z0-9_\.]+$')
    
    def __init__(self, variable_name):
        if Variable.pattern.match(variable_name) is None:
            raise Variable.NameError()
        self.name = variable_name
    
    def __str__(self):
        return self.name


class Value:
    ''' 値クラス '''
    VALUE = 0 # 値
    CHUNK = 1 # 遅延評価式

    def __init__(self, value, _type=VALUE):
        self.value = value
        self.type = _type


def RPN(prestack):
    ''' 逆ポーランド記法計算関数を生成するデコレータ '''
    def wrapper(exp, *args, **kwargs):
        ''' 逆ポーランド記法を計算する関数
        params:
            exp list: 逆ポーランド記法プログラムの配列
                el: [Value(1), Value(2), (lambda x, y: x.value + y.value)] => 1 + 2
        '''
        
        # stackから引数をとって関数をcallする関数
        def call(func, stack):
            argc = len(signature(func).parameters) # 関数の引数の数を取得
            res = func(*stack[-argc:]) # stackの後ろから引数を取得し、関数実行
            del stack[-argc:] # 引数分をstackから削除
            if res is not None:
                stack.append(res) # 関数の戻り値をstack
        
        stack = []
        for e in exp:
            if callable(e):
                # 関数なら関数実行
                call(e, stack)
            else:
                # stack前処理の結果をstack
                res = prestack(e, *args, **kwargs)
                if res is not None:
                    if callable(res):
                        # stack前処理が関数を返したら関数実行
                        call(res, stack)
                    else:
                        stack.append(res)
        return stack
    return wrapper


@RPN
def eval_rpn(e):
    ''' stack前処理を行わない単純なRPN処理系
    example:
        # 1 + 2
        eval_rpn([Value(1), Value(2), (lambda x, y: Value(x.value + y.value))])
    '''
    return e


@RPN
def eval_rpn_variable(e, operators):
    ''' 演算子と組み込み変数を自動判定するRPN処理系
    example:
        # 1 + 2
        eval_rpn(
            [1, 2, '+'], # RPN式
            {'+': lambda x, y: x + y} # 演算子, 組み込み変数
        )
    '''
    f = operators.get(e)
    if f is not None:
        return f
    return e
