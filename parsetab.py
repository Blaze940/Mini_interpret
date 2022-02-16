
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftANDleftORnonassocINFTOSUPTOAFFECTleftPLUSMINUSleftTIMESDIVIDENUMBER MINUS PLUS TIMES DIVIDE LPAREN RPAREN AND OR TRUE FALSE SEMICOLON NAME AFFECT INFTO SUPTO SAME LACOL RACOL STR DBQUOTE PRINT IF WHILE ELSE FOR PRINTSTRSTART : BLOC BLOC : BLOC statement SEMICOLON\n           | statement SEMICOLON statement : PRINT LPAREN expression RPAREN statement : PRINTSTR LPAREN DBQUOTE STR DBQUOTE RPAREN statement : WHILE LPAREN expression RPAREN LACOL BLOC RACOL  statement : IF LPAREN expression RPAREN LACOL BLOC RACOL\n    | IF LPAREN expression RPAREN LACOL BLOC RACOL ELSE LACOL BLOC RACOL  statement : FOR LPAREN statement SEMICOLON expression SEMICOLON statement RPAREN LACOL BLOC RACOL statement : NAME AFFECT expression\n                | NAME PLUS PLUS\n                | NAME PLUS AFFECT expression\n    expression : expression PLUS expressionexpression : expression TIMES expressionexpression : expression SAME expressionexpression : expression MINUS expression\n\t\t\t\t| expression DIVIDE expressionexpression : LPAREN expression RPARENexpression : NUMBERexpression : NAMEexpression : TRUEexpression : FALSEexpression : expression AND expression\n                | expression OR expressionexpression : expression INFTO expression\n                    | expression SUPTO expression '
    
_lr_action_items = {'PRINT':([0,2,11,16,19,60,61,64,65,66,72,73,74,75,],[4,4,-3,4,-2,4,4,4,4,4,4,4,4,4,]),'PRINTSTR':([0,2,11,16,19,60,61,64,65,66,72,73,74,75,],[5,5,-3,5,-2,5,5,5,5,5,5,5,5,5,]),'WHILE':([0,2,11,16,19,60,61,64,65,66,72,73,74,75,],[6,6,-3,6,-2,6,6,6,6,6,6,6,6,6,]),'IF':([0,2,11,16,19,60,61,64,65,66,72,73,74,75,],[7,7,-3,7,-2,7,7,7,7,7,7,7,7,7,]),'FOR':([0,2,11,16,19,60,61,64,65,66,72,73,74,75,],[8,8,-3,8,-2,8,8,8,8,8,8,8,8,8,]),'NAME':([0,2,11,12,14,15,16,17,19,20,32,35,36,37,38,39,40,41,42,43,47,60,61,64,65,66,72,73,74,75,],[9,9,-3,23,23,23,9,23,-2,23,23,23,23,23,23,23,23,23,23,23,23,9,9,9,9,9,9,9,9,9,]),'$end':([1,2,11,19,],[0,-1,-3,-2,]),'SEMICOLON':([3,10,22,23,24,25,29,30,31,34,48,49,50,51,52,53,54,55,56,57,58,62,63,67,68,76,77,],[11,19,-19,-20,-21,-22,47,-10,-11,-4,-12,-18,-13,-14,-15,-16,-17,-23,-24,-25,-26,66,-5,-6,-7,-8,-9,]),'LPAREN':([4,5,6,7,8,12,14,15,17,20,32,35,36,37,38,39,40,41,42,43,47,],[12,13,14,15,16,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'AFFECT':([9,18,],[17,32,]),'PLUS':([9,18,21,22,23,24,25,27,28,30,33,48,49,50,51,52,53,54,55,56,57,58,62,],[18,31,35,-19,-20,-21,-22,35,35,35,35,35,-18,-13,-14,35,-16,-17,35,35,35,35,35,]),'RACOL':([11,19,64,65,74,75,],[-3,-2,67,68,76,77,]),'NUMBER':([12,14,15,17,20,32,35,36,37,38,39,40,41,42,43,47,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'TRUE':([12,14,15,17,20,32,35,36,37,38,39,40,41,42,43,47,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'FALSE':([12,14,15,17,20,32,35,36,37,38,39,40,41,42,43,47,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'DBQUOTE':([13,44,],[26,59,]),'RPAREN':([21,22,23,24,25,27,28,30,31,33,34,48,49,50,51,52,53,54,55,56,57,58,59,63,67,68,69,76,77,],[34,-19,-20,-21,-22,45,46,-10,-11,49,-4,-12,-18,-13,-14,-15,-16,-17,-23,-24,-25,-26,63,-5,-6,-7,71,-8,-9,]),'TIMES':([21,22,23,24,25,27,28,30,33,48,49,50,51,52,53,54,55,56,57,58,62,],[36,-19,-20,-21,-22,36,36,36,36,36,-18,36,-14,36,36,-17,36,36,36,36,36,]),'SAME':([21,22,23,24,25,27,28,30,33,48,49,50,51,52,53,54,55,56,57,58,62,],[37,-19,-20,-21,-22,37,37,37,37,37,-18,-13,-14,37,-16,-17,-23,-24,-25,-26,37,]),'MINUS':([21,22,23,24,25,27,28,30,33,48,49,50,51,52,53,54,55,56,57,58,62,],[38,-19,-20,-21,-22,38,38,38,38,38,-18,-13,-14,38,-16,-17,38,38,38,38,38,]),'DIVIDE':([21,22,23,24,25,27,28,30,33,48,49,50,51,52,53,54,55,56,57,58,62,],[39,-19,-20,-21,-22,39,39,39,39,39,-18,39,-14,39,39,-17,39,39,39,39,39,]),'AND':([21,22,23,24,25,27,28,30,33,48,49,50,51,52,53,54,55,56,57,58,62,],[40,-19,-20,-21,-22,40,40,40,40,40,-18,-13,-14,40,-16,-17,-23,-24,-25,-26,40,]),'OR':([21,22,23,24,25,27,28,30,33,48,49,50,51,52,53,54,55,56,57,58,62,],[41,-19,-20,-21,-22,41,41,41,41,41,-18,-13,-14,41,-16,-17,41,-24,-25,-26,41,]),'INFTO':([21,22,23,24,25,27,28,30,33,48,49,50,51,52,53,54,55,56,57,58,62,],[42,-19,-20,-21,-22,42,42,42,42,42,-18,-13,-14,42,-16,-17,42,42,None,None,42,]),'SUPTO':([21,22,23,24,25,27,28,30,33,48,49,50,51,52,53,54,55,56,57,58,62,],[43,-19,-20,-21,-22,43,43,43,43,43,-18,-13,-14,43,-16,-17,43,43,None,None,43,]),'STR':([26,],[44,]),'LACOL':([45,46,70,71,],[60,61,72,73,]),'ELSE':([68,],[70,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'START':([0,],[1,]),'BLOC':([0,60,61,72,73,],[2,64,65,74,75,]),'statement':([0,2,16,60,61,64,65,66,72,73,74,75,],[3,10,29,3,3,10,10,69,3,3,10,10,]),'expression':([12,14,15,17,20,32,35,36,37,38,39,40,41,42,43,47,],[21,27,28,30,33,48,50,51,52,53,54,55,56,57,58,62,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> START","S'",1,None,None,None),
  ('START -> BLOC','START',1,'p_start','Brouillon.py',84),
  ('BLOC -> BLOC statement SEMICOLON','BLOC',3,'p_bloc','Brouillon.py',91),
  ('BLOC -> statement SEMICOLON','BLOC',2,'p_bloc','Brouillon.py',92),
  ('statement -> PRINT LPAREN expression RPAREN','statement',4,'p_statement_print','Brouillon.py',99),
  ('statement -> PRINTSTR LPAREN DBQUOTE STR DBQUOTE RPAREN','statement',6,'p_statement_printString','Brouillon.py',103),
  ('statement -> WHILE LPAREN expression RPAREN LACOL BLOC RACOL','statement',7,'p_statement_while','Brouillon.py',107),
  ('statement -> IF LPAREN expression RPAREN LACOL BLOC RACOL','statement',7,'p_statement_if','Brouillon.py',110),
  ('statement -> IF LPAREN expression RPAREN LACOL BLOC RACOL ELSE LACOL BLOC RACOL','statement',11,'p_statement_if','Brouillon.py',111),
  ('statement -> FOR LPAREN statement SEMICOLON expression SEMICOLON statement RPAREN LACOL BLOC RACOL','statement',11,'p_statement_for','Brouillon.py',118),
  ('statement -> NAME AFFECT expression','statement',3,'p_statement_affect','Brouillon.py',122),
  ('statement -> NAME PLUS PLUS','statement',3,'p_statement_affect','Brouillon.py',123),
  ('statement -> NAME PLUS AFFECT expression','statement',4,'p_statement_affect','Brouillon.py',124),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop_plus','Brouillon.py',135),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop_times','Brouillon.py',139),
  ('expression -> expression SAME expression','expression',3,'p_expression_same','Brouillon.py',143),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop_divide_and_minus','Brouillon.py',147),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop_divide_and_minus','Brouillon.py',148),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','Brouillon.py',153),
  ('expression -> NUMBER','expression',1,'p_expression_number','Brouillon.py',157),
  ('expression -> NAME','expression',1,'p_expression_name','Brouillon.py',161),
  ('expression -> TRUE','expression',1,'p_expressionTrue','Brouillon.py',165),
  ('expression -> FALSE','expression',1,'p_expressionFalse','Brouillon.py',169),
  ('expression -> expression AND expression','expression',3,'p_expression_binop_boop','Brouillon.py',173),
  ('expression -> expression OR expression','expression',3,'p_expression_binop_boop','Brouillon.py',174),
  ('expression -> expression INFTO expression','expression',3,'p_expression_inequal','Brouillon.py',181),
  ('expression -> expression SUPTO expression','expression',3,'p_expression_inequal','Brouillon.py',182),
]
