#!/usr/bin/env python3

import argparse
import os
import xml.etree.ElementTree


def arguments():
    parser = argparse.ArgumentParser("Convert tcf files to vrt files suitable to import in CWB")
    parser.add_argument("TCF", type=os.path.abspath, help="Input file in tcf format")
    args = parser.parse_args()
    return args


def parse_file(filename):
    tree = xml.etree.ElementTree.parse(filename)
    root = tree.getroot()
    print(root.findall("*"))
    corpus = root.find("{http://www.dspin.de/data/textcorpus}TextCorpus")
    language = corpus.attrib["lang"]
    tokens = {}
    for token in corpus.findall("{http://www.dspin.de/data/textcorpus}tokens/{http://www.dspin.de/data/textcorpus}token"):
        tokens[token.attrib["ID"]] = token.text
    sentences = []
    for sentence in corpus.findall("{http://www.dspin.de/data/textcorpus}sentences/{http://www.dspin.de/data/textcorpus}sentence"):
        sentences.append((sentence.attrib["ID"], sentence.attrib["tokenIDs"].split()))
    lemmata = {}
    for lemma in corpus.findall("{http://www.dspin.de/data/textcorpus}lemmas/{http://www.dspin.de/data/textcorpus}lemma"):
        lemmata[lemma.attrib["tokenIDs"]] = lemma.text
    pos_tags = {}
    for pos_tag in corpus.findall("{http://www.dspin.de/data/textcorpus}POStags/{http://www.dspin.de/data/textcorpus}tag"):
        pos_tags[pos_tag.attrib["tokenIDs"]] = pos_tag.text
    print(pos_tags)
    corrections = {}
    for correction in corpus.findall("{http://www.dspin.de/data/textcorpus}orthography/{http://www.dspin.de/data/textcorpus}correction"):
        corrections[correction.attrib["tokenIDs"]] = correction.text
    return language, tokens, sentences, lemmata, pos_tags, corrections


def main():
    args = arguments()
    assert os.path.isfile(args.TCF)
    mapping = {"ADJA": "ADJ", "ADJD": "ADJ", "ADV": "ADV", "APPO":
               "ADP", "APPR": "ADP", "APPRART": "ADP", "APZR": "ADP", "ART": "DET",
               "CARD": "NUM", "FM": "X", "ITJ": "INTJ", "KOKOM": "ADP", "KON":
               "CCONJ", "KOUI": "SCONJ", "KOUS": "SCONJ", "NE": "PROPN", "NN":
               "NOUN", "PDAT": "DET", "PDS": "PRON", "PIAT": "DET", "PIDAT": "ADJ",
               "PIS": "PRON", "PPER": "PRON", "PPOSAT": "PRON", "PPOSS": "PRON",
               "PRELAT": "DET", "PRELS": "PRON", "PRF": "PRON", "PAV": "ADV", "PROP": "ADV",
               "PTKA": "ADV", "PTKANT": "INTJ", "PTKNEG": "PART", "PTKVZ": "ADP",
               "PTKZU": "PART", "PWAT": "DET", "PWAV": "ADV", "PWS": "PRON", "TRUNC":
               "NOUN", "VAFIN": "AUX", "VAIMP": "AUX", "VAINF": "AUX", "VAPP": "AUX",
               "VMFIN": "AUX", "VMINF": "AUX", "VMPP": "AUX", "VVFIN": "VERB",
               "VVIMP": "VERB", "VVINF": "VERB", "VVIZU": "VERB", "VVPP": "VERB",
               "XY": "X", "$,": "PUNCT", "$.": "PUNCT", "$(": "PUNCT"}
    language, tokens, sentences, lemmata, pos_tags, corrections = parse_file(args.TCF)
    tokens_in_sentences = set()
    basename = os.path.basename(args.TCF)
    with open(basename + ".vrt", mode="w") as out:
        print('<text id="t%s" lang="%s">' % (basename, language))
        for sentence_id, token_ids in sentences:
            print('<s id="t%s-%s">' % (basename, sentence_id))
            for token_id in token_ids:
                tokens_in_sentences.add(token_id)
                pos = pos_tags[token_id]
                lemma = lemmata[token_id]
                wc = mapping[pos]
                print("\t".join((tokens[token_id], pos, lemma, wc, "%s_%s" % (lemma, wc), corrections.get(token_id, ""))))
            print("</s>")
        print("</text>")
    assert tokens_in_sentences == set(tokens.keys())


if __name__ == "__main__":
    main()
