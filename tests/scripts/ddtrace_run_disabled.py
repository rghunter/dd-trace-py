from __future__ import print_function

from ddtrace import tracer

if __name__ == '__main__':
    assert not tracer.enabled
    print("Test success")
