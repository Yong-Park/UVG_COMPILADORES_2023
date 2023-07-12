grammar YAPL;

// Reglas léxicas
INT : [0-9]+;
ID : (LETTER | DIGIT | '_') (LETTER | DIGIT | '_')*;
TYPE_ID : LETTER (LETTER | DIGIT | '_')*;
OBJECT_ID : LETTER (LETTER | DIGIT | '_')*;
STRING : '"' (~[\b\t\n\f\\] | '\\' [btnf])* '"';
WS : [ \t\r\n\f]+ -> skip;

// Palabras reservadas
CLASS : [Cc][Ll][Aa][Ss][Ss];
ELSE : [Ee][Ll][Ss][Ee];
FALSE : [Ff][Aa][Ll][Ss][Ee];
FI : [Ff][Ii];
IF : [Ii][Ff];
IN : [Ii][Nn];
INHERITS : [Ii][Nn][Hh][Ee][Rr][Ii][Tt][Ss];
ISVOID : [Ii][Ss][Vv][Oo][Ii][Dd];
LOOP : [Ll][Oo][Oo][Pp];
POOL : [Pp][Oo][Oo][Ll];
THEN : [Tt][Hh][Ee][Nn];
WHILE : [Ww][Hh][Ii][Ll][Ee];
NEW : [Nn][Ee][Ww];
NOT : [Nn][Oo][Tt];
TRUE : [Tt][Rr][Uu][Ee];
LET : [Ll][Ee][Tt];
CASE : [Cc][Aa][Ss][Ee];
OF : [Oo][Ff];
ESAC : [Ee][Ss][Aa][Cc];

// Reglas de producción
program : class_list EOF;

class_list : class_def+;

class_def : CLASS TYPE_ID (INHERITS TYPE_ID)? '{' feature_list '}';

feature_list : feature_def*;

feature_def : OBJECT_ID ':' TYPE_ID (feature_body)? ';';

feature_body : '=' expr | '(' formal_list ')' ':' TYPE_ID '{' expr_list '}' | '{' expr_list '}';

formal_list : formal_param (',' formal_param)*;

formal_param : OBJECT_ID ':' TYPE_ID;

expr_list : expr (';' expr)*;
expr : IF expr THEN expr ELSE expr FI
     | WHILE expr LOOP expr POOL
     | '{' expr_list '}'
     | LET OBJECT_ID ':' TYPE_ID ('<-' expr)? (',' OBJECT_ID ':' TYPE_ID ('<-' expr)?)* IN expr
     | CASE expr OF case_list ESAC
     | NEW TYPE_ID
     | ISVOID expr
     | expr '.' OBJECT_ID '(' expr_list ')'
     | expr '@' TYPE_ID '.' OBJECT_ID '(' expr_list ')'
     | expr '~'
     | NOT expr
     | expr '*' expr
     | expr '/' expr
     | expr '+' expr
     | expr '-' expr
     | expr '<=' expr
     | expr '<' expr
     | expr '=' expr
     | expr ISVOID
     | '(' expr ')'
     | OBJECT_ID
     | INT
     | TRUE
     | FALSE
     | STRING;

case_list : case_def+;

case_def : OBJECT_ID ':' TYPE_ID '=>' expr ';';

// Reglas léxicas auxiliares
fragment LETTER : [a-zA-Z];
fragment DIGIT : [0-9];
