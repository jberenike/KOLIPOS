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
    corpus = root.find("{http://www.dspin.de/data/textcorpus}TextCorpus")
    tokens = {}
    for token in corpus.findall("{http://www.dspin.de/data/textcorpus}tokens/{http://www.dspin.de/data/textcorpus}token"):
        tokens[token.attrib["ID"]] = token.text
    sentences = []
    for sentence in corpus.findall("{http://www.dspin.de/data/textcorpus}sentences/{http://www.dspin.de/data/textcorpus}sentence"):
        sentences.append((sentence.attrib["ID"], sentence.attrib["tokenIDs"].split()))
    return tokens, sentences


def main():
    args = arguments()
    assert os.path.isfile(args.TCF)
    tokens, sentences = parse_file(args.TCF)
    for sentence_id, token_ids in sentences:
        print(" ".join((tokens[tid] for tid in token_ids)))


if __name__ == "__main__":
    main()
