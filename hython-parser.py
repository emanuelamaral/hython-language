import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'ACTORS', 'CASES', 'EXTENDS', 'INCLUDE', 'INHERIT', 'PACKAGE',
    'LBRACE', 'RBRACE', 'COMMA', 'EQUALS', 'IDENTIFIER', 'GT', 'SLASH',
    'CASE', 'SIMPLE', 'ACTOR'
)

t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_EQUALS = r'='
t_GT = r'>'
t_SLASH = r'/'
t_ignore = " \t"

def t_ACTORS(t):
    r'actors'
    return t

def t_CASES(t):
    r'cases'
    return t

def t_SIMPLE(t):
    r'\<simple\>'
    return t

def t_CASE(t):
    r'\<case\>'
    return t

def t_ACTOR(t):
    r'\<actor\>'
    return t

def t_EXTENDS(t):
    r'\<extends\>'
    return t

def t_INCLUDE(t):
    r'\<include\>'
    return t

def t_INHERIT(t):
    r'\<inherit\>'
    return t

def t_PACKAGE(t):
    r'\<package\>'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def p_program(p):
    '''program : definitions relations'''
    p[0] = {'definitions': p[1], 'relations': p[2]}

def p_definitions(p):
    '''definitions : definitions definition
                   | definition'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_definition(p):
    '''definition : ACTORS EQUALS LBRACE actors RBRACE
                  | CASES EQUALS LBRACE cases RBRACE'''
    p[0] = (p[1], p[4])

def p_actors(p):
    '''actors : actors COMMA IDENTIFIER
              | IDENTIFIER'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_cases(p):
    '''cases : cases COMMA IDENTIFIER
             | IDENTIFIER'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_relations(p):
    '''relations : PACKAGE IDENTIFIER relation_list'''
    p[0] = ('package', p[2], p[3])

def p_relation_list(p):
    '''relation_list : relation_list relation
                     | relation'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_relation(p):
    '''relation : EXTENDS CASE IDENTIFIER CASE identifier_list SLASH GT
                | INCLUDE CASE IDENTIFIER CASE identifier_list SLASH GT
                | INHERIT CASE IDENTIFIER CASE identifier_list SLASH GT
                | SIMPLE  CASE IDENTIFIER CASE identifier_list SLASH GT 
                | EXTENDS ACTOR IDENTIFIER CASE identifier_list SLASH GT
                | INCLUDE ACTOR IDENTIFIER CASE identifier_list SLASH GT
                | INHERIT ACTOR IDENTIFIER CASE identifier_list SLASH GT
                | SIMPLE  ACTOR IDENTIFIER CASE identifier_list SLASH GT'''
    if p[1] == 'simple':
        p[0] = (p[1], p[3], p[5])
    else:
        p[0] = (p[1], p[3], p[5])

def p_identifier_list(p):
    '''identifier_list : identifier_list COMMA IDENTIFIER
                       | IDENTIFIER'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}', line {p.lineno}")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

data = """
actors = {
    recepctionist
}

cases = {
    SchedulePatientAppointment,
    SchedulePatientHospitalAdmission,
    PatientRegistration,
    FileInsuranceFormsClaims,
    FileMedicalReports,
    PatientHospitalAdmission,
    InpatientHospitalAdmission,
    OutpatientHospitalAdmission,
    BedAllotment
}

<package> HospitalReception
    <simple> <actor> recepctionist <case> SchedulePatientAppointment />
    <simple> <actor> recepctionist <case> SchedulePatientHospitalAdmission />
    <simple> <actor> recepctionist <case> PatientRegistration />
    <simple> <actor> recepctionist <case> PatientHospitalAdmission />
    <simple> <actor> recepctionist <case> FileInsuranceFormsClaims />
    <simple> <actor> recepctionist <case> FileMedicalReports />
    <extends> <case> PatientRegistration <case> SchedulePatientAppointment, SchedulePatientHospitalAdmission />
    <include> <case> PatientHospitalAdmission <case> PatientRegistration />
    <inherit> <case> OutpatientHospitalAdmission <case> PatientHospitalAdmission />
    <inherit> <case> InpatientHospitalAdmission <case> PatientHospitalAdmission />
    <include> <case> InpatientHospitalAdmission <case> BedAllotment />
"""

result = parser.parse(data)
print(result)