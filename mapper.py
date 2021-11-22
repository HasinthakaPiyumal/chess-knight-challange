NUMBERS = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
STRINGS = '_abcdefgh'

def mapper(obj):
    mapped = NUMBERS[obj] if str(obj).isalpha() else STRINGS[int(obj)].upper()
    return mapped
