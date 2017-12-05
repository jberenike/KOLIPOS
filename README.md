## KOLIPOS
Hackathon for advancing POS-annotation in KOLIMO

# Date 
7-8 December 2017

   Thur 8 early birds: @mwess @markuspaluch @hanna @jberenike groceries

   Thur 9-17 Hackathon I
   
   Fri 9-14 Hackathon II


# Place
Basel; Library Room 216

# TeilnehmerInnen
Basel: JBH, GL, TS, and students from "Textanalyse mit R"

Gö: MP, MW, HV

FAU: TP
   
# Aims
Our general aim is to to advance POS annotion in KOLIMO https://kolimo.uni-goettingen.de/ to facilitate multivariate analyses of Literary/Nonliterary Narrative Texts 1800-1930.

[For background and first results see below]

Annotation
- Final numbers Eval moot 
- Final numbers reliability tests

eXistDB
- backend ingest

Open Corpus Workbench
- ingest data
- run analyses

Style Analysis
- POS distribution in KOLIMO: z.B. historische Variation und Literarizität 

#  Topics 

New manual annotation of GB and TG, based on moot output, including group discussion (possibly)

Tie up open strands POS-tagging
- Final Decisions
- Documentation
   - problem cases by categories
      - approximately 40 cases (=Tags)
   - addendum to STTS manual
      
eXist-data base
- Backend: Ingest POS-tags
- (possibly) Frontend: Updates; Collection Browser https://kolimo.uni-goettingen.de/browse.html
- Documentation

DTA Evaluation  
- tagger comparison
- coder comparison (reliability tests)

# Background
- We have a small gold standard ("Referenzstandard") for POS 1800-1930 DTA texts
- Unsere Ergebnisse zeigen trotz hochqualitativer Tokenisierung und Normalisierung des DTA eine Fehlerrate von ca. 9% an, die allerdings stark nach POS-Tag variiert. 
- Die Grundgesamtheit der aus dem DTA entnommenen Stichprobe umfasste N= 64 924 458 Tokens, die der händisch annotierten Tokens umfasste n= 9 065 Tokens/POS-Tags, also 0.014% 
- manual post-annotation of a randomly drawn sample of the DTA 
- period 1800-1930
- combined a tagger comparison with a manual analysis
- Die Stichprobe wurde in ihrer tokenisierten und normalisierten Form aus dem DTA übernommen (vgl. DTA). 
- Der Taggervergleich nutzte neben dem DTA-Tagger moot (Jurish & Würzner 2013) den TreeTagger (Schmid, 1994), MarMoT (Müller et al., 2013) sowie den Perceptron-Tagger (Rosenblatt, 1958).
- Tagset des STTS (Schiller et al., 1999) 
- Wo angezeigt, wurden im Projekt zusätzliche Regeln für der Handhabung des STTS-Manuals vereinbart und dokumentiert. Hierzu gehört auch u.a. die systematische Einbindung eines korpusbasierten Wörterbuchs (http://www.duden.de/) bei Eigennamen und Fremdwörtern.
- Das Tagging wurde in drei Phasen durchgeführt. Primäres Ziel des Taggings war es, die Genauigkeit von moot auf der genannten Stichprobe gegen manuelles und automatisches Tagging (TT, MarMot, Perceptron) zu evaluieren. 
   - Die Phase I diente neben der Erarbeitung und Ergänzung des Tagging-Manuals und dem Einarbeiten der Coder einer ersten quantitativen und qualitativen Analyse des moot-Taggings. __Die untersuchte Stichprobe umfasste N=100 randomisiert extrahierte Sätze (N=3.635 Tokens). Jedes Token wurde bezüglich des zugewiesenen POS-Tag durch alle Coder unabhängig überprüft und ggf. korrigiert.__
   - In Phase II wurden dieselben Coder, Tagger und dieselbe Software eingesetzt, ebenso wie die in Phase 1 erarbeiteten Tagging-Guidelines. Anders als in der ersten Phase wurden jedoch nicht ganze Sätze, sondern jeweils einhundert Token pro POS-Kategorie aus dem DTA extrahiert. Dadurch wurde eine Ungleichverteilung der einzelnen POS-Kategorien, welche in natürlichen Sätzen gegeben ist (vgl. Evert, 2006, Kilgarriff, 2005), vermieden. __Für fünfundfünfzig POS-Kategorien des STTS wurden jeweils n=100 Wort/Token-POS-Paare sortiert nach STTS-Tag annotiert. Dies entspricht einer Grundgesamtheit von N=5.500 Tokens. Jedes Token wurde von zwei Codern unabhängig annotiert.__
   - Phase III: Diskussionsphase --> hier wurden die strittigen Fälle besprochen und finale Annotationen erarbeitet. Zu diesem Zweck wurden Statistiken für die Tags (über Coder und Tagger) analysiert und Nichtübereinstimmung der vergebenen Tags identifiziert. Für die statistische Evaluation wurde die Interrater-Reliabilität als Agreement und Cohen‘s Kappa berechnet (Package „irr“ in R Version 3.3). Darüber hinaus wurde für die Phase I ein Fleiss’-Kappa für die Coder berechnet (dies steht für Phase 2 noch aus).
   
# Ziel
- Evaluation aller handgetaggten Daten (inges. 242 Tabellen)
   - final annos für 55 plus 138 von 220 Tabellen = 198 von 220 Tabellen liegen bereits vor, sind aber noch nicht in Statistik drin.
   - final annos für ca. 40 Problemfälle aus Phase II ( = 22 Tabellen von 220 Tabellen aus Phase II).
   
# bisherige Ergebnisse
   - Evaluation basiert für Phase I auf den finalen Annotationen / für Phase II zum momentanen Zeitpunkt auf etwa der Hälfte der finalen Annotation
      - Phase I: 22 Tabellen mit 3.635 Tokens (sind bereits in Evaluation eingegangen)
      - Phase II: 55 von 220 Tabellen/ n= 5500 von n = 22000 Tokens. D.h. eine Tabelle/100 Tokens von jeder POS-Kategorie ist bereits in Eval. eingegangen)
   - für moot verglichen mit dem Referenzstandard: Gesamtgenauigkeit von 90,16% (TreeTagger 80,88%; MarMoT 83,99%; Perceptron 79,75%).
   - niedrige Gesamtgenauigkeit gemessen an 98,6% zur modernen Standardvarietät (Brants, 2000), entspricht aber in etwa den von Scheible et al. (2011) für das Frühneuhochdeutsche erhobenen 91,6%. 
   - Die Übereinstimmung zwischen Codern vor der Diskussion und Referenzstandard ist hingegen vergleichsweise hoch, auch wenn sie in der zweiten Tagging-Phase etwas abfällt (Agreement Phase I = 95,47 – 98,13%, Agreement Phase II = 95,56 – 96,22%, Cohen‘s Kappa Phase I = 0,95 – 0,98, Cohen‘s Kappa Phase II = 0,95 – 0,96). Gleiches gilt für die Interrater-Reliabilität (Übereinstimmung zwischen Codern vor Diskussion) obwohl die Differenz zwischen den beiden Phasen größer ist (Agreement Phase I = 94,14 – 95,20%, Agreement Phase II = 89,45 – 92,64%, Cohen‘s Kappa Phase I = 0,94 – 0,95, Cohen‘s Kappa Phase II = 0,89 – 0,92). Das Fleiss’ Kappa weist mit 0,94 einen hohen Wert auf. Die Coder annotieren in beiden Phasen also genauer als moot. 
   - Für die einzelnen POS-Kategorien variiert die Genauigkeit zwischen 0% und 100%, wobei moot die höchste mittlere Genauigkeit (Mittelwert = 88,65%) und niedrigste Streuung (Standardabweichung = 17,25) aufweist (TreeTagger = 67,05 ± 28,52, MarMoT = 73,41 ± 27,49, Perceptron = 62,66 ± 31,37). Eine detaillierte Analyse der einzelnen POS-Tag-Kategorien zeigt, dass moot in den meisten, aber nicht allen, POS-Kategorien die besten Ergebnisse erzielt (vgl. Tabelle 1). 
   
Table 1: Accuracy  moot, TreeTagger, MarMoT and Perceptron per POS-Category [preliminary findings: Phase I and half of Phase II = 9 065 Tokens]

|      POS      	|     moot    	|    TreeTagger    	|    MarMoT    	|    Perceptron    	|
|:-------------:	|:-----------:	|:----------------:	|:------------:	|:----------------:	|
|    $,         	|    99,47    	|    100           	|    100       	|    100           	|
|    $.         	|    99,46    	|    100           	|    100       	|    100           	|
|    $(         	|    100      	|    39,06         	|    37,5      	|    32,81         	|
|    ADJA       	|    94,5     	|    93            	|    93,5      	|    95            	|
|    ADJD       	|    85,37    	|    79,67         	|    78,05     	|    76,42         	|
|    ADV        	|    81,2     	|    72,93         	|    75,56     	|    68,42         	|
|    APPO       	|    90,48    	|    71,43         	|    80,95     	|    28,57         	|
|    APPR       	|    96,31    	|    92,21         	|    90,98     	|    92,21         	|
|    APPRART    	|    96,77    	|    96,77         	|    93,55     	|    93,55         	|
|    APZR       	|    100      	|    69,57         	|    91,3      	|    73,91         	|
|    ART        	|    99,46    	|    98,92         	|    99,46     	|    99,46         	|
|    CARD       	|    86,57    	|    88,56         	|    91,54     	|    92,54         	|
|    FM         	|    72,73    	|    5,45          	|    45,45     	|    1,82          	|
|    FM.xy      	|    100      	|    0             	|    0         	|    0             	|
|    ITJ        	|    89,29    	|    57,14         	|    64,29     	|    0             	|
|    KOKOM      	|    49,02    	|    72,55         	|    56,86     	|    49,02         	|
|    KON        	|    91,53    	|    92,37         	|    90,68     	|    90,68         	|
|    KOUI       	|    100      	|    92,59         	|    85,19     	|    96,3          	|
|    KOUS       	|    76,56    	|    79,69         	|    71,88     	|    70,31         	|
|    NE        	|    75,25    	|    61,87         	|    63,55     	|    87,63         	|
|    NN         	|    92,81    	|    93,46         	|    92,32     	|    91,67         	|
|    PAV       	|    100      	|    92,31    	|    94,87    	|    84,62    	|
|    PDAT      	|    89,36    	|    53,19    	|    51,06    	|    46,81    	|
|    PDS       	|    74,42    	|    55,81    	|    65,12    	|    41,86    	|
|    PIAT      	|    91,89    	|    89,19    	|    81,08    	|    83,78    	|
|    PIDAT     	|    0        	|    0        	|    0        	|    0        	|
|    PIS       	|    77,42    	|    72,58    	|    83,87    	|    59,68    	|
|    PPER      	|    92,7     	|    83,21    	|    87,59    	|    87,59    	|
|    PPOSAT    	|    100      	|    60,34    	|    60,34    	|    63,79    	|
|    PPOSS     	|    96,15    	|    26,92    	|    3,85     	|    0        	|
|    PRELAT    	|    100      	|    62,5     	|    62,5     	|    66,67    	|
|    PRELS     	|    67,9     	|    77,78    	|    61,73    	|    60,49    	|
|    PRF       	|    94,44    	|    33,33    	|    33,33    	|    33,33    	|
|    PTKA      	|    100      	|    59,09    	|    95,45    	|    40,91    	|
|    PTKANT    	|    100      	|    70       	|    100      	|    40       	|
|    PTKNEG    	|    100      	|    100      	|    100      	|    100      	|
|    PTKVZ     	|    72,34    	|    72,34    	|    70,21    	|    59,57    	|
|    PTKZU     	|    97,87    	|    80,85    	|    100      	|    89,36    	|
|    PWAT      	|    100      	|    25       	|    100      	|    75       	|
|    PWAV      	|    100      	|    77,78    	|    88,89    	|    94,44    	|
|    PWS       	|    82,76    	|    68,97    	|    93,1     	|    86,21    	|
|    TRUNC     	|    100      	|    100      	|    100      	|    90       	|
|    VAFIN     	|    92,11    	|    80,7     	|    79,82    	|    76,32    	|
|    VAIMP     	|    95,24    	|    0        	|    0        	|    0        	|
|    VAINF     	|    100      	|    71,05    	|    76,32    	|    73,68    	|
|    VAPP      	|    100      	|    81,48    	|    85,19    	|    85,19    	|
|    VMFIN     	|    81,54    	|    81,54    	|    69,23    	|    69,23    	|
|    VMINF     	|    93,75    	|    75       	|    68,75    	|    62,5     	|
|    VMPP      	|    100      	|    20,83    	|    95,83    	|    54,17    	|
|    VVFIN     	|    87,5     	|    80,68    	|    84,09    	|    80,68    	|
|    VVIMP     	|    61,9     	|    28,57    	|    28,57    	|    9,52     	|
|    VVINF     	|    98,51    	|    71,64    	|    91,04    	|    64,18    	|
|    VVIZU     	|    100      	|    90       	|    86,67    	|    43,33    	|
|    VVPP      	|    94,32    	|    78,41    	|    90,91    	|    71,59    	|
|    XY        	|    56,6     	|    9,43     	|    45,28    	|    11,32    	|

# Identified problems

Taggers (z.B. bei Abkürzungen, Relativpronomen). 

STTS-Guideline nicht präzise genug (z.B. bei Vergleichspartikeln, Possessivpronomen, Indefinitpronomina). 

Dabei war die Analyse der Disagreements eine produktive Heuristik, um (computer-)linguistisch und literarturwissenschaftlich interessante Fälle aufzuwerfen. So scheint gerade in literarischen Fällen eine Ambiguität (etwa zwischen Adjektiv und Verb bei Partizipien) geradezu intentional. Ähnlich und in „Bravo! Warum denn nicht? Bravo! Und wieder Bravo!“ (Kafka, Der Prozess), welches als Konjunktion, aber auch als Diskurspartikel interpretiert werden kann.


# Literature

Biber, D., & Conrad, S. (2009). Register, genre, and style. Cambridge: Cambridge University Press.

Thorsten Brants. 2000. Inter-annotator Agreement for a German Newspaper Corpus. Proceedings of the Second International Conference on Language Resources and Evaluation (LREC-2000), Athens, Greece. European Language Resources Association (ELRA).

Brants, S., Dipper, S., Eisenberg, P., Hansen-Schirra, S., König, E., Lezius, W., Uszkoreit, H. (2004). TIGER: Linguistic Interpretation of a German Corpus. Research on Language and Computation, 2(4), 597–620.

Berlin-Brandenburgische Akademie der Wissenschaften. http://www.deutschestextarchiv.de/doku/software#cab. Deutsches Textarchiv. Online; accessed 24-May-2016.

Giesbrecht, Eugenie and Evert, Stefan (2009). Part-of-speech tagging - a solved task? An evaluation of POS taggers for the Web as corpus. In I. Alegria, I. Leturia, and S. Sharoff, editors, Proceedings of the 5th Web as Corpus Workshop (WAC5), San Sebastian, Spain.

Evert, Stefan. "How random is a corpus? The library metaphor."   Zeitschrift für Anglistik und Amerikanistik   54.2 (2006): 177-190.

Jurish, Bryan, and Kay-Michael Würzner. "Word and Sentence Tokenization with Hidden Markov Models."   JLCL   28.2 (2013): 61-83.

Kilgarriff, Adam. "Language is never, ever, ever, random."   Corpus linguistics and linguistic theory   1.2 (2005): 263-276.

Müller, Thomas, Helmut Schmid, and Hinrich Schütze. "Efficient higher-order CRFs for morphological Tagging."   Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing. 2013.

Rosenblatt, Frank. "The perceptron: A probabilistic model for information storage and organization in the brain."   Psychological review   65.6 (1958): 386.

Scheible, S., Whitt, R. J., Durrell, M., & Bennett, P. (2011). A Gold Standard Corpus of Early Modern German. Proceedings of the 5th Linguistic Annotation Workshop, 124–128.

Schmid, Helmut. "Probabilistic part-of speech Tagging using decision trees."   New methods in language processing. 2013.

Halteren, H., Daelemans, W., & Zavrel, J. (2001). Improving Accuracy in Word Class Tagging through the Combination of Machine Learning Systems. Computational Linguistics, 27.
