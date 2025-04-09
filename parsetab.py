
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACTOR ACTORS CASE CASES COMMA EQUALS EXTENDS GT IDENTIFIER INCLUDE INHERIT LBRACE PACKAGE RBRACE SIMPLE SLASHprogram : definitions relationsdefinitions : definitions definition\n| definitiondefinition : ACTORS EQUALS LBRACE actors RBRACE\n| CASES EQUALS LBRACE cases RBRACEactors : actors COMMA IDENTIFIER\n| IDENTIFIERcases : cases COMMA IDENTIFIER\n| IDENTIFIERrelations : PACKAGE IDENTIFIER relation_listrelation_list : relation_list relation\n| relationrelation : EXTENDS CASE IDENTIFIER CASE identifier_list SLASH GT\n| INCLUDE CASE IDENTIFIER CASE identifier_list SLASH GT\n| INHERIT CASE IDENTIFIER CASE identifier_list SLASH GT\n| SIMPLE  CASE IDENTIFIER CASE identifier_list SLASH GT \n| EXTENDS ACTOR IDENTIFIER CASE identifier_list SLASH GT\n| INCLUDE ACTOR IDENTIFIER CASE identifier_list SLASH GT\n| INHERIT ACTOR IDENTIFIER CASE identifier_list SLASH GT\n| SIMPLE  ACTOR IDENTIFIER CASE identifier_list SLASH GTidentifier_list : identifier_list COMMA IDENTIFIER\n| IDENTIFIER'
    
_lr_action_items = {'ACTORS':([0,2,3,7,33,35,],[4,4,-3,-2,-4,-5,]),'CASES':([0,2,3,7,33,35,],[5,5,-3,-2,-4,-5,]),'$end':([1,6,14,15,24,73,75,76,77,78,79,80,81,],[0,-1,-10,-12,-11,-13,-17,-14,-18,-15,-19,-16,-20,]),'PACKAGE':([2,3,7,33,35,],[8,-3,-2,-4,-5,]),'EQUALS':([4,5,],[9,10,]),'IDENTIFIER':([8,12,13,25,26,27,28,29,30,31,32,34,36,47,48,49,50,51,52,53,54,65,],[11,21,23,37,38,39,40,41,42,43,44,45,46,55,55,55,55,55,55,55,55,74,]),'LBRACE':([9,10,],[12,13,]),'EXTENDS':([11,14,15,24,73,75,76,77,78,79,80,81,],[16,16,-12,-11,-13,-17,-14,-18,-15,-19,-16,-20,]),'INCLUDE':([11,14,15,24,73,75,76,77,78,79,80,81,],[17,17,-12,-11,-13,-17,-14,-18,-15,-19,-16,-20,]),'INHERIT':([11,14,15,24,73,75,76,77,78,79,80,81,],[18,18,-12,-11,-13,-17,-14,-18,-15,-19,-16,-20,]),'SIMPLE':([11,14,15,24,73,75,76,77,78,79,80,81,],[19,19,-12,-11,-13,-17,-14,-18,-15,-19,-16,-20,]),'CASE':([16,17,18,19,37,38,39,40,41,42,43,44,],[25,27,29,31,47,48,49,50,51,52,53,54,]),'ACTOR':([16,17,18,19,],[26,28,30,32,]),'RBRACE':([20,21,22,23,45,46,],[33,-7,35,-9,-6,-8,]),'COMMA':([20,21,22,23,45,46,55,56,57,58,59,60,61,62,63,74,],[34,-7,36,-9,-6,-8,-22,65,65,65,65,65,65,65,65,-21,]),'SLASH':([55,56,57,58,59,60,61,62,63,74,],[-22,64,66,67,68,69,70,71,72,-21,]),'GT':([64,66,67,68,69,70,71,72,],[73,75,76,77,78,79,80,81,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'definitions':([0,],[2,]),'definition':([0,2,],[3,7,]),'relations':([2,],[6,]),'relation_list':([11,],[14,]),'relation':([11,14,],[15,24,]),'actors':([12,],[20,]),'cases':([13,],[22,]),'identifier_list':([47,48,49,50,51,52,53,54,],[56,57,58,59,60,61,62,63,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> definitions relations','program',2,'p_program','hython-parser.py',69),
  ('definitions -> definitions definition','definitions',2,'p_definitions','hython-parser.py',73),
  ('definitions -> definition','definitions',1,'p_definitions','hython-parser.py',74),
  ('definition -> ACTORS EQUALS LBRACE actors RBRACE','definition',5,'p_definition','hython-parser.py',81),
  ('definition -> CASES EQUALS LBRACE cases RBRACE','definition',5,'p_definition','hython-parser.py',82),
  ('actors -> actors COMMA IDENTIFIER','actors',3,'p_actors','hython-parser.py',86),
  ('actors -> IDENTIFIER','actors',1,'p_actors','hython-parser.py',87),
  ('cases -> cases COMMA IDENTIFIER','cases',3,'p_cases','hython-parser.py',94),
  ('cases -> IDENTIFIER','cases',1,'p_cases','hython-parser.py',95),
  ('relations -> PACKAGE IDENTIFIER relation_list','relations',3,'p_relations','hython-parser.py',102),
  ('relation_list -> relation_list relation','relation_list',2,'p_relation_list','hython-parser.py',106),
  ('relation_list -> relation','relation_list',1,'p_relation_list','hython-parser.py',107),
  ('relation -> EXTENDS CASE IDENTIFIER CASE identifier_list SLASH GT','relation',7,'p_relation','hython-parser.py',114),
  ('relation -> INCLUDE CASE IDENTIFIER CASE identifier_list SLASH GT','relation',7,'p_relation','hython-parser.py',115),
  ('relation -> INHERIT CASE IDENTIFIER CASE identifier_list SLASH GT','relation',7,'p_relation','hython-parser.py',116),
  ('relation -> SIMPLE CASE IDENTIFIER CASE identifier_list SLASH GT','relation',7,'p_relation','hython-parser.py',117),
  ('relation -> EXTENDS ACTOR IDENTIFIER CASE identifier_list SLASH GT','relation',7,'p_relation','hython-parser.py',118),
  ('relation -> INCLUDE ACTOR IDENTIFIER CASE identifier_list SLASH GT','relation',7,'p_relation','hython-parser.py',119),
  ('relation -> INHERIT ACTOR IDENTIFIER CASE identifier_list SLASH GT','relation',7,'p_relation','hython-parser.py',120),
  ('relation -> SIMPLE ACTOR IDENTIFIER CASE identifier_list SLASH GT','relation',7,'p_relation','hython-parser.py',121),
  ('identifier_list -> identifier_list COMMA IDENTIFIER','identifier_list',3,'p_identifier_list','hython-parser.py',128),
  ('identifier_list -> IDENTIFIER','identifier_list',1,'p_identifier_list','hython-parser.py',129),
]
