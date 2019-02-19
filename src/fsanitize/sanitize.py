import os
from fsanitize.logmgr import logger


set_of_sanitized_paths = set()


def recursive_rename(direc):
    '''Main renaming function.

    Arguments:
    direc -- the directory to sanitize
    '''

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


def renamer(x):
    '''Call os.rename on argument provided.

    Argument:
    x -- path of file or directory to rename.
    '''

    fbit = False if x.is_dir() else True

    old_path = x.path
    new_path = os.path.join(os.path.dirname(x), name_maker(x.name, fbit))

    if new_path in set_of_sanitized_paths:
        new_path += "_1"
    set_of_sanitized_paths.add(new_path)

    if not old_path == new_path:
        os.rename(old_path, new_path)
        logger.info('renamed file %s to %s', old_path, new_path)


def name_maker(fname, fbit=False):
    """Creates new name for files using str.maketrans

    Arguments:
    fname -- filename to sanitize

    Keyword Arguments:
    fbit -- boolean, set true to save the last . and preserve file extensions (default False)
    """

    upper_letters = 'QAZWSXEDCRFVTGBYHNUJMIKOLP'
    lower_letters = 'qazwsxedcrfvtgbyhnujmikolp'

    if not fbit:
        # make a string translation table for directory names

        symbols = '~!@#$%^&*()_+=-`][|}{":;?></ ,.'
        underscores = '_' * len(symbols)

        original_string = upper_letters + symbols
        translation_string = lower_letters + underscores

        # create mapping and translate
        table = str.maketrans(original_string, translation_string)
        newname = fname.translate(table)

    else:
        # for files, don't modify the . (dot)

        symbols = '~!@#$%^&*()_+=-`][|}{":;?></ ,'
        underscores = '_' * len(symbols)

        original_string = upper_letters + symbols
        translation_string = lower_letters + underscores

        # create mapping and translate
        table = str.maketrans(original_string, translation_string)
        newname = fname.translate(table)

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
    """Removes multiple consecutive underscores from the argument and return it.

    Arguments:
    name -- string to remove multiple consecutive underscores from
    """

    new_name = name[:1]

    for i in range(len(name)):
        if not i == 0:
            if name[i] == '_' and name[i-1] == '_':
                continue
            else:
                new_name += name[i]
    return new_name
