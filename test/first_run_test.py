import unittest
import os
import sys

sys.path.append(os.path.join(os.getcwd()))

import launch

class FirstRun(unittest.TestCase):
    def test_browser_dir(self):
        browser_dir_path = None
        # Maybe people would like to pass their own browser dir path...
        if sys.platform.startswith("linux"):
            browser_dir_path = os.path.join(os.path.expanduser("~"), ".zeronet")
        elif sys.platform.startswith("win"):
            browser_dir_path = os.path.join(os.path.expanduser("~"), "AppData","Roaming", "Zeronet Browser")
        elif sys.platform.startswith("darwin"):
            browser_dir_path = os.path.join(os.path.expanduser("~"), "Library", "Application Support", "Zeronet Browser")
        else:
            return
        launch.first_run(browser_dir_path)
        self.assertTrue(os.path.isfile(os.path.join(browser_dir_path, "zeronet.conf")))
        self.assertTrue(os.path.isfile(os.path.join(browser_dir_path, "lock.pid")))


if __name__ == "__main__":
    unittest.main()
