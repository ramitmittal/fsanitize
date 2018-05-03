import unittest
import os
import shutil
from filename_sanitizer import sanitize


class Test00(unittest.TestCase):
    """Tests the name_maker function."""

    def test_name_maker(self):

        str00 = 'A&*(Kkdf)  '
        str01 = 'A&*DF8876-=__'
        str02 = '   -   .ex'
        str03 = 'Lord of the Rings - The Return of The King.mp4'

        str10 = 'a___kkdf___'
        str11 = 'a__df8876____'
        str12 = '_______.ex'
        str13 = 'lord_of_the_rings___the_return_of_the_king.mp4'

        self.assertEqual(sanitize.name_maker(str00), str10)
        self.assertEqual(sanitize.name_maker(str01), str11)
        self.assertEqual(sanitize.name_maker(str02), str12)
        self.assertEqual(sanitize.name_maker(str03), str13)


class Test01(unittest.TestCase):
    """Tests the recursive_rename function, which is basically everything."""

    def setUp(self):
        os.mkdir('test_dir')
        os.mkdir('test_dir/SOES44')
        open('test_dir/taydsd&&{a.mp3', 'a').close()
        open('test_dir/ii**IIIp3', 'a').close()
        open('test_dir/SOES44/8U^ut.txt', 'a').close()

    def tearDown(self):
        shutil.rmtree('test_dir')

    def test_everything(self):
        sanitize.recursive_rename('test_dir')
        self.assertEqual(os.listdir('test_dir'), ['soes44', 'ii__iiip3', 'taydsd___a.mp3'])
        self.assertEqual(os.listdir('test_dir/soes44'), ['8u_ut.txt'])


if __name__ == '__main__':
    unittest.main()
