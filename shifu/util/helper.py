from subprocess import check_output, CalledProcessError
import os


class Helper(object):
    @staticmethod
    def get_current_path():
        return os.getcwd()

    @staticmethod
    def run_shell(common_list):
        try:
            output = check_output(common_list)
        except CalledProcessError:
            output = None
        return output

    @staticmethod
    def get_environment_variable(variable_name):
        return os.environ[variable_name] if variable_name in os.environ else None

