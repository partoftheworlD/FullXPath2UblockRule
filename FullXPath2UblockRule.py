#!/usr/bin/python3
import sys


def generate_rule(site, xpath):
    temp_string = ''

    temp_string += site

    xpath = xpath.replace('//', '/')
    xpath = xpath.replace('/html', '##html')
    xpath = xpath.replace('/', ' > ')
    xpath = xpath.replace('[', ":nth-of-type(")
    xpath = xpath.replace(']', ")")

    temp_string += xpath
    print(temp_string)


def main():
    if len(sys.argv) != 3:
        print("Example: FullXPath2UblockRule.py site fullxpath")
    else:
        generate_rule(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
