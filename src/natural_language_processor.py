from typing import List

from spacy import load


class NLP:
    def __init__(self, model: str):
        self.nlp = load(model)
        self.doc = None

    def read_text(self, text: str):
        self.doc = self.nlp(text)

    def extract_words(self, ignore_proper_nouns: bool = False) -> List[str]:
        words = []
        for token in self.doc:
            word = token.text
            if not (token.is_punct or token.is_space):
                if ignore_proper_nouns:
                    if token.pos_ == "PROPN":
                        words.append(word)
                else:
                    words.append(word)
        return words

    def extract_base_words(self, ignore_proper_nouns: bool = False) -> List[str]:
        words = []
        for token in self.doc:
            word = token.lemma_
            if not (token.is_punct or token.is_space):
                if ignore_proper_nouns:
                    if token.pos_ != "PROPN":
                        words.append(word)
                else:
                    words.append(word)
        return words
