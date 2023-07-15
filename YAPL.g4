grammar YAPL;

program   : classDefine+ # start
          ;
classDefine : CLASS CLASSTYPE (inherit)? OPENBRACE (feature SEMICOLON)* CLOSEBRACE  SEMICOLON# classDef
          ;
inherit   : INHERITS CLASSTYPE # inherits
          ;
feature   : ID OPENPARENTHESES (parameter (COMMA parameter)*)? CLOSEPARENTHESES COLON CLASSTYPE OPENBRACE expr CLOSEBRACE # method
          | ID COLON CLASSTYPE (ASSIGN expr )? # property
          ;
parameter : ID COLON CLASSTYPE # param;
expr      : expr(AT CLASSTYPE)? DOT ID OPENPARENTHESES ( expr (COMMA expr)*)? CLOSEPARENTHESES # methodCall
          | ID OPENPARENTHESES ( expr (COMMA expr)*)? CLOSEPARENTHESES # ownMethodCall
          | IF expr THEN expr ELSE expr FI # if
          | WHILE expr LOOP expr POOL # while
          | OPENBRACE (expr SEMICOLON)+ CLOSEBRACE  # block
          | LET let_expr # let
          | NEW CLASSTYPE # newObject
          | ISVOID expr # void
          | expr MUL expr # mul
          | expr DIV expr # div
          | expr ADD expr # add
          | expr SUB expr # sub
          | INTEGER_NEGATIVE expr # invert
          | expr LT expr # lt
          | expr LTEQ expr # lteq
          | expr EQUAL expr # equal
          | NOT expr # not
          | OPENPARENTHESES expr CLOSEPARENTHESES # factExpr
          | STRING # string
          | NUM # num
          | ID # id
          | TRUE # true
          | FALSE # false
          | ID ASSIGN expr # assign
          ;

let_expr  : ID COLON CLASSTYPE COMMA let_expr # nestedLet
          | ID COLON CLASSTYPE IN expr # letIn
          | ID COLON CLASSTYPE ASSIGN expr COMMA let_expr # letAssignLet
          | ID COLON CLASSTYPE ASSIGN expr IN expr # letAssignIn
          ;

// Key words
CLASS: C L A S S;
ELSE: E L S E;
FALSE: 'false';
TRUE: 'true';
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
LET: L E T;

// Basic definitions
NUM: [0-9]+;
ID: [a-z_][a-zA-Z0-9_]*;
CLASSTYPE: 'SELF_TYPE' | [A-Z][a-zA-Z_0-9]*;
STRING: '"' (('\\'|'\t'|'\r\n'|'\r'|'\n'|'\\"') | ~('\\'|'\t'|'\r'|'\n'|'"'))* '"';

// Special characters
SEMICOLON: ';';
OPENBRACE: '{';
CLOSEBRACE: '}';
COLON: ':';
COMMA: ',';
OPENPARENTHESES: '(';
CLOSEPARENTHESES: ')';
DOT: '.';
AT: '@';
INTEGER_NEGATIVE: '~';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
EQUAL: '=';
LT: '<';
LTEQ: '<=';
ASSIGN: '<-';

// Ignored tokens
SINGLECOMMENT: '--' ~[\r\n]* -> skip;
MULTICOMMENT: '(*' .*? '*)' -> skip;
WS: [ \n\t\r\f]+ -> skip;

ERROR : . ;

// Letters to use uncase sensitive
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