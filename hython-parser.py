import ply.lex as lex
import ply.yacc as yacc

"""
=============================================
                ANÁLISE LÉXICA
=============================================
Esta seção define os tokens e regras léxicas para o analisador.
Os tokens representam os componentes básicos da linguagem.
"""


tokens = (
    'ACTORS', 'CASES', 'EXTENDS', 'INCLUDE', 'INHERIT', 'PACKAGE',
    'LBRACE', 'RBRACE', 'COMMA', 'EQUALS', 'IDENTIFIER', 'GT', 'SLASH',
    'CASE', 'SIMPLE', 'ACTOR', 'CLASS', 'COMPONENT', 'ASSOCIATES', 
    'REALIZES', 'DEPENDS', 'USES', 'INTERFACE'
)

# Tokens simples
t_LBRACE = r'\{' # Delimitador de início de bloco
t_RBRACE = r'\}' # Delimitador de fim de bloco
t_COMMA = r','   # Separador de itens em listas
t_EQUALS = r'='  # Operador de atribuição
t_GT = r'>'      # Símbolo maior que (usado em tags)
t_SLASH = r'/'   # Barra (usada no fechamento de tags)
t_ignore = " \t" # Caracteres a serem ignorados (espaços e tabs)

# Palavras-chave com tags
def t_ACTORS(t):
    r'actors'
    return t

def t_CASES(t):
    r'cases'
    return t

def t_SIMPLE(t):
    r'<simple>'
    return t

def t_CASE(t):
    r'<case>'
    return t

def t_ACTOR(t):
    r'<actor>'
    return t

def t_EXTENDS(t):
    r'<extends>'
    return t

def t_INCLUDE(t):
    r'<include>'
    return t

def t_INHERIT(t):
    r'<inherit>'
    return t

def t_PACKAGE(t):
    r'<package>'
    return t

def t_CLASS(t):
    r'<class>'
    return t

def t_COMPONENT(t):
    r'<component>'
    return t

def t_INTERFACE(t):
    r'<interface>'
    return t

def t_USES(t):
    r'<uses>'
    return t

def t_REALIZES(t):
    r'<realizes>'
    return t

def t_ASSOCIATES(t):
    r'<associates>'
    return t

def t_DEPENDS(t):
    r'<depends>'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Tratamento de quebras de linha (importante para mensagens de erro)
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erros léxicos
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

"""
=============================================
              ANÁLISE SINTÁTICA
=============================================
Esta seção define a gramática da linguagem e como os tokens
se combinam para formar estruturas válidas.
"""

def p_program(p):
    '''program : definitions relations'''
    p[0] = {'definitions': p[1], 'relations': p[2]}

    """
    Um programa completo consiste em:
    1. Definições (atores e casos de uso)
    2. Relações entre os elementos
    """

def p_definitions(p):
    '''definitions : definitions definition
                  | definition'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

    """
    Lista de definições pode ser:
    1. Uma definição isolada
    2. Ou várias definições em sequência
    """

def p_definition(p):
    '''definition : ACTORS EQUALS LBRACE actors RBRACE
                 | CASES EQUALS LBRACE cases RBRACE'''
    p[0] = (p[1], p[4])

    """
    Cada definição pode ser:
    1. Conjunto de atores
    2. Conjunto de casos de uso
    """

# Listas de atores e casos de uso
def p_actors(p):
    '''actors : actors COMMA IDENTIFIER
             | IDENTIFIER'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

    """
    Lista de atores pode ser:
    1. Um único ator
    2. Vários atores separados por vírgulas
    """

def p_cases(p):
    '''cases : cases COMMA IDENTIFIER
            | IDENTIFIER'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

    """
    Lista de casos de uso segue a mesma estrutura dos atores
    """

def p_relations(p):
    '''relations : PACKAGE IDENTIFIER relation_list'''
    p[0] = ('package', p[2], p[3])

    """
    Bloco de relações deve:
    1. Começar com tag <package> e nome
    2. Conter lista de relações
    """

def p_relation_list(p):
    '''relation_list : relation_list relation
                    | relation'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

    """
    Lista de relações pode ser:
    1. Uma única relação
    2. Várias relações em sequência
    """
    

def p_relation(p):
    '''relation : relation_type source target_participants SLASH GT'''
    p[0] = {
        'type': p[1],
        'participants': [p[2]] + p[3]
    }
    
    """
    Define uma relação entre elementos UML
    Combina o tipo de relação com os participantes (fonte + alvos)
    """

def p_source(p):
    '''source : element_type IDENTIFIER'''
    p[0] = {'type': p[1], 'name': p[2]}

    # Define quem inicia a relação (ex: <actor> Usuário)

def p_target_participants(p):
    '''target_participants : target_participants element_type IDENTIFIER
                          | element_type IDENTIFIER'''
    if len(p) == 3:
        p[0] = [{'type': p[1], 'name': p[2]}]
    else:
        p[0] = p[1] + [{'type': p[2], 'name': p[3]}]

    """
    Permite vários elementos como destino na relação
    # Ex: <case> Login, <case> Verificação2FA
    """

def p_element_type(p):
    '''element_type : CASE
                   | ACTOR
                   | CLASS
                   | COMPONENT
                   | INTERFACE'''
    p[0] = p[1]

    # Tipos de elementos que podem participar das relações

def p_relation_type(p):
    '''relation_type : EXTENDS
                    | INCLUDE
                    | INHERIT
                    | SIMPLE
                    | USES
                    | REALIZES
                    | ASSOCIATES
                    | DEPENDS'''
    p[0] = p[1]

    # Tipos de conexões permitidas entre elementos

def p_error(p):
    if p:
        print(f"Erro sintático em '{p.value}' na linha {p.lineno}")
    else:
        print("Erro sintático no final do arquivo")

parser = yacc.yacc()

data = """
actors = {
    Customer,
    Admin
}

cases = {
    BrowseProducts,
    AddToCart,
    PlaceOrder,
    ProcessPayment,
    TrackShipment,
    ManageInventory,
    ApplyDiscount,
    InternationalOrder,
    GuestCheckout
}

<package> ECommerceSystem
    <simple> <actor> Customer <case> BrowseProducts />
    <simple> <actor> Customer <case> AddToCart />
    <include> <case> PlaceOrder <case> AddToCart <case> ProcessPayment />
    <extends> <case> InternationalOrder <case> PlaceOrder />
    <inherit> <case> GuestCheckout <case> PlaceOrder />
    <simple> <actor> Admin <case> ManageInventory />
    <associates> <class> ShoppingCart <class> Product />
"""

result = parser.parse(data)
print(result)