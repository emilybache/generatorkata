def simple_generator():
    yield 1

def clean_phonenumber(number):
    number = number.strip()
    number = number.replace("-", "")
    number = number.replace(" ", "")
    return number

def cleaning_generator(lines):
    for name, number in splitting_generator(lines):
        yield "{},{}".format(name, clean_phonenumber(number))

def clean_phone_in_line(args_as_tuple):
    name, number = args_as_tuple
    return (name, clean_phonenumber(number))

def splitting_generator(lines):
    for line in lines:
        name, number = line.split(",")[:2]
        yield name, number


def b_names_generator(lines):
    for name, number in splitting_generator(lines):
        lastname = name.split()[-1]
        if "b" in lastname.lower():
            yield (name, number)

