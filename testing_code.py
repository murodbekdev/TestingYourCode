# Testing a Function

def get_formatted_name(first, last):
    '''Generate a neatly formatted full name.'''
    full_name = f"{first} {last}"
    return full_name.title()

def get_formatted_midlle_name(frst, last, midlle =""):
    '''Generate a neatly formatted full name.'''
    full_name = f"{frst} {midlle} {last}"
    return full_name.title()