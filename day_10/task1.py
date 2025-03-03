def format_name(first_name, last_name):
    """Take a first and last name and return a formatted name."""
    name = first_name + ' ' + last_name
    return name.title()

name = format_name('xxx', 'ddddddddddddd ')
print(name)

