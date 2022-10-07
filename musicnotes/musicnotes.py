import typing

import fretboard

from musicnotes.utils import show


class String:

    def __init__(self, string_nr: int):
        self.string_nr = string_nr
        self.frets = []

    def set(self, frets: typing.Iterator):
        for fret in frets:
            self.frets.append(fret)
        self.frets.sort()


class Strings:

    def __init__(self, nr_strings = 6):
        self.strings = {}
        for string_nr in range(1,nr_strings+1):
            self.strings[string_nr] = String(string_nr)

    def __getitem__(self, item):
        assert 1 <= item <= 6
        return self.strings[item]

    def get_nr_strings(self):
        return len(self.strings.keys())


class Guitar:

    def __init__(self):
        self.strings: Strings = Strings()

    def press(self, settings: typing.List[typing.List]):
        for string_nr, string_config in zip(range(6,0,-1), settings):
            self.strings[string_nr].set(string_config)
        return self

    def show(self):
        min_fret = min([min(frets) for frets in [ string.frets for string in self.strings.strings.values()]])
        max_fret = max([max(frets) for frets in [ string.frets for string in self.strings.strings.values()]])
        fb = fretboard.Fretboard(frets=(min_fret, max_fret), style={'marker': {'color': 'dodgerblue'}})

        for string_nr in range(1,7):
            string = self.strings[string_nr]
            for fret in string.frets:
                fb.add_marker(self.strings.get_nr_strings()-string_nr, fret)
        show(fb)

