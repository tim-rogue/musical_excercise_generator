from excercise_generator_lilypond import randomNotes
from abjad import *
import copy



'''
print("^^^^^^ my program ^^^^^^^^^^^^^^^^^^")
#time-signature tuples
four_four = (4, 4)
time_signature = four_four
  
notes = randomNotes()
measure_string = notes.getRandomMeasureString(four_four,notes.minor_pentatonic_scale,'Bmin')
measure_string = "a'8 g'8 f'8 e'8"
print("this is the measure:")
print(measure_string)

#'''
print("------------------ online example -----------------")

#the numerical sum of notes in a bar.
# i.e for 4/4: 0.25 + 0.25 + 0.25 + 0.25 = 1
# i.e for 6/8: 0.125 + 0.125 + 0.125 + 0.125 + 0.125 + 0.125 = 0.75
four_four = 1

number_of_measures = 45
  
notes = randomNotes()
#measure_string = notes.getMeasure_IdenticalRhythmNoRests(four_four,notes.minor_pentatonic_scale,'Bmin','alto sax','8')
#measure_string = "c4 c4 c4 c4"
#print(measure_string)

score = Score([])
staff = Staff([])
score.append(staff)
key = notes.getRandomKey()

measures = []
for i in range(number_of_measures):
    measures.append(Measure((4, 4), []))
    staff.extend(measures)
    measure_string = notes.getMeasure_IdenticalRhythmNoRests(four_four,notes.minor_pentatonic_scale,key,'alto sax','8')
    measures[i].extend(measure_string)



# measures[0].extend(measure_string)
# measures[1].extend(measure_string)
# measures[2].extend(measure_string)
# measures[3].append(measure_string)
# measures[4].append(measure_string)

show(staff)




#'''
'''
upper_voice = Voice("b2", name='upper voice')
command = indicatortools.LilyPondCommand('voiceOne')
attach(command, upper_voice)
lower_voice = Voice("b4 a4", name='lower voice')
command = indicatortools.LilyPondCommand('voiceTwo')
attach(command, lower_voice)
lower_measures[3].extend([upper_voice, lower_voice])
lower_measures[3].is_simultaneous = True

upper_voice = Voice("b2", name='upper voice')
command = indicatortools.LilyPondCommand('voiceOne')
attach(command, upper_voice)
lower_voice = Voice("g2", name='lower voice')
command = indicatortools.LilyPondCommand('voiceTwo')
attach(command, lower_voice)
lower_measures[4].extend([upper_voice, lower_voice])
lower_measures[4].is_simultaneous = True
'''







'''
notes = randomNotes()
notes.printScaleAndIntervals(notes.minor_pentatonic_scale_tones,'Cmin')

for i in range(20):
     note = notes.getRandomScaleTone(notes.minor_pentatonic_scale_tones,'Cmin') 
     noteOctave = notes.assignOctave(note,'\'\'')      
     print('notes with rythem and octave %s' %notes.assignRythem(noteOctave,'8'))   
'''

''' 
abjad example snippets:

measure = Measure((4, 8), "c'8 d'8 e'8 f'8")
show(measure)

staff = Staff("c'8 d'8 e'8 f'8")
show(staff) 






'''