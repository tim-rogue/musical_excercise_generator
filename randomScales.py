import random

class randomScales:

    # a dictionary mapping a Key's chromatic distance from C as a number, used as an offset.
    # i.e the key of C is 0 semi-tones away from the key of C, the key of F is 5 semitones away from C
    key_dict = {'Cmaj':0,'Cmin':0,'C#maj':1,'C#min':1, 'Dbmaj':1,'Dmaj':2,'Dmin':2,'D#min':3\
               ,'Ebmaj':3,'Ebmin':3,'Emaj':4,'Emin':4,'Fmaj':5,'Fmin':5,'F#maj':6,'F#min':6\
               ,'Gbmaj':6,'Gmaj':7,'Gmin':7,'G#min':8,'Abmaj':8,'Abmin':8,'Amaj':9,'Amin':9\
               ,'A#min':10,'Bbmaj':10,'Bbmin':10,'Bmaj':11,'Bmin':11}
               
    note_order_list = ['3rds','4ths','up 4 notes, jump down a third','jump up a fifth, down 4 notes','jump up a 4rth, play 2nd and 3rd']
    scales_types = ['pentatonic','blues','major','natural minor']
    
    def __init__(self):
        pass
    
    
    def getRandomScale(self):
        
        musical_key = random.sample(self.key_dict,1)[0]
        scale = random.choice(self.scales_types)
        note_order = random.choice(self.note_order_list)
        
        print("Play a \" %s \" scale. " %scale)
        print("In the key of \" %s \" ." %musical_key)
        print("With a note order of \" %s \" . \n\n" %note_order)
        
        


scales = randomScales()
for i in range(20):
    
    scales.getRandomScale()
    
    
        
        
        
        