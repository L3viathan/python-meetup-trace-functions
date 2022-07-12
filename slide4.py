import sys

# trace function: called at certain times by Python, with the current frame
def trace(frame, event, arg):
    # event types: call, line, return, exception, opcode
    print("Tracing", frame, "with", event)

# set global trace function
sys.settrace(trace)
