import textwrap
from inoa.txtcolors import textcolor

def remove_spaces(text):
    if not text:
        return ""

    while True:
        if text.find("  ") > -1:
            text = text.replace("  ", " ")
        else:
            break

    return text

class cError(Exception, object):
    def __init__(self, e=None):
        Exception.__init__(self)
        return

    def __str__(self):
        max_len = max([len(l) for l in textwrap.fill(self.e, 80).split('\n')])
        error_lines = ['%s%s' % (l, ' ' * (max_len - len(l))) for l in textwrap.fill(self.e, 80).split('\n')]

        error_message = ['%s: %s' % (textcolor(self.error_type, 'red'), error_lines[0])]
        for error_line in error_lines[1:]:
            error_message.append('%s%s' % (' ' * (len(self.error_type) + 2), error_line))
            
        return '\n\n' + '\n'.join(error_message) + '\n\n'


    def clear_text(self):
        return self.e

class ConfigError(cError):
    def __init__(self, e=None):
        self.e = remove_spaces(e)
        self.error_type = 'Config Error'
        cError.__init__(self)
        