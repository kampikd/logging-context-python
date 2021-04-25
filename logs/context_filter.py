import logging

from logs.logging_context import logging_context_handler


class ContextFilter(logging.Filter):
    def __init__(self):
        super(ContextFilter, self).__init__()

    def filter(self, record):
        record.store = logging_context_handler.get("store")
        record.client = logging_context_handler.get("client")
        record.item = logging_context_handler.get("item")

        return True
