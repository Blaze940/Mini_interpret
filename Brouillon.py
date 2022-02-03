# -----------------------------------------------------------------------------
# calc.py
#
# Expressions arithmétiques sans variables
# -----------------------------------------------------------------------------
from genereTreeGraphviz2 import printTreeGraph

reserved = {
    'print' : 'PRINT'
    #print en minuscule reconnu dans calc
}
tokens = [
    'NUMBER','MINUS',
    'PLUS','TIMES','DIVIDE',
    'LPAREN','RPAREN', 'AND', 'OR','TRUE','FALSE', 'SEMICOLON','NAME','AFFECT', 'INFTO', 'SUPTO','SAME'
    ] + list(reserved.values())
# Tokens
t_SEMICOLON = r'\;'
t_PLUS    = r'\+'
t_MINUS   = r'\-'
t_AND     = r'\&'
t_OR      = r'\|'
t_TIMES   = r'\*'
t_DIVIDE  = r'\/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_TRUE    = r'T'
t_FALSE   = r'F'
t_AFFECT  = r'='
t_INFTO   = r'\<'
t_SUPTO   = r'\>'
t_SAME    = r'=='
names = {}
tup = (('*', ('+', 1, 2),3))

def t_NAME(t):
    r'_[a-zA-Z_0-9]+ | [a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'NAME')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()

precedence = (
    ('left', 'AND'),
    ('left', 'OR'),
    ('nonassoc', 'INFTO', 'SUPTO', 'AFFECT'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    #('right','UMINUS'),
    )

def p_start(p):
    'START : BLOC'
    p[0] = ('START',p[1])
    print('Arbre de dérivation = ',p[0])
    printTreeGraph(p[0])
    evalInst(p[1])

def p_bloc(p):
    ''' BLOC : BLOC statement SEMICOLON
           | statement SEMICOLON '''
    if len(p) == 4 :
        p[0] = ('bloc',p[1], p[2])
    else:
        p[0] = ('bloc',p[1], 'empty')

def p_statement_print(p):
    'statement : PRINT LPAREN expression RPAREN'
    p[0] = ('print', p[3])

def p_statement_affect(p):
    'statement : NAME AFFECT expression '
    p[0] = ('assign', p[1], p[3])

def p_expression_binop_plus(p):
    'expression : expression PLUS expression'
    p[0] = ('+', p[1], p[3])

def p_expression_binop_times(p):
    'expression : expression TIMES expression'
    p[0] = ('*', p[1], p[3])

def p_expression_binop_divide_and_minus(p):
    '''expression : expression MINUS expression
				| expression DIVIDE expression'''
    if p[2] == '-': p[0] = ('-', p[1], p[3])
    else : p[0] = ('/', p[1], p[3])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_name(p):
    'expression : NAME'
    p[0] = p[1]

def p_expressionTrue(p) :
    'expression : TRUE'
    p[0] = True

def p_expressionFalse(p) :
    'expression : FALSE'
    p[0] = False

def p_expression_binop_boop(p) :
    '''expression : expression AND expression
                | expression OR expression'''
    if p[2] == '&':
        p[0] = ('Expr', p[1], '&', p[3])
    elif p[2] == '|':
        p[0] = ('Expr', p[1], '|', p[3])

def p_expression_inequal(p) :
    '''expression : expression INFTO expression
                    | expression SUPTO expression '''
    if p[2] == '<':
        p[0] = ('<',p[1],p[3])
    elif p[2] == '>':
        p[0] = ('>',p[1],p[3])

def p_error(p):
    print("Syntax error at '%s'" % p.value)

def evalInst(t) :
    print(' evalInst de ', t)
    if t == 'empty': return
    elif t[0] == 'bloc':
        evalInst(t[1])
        evalInst(t[2])
    elif t[0] == 'assign':
        names[t[1]] = eval(t[2])
    elif t[0] == 'print':
        print('Calc >>',eval(t[1]))


def eval(t) : #evalExpre
    print(' eval de ', t)
    if type(t) is int:
        return t
    if type(t) is str:
        return names[t]
    if type(t) is tuple:
        if t[0] == '+':
            return eval(t[1]) + eval(t[2])
        elif t[0] == '-':
            return eval(t[1]) - eval(t[2])
        elif t[0] == '*' :
            return eval(t[1]) * eval(t[2])
        elif t[0] == '/':
            return eval(t[1]) / eval(t[2])
        elif t[0] == '&':
            return eval(t[1]) & eval(t[2])
        elif t[0] == '|':
            return eval(t[1]) | eval(t[2])
        elif t[0] == '<':
            return eval(t[1]) < eval(t[2])
        elif t[0] == '>':
            return eval(t[1]) > eval(t[2])
        elif t[0] == '==':
            return eval(t[1]) == eval(t[2])



import ply.yacc as yacc
yacc.yacc()
s = ' a=2 ; print(a) ; '
#s = input('calc > ')
#s = ' eval(tup) ; '
yacc.parse(s)

