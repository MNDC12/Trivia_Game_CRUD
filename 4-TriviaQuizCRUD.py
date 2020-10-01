# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 09:41:14 2020
Last Edit on Tue Sep 22
@author: Mary PC
Objective: Trivia Quiz
"""
from random import choice
import time
import csv
import json

Quest_Ans = {'woody':'What is the name of the toy cowboy in Toy Story? ',
       'k':'What is the symbol for potassium? ',
       'earth':'What is the 3rd planet from the sun? ',
       'heart':'Which organ has four chambers? ',
       'beyonce':' Which musical legend is Jay-Z married to? ',
       'stairs':'What goes up and down, but still remains in the same place? ',
       'butterfly':'What does a caterpillar turn into? ',
       'aassia':'What is the largest cntnnt in the world? ',
       }

exclaim = {'right':['Wow! You got it correct!',
                      'You are awesome! Your answer is correct.',
                      'Amazing! You\'re correct!',
                      'You are doing great! Keep it up!',
                      'You\'re correct! You\'re doing a good job!'],
           'wrong':['Sad. You are wrong.',
                    'You are wrong but that is okay!',
                    'Aww. It is wrong!',
                    'Your answer is not correct.',
                    'This is wrong but it\'s fine!'],
           }

name_list = []; score_list = []

def check(ask):
    ans = input(ask).title()
    while ans not in ['Yes','No']:
        print('Hmm. Something is wrong. Check your spelling!')
        print('Here, try again.') 
        ans = input(ask).title()
    return ans

def game(Exclaim=exclaim, score = 0):
    global Quest_Ans
    print('\nWelcome to the Ultimate Trivia Game!') 
    
    ready = check('Are you ready (\'Yes\' or \'No\')? ')
    if ready == 'No': return print('Okay! See you later~')
    
    name = input('Enter your name: ')
    name_list.append(name)   
    print('Let us begin!')
    
    for correct in Quest_Ans:
        answer = input(Quest_Ans[correct]).lower()
        if answer == correct: 
            print(choice(Exclaim['right'])); score += 1
        else: print(choice(Exclaim['wrong']))  
    
    total = len(Quest_Ans)
    print('\nYou answered %d out of %d questions correct.'%(score,total))
    if score <= (total/2): print('You failed but that\'s okay.')
    elif score == total: print('Wow! You got a perfect score!')
    else: print('Nice. You did a good job!')
    
    score_list.append(score)
    
    again = check('Do you want to try again (\'Yes\' or \'No\')? ')
    if again == 'Yes': return game()
    print('Okay! Thank you for answering~')
    
def take(last, players = name_list,scores = score_list):
    print('The last %d players are:' % last)
    newp = players[-last:]; news = scores[-last:]
    for i in range(last):
        print('NAME: {}'.format(newp[i]))
        print('SCORE: {}\n'.format(str(news[i])))
        
def buffer(string1,string2):
    print('NOW %s...'%string1); time.sleep(1)
    print('SUCCESSFULLY %s!'%string2); time.sleep(1)
    
def CRUD():
    global Quest_Ans
    
    print('\nCurrently, the questions and answer are the following:\n'); time.sleep(1)
    for ans, que in Quest_Ans.items():
        print('Question: %s'%que)
        print('Answer: %s'%ans)
    time.sleep(1)
    
    action = str(input('What do you want to do? [\'create\', \'retrieve\', \'update\', \'delete\' or \'quit\'] ')).lower()
    
    if action == 'delete':
        answer = str(input('What is the answer to the Q&A you want to delete? ')).lower()
        del Quest_Ans[answer]; buffer('DELETING','DELETED') 
        
    elif action == 'create':
        question = str(input('What is the question you want to add? '))
        answer = str(input('What is the answer to the question you want to add? ')).lower()
        Quest_Ans[answer]=question; buffer('CREATING','CREATED')
        
    elif action == 'update':
        answer = str(input('What is the answer to the Q&A you want to update? ')).lower()
        action2 = str(input('Update \'answer\' or \'question\'? ')).lower()
        if action2 == 'answer':
            new = str(input('Update \'%s\' into? '% answer))
            Quest_Ans[new] = Quest_Ans[answer]
            del Quest_Ans[answer]; buffer('UPDATING','UPDATED')
        elif action2 == 'question':
            new = str(input('Update \'%s\' into? '% Quest_Ans[answer]))
            Quest_Ans[answer]= new; buffer('UPDATING','UPDATED')
        else: print('CRUD does not understand. Please repeat again.')
        
    elif action == 'retrieve':
        ftype = str(input('Enter filetype [\'txt\' or \'csv\']: '))
        fname = str(input('Enter filename: '))
        f = fname + '.' + ftype
        if ftype == 'csv':
            w = csv.writer(open(f, "w"))
            for key, val in Quest_Ans.items():
                w.writerow([key, val])
            buffer('RETRIEVING','RETRIEVED')
        elif ftype == 'txt':
            file = open(f,"w")
            file.write(str(Quest_Ans))
            file.close(); buffer('RETRIEVING','RETRIEVED')
        else: print('Filetype unavailable.')
        
    elif action == 'quit':
        return print('Thank you for using CRUD!')
    
    else:
        print('CRUD does not understand. Please repeat again.')
    CRUD()
        
    
        


    

    
    
    
    