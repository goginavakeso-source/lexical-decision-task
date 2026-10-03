from psychopy import core, visual, event
import random
import csv
import time

results = 'characters,isWord,correct,reactionTime,\n'

with open('conditions.csv', newline='') as csvfile:
    
    #read and convert to list
    conditions = list(csv.reader(csvfile)) 
    
    #remove header
    conditions.pop(0)
    
    random.shuffle(conditions)
    
    conditionsCount = len(conditions)

window = visual.Window(size=(800, 700), color='black')

welcome = '''
Welcome to the lexical decision task.

You are about to see a series of characters.

If the  characters make up a word,
press the RIGHT arrow key.

If the characters do not make up a word, 
press the LEFT arrow key.

Press SPACE to begin.
'''

instructions = visual.TextStim(window, color='white', text=welcome, units='pix', height=20)

instructions.draw()
window.flip()
event.waitKeys(keyList=['space'])

#trials
for index,condition in enumerate(conditions):
    
    characters = condition[0]
    isWord = int(condition[1])
    
    #define stimulus
    word = visual.TextStim(window, color='white', text=characters, units='pix', height=40)
    
    #display stimulus
    word.draw()
    window.flip()
    
    #start timer
    startTime = core.getTime()
    
    response = event.waitKeys(keyList=['right', 'left'])
    
    #calculate reaction time
    reactionTime = core.getTime() - startTime
    
    #response accuracy
    if(isWord == 1 and response[0] == 'right'):
        correct = 1
    elif(isWord == 0 and response[0] == 'left'):
        correct = 1
    else:
        correct = 0
        
    results += characters + ',' + str(isWord) + ',' + str(correct) + ',' + str(reactionTime) + '\n'

    # pause before next stimulus excluding the last condition
    if(index != conditionsCount - 1):
        pause = visual.TextStim(window, color='white', text='+', units='pix', height=40)
        pause.draw()
        window.flip()
        core.wait(1)

with open('results-' + str(time.time()) + '.csv', 'w') as file:
    file.write(results)
    
print(results)

exitText = visual.TextStim(window, color='white', text='Thank you for participating! \n\n press SPACE to exit,', units='pix', height=20)
exitText.draw()
window.flip()
event.waitKeys(keyList=['space'])


window.close()
core.quit()