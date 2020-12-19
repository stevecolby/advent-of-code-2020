import re, ast

def Run(lines):
    ans = 0

    for line in lines:
        chunk = ''
        chunk_pos = 0
        for char in line:
            chunk += char
            if char == '(':
                chunk_pos += 1
            elif char == ')':
                opening_brace_loc = chunk.rfind('(', 0, chunk_pos)
                bracket_calc = single_calc(chunk[opening_brace_loc : chunk_pos+1])
                chunk = chunk[:opening_brace_loc] + bracket_calc
            else:
                chunk_pos += 1
        print(int(single_calc(chunk)))
        ans += int(single_calc(chunk))

    print(ans)


def single_calc(t: str):
    t2 = t.replace('(','').replace(')','').split(' ')
    while '+' in t2:
        i = t2.index('+')
        t2[i-1] = str(int(t2[i-1]) + int(t2[i+1]))
        t2.pop(i)
        t2.pop(i)
    return str(eval(' '.join(t2)))