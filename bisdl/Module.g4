grammar Module ;

// parser rules
root           : 'MODULE' ID timescale? scopes paracrine_signals? ;
timescale      : 'TIMESCALE' INT ;
scopes         : ( 'SCOPE' scope )* ;
scope          : ID coords processes? juxtacrine_signal* ;
coords         : RO INT COMMA INT RC ;
processes      : ( 'PROCESS' process )+ ;
process        : ID (timescale process_type+)? ;
process_type   : transcription //#type_transcription
                 | translation //#type_translation
                 | degradation //#type_degradation
                 | protein_complex_formation //#type_protein_complex_formation
                 | enzymatic_reaction //#type_enzymatic_reaction
                 | custom_process //#type_custom_process
                 ;
transcription  : 'TRANSCRIPTION' RO GENE COMMA mult? MRNA (COMMA regulation )* RC ;
translation    : 'TRANSLATION' RO MRNA COMMA mult? PROTEIN (COMMA regulation )* RC ;
degradation    : 'DEGRADATION' RO mult? (MRNA | PROTEIN) RC ;
protein_complex_formation : 'PROTEIN_COMPLEX_FORMATION' RO m_list COMMA mult? molecule RC ;
enzymatic_reaction : 'ENZYMATIC_REACTION' RO PROTEIN COMMA SO m_list SC COMMA SO m_list SC RC ;
custom_process : 'PROCESS' RO mult? molecule COMMA mult? molecule (COMMA regulation )* RC ;
regulation     : regulation_type COLON m_list ;
regulation_type : 'INHIBITORS' #type_inhibitors
                | 'INDUCERS' #type_inducers
                | 'ACTIVATORS' #type_activators
                ;
m_list         : mult? molecule ( COMMA mult? molecule )* ;
mult           : INT STAR ;
molecule       : GENE #type_gene
               | MRNA #type_mrna
               | PROTEIN #type_protein
               ;
paracrine_signals  : 'PARACRINE_SIGNALS' molecule (COMMA molecule)* ;
juxtacrine_signal  : 'JUXTACRINE_SIGNAL' PROTEIN RARROW ID ;

// lexer rules
GENE : ID'_gene' ;
MRNA : ID'_mrna' ;
PROTEIN : ID'_protein' ;
RECEPTOR : ID'_receptor'ID* ;
INT  : '0' | [1-9][0-9]* ;
RO : '(' ;
RC : ')' ;
SO : '[' ;
SC : ']' ;
COMMA : ',' ;
COLON : ':' ;
STAR : '*' ;
RARROW : '->' ;
ID   : [a-zA-Z_][a-zA-Z_0-9]* ;
//NL   : [\r\n] ;
//TAB  : [\t] ;
WS   : [ \t\r\n]+ -> skip ;
LINE_COMMENT : '#' ~[\r\n]* -> skip	;
