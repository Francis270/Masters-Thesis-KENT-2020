from bs4 import BeautifulSoup
import requests

def get_list(what):
    xlist = []
    page = requests.get('https://www.nhs.uk/' + what + '/')
    soup = BeautifulSoup(page.text, 'html.parser')
    name_list = soup.find_all('a', {'nhsuk-list-panel__link'})
    for item in name_list:
        xlist.append(item.getText().lower())
    return xlist

def get_common_questions(what):
    questions = {}
    what = what.replace('(', '').replace(')', '').replace(' ', '-')
    page = requests.get('https://www.nhs.uk/medicines/' + what + '/')
    soup = BeautifulSoup(page.text, 'html.parser')
    name_list = soup.find_all('div', {'block-question'})
    for item in name_list:
        question_ = item.find('span', {'nhsuk-details__summary-text'}).getText().replace('\n', '').split(' ')
        question_ = list(filter(None, question_))
        question = ''
        for word in question_:
            if len(question) != 0:
                question += ' '
            question += word
        text_ = item.find('div', {'nhsuk-details__text'}).getText().replace('\n', '').split(' ')
        text_ = list(filter(None, text_))
        text = ''
        for word in text_:
            if len(text) != 0:
                text += ' '
            text += word
        questions[question] = text
    return questions

def get_section(medicine, section):
    text = ''
    medicine = medicine.replace('(', '').replace(')', '').replace(' ', '-')
    page = requests.get('https://www.nhs.uk/medicines/' + medicine + '/')
    soup = BeautifulSoup(page.text, 'html.parser')
    name_list = soup.find_all('section', {})
    for item in name_list:
        if item.find_all('h2', {})[0].getText()[0] == section:
            text = item.find('div', {'block-richtext'}).getText()
            break
        #print(item.find('div', {'block-richtext'}).getText())
    return text