# -----------------------------------------------------------------------------
# calc.py
#
# Expressions arithmétiques sans variables
# -----------------------------------------------------------------------------
from genereTreeGraphviz2 import printTreeGraph

reserved = {
    'print': 'PRINT',
    'if': 'IF',
    'while': 'WHILE',
    'else': 'ELSE',
    'for': 'FOR',
    'printString': 'PRINTSTR',
    'fonction': 'FONCTION'
    #print en minuscule reconnu dans calc
}
#Lexique pour grammaire
tokens = [
    'NUMBER','MINUS',
    'PLUS','TIMES','DIVIDE',
    'LPAREN','RPAREN', 'AND', 'OR','TRUE','FALSE', 'SEMICOLON','NAME','AFFECT', 'INFTO', 'SUPTO','SAME','LACOL','RACOL','STR'
    ] + list(reserved.values())
# Tokens (ce qui est marqué sur la console )
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
t_LACOL   = r'\{'
t_RACOL   = r'\}'
# t_DBQUOTE = r'\"'
names = {} #Stocke le nom des variables et a pour clefs, les valeurs des vriables
functions = {} #Stocke le nom des functions , et a pour valeur, le tuple des parametres et le corps de la fonction

def t_NAME(t):
    r'_[a-zA-Z_0-9]+ | [a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'NAME')
    return t

def t_STR(t):
    r' "[a-z A-Z0-9:_]+" '
    t.type = reserved.get(t.value,'STR')
    return t

"toto"
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
    'statement : PRINT LPAREN expression RPAREN '
    p[0] = ('print', p[3])

def p_statement_fonction_void_spm(p):
    'statement : FONCTION NAME LPAREN RPAREN LACOL BLOC RACOL'
    p[0] = ('function','empty',p[2], p[6])
    #A refaire

def p_statement_Call_fonction_void_spm(p):
    'statement : NAME LPAREN RPAREN'
    p[0] = ('call',p[1])

def p_statement_printString(p):
    'statement : PRINTSTR LPAREN STR RPAREN '
    p[0] = ('printString', p[3])

def p_statement_while(p):
    'statement : WHILE LPAREN expression RPAREN LACOL BLOC RACOL '
    p[0] = ('while', p[3], p[6])

def p_statement_if(p):
    ''' statement : IF LPAREN expression RPAREN LACOL BLOC RACOL
    | IF LPAREN expression RPAREN LACOL BLOC RACOL ELSE LACOL BLOC RACOL '''
    if len(p) == 8:
        p[0] = ('if', p[3], p[6])
    else:
        p[0] = ('if', p[3], p[6], 'else', p[10])

def p_statement_for(p):
    ''' statement : FOR LPAREN statement SEMICOLON expression SEMICOLON statement RPAREN LACOL BLOC RACOL '''
    p[0] = ('for', p[3], p[5], p[7], p[10])

def p_statement_affect(p):
    '''statement : NAME AFFECT expression
                | NAME PLUS PLUS
                | NAME PLUS AFFECT expression
    '''
    if len(p) == 5 :
        p[0] = ('incr', p[1],p[4])
    else :
        if p[2] == '=' :
            p[0] = ('assign', p[1], p[3])
        elif (p[2] == '+') and (p[3] == '+') :
            p[0] = ('plus_one', p[1], 1)

def p_expression_binop_plus(p):
    'expression : expression PLUS expression'
    p[0] = ('+', p[1], p[3])

def p_expression_binop_times(p):
    'expression : expression TIMES expression'
    p[0] = ('*', p[1], p[3])

def p_expression_same(p):
    'expression : expression SAME expression'
    p[0] = ('==', p[1], p[3])

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

def evalInst(t) :
    print(' evalInst de ', t)
    if t == 'empty': return
    elif t[0] == 'bloc':
        evalInst(t[1])
        evalInst(t[2])
    elif t[0] == 'function':
        functions[t[2]] = t[3]
    elif t[0] == 'call':
        f = functions[t[1]]
        evalInst(f)
    elif t[0] == 'assign':
        names[t[1]] = eval(t[2])
    elif t[0] == 'incr':
        names[t[1]] = names[t[1]]+eval(t[2])
    elif t[0] == 'plus_one':
        names[t[1]] = names[t[1]]+1
    elif t[0] == 'print':
        print('SORTIE >>',eval(t[1]))
    elif t[0] == 'printString':
        print('SORTIE >>',t[1][1:-1])
    elif t[0] == 'if':
        if len(t) == 3:
            if eval(t[1]):
                evalInst(t[2])
        elif len(t) == 5:
            if eval(t[1]):
                evalInst(t[2])
            else:
                evalInst(t[4])
    elif t[0] == 'while':
        while eval(t[1]):
            evalInst(t[2])
    elif t[0] == 'for':
        evalInst(t[1])
        while eval(t[2]):
            evalInst(t[4])
            evalInst(t[3])


import ply.yacc as yacc
yacc.yacc()
# s = 'f0 = 0; f1 = 1 ; i = 0 ; while(i<10){ fs = f0+f1 ; print(fs) ; f0 = f1 ; f1 = fs; i = i+1 ; } ;' #FIBONACCI
# s = ' if(1){ print(10) ; printString("Mr BAUDOIN") ;};' #IF + printString
# s = input('calc > ')
s = 'fonction test(){print(1+1); printString("Reussi");}; test();'
#s = 'fonction test(){print(1+1); printString("Reussi");}; test(); fonction poutine(){printString("Explosion");}; poutine() ;'

#BONUS
# s = ' for(x=0 ; x<20 ; x+=5) { print(x); } ; ' #x+=
# s = ' for(x=0 ; x<5 ; x++) { print(x); } ; ' #x++
yacc.parse(s)