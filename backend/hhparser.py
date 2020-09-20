from typing import List, Union, Dict

import numpy as np
import multiprocessing

from selenium import webdriver

from bs4 import BeautifulSoup
import unicodedata

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

base_url = "https://spb.hh.ru/resume/"

options = Options()
options.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


def salary(content) -> int:
    soup = BeautifulSoup(content)
    text = soup.find('span',
                     {
                         'class': 'resume-block__salary resume-block__title-text_salary',
                         "data-qa": "resume-block-salary"
                     }).text
    text = unicodedata.normalize('NFKD', text)
    salary_list = [char for char in text if char.isdigit()]
    return int(''.join(salary_list))


def work_exp(content) -> str:
    soup = BeautifulSoup(content)
    text = soup.find('span', {
        'class': 'resume-block__title-text resume-block__title-text_sub'
    }).text

    text = unicodedata.normalize('NFKD', text)
    return text.replace('Опыт работы', '').strip()


def drive_exp(content) -> str:
    soup = BeautifulSoup(content)
    div = soup.find_all('div', {
        'data-qa': 'resume-block-driver-experience'
    })[0]
    text = div.find_all('div', {'class': 'resume-block-item-gap'})[0].text
    text = unicodedata.normalize('NFKD', text)
    return text.strip()


def education(content) -> str:
    soup = BeautifulSoup(content)
    div = soup.find_all('div', {
        'data-qa': 'resume-block-education'
    })[0]
    text = div.find_all('div', {'class': 'resume-block-item-gap'})[0].text
    text = unicodedata.normalize('NFKD', text)
    return text.strip()


def employment(content) -> str:
    soup = BeautifulSoup(content)
    div = soup.find_all('div', {
        'data-qa': 'resume-block-position',
        'class': 'resume-block',
    })[0]
    text = div.find_all('div', {'class': 'resume-block-item-gap'})[0].div.div.p.text
    text = unicodedata.normalize('NFKD', text)

    return text.replace('Занятость:', '').strip()


def schedule(content) -> str:
    soup = BeautifulSoup(content)
    div = soup.find_all('div', {
        'data-qa': 'resume-block-position',
        'class': 'resume-block',
    })[0]
    text = div.find_all('div', {'class': 'resume-block-item-gap'})[0].div.div.find_all('p')[1].text
    text = unicodedata.normalize('NFKD', text)

    return text.replace('График работы:', '').strip()


term_parsers = {
    'зарплата': salary,
    'зп': salary,
    'опыт работы': work_exp,
    'опыт': work_exp,
    'опыт вождения': drive_exp,
    'образование': education,
    'занятость': employment,
    'график': schedule
}


def parse_question(name, content):
    output = {}
    if name in term_parsers.keys():
        name_term = term_parsers[name](content)
        if type(name_term) is str:
            name_term = name_term.lower()
        output[name] = name_term
    return output


def parsehh(uid: str, question_terms=term_parsers.keys()) -> Union[Dict[str, Union[int, str]], None]:
    driver.get(base_url + uid)
    content = driver.page_source
    output = {}
    question_terms = np.concatenate([word.split(' ') for word in question_terms] + [question_terms])
    print(question_terms)
    for name in question_terms:
        try:
            output.update(parse_question(name, content))
        except:
            pass
    return output
