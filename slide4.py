import sys

# trace function: called at certain times by Python, with the current frame
def trace(frame, event, arg):
    # event types: call, line, return, exception, opcode
    print("Tracing", frame, "with", event)
    return trace

# set global trace function
sys.settrace(trace)

def add(x, y):
    return x + y

add(23, 42)
