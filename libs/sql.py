# encoding: utf-8
from .rpn import RPN, Value

class QueryBuilder(RPN):
    ''' SQLクエリ構築クラス '''
    
    @staticmethod
    def _operator(x, y, op, binds):
        ''' クエリ構築基本式
        [column, value, operator]
        => exp: '(column operator ?)', binds: [value]
        '''
        exp = '('
        if x.type == Value.VALUE:
            binds += [x.value]
            exp += '?'
        else:
            exp += x.value
        exp += ' ' + op + ' '
        if y.type == Value.VALUE:
            binds += [y.value]
            exp += '?'
        else:
            exp += y.value
        exp += ')'
        return Value(exp, Value.CHUNK)


    @classmethod
    def query(self, s_exp):
        ''' ポーランド記法のクエリ式からSQLクエリ構築
        params:
            s_exp(dict): ポーランド記法のクエリ {
                '演算子': {'カラム': 値},
                '演算子': [式, ...],
            }
        return:
            query(str): SQLクエリ,
            binds(list): バインディングされた値(list)を取得
        '''
        # binding values
        binds = []

        # SQLクエリ演算子定義
        self.operators = {
            '<': lambda x, y: QueryBuilder._operator(x, y, '<', binds), '<=': lambda x, y: QueryBuilder._operator(x, y, '<=', binds),
            '>': lambda x, y: QueryBuilder._operator(x, y, '>', binds), '>=': lambda x, y: QueryBuilder._operator(x, y, '>=', binds),
            '=': lambda x, y: QueryBuilder._operator(x, y, '=', binds), '!=': lambda x, y: QueryBuilder._operator(x, y, '!=', binds),
            'and': lambda x, y: QueryBuilder._operator(x, y, 'and', binds), 'or': lambda x, y: QueryBuilder._operator(x, y, 'or', binds),
            'like': lambda x, y: QueryBuilder._operator(x, y, 'like', binds)
        }
        
        # クエリ構築
        exp = self.build(s_exp)
        return self.eval(exp)[0].value, binds
