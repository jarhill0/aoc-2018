from os import makedirs, path

import requests


class AOCInput:
    url = 'https://adventofcode.com/{year}/day/{day}/input'

    def __init__(self, day, year='2018'):
        self.year = year
        self.day = day
        self._value = None
        self._session_cookie = None

    def _filename(self):
        return path.join('inputs', '{} {}.aocinput'.format(self.year, self.day))

    @property
    def _session(self):
        if self._session_cookie is None:
            with open('secrets.txt') as f:
                self._session_cookie = f.read().strip()
        return self._session_cookie

    @property
    def value(self):
        if self._value is None:
            # check if it's on disk
            try:
                with open(self._filename()) as f:
                    self._value = f.read()
            except FileNotFoundError:
                # if not, get it and save it
                self._value = requests.get(AOCInput.url.format(day=self.day, year=self.year),
                                           cookies={
                                               'session': self._session}).text

                makedirs(path.dirname(self._filename()), exist_ok=True)
                with open(self._filename(), 'w') as f:
                    f.write(self._value)
        return self._value.rstrip("\r\n")
