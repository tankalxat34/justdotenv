"""
File Parser `.env`

(c) tankalxat34 - 2023
"""
import pathlib
import re


def strip(s: str) -> str:
    """Apply classic `strip` method to string"""
    return s.strip()


def multiReplacer(s: str, mask: dict) -> str:
    """Return new string with replaced symbols by mask dictionary"""
    for m in mask.keys():
        s = s.replace(m, mask[m])
    return s


class DotEnv:
    def __init__(self, path: str = pathlib.Path(pathlib.Path().resolve(), ".env"), parse_int: bool = True, parse_float: bool = True, encoding: str = "UTF-8"):
        """
        Class for work with file `.env`

        :param path - path to file `.env`
        """

        with open(path, "r", encoding=encoding) as env:
            strings = list(map(strip, env.readlines()))

        for line in strings:
            # detect key and value
            if "=" in line:
                k, v = line.split("=")
            else:
                k = list(self.__dict__.keys())[-1]
                v = self.__dict__[list(self.__dict__.keys())[-1]] + line

            # replacing symbols
            v = multiReplacer(v, {
                "'": "",
                '"': "",
                "\n": ""
            })

            # apply types
            if parse_float and "." in v:
                try:
                    v = float(v)
                except ValueError:
                    pass
            elif parse_int:
                try:
                    v = int(v)
                except ValueError:
                    pass

            self.__setattr__(k, v)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, __name: str):
        try:
            return getattr(self, __name)
        except AttributeError:
            return None

    def __str__(self) -> str:
        return multiReplacer(f"DotEnv({self.__dict__})", {
            "',": ",",
            "': ": "=",
            "'": "",
            "}": "",
            "{": ""
        })

    def get(self, key: str) -> any:
        return self.__dict__[key]
