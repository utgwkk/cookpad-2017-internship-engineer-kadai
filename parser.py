import sys
import re
from collections import deque


def calculate_level(text):
    if text.startswith('    '):
        return 0
    text = text.lstrip()
    if text.startswith('####### '):
        return 0
    elif text.startswith('###### '):
        return 1
    elif text.startswith('##### '):
        return 2
    elif text.startswith('#### '):
        return 3
    elif text.startswith('### '):
        return 4
    elif text.startswith('## '):
        return 5
    elif text.startswith('# '):
        return 6
    else:
        return 0


def unescape_sharp(text):
    return text.replace('\#', '#')


def sanitize(text):
    level = calculate_level(text)
    if level > 0:
        header = text[text.index('# ')+1:].strip()
        if re.search(r' (#)+$', header):
            new_header = header[:header.rindex(' #')]
            return new_header
        else:
            return unescape_sharp(header)
    else:
        return unescape_sharp(text)


def parse(text):
    res = []

    for line in text.splitlines():
        if not line:
            continue

        level = calculate_level(line)
        res.append((level, sanitize(line)))

    return res


def answer(tokenized, query):
    if len(query) == 0:
        raise Exception('Please specify query.')

    stack = deque([(7, 'dummy')])
    idx = 0
    answers = []

    for token in tokenized:
        if token[0] < stack[-1][0]:
            stack.append(token)
        elif token[0] > stack[-1][0]:
            while token[0] >= stack[-1][0]:
                top = stack.pop()
                if idx == len(query):
                    return answers
            if query[idx] == stack[-1][1]:
                idx += 1
            stack.append(token)
        elif token[0] == 0 and stack[-1][0] == 0:
            stack.append(token)

        if idx == len(query):
            answers.append(stack[-1][1])
        elif query[idx] == stack[-1][1]:
            idx += 1
        # print(stack)

    return answers


def main(argv):
    tokenized = parse(sys.stdin.read())
    answers = answer(tokenized, argv[1:])

    print('\n'.join(answers))

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
