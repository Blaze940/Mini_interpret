
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftANDleftORnonassocINFTOSUPTOAFFECTleftPLUSMINUSleftTIMESDIVIDENUMBER MINUS PLUS TIMES DIVIDE LPAREN RPAREN AND OR TRUE FALSE SEMICOLON NAME AFFECT INFTO SUPTO SAME LACOL RACOL STR PRINT IF WHILE ELSE FOR PRINTSTR FONCTIONSTART : BLOC BLOC : BLOC statement SEMICOLON\n           | statement SEMICOLON statement : PRINT LPAREN expression RPAREN statement : FONCTION NAME LPAREN RPAREN LACOL BLOC RACOLstatement : NAME LPAREN RPARENstatement : PRINTSTR LPAREN STR RPAREN statement : WHILE LPAREN expression RPAREN LACOL BLOC RACOL  statement : IF LPAREN expression RPAREN LACOL BLOC RACOL\n    | IF LPAREN expression RPAREN LACOL BLOC RACOL ELSE LACOL BLOC RACOL  statement : FOR LPAREN statement SEMICOLON expression SEMICOLON statement RPAREN LACOL BLOC RACOL statement : NAME AFFECT expression\n                | NAME PLUS PLUS\n                | NAME PLUS AFFECT expression\n    expression : expression PLUS expressionexpression : expression TIMES expressionexpression : expression SAME expressionexpression : expression MINUS expression\n\t\t\t\t| expression DIVIDE expressionexpression : LPAREN expression RPARENexpression : NUMBERexpression : NAMEexpression : TRUEexpression : FALSEexpression : expression AND expression\n                | expression OR expressionexpression : expression INFTO expression\n                    | expression SUPTO expression '
    
_lr_action_items = {'PRINT':([0,2,12,21,22,65,66,67,69,70,71,72,79,80,81,82,],[4,4,-3,4,-2,4,4,4,4,4,4,4,4,4,4,4,]),'FONCTION':([0,2,12,21,22,65,66,67,69,70,71,72,79,80,81,82,],[5,5,-3,5,-2,5,5,5,5,5,5,5,5,5,5,5,]),'NAME':([0,2,5,12,13,16,19,20,21,22,23,33,40,41,42,43,44,45,46,47,48,54,65,66,67,69,70,71,72,79,80,81,82,],[6,6,14,-3,26,26,26,26,6,-2,26,26,26,26,26,26,26,26,26,26,26,26,6,6,6,6,6,6,6,6,6,6,6,]),'PRINTSTR':([0,2,12,21,22,65,66,67,69,70,71,72,79,80,81,82,],[7,7,-3,7,-2,7,7,7,7,7,7,7,7,7,7,7,]),'WHILE':([0,2,12,21,22,65,66,67,69,70,71,72,79,80,81,82,],[8,8,-3,8,-2,8,8,8,8,8,8,8,8,8,8,8,]),'IF':([0,2,12,21,22,65,66,67,69,70,71,72,79,80,81,82,],[9,9,-3,9,-2,9,9,9,9,9,9,9,9,9,9,9,]),'FOR':([0,2,12,21,22,65,66,67,69,70,71,72,79,80,81,82,],[10,10,-3,10,-2,10,10,10,10,10,10,10,10,10,10,10,]),'$end':([1,2,12,22,],[0,-1,-3,-2,]),'SEMICOLON':([3,11,25,26,27,28,30,31,32,37,39,50,51,55,56,57,58,59,60,61,62,63,64,68,73,74,75,83,84,],[12,22,-21,-22,-23,-24,-6,-12,-13,54,-4,-14,-7,-20,-15,-16,-17,-18,-19,-25,-26,-27,-28,72,-5,-8,-9,-10,-11,]),'LPAREN':([4,6,7,8,9,10,13,14,16,19,20,23,33,40,41,42,43,44,45,46,47,48,54,],[13,15,18,19,20,21,23,29,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'AFFECT':([6,17,],[16,33,]),'PLUS':([6,17,24,25,26,27,28,31,35,36,38,50,55,56,57,58,59,60,61,62,63,64,68,],[17,32,40,-21,-22,-23,-24,40,40,40,40,40,-20,-15,-16,40,-18,-19,40,40,40,40,40,]),'RACOL':([12,22,69,70,71,81,82,],[-3,-2,73,74,75,83,84,]),'NUMBER':([13,16,19,20,23,33,40,41,42,43,44,45,46,47,48,54,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'TRUE':([13,16,19,20,23,33,40,41,42,43,44,45,46,47,48,54,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'FALSE':([13,16,19,20,23,33,40,41,42,43,44,45,46,47,48,54,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'RPAREN':([15,24,25,26,27,28,29,30,31,32,34,35,36,38,39,50,51,55,56,57,58,59,60,61,62,63,64,73,74,75,76,83,84,],[30,39,-21,-22,-23,-24,49,-6,-12,-13,51,52,53,55,-4,-14,-7,-20,-15,-16,-17,-18,-19,-25,-26,-27,-28,-5,-8,-9,78,-10,-11,]),'STR':([18,],[34,]),'TIMES':([24,25,26,27,28,31,35,36,38,50,55,56,57,58,59,60,61,62,63,64,68,],[41,-21,-22,-23,-24,41,41,41,41,41,-20,41,-16,41,41,-19,41,41,41,41,41,]),'SAME':([24,25,26,27,28,31,35,36,38,50,55,56,57,58,59,60,61,62,63,64,68,],[42,-21,-22,-23,-24,42,42,42,42,42,-20,-15,-16,42,-18,-19,-25,-26,-27,-28,42,]),'MINUS':([24,25,26,27,28,31,35,36,38,50,55,56,57,58,59,60,61,62,63,64,68,],[43,-21,-22,-23,-24,43,43,43,43,43,-20,-15,-16,43,-18,-19,43,43,43,43,43,]),'DIVIDE':([24,25,26,27,28,31,35,36,38,50,55,56,57,58,59,60,61,62,63,64,68,],[44,-21,-22,-23,-24,44,44,44,44,44,-20,44,-16,44,44,-19,44,44,44,44,44,]),'AND':([24,25,26,27,28,31,35,36,38,50,55,56,57,58,59,60,61,62,63,64,68,],[45,-21,-22,-23,-24,45,45,45,45,45,-20,-15,-16,45,-18,-19,-25,-26,-27,-28,45,]),'OR':([24,25,26,27,28,31,35,36,38,50,55,56,57,58,59,60,61,62,63,64,68,],[46,-21,-22,-23,-24,46,46,46,46,46,-20,-15,-16,46,-18,-19,46,-26,-27,-28,46,]),'INFTO':([24,25,26,27,28,31,35,36,38,50,55,56,57,58,59,60,61,62,63,64,68,],[47,-21,-22,-23,-24,47,47,47,47,47,-20,-15,-16,47,-18,-19,47,47,None,None,47,]),'SUPTO':([24,25,26,27,28,31,35,36,38,50,55,56,57,58,59,60,61,62,63,64,68,],[48,-21,-22,-23,-24,48,48,48,48,48,-20,-15,-16,48,-18,-19,48,48,None,None,48,]),'LACOL':([49,52,53,77,78,],[65,66,67,79,80,]),'ELSE':([75,],[77,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'START':([0,],[1,]),'BLOC':([0,65,66,67,79,80,],[2,69,70,71,81,82,]),'statement':([0,2,21,65,66,67,69,70,71,72,79,80,81,82,],[3,11,37,3,3,3,11,11,11,76,3,3,11,11,]),'expression':([13,16,19,20,23,33,40,41,42,43,44,45,46,47,48,54,],[24,31,35,36,38,50,56,57,58,59,60,61,62,63,64,68,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> START","S'",1,None,None,None),
  ('START -> BLOC','START',1,'p_start','BrouillonTP3.py',85),
  ('BLOC -> BLOC statement SEMICOLON','BLOC',3,'p_bloc','BrouillonTP3.py',92),
  ('BLOC -> statement SEMICOLON','BLOC',2,'p_bloc','BrouillonTP3.py',93),
  ('statement -> PRINT LPAREN expression RPAREN','statement',4,'p_statement_print','BrouillonTP3.py',100),
  ('statement -> FONCTION NAME LPAREN RPAREN LACOL BLOC RACOL','statement',7,'p_statement_fonction_void_spm','BrouillonTP3.py',104),
  ('statement -> NAME LPAREN RPAREN','statement',3,'p_statement_Call_fonction_void_spm','BrouillonTP3.py',109),
  ('statement -> PRINTSTR LPAREN STR RPAREN','statement',4,'p_statement_printString','BrouillonTP3.py',113),
  ('statement -> WHILE LPAREN expression RPAREN LACOL BLOC RACOL','statement',7,'p_statement_while','BrouillonTP3.py',117),
  ('statement -> IF LPAREN expression RPAREN LACOL BLOC RACOL','statement',7,'p_statement_if','BrouillonTP3.py',121),
  ('statement -> IF LPAREN expression RPAREN LACOL BLOC RACOL ELSE LACOL BLOC RACOL','statement',11,'p_statement_if','BrouillonTP3.py',122),
  ('statement -> FOR LPAREN statement SEMICOLON expression SEMICOLON statement RPAREN LACOL BLOC RACOL','statement',11,'p_statement_for','BrouillonTP3.py',129),
  ('statement -> NAME AFFECT expression','statement',3,'p_statement_affect','BrouillonTP3.py',133),
  ('statement -> NAME PLUS PLUS','statement',3,'p_statement_affect','BrouillonTP3.py',134),
  ('statement -> NAME PLUS AFFECT expression','statement',4,'p_statement_affect','BrouillonTP3.py',135),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop_plus','BrouillonTP3.py',146),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop_times','BrouillonTP3.py',150),
  ('expression -> expression SAME expression','expression',3,'p_expression_same','BrouillonTP3.py',154),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop_divide_and_minus','BrouillonTP3.py',158),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop_divide_and_minus','BrouillonTP3.py',159),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','BrouillonTP3.py',164),
  ('expression -> NUMBER','expression',1,'p_expression_number','BrouillonTP3.py',168),
  ('expression -> NAME','expression',1,'p_expression_name','BrouillonTP3.py',172),
  ('expression -> TRUE','expression',1,'p_expressionTrue','BrouillonTP3.py',176),
  ('expression -> FALSE','expression',1,'p_expressionFalse','BrouillonTP3.py',180),
  ('expression -> expression AND expression','expression',3,'p_expression_binop_boop','BrouillonTP3.py',184),
  ('expression -> expression OR expression','expression',3,'p_expression_binop_boop','BrouillonTP3.py',185),
  ('expression -> expression INFTO expression','expression',3,'p_expression_inequal','BrouillonTP3.py',192),
  ('expression -> expression SUPTO expression','expression',3,'p_expression_inequal','BrouillonTP3.py',193),
]
