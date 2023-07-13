grammar YAPL;

program     : class+
            ;

class       : 'class' TYPE ('inherits' TYPE)? '{' feature* '}'
            ;

feature     : ID '(' formalList? ')' ':' TYPE expr
            | ID ':' TYPE ('<-' expr)?
            ;

formalList  : formal (',' formal)*
            ;

formal      : ID ':' TYPE
            ;

expr        : assignExpr
            ;

assignExpr  : condExpr ('<-' assignExpr)?
            ;

condExpr    : orExpr ('if' orExpr 'then' expr 'else' condExpr)?
            ;

orExpr      : andExpr ('or' andExpr)*
            ;

andExpr     : relExpr ('and' relExpr)*
            ;

relExpr     : addExpr (('<' | '<=' | '=' | 'not') addExpr)?
            ;

addExpr     : multExpr (('+' | '-') multExpr)*
            ;

multExpr    : unaryExpr (('*' | '/') unaryExpr)*
            ;

unaryExpr   : ('not' | '-')? atomExpr
            ;

atomExpr    : ID '(' exprList? ')'
            | 'if' expr 'then' expr 'else' expr 'fi'
            | 'while' expr 'loop' expr 'pool'
            | '{' expr (',' expr)* '}'
            | 'let' letBindingList 'in' expr
            | 'new' TYPE
            | 'isvoid' expr
            | '(' expr ')'
            | ID
            | INTEGER
            | STRING
            | 'true'
            | 'false'
            ;

letBindingList : letBinding (',' letBinding)*
               ;

letBinding  : ID ':' TYPE ('<-' expr)?
            ;

exprList    : expr (',' expr)*
            ;

TYPE        : [A-Z][a-zA-Z0-9]*
            ;

ID          : [a-z][a-zA-Z0-9]*
            ;

INTEGER     : [0-9]+
            ;

STRING      : '"' (~["\r\n] | '\\' [btnf])* '"'
            ;

WS          : [ \t\r\n\f]+ -> skip
            ;
