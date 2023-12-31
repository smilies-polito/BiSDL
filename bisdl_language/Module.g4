grammar Module ;

// parser rules
root           : 'MODULE' ID timescale? scopes paracrine_signals? diffusion*;
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
//                 | constant
                 ;
transcription  : 'TRANSCRIPTION' RO GENE COMMA MRNA (COMMA regulation )* RC ;
translation    : 'TRANSLATION' RO MRNA COMMA PROTEIN (COMMA regulation )* RC ;
degradation    : 'DEGRADATION' RO molecule RC ;
protein_complex_formation : 'PROTEIN_COMPLEX_FORMATION' RO m_list COMMA molecule RC ;
enzymatic_reaction : 'ENZYMATIC_REACTION' RO PROTEIN COMMA SO m_list SC COMMA SO m_list SC RC ;
custom_process : 'CUSTOM_PROCESS' RO SO m_list SC COMMA SO m_list SC (COMMA regulation )* RC ;
//constant       : 'CONSTANT' RO molecule RC ;
regulation     : regulation_type COLON m_list ;
regulation_type : 'INHIBITORS' #type_inhibitors
                | 'INDUCERS' #type_inducers
                | 'ACTIVATORS' #type_activators
                ;
m_list         : molecule ( COMMA molecule )* ;
molecule       : GENE #type_gene
               | MRNA #type_mrna
               | PROTEIN #type_protein
               | MOLECULE #type_molecule
               | COMPLEX #type_complex
               ;
signal         : PROTEIN | MOLECULE | COMPLEX ;
signals        : signal (COMMA signal)* ;
paracrine_signals  : 'PARACRINE_SIGNALS' signals ;
juxtacrine_signal  : 'JUXTACRINE_SIGNAL' signal RARROW ID ;
diffusion          : 'DIFFUSION' ID COMMA ID COMMA SO signals SC ;

// lexer rules
GENE : ID'_gene' ;
MRNA : (MULT STAR)?ID'_mrna' ;
PROTEIN : (MULT STAR)?ID'_protein' ;
RECEPTOR : (MULT STAR)?ID'_receptor'ID* ;
MOLECULE : (MULT STAR)?ID'_molecule' ;
COMPLEX : (MULT STAR)?ID'_complex' ;
ID   : [a-zA-Z_][a-zA-Z_0-9]* ;
INT  : '0' | [1-9][0-9]* ;
RO : '(' ;
RC : ')' ;
SO : '[' ;
SC : ']' ;
COMMA : ',' ;
COLON : ':' ;
STAR : '*' ;
RARROW : '->' ;
MULT : [1-9][0-9]* ;
//NL   : [\r\n] ;
//TAB  : [\t] ;
WS   : [ \t\r\n]+ -> skip ;
LINE_COMMENT : '#' ~[\r\n]* -> skip	;
