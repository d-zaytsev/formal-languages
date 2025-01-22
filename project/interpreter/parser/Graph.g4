grammar Graph;

// Parser rules
prog : stmt* ;

stmt : bind | add | remove | declare ;

declare : LET var IS GRAPH ;

bind : LET var EQUAL expr ;

remove : REMOVE (VERTEX | EDGE | VERTICES) expr FROM var ;

add : ADD (VERTEX | EDGE) expr TO var ;

expr : num | char | var | edge_expr | set_expr | regexp | select ;

set_expr : L_SQ_BRACKET expr (COMMA expr)* R_SQ_BRACKET ;

edge_expr : L_PARENTHESIS expr COMMA expr COMMA expr R_PARENTHESIS ;

regexp: char
        | var
        | L_PARENTHESIS regexp R_PARENTHESIS
        | regexp PIPE regexp
        | regexp CIRCUMFLEX range
        | regexp DOT regexp
        | regexp AMPERSAND regexp;

range : L_SQ_BRACKET num ELLIPSIS? num? R_SQ_BRACKET ;

select : v_filter? v_filter? RETURN var (COMMA var)? WHERE var REACHABLE FROM var IN var BY expr ;

v_filter : FOR var IN expr ;

num: NUM ;
char: CHAR ;
var: VAR_ID ;

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
