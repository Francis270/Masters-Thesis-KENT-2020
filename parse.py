from bs4 import BeautifulSoup
from nhs import get_list
import requests
import os

def get_list_url(subject):
    raw = get_list(subject)
    names = []
    for medicine in raw:
        names.append({'name': medicine, 'url': medicine.replace('(', '').replace(')', '').replace(' ', '-')})
    return names

def get_content(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    content = ''
    return content

def get_all_content(subject):
    contents = {}
    topics = get_list_url(subject)
    for topic in topics:
        url = 'https://www.nhs.uk/' + subject + '/' + topic['url']
        content = get_content(url)
        contents[topic['name']] = content
    return contents

def save(subject_type, subject, content):
    if not os.path.exists(subject_type):
        os.makedirs(subject_type)
    with open(subject_type + '/' + subject.replace('/', ' ').replace('"', '') + '.txt', 'a') as fd:
        fd.write(content)

def save_list(xlist, subject_type):
    for item in xlist:
        save(subject_type, item, xlist[item])

medicines = get_all_content('medicines')
conditions = get_all_content('conditions')

save_list(medicines, 'medicines')
save_list(conditions, 'conditions')