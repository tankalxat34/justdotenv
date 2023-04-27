# justdotenv
Python module for parsing .env file

## How to install?

Perform this command in your cmd:
```
curl https://raw.githubusercontent.com/tankalxat34/justdotenv/main/dotenv.py -o justdotenv.py
```

## Example of use

```py
>>> import dotenv
>>> _env = dotenv.DotEnv()

>>> print(_env)
DotEnv(ALLUSERSPROFILE=C:\\ProgramData, ... TOKEN=wefawerrgfearsg34gw3qgg4, NAME=alex123, TEST=1)

>>> print(_env.TEST)
1
>>> print(type(_env["TEST"]))
<class 'int'>

>>> print(_env.ALLUSERSPROFILE)
C:\\ProgramData
>>> print(_env.TOKEN)
wefawerrgfearsg34gw3qgg4
```
