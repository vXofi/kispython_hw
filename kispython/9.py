import re


def main(input_string):
    pattern = r"new\s*#\s*([-\d]+)\s*==>\s*'([^']+)'"
    matches = re.findall(pattern, input_string)

    result = [(match[1], int(match[0])) for match in matches]
    return result
