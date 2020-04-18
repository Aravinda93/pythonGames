import random
import string

def passwordGenerator():
    lowerchars      =   list(string.ascii_lowercase)
    upperchars      =   list(string.ascii_uppercase)
    speciachars     =   ['&','!','_','@']
    numericchars    =   list(range(0,9))
    otherrandom     =   lowerchars + upperchars + numericchars + speciachars
    password        = random.choice(lowerchars) + random.choice(upperchars) + random.choice(speciachars) + str(random.choice(numericchars)) + str(random.choice(otherrandom)) + str(random.choice(otherrandom)) + str(random.choice(otherrandom)) + str(random.choice(otherrandom))
    print(password)

passwordGenerator()

