import os
from filename_sanitizer.logmgr import logger


def recursive_rename(direc):
    '''main renaming function
    requires directory as argument
    calls itself on directories and renamer() on files'''

    try:
        for x in os.scandir(direc):
            if x.is_dir():
                recursive_rename(x)
            renamer(x)
    except PermissionError as error:
        logger.error('encountered error %s in %s', error.__str__(), x)


def renamer(x):
    '''calls os.rename, checks if file to rename is a directory'''

    fbit = False if x.is_dir() else True
    fname1, fname2 = (x.path, os.path.join(os.path.dirname(x), name_maker(x.name, fbit)))
    try:
        os.rename(fname1, fname2)
        logger.info('renamed file %s to %s', fname1, fname2)
    except PermissionError as error:
        logger.error('encountered error %s in %s', error.__str__(), x)


def name_maker(fname, fbit=False):
    '''creates new name for files using str.maketrans()'''

    upper = 'QAZWSXEDCRFVTGBYHNUJMIKOLP'
    lower = 'qazwsxedcrfvtgbyhnujmikolp'
    symbols = '~!@#$%^&*()_+=-`][|}{":;?></ ,'
    undersc = '______________________________'
    orig = upper + symbols
    tran = lower + undersc
    table = str.maketrans(orig, tran)
    newname = fname.translate(table)
    if fbit:
        corrected = False
        for index, value in enumerate(fname[::-1]):
            if value == '.':
                if corrected is False:
                    corrected = True
                else:
                    newname = newname[:(len(newname) - 1 - index)] + '_' + newname[-index:]
    return newname
