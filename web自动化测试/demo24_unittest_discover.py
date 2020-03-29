import unittest

discover = unittest.defaultTestLoader.discover("./cases", pattern="test*.py")
runner = unittest.TextTestRunner()
runner.run(discover)
