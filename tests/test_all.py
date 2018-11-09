import pytest
import os
import shutil
from fsanitize import sanitize

@pytest.mark.xfail()
@pytest.mark.parametrize("str00, str01",
                        [('A&*(Kkdf)  ', 'a___kkdf___'),
                        ('A&*DF8876-=__', 'a__df8876____'),
                        ('   -   .ex', '_______.ex'),
                        ('Lord of the Rings - The Return of The King.mp4', 'lord_of_the_rings___the_return_of_the_king.mp4')])
def test_name_maker(str00, str01):
    """This test if for the older version of name_maker that doesn't remove multiple underscores"""
    assert sanitize.name_maker(str00) == str01


@pytest.mark.parametrize("str00, str01",
                        [('A&*(Kkdf)  ', 'a_kkdf_'),
                        ('A&*DF8876-=_', 'a_df8876_'),
                        ('   -   .ex', '_.ex'),
                        ('Lord of the Rings - The Return of The King.mp4', 'lord_of_the_rings_the_return_of_the_king.mp4')])
def test_new_name_maker(str00, str01):
    assert sanitize.name_maker(str00) == str01


@pytest.fixture
def dir_set_up():
    os.mkdir('test_dir')
    os.mkdir('test_dir/SOES44')
    open('test_dir/taydsd&&{a.mp3', 'a').close()
    open('test_dir/ii**IIIp3', 'a').close()
    open('test_dir/SOES44/8U^ut.txt', 'a').close()
    yield
    shutil.rmtree('test_dir')


def test_recursive_rename(dir_set_up):
    sanitize.recursive_rename('test_dir')
    for x in os.listdir('test_dir'):
        assert x in ('soes44', 'ii_iiip3', 'taydsd_a.mp3')
    assert os.listdir('test_dir/soes44') == ['8u_ut.txt']


def test_renamer():
    '''Yet to be written.'''
    pass


@pytest.mark.parametrize("name, corrected_name",
                        [("__toothbrush.py", "_toothbrush.py"),
                        ("0xs__r____rR___.mp3", "0xs_r_rR_.mp3")])
def test_remove_multiple_underscores(name, corrected_name):
    assert sanitize.remove_multiple_underscores(name) == corrected_name
