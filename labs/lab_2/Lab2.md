
# Lab2 - Section 4 & 5

## Last Week Review

### Command Line

```bash
pwd
ls
cd
cd ..
mkdir
touch
python3
code
```

:bulb: You can always press ```tab``` to autocomplete the path

:bulb: You can wildcard character ```*``` to match any string in the path

### Add Color to Your Shell

[zsh shell](https://ohmyz.sh/)
[bash shell](https://ohmybash.github.io/)

### Python Interactive Console (Python Shell)

```bash
➜  506Fall2020 python3
Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> quit() / exit()
```

## This Week

### Comment

```python
# This is a line comment
"This part is not commented :)" # Comment all the following code in this line
"""
This is a string (block comment)
"""
```

:bulb: You can always use shortcut ```command/ctrl + /```
:bulb: line comment would not be read into Python interpreter but string would be read into and then ignored

### Variables

#### Immutable

- number(integer, float,...)
- string
- boolean
- tuple

:bulb: ```3``` vs ```"3"```

#### Mutable

- list
- dict
- set

#### Variable Creation

```python
mood = "happy"
feeling = "happy"
```
:bulb: ```=``` here is an **assignment operator**
:bulb: Why we need variables?
:bulb: What's the difference between ```mood``` and ```feeling```?

### Built-in Functions

- print()
- type()
- len()
- *id()

:bulb: input -> function -> output
:bulb: python shell would execute print() automatically

#### id()

```bash
>>> mood = "happy"
>>> id(mood)
4502209520
>>> feeling = "happy"
>>> id(feeling)
4502209520
>>> mood == feeling
True
>>> mood is feeling
True
```

```bash
>>> list1 = [1]
>>> id(list1)
4502118016
>>> list2 = [1]
>>> id(list2)
4502117952
>>> list1 == list2
True
>>> list1 is list2
False
>>> list1[0] is list2[0]
True
```

### Arithmetic Operators

```bash
# exponentiation
>>> 2**3
8
# modulus
>>> 7%3
1
>>> 7/3
2.3333333333333335
# floor division
>>> 7//3
2
```

## Lab Exercise