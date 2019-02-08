import random
import re


class randomNotes:

    #intervals mapped to scale tones of the chromatic scale
    #i.e root is 0 semi-tones away from the root, a Perfect 5th is 8 semi-tones away from the root
    chromatic_scale_tones= {'root':0,'-2':1,'+2':2,'-3':3,'+3':4,'P4':5,'x4/b5':6,'P5':7,'-6':8,'+6':9,'-7':10,'+7':11}

    # a dictionary mapping a Key's chromatic distance from C as a number, used as an offset.
    # i.e the key of C is 0 semi-tones away from the key of C, the key of F is 5 semitones away from C
    key_dict = {'Cmaj':0,'Cmin':0,'C#maj':1,'C#min':1, 'Dbmaj':1,'Dmaj':2,'Dmin':2,'D#min':3\
               ,'Ebmaj':3,'Ebmin':3,'Emaj':4,'Emin':4,'Fmaj':5,'Fmin':5,'F#maj':6,'F#min':6\
               ,'Gbmaj':6,'Gmaj':7,'Gmin':7,'G#min':8,'Abmaj':8,'Abmin':8,'Amaj':9,'Amin':9\
               ,'A#min':10,'Bbmaj':10,'Bbmin':10,'Bmaj':11,'Bmin':11}
    
    #list of string lilypond uses as rythmic values
    #list_of_rhythmic_values = ['1','2','4','8','16','32']
    list_of_rhythmic_values = ['4','8','16','32']
    
    #list_of_octave_symbols = [',,',',','','\'','\'\'','\'\'\'']
    list_of_octave_symbols = ['','\'','\'\'','\'\'\'']

    #two lists of notes in the format that lilypond uses to be compiled as notes on a page
    # the 'is' siffix means sharp, the 'es' suffix means flat
    chromatic_sharp_list = ['c','cs','d','ds','e','f','fs','g','gs','a','as','b']
    chromatic_flat_list =  ['c','df','d','ef','e','f','gf','g','af','a','bf','b']

    #list containing string of all the sharp and flat keys
    listOfSharpKeys = ['Gmaj','Dmaj','Amaj','Emaj','Bmaj','F#maj','C#maj'\
                      ,'Emin','Bmin','F#min','C#min','D#min','A#min']
                      
    listOfFlatKeys = ['Fmaj','Bbmaj','Ebmaj','Abmaj','Dbmaj','Gbmaj'\
                      ,'Cbmaj','Dmin','Gmin','Cmin','Fmin','Bbmin','Ebmin','Abmin']
    
    # a list containing the intervals of the minor pentatonic scale. not really necessary, but helps with readability
    minor_pentatonic_scale= [chromatic_scale_tones['root'],chromatic_scale_tones['-3'],chromatic_scale_tones['P4']\
                                   ,chromatic_scale_tones['P5'],chromatic_scale_tones['-7']]

    #number of notes in the minor pentatonic scale
    NUM_PENTATONIC_SCALE_TONES = 5
    
    #notes in the current octave configuration that are outside the range of my sax playing
    alto_sax_below_range = ['cs','a','af','gs','g','gf','fs','f','e','ef','ds','d','df']
    alto_sax_above_range = ['b\'\'\'','bf\'\'\'','as\'\'\'','a\'\'\'','af\'\'\'','gs\'\'\'','g\'\'\'','gf\'\'\'','fs\'\'\'',] 

    
    def __inti__(self):
        
        self.current_note = ''
    
    
    #get a random scale tone within an octave
    # 
    def getRandomScaleTone(self,scale,key,range):

    
        #print("number of notes in first octave: %d" %first_octave)
        #get a random integer between 0 and 1000000
        random_int = random.randint(0,1000000)
        #print("nradome number between 1 - 10^6: %d" %random_int)
    
        #maps the random integer to the subset of number of tones in scale
        scale_tone = random_int%len(scale)
        #print("random scale tone: %d" %scale_tone)
    
        #maps the random scale tone to the tones from the chromatic scale
        chromatic_scale_tone = scale[int(scale_tone)]
        #print("random chromatic scale tone: %d" %chromatic_scale_tone)
        
        #maps the tones from the chromatic scale to lilypond formatted note strings
        if (key in self.listOfSharpKeys):
            pitch = self.chromatic_sharp_list[(chromatic_scale_tone+self.key_dict[key])%len(self.chromatic_sharp_list)]
        else:
            pitch = self.chromatic_flat_list[(chromatic_scale_tone+self.key_dict[key])%len(self.chromatic_flat_list)]        
        
        #get a random octave
        octave = self.getRandomOctave()
        #assign the octave symbol to the pitch
        note = pitch + octave
        
        #check the range of the instrument
        
        if range == 'alto sax':
            
            #if the random note is below the range of alto sax, bump it up an octave
            if note in self.alto_sax_below_range:
                note += "\'"
            
            #if the random note is above the range of alto sax, bump it down an octave
            if note in self.alto_sax_above_range:
                #strip the note of it's octave symboles
                note = note.rstrip("\'") 
                #put the note back in the topmost octave for the instruement 
                note += "\'\'"
            
            
        
        
        return note
     
    #prints the intervals of a scale in a given key mapped onto the chromatic scale,
    #as well as the note names of that scale.   
    def printScaleAndIntervals(self,scale,key):
        
        noteList = []
        keyList = []
        
        if key in self.listOfSharpKeys:
            keyList =  self.chromatic_sharp_list
        else:
            keyList =  self.chromatic_flat_list
            
        
        for note in scale:
        
            noteList.append(keyList[(note+self.key_dict[key])%len(keyList)])
            
        #print("list of scale intervals:")
        # print(scale)
#         print("list of notes:")
#         print(noteList)
    
    #returns a random octave string
    def getRandomOctave(self):
    
        random_int = random.randint(0,1000000)
        octave_index = random_int%len(self.list_of_octave_symbols)
        
        return self.list_of_octave_symbols[octave_index]
    
    #returns a random musical key from key_dict
    def getRandomKey(self):
        
        #random.sample() returns a list of the number of keys specified in the function call
        random_key = random.sample(self.key_dict,1)[0]
        
        return random_key
    
    #assigns a given note a random octave (this function must be called BEFORE the note has been assigned a rhythm)
    def giveRandomOctave(self,note):
    
        random_int = random.randint(0,1000000)
        octave_index = random_int%len(self.list_of_octave_symbols)
        noteWithOctave = note+self.list_of_octave_symbols[octave_value]
        
        #print('a note with random Octave added to it: %s' %noteWithOctave)
        return noteWithOctave 
    
    #assigns a given note a given octave (this function must be called BEFORE the note has been assigned a rhythm)
    def assignOctave(self,note,octave):
    
        noteWithOctave = note+octave
        
        return noteWithOctave 

    #returns a random rhythm string 
    def getRandomRhythmicValue(self):
    
        random_int = random.randint(0,1000000)
        rhythm_index = random_int%len(self.list_of_rhythmic_values)
        
        return self.list_of_rhythmic_values[rhythm_index]
        

    
    #assigns a given note a random rhythm (this function must be called AFTER the note has been assigned an Octave)    
    def giveRandomRhythmicValue(self,note):
    
        random_int = random.randint(0,1000000)
        rhythm_index = random_int%len(self.list_of_rhythmic_values)
        noteWithrhythm = note+self.list_of_rythmic_values[rhythm_index]
        
        #print('a note with random rhythm added to it: %s' %noteWithrhythm)
        return noteWithrhythm
     
    #assigns a given note a given rhythm (this function must be called AFTER the note has been assigned an Octave)    
    def assignRhythm(self,note,rhythm):
    
        noteWithRhythm = note+rhythm
        
        return noteWithRhythm
        
     
    #assigns a given rhythm and octave to a given note 
    def assignOctaveAndRhythm(self, note,rhythm,octave):
        
        return note+octave+rhythm
        
        
        
    #assigns a rest a random rhythm     
    def getRandomRest(self):
    
        random_int = random.randint(0,1000000)
        rhythm_value = random_int%len(self.list_of_rhythmic_values)
        restWithRhythm = 'r'+self.list_of_rhythmic_values[rhythm_value]
        
        #print('a rest with random rhythm added to it: %s' %restWithRhythm)
        return restWithRhythm
     
    #assigns a given note a given rhythm (this function must be called AFTER the note has been assigned an Octave)    
    def assignRhythmToRest(self,rhythm):
    
        restWithRhythm = 'r'+rhythm
        
        return restWithRhythm
    
    
    # this function returns the rhythm value of a  note or rest
    # as an integer. It asumes it is being called on  a string that contains a number. 
    def findRhythmAsInt(self,noteRest):
        
        #returns a list of all numbers in the noteRest string as a list of string
        #uses the regular expression library to find all decimal numbers in a string (\d) one or more time
        # +. so r'\d+' returns all numbers in a string
        string_rhythm = re.findall(r'\d+',noteRest)
        
        #convert list of string number to int
        intRhythm = int(string_rhythm[0])
        
        return intRhythm
        
        
    def getMeasure_RandomEverything(self,timeSignature,scale,key,range):
        
        measure_counter = 0.0
        measure_string = ''
        item = ''
        
        #while measure counter is less than the number of beats in the measure
        #i.e while the measure isn't full
        while (measure_counter < float(timeSignature)):
            
            #get a random rhythm
            rhythm = self.getRandomRhythmicValue()
            #add this rhythmic value to the measure counter
            measure_counter += (1/float(rhythm))
            #print("the cumultative beats in the measure so far are: %f " %measure_counter)
            
            #check to see the new rhythm value hasn't acused the
            #total time to exceed the size of the measure
            while(measure_counter > float(timeSignature)):
                
                #print("new rhythm: %s is too big to fit into bar." %rhythm)
                
                #remove the too-big rhythm's time form the counter
                measure_counter -= (1/float(rhythm)) 
                #get the index of the too-big rhythm in the list of rhythm values
                
                rhythm_index = self.list_of_rhythmic_values.index(rhythm)
                # print("the new rhythem index is %d" %rhythm_index)
#                 print("the list of rhythmic values is:")
#                 print(self.list_of_rhythmic_values)
                
                #increase the index by 1 to move to the next smaller rhythm  
                rhythm_index += 1
                
                
                rhythm = self.list_of_rhythmic_values[rhythm_index]
#                 print("the new rhythm is %s" %rhythm)
                #add the new rhythm value to the counter
                measure_counter += (1/float(rhythm))
            
            
            #all the rhythm stuff has been worked out.
            #select a note or rest to apply the rhythm too
            random_int = random.randint(0,4)
            if (random_int != 0):
            
                #get a note if random int is 0
                pitchAndOctave = self.getRandomScaleTone(scale,key,range)
                #octave = self.getRandomOctave()
                note = self.assignRhythm(pitchAndOctave,rhythm)
                #note = self.assignRhythm(pitch,rhythm)
                #assign note to item and add a space for lilypond formatting
                item = note+' '
            else:
                #get a rest if random int is 1
                rest = 'r'+rhythm
                #assign rest to item and add a space for lilypond formatting
                item = rest+' '
        
            #add item to the 
            measure_string += item
#             print("the measure string thuse far is %s" %measure_string)
            
        #remove the extra space at the end of the string             
        measure_string.rstrip(' ')
#             print("the final measure string thuse far is %s" %measure_string)
#             print("total measure time used is %f" %measure_counter)
#             print("Number of beats in the bar is %f" %float(timeSignature[0]))
        print(measure_string)
        return measure_string 
        
        
        
    def getMeasure_IdenticalRhythmNoRests(self,timeSignature,scale,key,range,rhythm):
        
        measure_counter = 0.0
        measure_string = ''
        item = ''
        
        
        while (measure_counter < float(timeSignature)):
        
            #get a note
            pitchAndOctave = self.getRandomScaleTone(scale,key,range)
            #assign the rhythm to the note
            note = self.assignRhythm(pitchAndOctave,rhythm)
            #add this rhythmic value to the measure counter
            measure_counter += (1/float(rhythm))
            #assign note to item and add a space for lilypond formatting
            note +=' '
            #add note to the measure string
            measure_string += note
            
            
                
        #remove the extra space at the end of the string             
        measure_string.rstrip(' ')  
        print(measure_string)
        return measure_string   
            
            
           
            
               
            
            
        
        
        
        
    
        
        
        
           
   
         

        
        