from django.test import TestCase

from django.conf import settings

class MyTest(TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_printPaths(self):
        """This was just to see what the filepaths end up being so I can compare to the path in the browser and be sure whether I got them right"""
        print("\n\nDJANGO SETTINGS PRINTOUT: \n")
        print("BASE_DIR: {} \nVUE_DIR: {}".format(settings.BASE_DIR, settings.VUE_DIR))
        print("STATIC_ROOT: {} \nSTATICFILES_DIRS: {}".format(settings.STATIC_ROOT, settings.STATICFILES_DIRS))
        print("WEBPACK_LOADER: {}".format(settings.WEBPACK_LOADER))
