
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftANDleftORnonassocINFTOSUPTOAFFECTleftPLUSMINUSleftTIMESDIVIDENUMBER MINUS PLUS TIMES DIVIDE LPAREN RPAREN AND OR TRUE FALSE SEMICOLON NAME AFFECT INFTO SUPTO PRINTSTART : expression START : START statement SEMICOLON\n           | statement SEMICOLON statement : PRINT LPAREN expression RPARENstatement : NAME AFFECT expression expression : expression PLUS expressionexpression : expression TIMES expressionexpression : expression MINUS expression\n\t\t\t\t| expression DIVIDE expressionexpression : LPAREN expression RPARENexpression : NUMBERexpression : NAMEexpression : TRUEexpression : FALSEexpression : expression AND expression\n                | expression OR expressionexpression : expression INFTO expression\n                    | expression SUPTO expression '
    
_lr_action_items = {'LPAREN':([0,4,9,12,13,14,15,16,17,18,19,23,24,],[4,4,24,4,4,4,4,4,4,4,4,4,4,]),'NUMBER':([0,4,12,13,14,15,16,17,18,19,23,24,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'NAME':([0,1,2,4,5,6,7,8,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,30,31,32,33,34,],[6,11,-1,22,-11,-12,-13,-14,22,22,22,22,22,22,22,22,-3,-12,22,22,-2,-6,-7,-8,-9,-15,-16,-17,-18,-10,]),'TRUE':([0,4,12,13,14,15,16,17,18,19,23,24,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'FALSE':([0,4,12,13,14,15,16,17,18,19,23,24,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'PRINT':([0,1,2,5,6,7,8,20,22,25,26,27,28,29,30,31,32,33,34,],[9,9,-1,-11,-12,-13,-14,-3,-12,-2,-6,-7,-8,-9,-15,-16,-17,-18,-10,]),'$end':([1,2,5,6,7,8,20,22,25,26,27,28,29,30,31,32,33,34,],[0,-1,-11,-12,-13,-14,-3,-12,-2,-6,-7,-8,-9,-15,-16,-17,-18,-10,]),'PLUS':([2,5,6,7,8,21,22,26,27,28,29,30,31,32,33,34,35,36,],[12,-11,-12,-13,-14,12,-12,-6,-7,-8,-9,12,12,12,12,-10,12,12,]),'TIMES':([2,5,6,7,8,21,22,26,27,28,29,30,31,32,33,34,35,36,],[13,-11,-12,-13,-14,13,-12,13,-7,13,-9,13,13,13,13,-10,13,13,]),'MINUS':([2,5,6,7,8,21,22,26,27,28,29,30,31,32,33,34,35,36,],[14,-11,-12,-13,-14,14,-12,-6,-7,-8,-9,14,14,14,14,-10,14,14,]),'DIVIDE':([2,5,6,7,8,21,22,26,27,28,29,30,31,32,33,34,35,36,],[15,-11,-12,-13,-14,15,-12,15,-7,15,-9,15,15,15,15,-10,15,15,]),'AND':([2,5,6,7,8,21,22,26,27,28,29,30,31,32,33,34,35,36,],[16,-11,-12,-13,-14,16,-12,-6,-7,-8,-9,-15,-16,-17,-18,-10,16,16,]),'OR':([2,5,6,7,8,21,22,26,27,28,29,30,31,32,33,34,35,36,],[17,-11,-12,-13,-14,17,-12,-6,-7,-8,-9,17,-16,-17,-18,-10,17,17,]),'INFTO':([2,5,6,7,8,21,22,26,27,28,29,30,31,32,33,34,35,36,],[18,-11,-12,-13,-14,18,-12,-6,-7,-8,-9,18,18,None,None,-10,18,18,]),'SUPTO':([2,5,6,7,8,21,22,26,27,28,29,30,31,32,33,34,35,36,],[19,-11,-12,-13,-14,19,-12,-6,-7,-8,-9,19,19,None,None,-10,19,19,]),'SEMICOLON':([3,5,7,8,10,22,26,27,28,29,30,31,32,33,34,35,37,],[20,-11,-13,-14,25,-12,-6,-7,-8,-9,-15,-16,-17,-18,-10,-5,-4,]),'RPAREN':([5,7,8,21,22,26,27,28,29,30,31,32,33,34,36,],[-11,-13,-14,34,-12,-6,-7,-8,-9,-15,-16,-17,-18,-10,37,]),'AFFECT':([6,11,],[23,23,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'START':([0,],[1,]),'expression':([0,4,12,13,14,15,16,17,18,19,23,24,],[2,21,26,27,28,29,30,31,32,33,35,36,]),'statement':([0,1,],[3,10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> START","S'",1,None,None,None),
  ('START -> expression','START',1,'p_start','Brouillon.py',70),
  ('START -> START statement SEMICOLON','START',3,'p_bloc','Brouillon.py',77),
  ('START -> statement SEMICOLON','START',2,'p_bloc','Brouillon.py',78),
  ('statement -> PRINT LPAREN expression RPAREN','statement',4,'p_statement_print','Brouillon.py',82),
  ('statement -> NAME AFFECT expression','statement',3,'p_statement_affect','Brouillon.py',86),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop_plus','Brouillon.py',90),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop_times','Brouillon.py',94),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop_divide_and_minus','Brouillon.py',98),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop_divide_and_minus','Brouillon.py',99),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','Brouillon.py',104),
  ('expression -> NUMBER','expression',1,'p_expression_number','Brouillon.py',108),
  ('expression -> NAME','expression',1,'p_expression_name','Brouillon.py',112),
  ('expression -> TRUE','expression',1,'p_expressionTrue','Brouillon.py',116),
  ('expression -> FALSE','expression',1,'p_expressionFalse','Brouillon.py',120),
  ('expression -> expression AND expression','expression',3,'p_expression_binop_boop','Brouillon.py',124),
  ('expression -> expression OR expression','expression',3,'p_expression_binop_boop','Brouillon.py',125),
  ('expression -> expression INFTO expression','expression',3,'p_expression_inequal','Brouillon.py',132),
  ('expression -> expression SUPTO expression','expression',3,'p_expression_inequal','Brouillon.py',133),
]
