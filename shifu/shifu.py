"""
Shifu client to call java module.
"""
from __future__ import print_function
import sys
from util.helper import Helper


class Shifu(object):
    def __init__(self, name):
        self.name = name
        self.path = ""
        self.current_step = ""

    def new(self, name):
        print ("New model: %s" % self.name)
        current_path = Helper.get_current_path()

    def init(self):
        print ("init model: %s" % self.name)

    def status(self):
        print ("status model: %s" % self.name)

    def norm(self):
        print("norm model: %s" % self.name)

    def varsel(self):
        print ("varsel model: %s" % self.name)

    def train(self):
        print ("train model: %s" % self.name)

    def eval(self):
        print ("eval model: %s" % self.name)


def main():
    """
    Entry point of the app.
    """
    print("Hello World.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
