# exc must be exception instance or None.
raise RuntimeError from exc

def func():
    raise IOError

try:
    func()
except IOError as exc:
    raise RuntimeError('Failed to open database') from exc

