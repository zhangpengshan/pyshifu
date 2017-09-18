from check import Check


class Stats(Check):
    def para_check(self):
        pass

    def __init__(self, max_num_bin=10, binning_method="EqualPositive", sample_rate=0.8, sample_neg_only=False,
                 binning_algorithm="SPDTI"):
        self._max_num_bin = max_num_bin
        self._binning_method = binning_method
        self._sample_rate = sample_rate
        self._sample_neg_only = sample_neg_only
        self._binning_algorithm = binning_algorithm