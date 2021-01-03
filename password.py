import random
import string
print("welcome to random password generator")
n= int(input(print("What length of password do u want")))
print(n)
psd = []
def alphabet() :
    lower_upper_alphabet = string.ascii_letters
    psd.append(random.choice(lower_upper_alphabet))

def numbe() :
    psd.append(str(random.randint(0,9)))

def special_char() :
    psd.append(random.choice(string.punctuation))

def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1

for i in range(0,n):
    o= random.randint(0,2)
    if (o==0):
        alphabet()
    elif (o==1):
        numbe()

    else:
        special_char()
print ("your Generated password is  "+ listToString(psd))
