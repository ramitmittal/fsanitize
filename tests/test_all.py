import pytest
import os
import shutil
from fsanitize import sanitize


@pytest.mark.parametrize("str00, str01",
                         [('A&*(Kkdf)  .html', 'a_kkdf_.html'),
                          ('A&*DF8.876-=_.ogg', 'a_df8_876_.ogg'),
                          ('   -   .ex', '_.ex'),
                          ('[[.mp3', '_.mp3'),
                          ('Lord of the Rings - The Return of The King.mp4',
                           'lord_of_the_rings_the_return_of_the_king.mp4')])
def test_name_maker_files(str00, str01):
    assert sanitize.name_maker(str00, fbit=True) == str01


@pytest.mark.parametrize("str00, str01",
                         [("superLOLC#2", "superlolc_2"),
                          ("[[", "_"),
                          ("my.new.files", "my_new_files")])
def test_name_maker_dirs(str00, str01):
    assert sanitize.name_maker(str00) == str01


@pytest.fixture
def duplicate_dir_set_up():
    os.mkdir('another_test_dir')
    os.mkdir('another_test_dir/dir_1')
    os.mkdir('another_test_dir/dir-1')
    open('another_test_dir/dir_1/one_.txt', 'a').close()
    open('another_test_dir/dir_1/one-.txt', 'a').close()
    open('another_test_dir/dir-1/b{a', 'a').close()
    open('another_test_dir/dir-1/b}a', 'a').close()
    yield
    shutil.rmtree('another_test_dir')


def test_duplicate_names(duplicate_dir_set_up):
    sanitize.recursive_rename('another_test_dir')
    final_names = ('one_.txt', 'one__.txt', 'b_a', 'b_a_')
    for x in os.listdir('another_test_dir/dir_1'):
        assert x in final_names
    for x in os.listdir('another_test_dir/dir_1_'):
        assert x in final_names


@pytest.mark.parametrize("name, corrected_name",
                         [("__toothbrush.py", "_toothbrush.py"),
                          ("0xs__r____rR___.mp3", "0xs_r_rR_.mp3")])
def test_remove_multiple_underscores(name, corrected_name):
    assert sanitize.remove_multiple_underscores(name) == corrected_name


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
