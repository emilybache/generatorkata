# generatorkata
A kata focused on learning Python Generators

This kata makes use of phone_data_10000.txt from the [Phone Numbers Kata](https://github.com/emilybache/Phone-Numbers-Kata) found in the ["The Coding Dojo Handbook"](http://leanpub.com/codingdojohandbook) by Emily Bache.

## Prerequisites

* Python >= 3.3
* [PyTest](https://docs.pytest.org/en/latest/)

## Test Driven Development

Write unit tests in `test_generatorkata.py` for each step below in  corresponding implementation code in `generatorkata.py`.

## How to run tests

    $ pytest test_generatorkata.py -v

## Exercises

### Step 1

Write a generator function that given a list of names and phone numbers generates "pure" phone numbers, i.e. no spaces or dashes.

Example:

Input list/iterator:

    Silas Scarth,0394 012-5-02
    Micheal Veronesi,01725 30 75
    Blythe Milby,0027360 8 81

Generator function yields:

    Silas Scarth,0394012502
    Micheal Veronesi,017253075
    Blythe Milby,0027360881

### Step 2

Write a generator function that given a list of names and phone numbers only yields those lines where the last name contains character "b"

Example:

Input list/iterator:

    Adena Helble,0163 2783782
    Elda Keough,0560397-05-82

Generator function yields:

    Adena Helble,0163 2783782

### Step 3

Write a generator function, gen_open, that opens a file and yields all lines.

### Step 4

Combine generator functions in step 1, 2 and 3 to print out all "pure" phone numbers from phone_data_10000.txt where the last name contains character "b"

### Step 5

Modify the generator function in step 2 to let the client change what character to search for each time the generator is resumed using the send method.

Example:

    Adena Helble,0163 2783782
    Elda Keough,0560397-05-82
    Bret Pistole,083-018-52-62
    Elfreda Capron,01780 47 57

Generator client:

    g_it = generator()
    print(g_it.send("i")
    print(g_it.send("x")

Should yield:

    Adena Helble,0163 2783782
    Bret Pistole,083-018-52-62

### Step 6

Write a generator function similar to the one in step 1. But instead of removing all spaces and dashes it inserts a dash after every third character.

### Step 7

Use the generator functions in step 1 and step 6 as sub generators and switch between them depending on start value passed to the parent generator.