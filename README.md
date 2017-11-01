## KOLIPOS
Hackathon for advancing POS-annotation in KOLIMO

# Date 
7-8 December 2017
# Place
Basel; Library Room 216

# TeilnehmerInnen
Basel: JBH, GL, 

Gö: MP, MW, evtl. FM

NN.
   
# Aims
Our general aim is to to advance POS annotion in KOLIMO https://kolimo.uni-goettingen.de/ to facilitate multivariate analyses of Literary/Nonliterary Narrative Texts 1800-1930.

[For background and first results see below]

Annotation
- Final numbers Eval moot 
- Final numbers reliability tests

Analysis
- POS distribution in KOLIMO


# Topics

New manual annotation of GB and TG, based on moot output, including group discussion (possibly)

Tie up open strands
   - Final Decisions
   - Documentation
      - problem cases by categories
      - addendum to STTS manual
    - Ingest POS-tags into eXist-data base
    
DTA Evaluation  
    - tagger comparison
    - coder comparison (reliability tests)

Quantitative text analyses (possibly)
   - POS distribution in KOLIMO
    - descriptive analyses & inferential stats
    - MD analyses

# Background
- We have a small gold standard ("Referenzstandard") for POS 1800-1930 DTA texts
  - Die Grundgesamtheit der aus dem DTA entnommenen Stichprobe umfasste N= 64 924 458 Tokens, die der händisch annotierten Tokens umfasste n= 9 065 Tokens/POS-Tags, also 0.014% 
   - manual post-annotation of a randomly drawn sample of the DTA 
   - period 1800-1930
   - combined a tagger comparison with a manual analysis
   - Die Stichprobe wurde in ihrer tokenisierten und normalisierten Form aus dem DTA übernommen (vgl. DTA). 
   - Der Taggervergleich nutzte neben dem DTA-Tagger moot (Jurish & Würzner 2013) den TreeTagger (Schmid, 1994), MarMoT (Müller et al., 2013) sowie den Perceptron-Tagger (Rosenblatt, 1958).
   - Tagset des STTS (Schiller et al., 1999) 
   - Wo angezeigt, wurden im Projekt zusätzliche Regeln für der Handhabung des STTS-Manuals vereinbart und dokumentiert. Hierzu gehört auch u.a. die systematische Einbindung eines korpusbasierten Wörterbuchs (http://www.duden.de/) bei Eigennamen und Fremdwörtern.
- Das Tagging wurde in drei Phasen durchgeführt. Primäres Ziel des Taggings war es, die Genauigkeit von moot auf der genannten Stichprobe gegen manuelles und automatisches Tagging (TT, MarMot, Perceptron) zu evaluieren. 
   - Die Phase I diente neben der Erarbeitung und Ergänzung des Tagging-Manuals und dem Einarbeiten der Coder einer ersten quantitativen und qualitativen Analyse des moot-Taggings. Die untersuchte Stichprobe umfasste N=100 randomisiert extrahierte Sätze (N=3.635 Tokens). Jedes Token wurde bezüglich des zugewiesenen POS-Tag durch alle Coder unabhängig überprüft und ggf. korrigiert.
   - In Phase II wurden dieselben Coder, Tagger und dieselbe Software eingesetzt, ebenso wie die in Phase 1 erarbeiteten Tagging-Guidelines. Anders als in der ersten Phase wurden jedoch nicht ganze Sätze, sondern jeweils einhundert Token pro POS-Kategorie aus dem DTA extrahiert. Dadurch wurde eine Ungleichverteilung der einzelnen POS-Kategorien, welche in natürlichen Sätzen gegeben ist (vgl. Evert, 2006, Kilgarriff, 2005), vermieden. Für fünfundfünfzig POS-Kategorien des STTS wurden jeweils n=100 Wort/Token-POS-Paare sortiert nach STTS-Tag annotiert. Dies entspricht einer Grundgesamtheit von N=5.500 Tokens. Jedes Token wurde von zwei Codern unabhängig annotiert.
   - Phase III: Diskussionsphase --> hier wurden die strittigen Fälle besprochen und finale Annotationen erarbeitet. Zu diesem Zweck wurden Statistiken für die Tags (über Coder und Tagger) analysiert und Nichtübereinstimmung der vergebenen Tags identifiziert. Für die statistische Evaluation wurde die Interrater-Reliabilität als Agreement und Cohen‘s Kappa berechnet (Package „irr“ in R Version 3.3). Darüber hinaus wurde für die Phase I ein Fleiss’-Kappa für die Coder berechnet (dies steht für Phase 2 noch aus).
   
# bisherige Ergebnisse
   - basieren für Phase I auf den finalen Annotationen / für Phase II zum momentanen Zeitpunkt auf etwa der Hälfte der finalen Annotation
   - für moot verglichen mit dem Referenzstandard: Gesamtgenauigkeit von 90,16% (TreeTagger 80,88%; MarMoT 83,99%; Perceptron 79,75%).
   - Dies ist eine niedrige Gesamtgenauigkeit gemessen an 98,6% zur modernen Standardvarietät (Brants, 2000), entspricht aber in etwa den von Scheible et al. (2011) für das Frühneuhochdeutsche erhobenen 91,6%. 
   - Die Übereinstimmung zwischen Codern vor der Diskussion und Referenzstandard ist hingegen vergleichsweise hoch, auch wenn sie in der zweiten Tagging-Phase etwas abfällt (Agreement Phase I = 95,47 – 98,13%, Agreement Phase II = 95,56 – 96,22%, Cohen‘s Kappa Phase I = 0,95 – 0,98, Cohen‘s Kappa Phase II = 0,95 – 0,96). Gleiches gilt für die Interrater-Reliabilität (Übereinstimmung zwischen Codern vor Diskussion) obwohl die Differenz zwischen den beiden Phasen größer ist (Agreement Phase I = 94,14 – 95,20%, Agreement Phase II = 89,45 – 92,64%, Cohen‘s Kappa Phase I = 0,94 – 0,95, Cohen‘s Kappa Phase II = 0,89 – 0,92). Das Fleiss’ Kappa weist mit 0,94 einen hohen Wert auf. Die Coder annotieren in beiden Phasen also genauer als moot. 
   - Für die einzelnen POS-Kategorien variiert die Genauigkeit zwischen 0% und 100%, wobei moot die höchste mittlere Genauigkeit (Mittelwert = 88,65%) und niedrigste Streuung (Standardabweichung = 17,25) aufweist (TreeTagger = 67,05 ± 28,52, MarMoT = 73,41 ± 27,49, Perceptron = 62,66 ± 31,37). Eine detaillierte Analyse der einzelnen POS-Tag-Kategorien zeigt, dass moot in den meisten, aber nicht allen, POS-Kategorien die besten Ergebnisse erzielt (vgl. Tabelle 2). 
