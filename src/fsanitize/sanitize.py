import os
from fsanitize.logmgr import logger


def recursive_rename(direc):
    '''main renaming function
    requires directory as argument
    calls itself on directories and renamer on files'''

    try:
        for x in os.scandir(direc):
            if x.is_dir():
                recursive_rename(x)
            renamer(x)
    except PermissionError as error:
        logger.error('%s', str(error))
    except Exception as error:
        message = "An exception of type {}, with args {}, message {}".format(type(error).__name__, error.args, str(error))
        logger.error('Unexpected: %s', message)
    return None


def renamer(x):
    '''calls os.rename, checks if file to rename is a directory'''

    fbit = False if x.is_dir() else True
    fname1, fname2 = (x.path, os.path.join(os.path.dirname(x), name_maker(x.name, fbit)))
    if not fname1 == fname2:
        os.rename(fname1, fname2)
        logger.info('renamed file %s to %s', fname1, fname2)
    return None


def name_maker(fname, fbit=False):
    """creates new name for files using str.maketrans"""

    # make a string translation table
    # note: . (dots) are handled later
    upper = 'QAZWSXEDCRFVTGBYHNUJMIKOLP'
    lower = 'qazwsxedcrfvtgbyhnujmikolp'
    symbols = '~!@#$%^&*()_+=-`][|}{":;?></ ,'
    undersc = '______________________________'
    orig = upper + symbols
    tran = lower + undersc
    table = str.maketrans(orig, tran)

    # translate
    newname = fname.translate(table)

    # files should have an extension
    if fbit:
        corrected = False

        # iterate over the name in reverse, and skip the first .
        for index, value in enumerate(fname[::-1]):
            if value == '.':
                if corrected is False:
                    corrected = True
                else:
                    newname = newname[:(len(newname) - 1 - index)] + '_' + newname[-index:]

    newname = remove_multiple_underscores(newname)
    return newname


def remove_multiple_underscores(name):
    """removes multiple underscores from file names."""

    new_name = name[:1]

    for i in range(len(name)):
        if not i == 0:
            if name[i] == '_' and name[i-1] == '_':
                continue
            else:
                new_name += name[i]
    return new_name