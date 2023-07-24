grammar YAPL;

program   : (classDefine SEMICOLON)+ # start
          ;
classDefine : CLASS TYPE (INHERITS TYPE)? OPENBRACE (feature SEMICOLON)* CLOSEBRACE # defClase
          ;
feature   : ID OPENPARENTHESES (formal (COMMA formal)*)? CLOSEPARENTHESES COLON TYPE OPENBRACE expr CLOSEBRACE # method
          | ID COLON TYPE (ASSIGN expr )? # property
          ;
formal    : ID COLON TYPE # forml
          ;
expr      : expr(AT TYPE)? DOT ID OPENPARENTHESES ( expr (COMMA expr)*)? CLOSEPARENTHESES #methodCall
          | ID OPENPARENTHESES ( expr (COMMA expr)*)? CLOSEPARENTHESES #ownMethodCall
          | IF expr THEN expr ELSE expr FI # if
          | WHILE expr LOOP expr POOL # while
          | OPENBRACE (expr SEMICOLON)+ CLOSEBRACE #block
          | LET let_expr # let
          | NEW TYPE # newObject
          | TILDE expr # invert
          | ISVOID expr # void
          | ID ASSIGN expr # assign
          | expr OR expr # or
          | expr AND expr # and
          | expr MUL expr # mul
          | expr DIV expr # div
          | expr ADD expr # add
          | expr SUB expr # sub
          | expr LTEQ expr # lteq
          | expr LT expr # lt
          | expr EQUAL expr # equal
          | NOT expr # not
          | OPENPARENTHESES expr CLOSEPARENTHESES # factExpr
          | ID # id
          | INTEGER # INTEGER
          | STRING # string
          | TRUE # true
          | FALSE # false
          ;

let_expr  : ID COLON TYPE COMMA let_expr # nestedLet
          | ID COLON TYPE IN expr # letIn
          | ID COLON TYPE ASSIGN expr COMMA let_expr # letAssignLet
          | ID COLON TYPE ASSIGN expr IN expr # letAssignIn
          ;

// Palabras reservadas
CLASS: C L A S S;
ELSE: E L S E;
FI: F I;
IF: I F;
IN: I N;
INHERITS: I N H E R I T S;
ISVOID: I S V O I D;
LOOP: L O O P;
POOL: P O O L;
THEN: T H E N;
WHILE: W H I L E;
NEW: N E W;
NOT: N O T;
FALSE: 'false';
TRUE: 'true';
LET: L E T;

// Definicion de integer, Identificadores y Cadenas
INTEGER: [0-9]+;                                                                            // Integer
ID: [a-z][a-zA-Z0-9_]*;                                                                    // Identificador de objeto
TYPE: 'self' | 'SELF_TYPE' | [A-Z][a-zA-Z_0-9]*;                                            // Identificador de tipo
STRING: '"' (('\\'|'\t'|'\r\n'|'\r'|'\n'|'\\"') | ~('\\'|'\t'|'\r'|'\n'|'"'))* '"';         // Cadena

// Caracteres especiales que se utilizaran para la construccion
SEMICOLON: ';';
OPENBRACE: '{';
CLOSEBRACE: '}';
COLON: ':';
COMMA: ',';
OPENPARENTHESES: '(';
CLOSEPARENTHESES: ')';
DOT: '.';
AT: '@';
TILDE: '~';
MUL: '*';
ADD: '+';
SUB: '-';
DIV: '/';
EQUAL: '=';
LT: '<';
LTEQ: '<=';
ASSIGN: '<-';
OR: '|';
AND: '&';

// Tokens de ingorar
SINGLECOMMENT: '--' ~[\r\n]* -> skip;                     // Un solo comentario
MULTICOMMENT: '(*' .*? '*)' -> skip;                      // Multiple comentarios
WS: [ \n\t\r\f]+ -> skip;                                 // Caracteres especiales como salto, tab y entre otros

ERROR : . ;

// Asignacion de letras para utilizarlos en el case insensitive
fragment A : [aA];
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment H : [hH];
fragment I : [iI];
fragment L : [lL];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment V : [vV];
fragment W : [wW];
fragment ESC : '\\' (["\\/bfnrt] | UNICODE);
fragment UNICODE : 'u' HEX HEX HEX HEX;
fragment HEX : [0-9a-fA-F];