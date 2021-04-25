from collections import deque
from contextlib import contextmanager


class LoggingContextHandler:
    def __init__(self):
        self.attributes = deque([{}])

    def add(self, **new_context_vars):
        old_context = self.attributes[0]
        new_context = {**old_context, **new_context_vars}
        self.attributes.appendleft(new_context)

    def get(self, key):
        return self.attributes[0].get(key)

    def remove(self):
        self.attributes.popleft()

    def __str__(self):
        return str(self.attributes)


logging_context_handler = LoggingContextHandler()


@contextmanager
def logging_context(**kwargs):
    logging_context_handler.add(**kwargs)

    yield

    logging_context_handler.remove()
