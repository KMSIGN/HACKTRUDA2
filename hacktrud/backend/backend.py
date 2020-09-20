import json
from backend.hhparser import parsehh
from string import punctuation
from typing import List
import os
import numpy as np
import nltk

from nltk.corpus import stopwords
import rutermextract
from pymystem3 import Mystem


class HHParser:
    def __init__(self) -> None:
        self.mystem = Mystem()
        self.term_extractor = rutermextract.TermExtractor()
        self.russian_stopwords = stopwords.words("russian")
        with open(os.path.dirname(os.path.realpath(__file__)) + '/models.json', 'rb') as file:
            self.models = dict(json.load(file))
        nltk.download("stopwords")

    def preprocess_text(self, text: str, word_limit: int):
        tokens = self.mystem.lemmatize(text.lower())
        tokens = [token.split(" ") for token in tokens]
        tokens = np.concatenate(tokens)
        tokens = [token.strip() for token in tokens if token not in self.russian_stopwords \
                  and token != " " \
                  and token.strip() not in punctuation]
        text = " ".join(tokens)
        terms = self.term_extractor(text, limit=word_limit, strings=True)

        return terms

    def answer_questions(self, uid: str, questions: List[str]):
        answers = {}
        for question in questions:
            question_terms = self.preprocess_text(question, 2)
            answer = parsehh(uid, question_terms=question_terms)
            if answer is not None and answer is not {}:
                answers[question] = answer
        return answers
