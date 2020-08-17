from nhs import get_list, get_common_questions, get_section
import sys
import re

def speak(msg):
    print('\tawesomebot\t> ' + msg)

medecines = get_list('medicines')
conditions = get_list('conditions')

subject = ''
subject_type = ''
raw_input = ''

while raw_input != 'exit':                                  # use dictionary of exit words and look for them in raw_input

    if subject == '':
        speak('Hello, I\'m awesomebot, ask me anything about medecines !')

    raw_input = input('\tuser\t\t> ')

    if raw_input == 'exit':
        break
    
    raw_input = raw_input.lower()                           # sanitize input
    raw_input = re.sub(r'[^A-Za-z0-9 ]+', '', raw_input)

    # for each word, compare them with medecines list and conditions list
    stop = False
    for word in raw_input.split(' '):
        for medecine in medecines:
            if word in medecine.split(' '):
                subject = medecine
                subject_type = 'medecine'
                speak('* subject is ' + medecine + ' *')
                stop = True
                break
        '''for condition in conditions:
            if word in condition.split(' '):
                subject = condition
                subject_type = 'condition'
                stop = True
                break'''
        if stop == True:
            break
    
    if subject != '':
        # try to find matching section
        # if not talk about presentation or key fact ?
        if subject_type == 'medecine':
            common_questions = get_common_questions(subject)
            for question in common_questions:
                pass
            about = get_section(subject, '1')
            speak(about)

speak('Bye !')