import ply.lex as lex
import ply.yacc as yacc

#Tokens almacenados del LP
tokens = (
  'num',
  'suma',
  'resta',
  'multiplicacion',
  'division',
  'leftpar',
  'rightpar',
  'leftsquare',
  'rightsquare',
  'keyleft',
  'keyright',
  'id',
  'op',
  'dec',
  'val',
  'ch',
  'float',
  'txt',
  'igualdad',
  'cc', #string
  'mayorsimbol',
  'menorsimbol',
  'menorigual',
  'mayorigual',
  'sv',
  'miss',
  'si',
  'contra',
  'contrasi',
  'lr',
  'mst',
  'start',
  'rec',
  'diferencia',
  'retorno',
  'coma',
  'exit',
  'ride'
)

t_op= r'op' # int
t_dec= r'dec' #double
t_val= r'val' 
t_ch= r'ch' #char
t_float= r'float'
t_sv= r'sv' #void
t_retorno=r'rt'#return
t_suma = r'\+'
t_resta = r'-'
t_division = r'/'
t_multiplicacion = r'\*'
t_coma = r','
t_diferencia=r'\=i\='
t_mst=r'mst'#cout
t_lr=r'lr'
t_start=r'start'
t_exit='exit'
t_ride='ride'
t_miss=r'miss'
t_si='si'
t_contra='contra'
t_contrasi='contra si'
t_leftpar = r'\('
t_rightpar = r'\)'
t_leftsquare = r'\['
t_rightsquare = r'\]'
t_keyleft = r'\{'
t_keyright = r'\}'
t_igualdad = r'\='
t_mayorsimbol=r'\>'
t_menorsimbol=r'\<'
t_menorigual=r'\<='
t_mayorigual=r'\>='

def t_num(t):
    r'[+-]?([1-9]\d*(\.\d*[1-9])?|0\.\d*[1-9]+)|\d+(\.\d*[1-9])?'
    t.value = float(t.value)    
    return t

def t_error(t):
	print ("    ¡Caracter ilegal identificado!'%s'" % t.value[0])
	t.lexer.skip(1)
    
def t_id(t):
    r'[+][a-zA-Z0-9]*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_txt(t):
    r'-x[^\n]*' # Comentario de una línea que comienza con "-x" y termina con el final de línea
    t.lexer.lineno += t.value.count('\n') # Aumenta el número de línea si hay saltos de línea en el comentario
    return t
    
def t_cc(t):
    r'[\'][a-zA-Z0-9@+(){}¿?¡! ]+[\']'
    return t

t_ignore  = ' \t'

print ("\nErrores encontrados:")
def camb(cadena):
    listi=[]
    fp = open("funcion1.txt")
    cadena = fp.read()
    fp.close()
    lexer=lex.lex()
    lexer.input(cadena)
    while True:
     tok = lexer.token()
     if not tok: 
         break      
     listi.append(tok)
    return listi


lexer = lex.lex()
fp = open("funcion1.txt")
cadena = fp.read()
fp.close()
lexer.input(cadena)
cadena3=[]
cadena2=[]
while True:
 tok = lexer.token()
 if not tok: 
     break    
 cadena3.append(tok)
 cadena2.append(tok.type)

print ("\n                            ANALIZADOR LÉXICO\n")
print ("                                 (TOKENS)\n")
class All_tokens:
    def __init__(self, type, lexeme, line, column):
        self.type = type
        self.lexeme = lexeme
        self.line = line
        self.column = column
      
def show_tokens(lexer):
    tokens_list = []
    while True:
        token = lexer.token()
        if not token:
            break
        line, column = find_position(lexer.lexdata, token.lexpos)
        token_data = All_tokens(token.type, token.value, line, column)
        tokens_list.append(token_data)
        print_token(token_data)
    return tokens_list

def find_position(input, lexpos):
    last_newline = input.rfind('\n', 0, lexpos)
    if last_newline < 0:
        last_newline = 0
    line = input.count('\n', 0, lexpos) + 1
    column = lexpos - last_newline
    return line, column

def print_token(token):
    print("\tLexema: {:<8}|  Tipo de Token: {:<10}|  Línea: {:<5}|  Columna: {:<5}".format(
        token.lexeme, token.type, token.line, token.column))

lexer = lex.lex()
fp = open("funcion1.txt")
cadena = fp.read()
fp.close()

lexer.input(cadena)
show_tokens(lexer)

print ("\n\n#################################################################################\n")

