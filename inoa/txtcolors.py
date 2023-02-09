import sys

text_display_colors = {
    'gray'    :{'normal': '\033[1;30m%s\033[1m', 'bold': '\033[0;30m%s\033[0m'},
    'red'     :{'normal': '\033[1;31m%s\033[1m', 'bold': '\033[0;31m%s\033[0m'},
    'green'   :{'normal': '\033[1;32m%s\033[1m', 'bold': '\033[0;32m%s\033[0m'},
    'yellow'  :{'normal': '\033[1;33m%s\033[1m', 'bold': '\033[0;33m%s\033[0m'},
    'blue'    :{'normal': '\033[1;34m%s\033[1m', 'bold': '\033[0;34m%s\033[0m'},
    'magenta' :{'normal': '\033[1;35m%s\033[1m', 'bold': '\033[0;35m%s\033[0m'},
    'cyan'    :{'normal': '\033[1;36m%s\033[1m', 'bold': '\033[0;36m%s\033[0m'},
    'white'   :{'normal': '\033[1;37m%s\033[1m', 'bold': '\033[0;37m%s\033[0m'},
    'crimson' :{'normal': '\033[1;38m%s\033[1m', 'bold': '\033[0;38m%s\033[0m'}
}

def textcolor(text, color="crimson", weight="bold"):
    if sys.stdout.isatty():
        return text_display_colors[color][weight] % text
    else:
        return text