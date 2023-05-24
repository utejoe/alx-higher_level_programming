#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4
    func_names = []
    for m in dir(hidden_4):
        if m[0] != "_":
            func_names.append(m)
    func_names.sort()
    for i in func_names:
        print(i)
