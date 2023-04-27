"""
File Parser `.env`
-----------------

## Example of use
    >>> import dotenv
    >>> _env = dotenv.DotEnv()
    >>> print(_env)
    DotEnv(TOKEN=wefawerrgfearsg34gw3qgg4, NAME=alex123, TEST=1, MULTILINE_STRING=wefwefwefwefwefweawefgeraghsrthrth)
    >>> print(_env.MULTILINE_STRING)
    wefwefwefwefwefweawefgeraghsrthrth

(c) tankalxat34 - 2023
"""
import pathlib
import re
import os


def strip(s: str) -> str:
    """Apply classic `strip` method to string"""
    return s.strip()


def multiReplacer(s: str, mask: dict) -> str:
    """Return new string with replaced symbols by mask dictionary"""
    for m in mask.keys():
        s = s.replace(m, mask[m])
    return s


class DotEnv:
    def __init__(self, path: str = pathlib.Path(pathlib.Path().resolve(), ".env"), parse_int: bool = True, parse_float: bool = True, encoding: str = "UTF-8", use_global_envs: bool = True):
        """
        Class for work with file `.env`

        path: path to file `.env` as `pathlib.Path` class instance. By default selecting this directory
        parse_int: `bool` value if you need to parse integers. By default is `True`
        parse_float: `bool` value if you need to parse float values. By default is `True`
        encoding: `str` value of encoding `.env` file. By default is `"UTF-8"`
        use_global_envs: `bool` value if you need to save in this class instance all available environment variables on your current PC session. By default is `True`
        """

        # saving global variables
        if use_global_envs:
            for k in list(dict(os.environ).keys()):
                v = os.environ[k]
                self.__setattr__(k, v)


        with open(path, "r", encoding=encoding) as env:
            strings = list(map(strip, env.readlines()))

        for line in strings:
            # detect key and value
            if line:
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
    
    def __contains__(self, __key) -> bool:
        return __key in self.__dict__

    def get(self, key: str) -> any:
        return self.__dict__[key]
