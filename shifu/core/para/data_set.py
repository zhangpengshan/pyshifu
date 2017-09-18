from check import Check


class DataSet(Check):
    def para_check(self):
        pass

    def __init__(self, source, data_path, header_path, data_delimiter="|", header_delimiter="|", filter_expressions="",
                 weight_column_name="", target_column_name="diagnosis", pos_tags=None, neg_tags=None,
                 missing_or_invalid_values=None,
                 meta_column_name_file="columns/meta.column.names",
                 categorical_column_name_file="columns/categorical.column.names"):
        self._source = source
        self._data_path = data_path
        self._header_path = header_path
        self._data_delimiter = data_delimiter
        self._header_delimiter = header_delimiter
        self._filter_expressions = filter_expressions
        self._weight_column_name = weight_column_name
        self._target_column_name = target_column_name
        self._pos_tags = ["M"] if pos_tags is None else pos_tags
        self._neg_tags = ["B"] if neg_tags is None else neg_tags
        self._missing_or_invalid_values = ["", "*", "#", "?", "null", "~"] if missing_or_invalid_values is None \
            else missing_or_invalid_values
        self._meta_column_name_file = meta_column_name_file
        self._categorical_column_name_file = categorical_column_name_file


