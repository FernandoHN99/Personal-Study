import os

class Util:

    @staticmethod
    def clean_terminal():
        os.system('clear')
    
    @staticmethod
    def set_overwriting(var_control):
        if var_control:
            return 'w+'
        else:
            return 'a+'


