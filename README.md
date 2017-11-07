
"You don’t need static type checking if you have 100% unit test coverage."
http://blog.cleancoder.com/uncle-bob/2016/05/01/TypeWars.html

**This is WRONG** 
This repo shows a simple example of how this is a incorrect.

This program has 100% coverage.

However this program doesn't work at all because the types between the functions don't match.

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