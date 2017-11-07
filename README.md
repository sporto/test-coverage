
"You don’t need static type checking if you have 100% unit test coverage."
http://blog.cleancoder.com/uncle-bob/2016/05/01/TypeWars.html

**This is WRONG** 

This repo shows a simple example of how this is incorrect.

This program has 100% coverage.

```
make test

Name     Stmts   Miss  Cover   Missing
--------------------------------------
app.py       5      0   100%
----------------------------------------------------------------------
Ran 2 tests in 0.012s
```

However this program doesn't work at all because the types between the functions don't match.

```
make run

Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "app.py", line 6, in run
    print user["firstName"]
KeyError: 'firstName'
```

By looking at `app.py` it is quite obvious what the issue is. But in a big application where functions that produce values and functions that use those values are far appart this issue with mismatching types is not obvious. Mocking which is a standard practice in unit tests makes this a big problem.

## Setup

```
easy_install mock
easy_install nose
```

## Run unit tests

```
make test
```

## Run program

```
make run
```