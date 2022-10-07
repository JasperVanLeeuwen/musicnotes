from IPython.core.display import SVG
from IPython.core.display_functions import display


def show(fretboard_object):
    a = fretboard_object.render()
    a.seek(0)
    b = a.read()
    display(SVG(b))
