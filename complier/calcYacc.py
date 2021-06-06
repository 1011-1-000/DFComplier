from ply import yacc
from complier.calcLex import tokens


class AddColumn:

    def __init__(self, params):
        self.params = params

    def exec(self):
        print(self.params)


def p_expression_start(p):
    """expression : VAR DOT function_chain"""
    p[0] = 2


def p_function_chain(p):
    """function_chain : function
                        | function DOT function_chain
    """
    for x in p:
        pass
    p[0] = 1


def p_function(p):
    """function : FUNCTION LPAREN params RPAREN """
    for x in p[3]:
        print(type(x), x)
    p[0] = 'test'


def p_params(p):
    """params : param COMMA param
                | param
    """
    params = []
    for x in p:
        if (not x) or (isinstance(x, str) and x.strip() == ','):
            pass
        else:
            params.append(x)
    p[0] = params


def p_atom(p):
    """atom : STRING
            | NUMBER
    """
    p[0] = p[1]


def p_list_elements(p):
    """list_elements : atom
                    | atom COMMA list_elements
                    | list_elements COMMA atom
    """
    list_elements = []
    for x in p:
        if isinstance(x, list):
            list_elements.extend(x)
        elif (not x) or (isinstance(x, str) and x.strip() == ','):
            pass
        else:
            list_elements.append(x)
    p[0] = list_elements


def p_list(p):
    """list : LBRACKET list_elements RBRACKET """
    p[0] = p[2]


def p_param(p):
    """param : list
            | STRING
            | NUMBER
    """
    p[0] = p[1]


def p_error(p):
    print("Syntax error in input!")


parser = yacc.yacc()

if __name__ == '__main__':
    s = "a.FN_ADD_COLUMN(['a', 'b'], 1)"
    result = parser.parse(s)
    print(result)
