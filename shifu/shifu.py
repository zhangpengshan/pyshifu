"""
Shifu client to call java module.
"""
from __future__ import print_function
from util.helper import Helper


class Shifu(object):
    def __init__(self, java_options=None):
        self._name = None
        self._path = ""
        self._current_step = ""
        self._java_options = java_options if java_options is not None \
            else "-server -XX:+UseParNewGC -XX:+UseConcMarkSweepGC -XX:CMSInitiatingOccupancyFraction=70"
        self._main_class = "ml.shifu.shifu.ShifuCLI"
        self._class_path = ".:${SHIFU_HOME}/conf:${SHIFU_HOME}/log4jconf:${CLASSPATH}"

    def new(self, name):
        self._name = name
        command_list = ['java', self._java_options, '-classpath', self._class_path, self._main_class, name]
        output = Helper.run_shell(command_list)
        print(output)

    def init(self):
        print ("init model: %s" % self._name)

    def status(self):
        print ("status model: %s" % self._name)

    def norm(self):
        print("norm model: %s" % self._name)

    def varsel(self):
        print ("varsel model: %s" % self._name)

    def train(self):
        print ("train model: %s" % self._name)

    def eval(self):
        print ("eval model: %s" % self._name)