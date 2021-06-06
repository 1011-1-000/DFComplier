# ------------------------------------------------------------
# calcLex.py
#
# tokenizer for the expression evaluator of DataFrame
# ------------------------------------------------------------

import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'LPAREN',
    'RPAREN',
    'COMMA',
    'DOT',
    'NUMBER',
    'VAR',
    'FUNCTION',
    'STRING',
    'LBRACKET',
    'RBRACKET'
)

# Regular expression rules for simple tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOT = r'\.'
t_COMMA = ','
t_LBRACKET = r'\['
t_RBRACKET = r'\]'


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_FUNCTION(t):
    r'(FN_[a-zA-Z0-9_]*)'
    return t


def t_STRING(t):
    r"\'(.*?)\'"
    t.value = t.value[1:-1]
    return t


def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()


def tokenize(statement):
    lexer.input(statement)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)


if __name__ == '__main__':
    s = "a.FN_ADD_COLUMN(['a', 'b'], 1)"
    tokenize(s)
