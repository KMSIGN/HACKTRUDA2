import json
from backend.hhparser import parsehh
from string import punctuation
from typing import List
import os
import numpy as np

import nltk

nltk.download("stopwords")
from nltk.corpus import stopwords

russian_stopwords = stopwords.words("russian")

import rutermextract

term_extractor = rutermextract.TermExtractor()

from pymystem3 import Mystem

mystem = Mystem()

with open(os.path.dirname(os.path.realpath(__file__)) + '/models.json', 'rb') as file:
    models = dict(json.load(file))


def preprocess_text(text: str, word_limit: int):
    tokens = mystem.lemmatize(text.lower())
    tokens = [token.split(" ") for token in tokens]
    tokens = np.concatenate(tokens)
    tokens = [token.strip() for token in tokens if token not in russian_stopwords \
              and token != " " \
              and token.strip() not in punctuation]
    text = " ".join(tokens)
    terms = term_extractor(text, limit=word_limit, strings=True)

    return terms


def answer_questions(uid: str, questions: List[str]):
    answers = {}
    for question in questions:
        question_terms = preprocess_text(question, 2)
        answer = parsehh(uid, question_terms=question_terms)
        if answer is not None and answer is not {}:
            answers[question] = answer
