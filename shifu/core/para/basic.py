from check import Check


class Basic(Check):
    def para_check(self):
        pass

    def __init__(self, name, author=None, description=None, run_mode="LOCAL", post_train_on=False, custom_paths=None):
        self._name = name
        self._author = author if author is not None else self._get_default_author()
        self._description = description if description is not None else self._get_default_description()
        self._run_mode = run_mode
        self._post_train_on = post_train_on
        self._custom_paths = custom_paths if custom_paths is not None else self._get_default_custom_paths()

    def _get_default_author(self):
        self._author = "get current user"

    def _get_default_description(self):
        self._description = "Created at 2017-09-10 11:27:00"

    def _get_default_custom_paths(self):
        self._custom_paths = []



