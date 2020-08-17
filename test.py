from subject import Subject
import numpy as np
import os

def speak(msg):
    print('\tawesomebot\t> ' + msg)

def load_files(subject_type):
    topics = {}
    for filename in os.listdir(subject_type):
        filename = filename.replace('.txt', '')
        path = subject_type + '/' + filename + '.txt'
        topics[filename] = Subject(filename, subject_type)
    return topics

subjects = {}
subjects_list = []

'''      SUBJECT IMPORT       '''

# Load all conditions and medicines looping into conditions/medicines folders
conditions = load_files('conditions')
medicines = load_files('medicines')
subjects = {**conditions, **medicines}

'''      SUBJECT IMPORT       '''

for subject in subjects:
    subjects_list.append(subject)

flag = True
speak('Hello, I\'m awesomebot, ask me anything about medecines or conditions!')

curr_subject = ''

while flag == True:
    user_response = input('\tuser\t\t> ')
    user_response = user_response.lower()
    
    for word in user_response.split(' '):
        for subject in subjects_list:
            if word == subject.split(' ')[0]:
                if subject != curr_subject:
                    curr_subject = subject
                    print('\t[DEBUG]\t\t> new subject :' + curr_subject)
                    break

    if 'bye' not in user_response:
        if curr_subject == '':
            speak('On what medicine or condition do you want to talk about ?')
        else:
            speak(subjects[curr_subject].response(user_response))
            subjects[curr_subject].sent_tokens.remove(user_response)
    else:
        flag = False
        speak('Take care !')