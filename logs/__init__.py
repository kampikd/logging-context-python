import logging
import sys

from logs.context_filter import ContextFilter


logger = logging.getLogger("myapp")
logger.setLevel(logging.INFO)

context_filter = ContextFilter()
logger.addFilter(context_filter)

format_string = "[%(store)s | %(client)s | %(item)s]: %(message)s"
stdout_formatter = logging.Formatter(format_string)
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setFormatter(stdout_formatter)
logger.addHandler(stdout_handler)
