grammar Graph;

// Parser rules
prog : stmt* ;

stmt : bind | add | remove | declare ;

declare : LET VAR_ID IS GRAPH ;

bind : LET VAR_ID EQUAL expr ;

remove : REMOVE (VERTEX | EDGE | VERTICES) expr FROM VAR_ID ;

add : ADD (VERTEX | EDGE) expr TO VAR_ID ;

expr : NUM | CHAR | VAR_ID | edge_expr | set_expr | regexp | select ;

set_expr : L_SQ_BRACKET expr (COMMA expr)* R_SQ_BRACKET ;

edge_expr : L_PARENTHESIS expr COMMA expr COMMA expr R_PARENTHESIS ;

// regexp = CHAR | VAR | '(' regexp ')' | (regexp '|' regexp) | (regexp '^' range) | (regexp '.' regexp) | (regexp '&' regexp)
regexp: term ('|' term)*;
term: factor (('.' | '&') factor)*;
factor: primary ('^' range)*;
primary: CHAR | VAR_ID | '(' regexp ')';

range : L_SQ_BRACKET NUM ELLIPSIS NUM? R_SQ_BRACKET ;

select : v_filter? v_filter? RETURN VAR_ID (COMMA VAR_ID)? WHERE VAR_ID REACHABLE FROM VAR_ID IN VAR_ID BY expr ;

v_filter : FOR VAR_ID IN expr ;


// Lexer rules
LET:            'let' ;
IS:             'is' ;
GRAPH:          'graph' ;
REMOVE:         'remove' ;
WHERE:          'where' ;
REACHABLE:      'reachable' ;
RETURN:         'return' ;
BY:             'by' ;
VERTEX:         'vertex' ;
EDGE:           'edge' ;
VERTICES:       'vertices' ;
FROM:           'from' ;
ADD:            'add' ;
TO:             'to' ;
FOR:            'for' ;
IN:             'in' ;

EQUAL:          '=' ;
L_SQ_BRACKET:   '[' ;
L_PARENTHESIS:  '(' ;
R_SQ_BRACKET:   ']' ;
R_PARENTHESIS:  ')' ;
COMMA:          ',' ;
CIRCUMFLEX:     '^' ;
DOT:            '.' ;
AMPERSAND:      '&' ;
ELLIPSIS:       '..' ;
PIPE:           '|' ;

VAR_ID : [a-zA-Z] [a-zA-Z0-9]* ;
NUM : [0-9]+ ;
CHAR : '"' [a-z] '"' | '\'' [a-z] '\'' ;

WS : [ \t\r\n\f]+ -> skip ;
