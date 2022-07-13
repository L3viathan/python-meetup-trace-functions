import sys
import inspect

def trace(frame, event, arg):
    with open(inspect.getsourcefile(frame)) as f:
        lines = f.readlines()
    line = lines[frame.f_lineno - 1].rstrip()
    print("->", line)
    while True:
        match input("mypdb> "):
            case "":
                continue
            case "l" | "line":
                print("->", line)
            case "c" | "continue":
                sys.settrace(None)
                return None
            case "n" | "next":
                break
            case "q":
                raise
            case command if command.startswith("!"):
                exec(command[1:], frame.f_globals, frame.f_locals)
            case _:
                print("unknown command")
    return trace

def set_trace():
    # install global trace function
    sys.settrace(trace)
    # also do that other thing
    sys._getframe().f_back.f_trace = trace
