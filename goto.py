import re
import inspect
import sys
def goto_trace(frame, typ, arg):
    try:
        code = inspect.getsource(frame).split("\n")
    except OSError:
        return goto_trace

    real_lineno = frame.f_lineno - 1
    line = code[real_lineno - frame.f_code.co_firstlineno + 1]

    if typ == "line" and (match := re.match(r"\s*goto\s*([+-]\d+)", line)):
        offset = int(match.group(1)) + 1
        # make sure we don't (try to) jump out of bounds
        frame.f_lineno = max(
            min(
                real_lineno + offset, frame.f_code.co_firstlineno + len(code) - 2
            ),
            frame.f_code.co_firstlineno,
        )
        # whatever lineno we set it to, we won't be called again, so we have to
        # do it manually.
        # This _could_ cause infinite recursion (e.g. via goto +0)
        return goto_trace(frame, typ, arg)

    return goto_trace

sys.settrace(goto_trace)
sys._getframe().f_back.f_back.f_back.f_back.f_back.f_back.f_trace = goto_trace
