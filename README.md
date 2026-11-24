# Python Practicle

Python Programming Practical Repository, organised **unit-wise**.
Every program is in its own file and the question is written at the top of the file.

## Repository structure

```
Python-Practicle/
├── README.md
├── Unit_1/   Foundations of Python and Control Structures      (question_1.py ... question_30.py)
├── Unit_2/   Functions and Modular Programming                 (question_1.py ... question_5.py)
│   ├── arithmetic.py            (user-defined module, used in question_5.py)
│   └── student/                 (user-defined package, used in question_5.py)
│       ├── __init__.py
│       ├── details.py
│       └── results.py
├── Unit_3/   Strings and Python Collections                    (question_1.py ... question_5.py)
└── Unit_4/   Exception Handling, File Processing and Standard Libraries
```

## How to run

Open the terminal inside the unit folder and run:

```
cd Unit_1
python question_1.py
```

Unit 4 Question 5 (command-line arguments):

```
cd Unit_4
python question_5.py 10 5 +
```

## Topics covered

### Unit 1 - Foundations of Python and Control Structures
| Questions | Topic |
|-----------|-------|
| 1 - 5   | Input/Output, operators and expressions, type conversion |
| 6 - 15  | Decision making (if, if-else, elif, nested if) |
| 16 - 20 | while loop and digit-based programs |
| 21 - 26 | Loops (guessing game, prime, Fibonacci, factors, GCD/LCM) |
| 27 - 28 | Nested loops (tables and patterns) |
| 29 - 30 | Menu-driven program and class statistics |

### Unit 2 - Functions and Modular Programming
| Question | Topic |
|----------|-------|
| 1 | Functions and function arguments (positional, keyword, default) |
| 2 | Variable-length arguments (`*args`, `**kwargs`) and return statement |
| 3 | Recursive functions (factorial, Fibonacci) |
| 4 | Scope, lifetime and lambda functions |
| 5 | User-defined modules and packages |

### Unit 3 - Strings and Python Collections
| Question | Topic |
|----------|-------|
| 1 | String operations and string methods |
| 2 | String slicing and string formatting |
| 3 | List operations and list comprehension |
| 4 | Tuples, sets and set operations |
| 5 | Dictionaries, dictionary comprehension and nested collections |

### Unit 4 - Exception Handling, File Processing and Standard Libraries
| Question | Topic |
|----------|-------|
| 1 | Exception handling (try, except, else, finally, raise) |
| 2 | File handling - read, write and append |
| 3 | File methods (`tell`, `seek`, ...) and file exception handling |
| 4 | Standard libraries: `question_4_math.py`, `question_4_random.py`, `question_4_datetime.py` |
| 5 | Command-line arguments |
