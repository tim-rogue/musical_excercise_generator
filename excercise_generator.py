import math
import random

#scale tones an dintervals of 2 octave chomatic scale
chromatic_scale_tones= {'root':0,'-2':1,'+2':2,'-3':3,'+3':4,'P4':5,'x4/b5':6,'P5':7,'-6':8,'+6':9,'-7':10,'+7':11,'P8':12,'-9':13,'+9':14,'-10':15,'+10':16,'P11':17,'x11/b12':18,'P12':19,'-13':20,'+13':21,'-14':22,'+14':23,'P16':24}

chromatic_sharp_list = ['c','cis','d','dis','e','f','fis','g','gis','a','ais','b']
chromatic_flat_list =  ['c','des','d','ees','e','f','ges','g','aes','a','bes','b']                        
#10 scale tones because we're doing 2 octaves
NUM_PENTATONIC_SCALE_TONES = 11 

#scale tones of 2 octave pentatonic scale
minor_pentatonic_scale_tones = [chromatic_scale_tones['root'],chromatic_scale_tones['-3'],chromatic_scale_tones['P4'],chromatic_scale_tones['P5'],chromatic_scale_tones['-7'],chromatic_scale_tones['P8'],chromatic_scale_tones['-10'],chromatic_scale_tones['P11'],chromatic_scale_tones['P12'],chromatic_scale_tones['-14'],chromatic_scale_tones['P16']]

 
def isodd(num):
    return num%2  

#get a random scale tone from both octaves                           
def getRandomScaleTone_BothOctaves(scale,numScaleTones):
    
    #get a random integer between 0 and 1000000
    random_int = random.randint(0,1000000)
    #map the random integer to the subset of tone in scale
    scale_tone = random_int%numScaleTones
    #using (scale_tone - 1) to account for the list indexing 0 - numElements
    #i.e if scale_tone is between 1 - 10, note will be indexed 0 - 9
    print("random chromatic scale tone using mod: %d" %scale[int(scale_tone )])
    #print("randome chromatic scale tone using random.choice(): %d" %random.choice(scale))
    return scale[int(scale_tone)]
    
#get a random scale tone from first octave
def getRandomScaleTone_1stOctave(scale,numScaleTones):

    #limit the number of tones to the first octave
    if(isodd(numScaleTones)):
        first_octave = int(numScaleTones/2)+1
    else:
        first_octave = int(numScaleTones/2)
    #print("number of notes in first octave: %d" %first_octave)
    #get a random integer between 0 and 1000000
    random_int = random.randint(0,1000000)
    #print("nradome number between 1 - 10^6: %d" %random_int)
    #map the random integer to the subset of tone in scale
    scale_tone = random_int%first_octave
    #print("random scale tone: %d" %scale_tone)
    #using (scale_tone - 1) to account for the list indexing 0 - numElements
    #i.e if scale_tone is between 1 - 10, note will be indexed 0 - 9
    print("random chromatic scale tone: %d" %scale[int(scale_tone )])
    return scale[int(scale_tone )]

#get a random scale tone from the 2nd octave    
def getRandomScaleTone_2ndOctave(scale,numScaleTones):
    
    #limit the number of tones to the first octave
    if(isodd(numScaleTones)):
        first_octave = int(numScaleTones/2)+1
    else:
        first_octave = int(numScaleTones/2)
    #get a random integer between 0 and 11881376
    random_int = random.randint(0,11881376)
    #map the random integer to the subset of tone in scale
    scale_tone = random_int%numScaleTones
    #move the randomly selected first octave note up an octave
    if(scale_tone < 5):
        scale_tone = scale_tone+first_octave
    print("randome chromatic scale tone: %d" %scale[int(scale_tone)])
    #using (scale_tone - 1) to account for the list indexing 0 - numElements
    #i.e if scale_tone is between 1 - 10, note will be indexed 0 - 9
    return scale[int(scale_tone)]

#convert integer scale tone to a midi pitch for saxophone (low Bb3 to high F6, 58 - 89)    
def scaleToneToMIDI(scaleTone, keyOffset):
    
    return scaleTone + keyOffset    
    
  
 

for i in range(0,20):

    #getRandomScaleTone_2ndOctave(minor_pentatonic_scale_tones,NUM_PENTATONIC_SCALE_TONES)
    #getRandomScaleTone_BothOctaves(minor_pentatonic_scale_tones,NUM_PENTATONIC_SCALE_TONES)
    getRandomScaleTone_FirstOctave(minor_pentatonic_scale_tones,NUM_PENTATONIC_SCALE_TONES)
    
    
