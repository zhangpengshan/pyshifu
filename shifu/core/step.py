class Step(object):
    def __init__(self):
        self.valueSet = ("new", "init", "stats", "normalize", "var-select", "train", "post-train", "eval")
        self.NEW = self.valueSet[0]
        self.INIT = self.valueSet[1]
        self.STATS = self.valueSet[2]
        self.NORMALIZE = self.valueSet[3]
        self.VAR_SELECT = self.valueSet[4]
        self.TRAIN = self.valueSet[5]
        self.POST_TRAIN = self.valueSet[6]
        self.EVAL = self.valueSet[7]
