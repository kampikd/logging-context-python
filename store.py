from logs import logger
from logs.logging_context import logging_context

clients = {"Jim": ["potatoes", "tomatoes"], "Tim": ["bread", "eggs", "milk"]}


def sell_goods(shopping_list):
    for item in shopping_list:
        with logging_context(item=item):
            logger.info("Sold 1 item.")


with logging_context(store="Hannah's Grocery Store"):
    for client, shopping_list in clients.items():
        with logging_context(client=client):
            sell_goods(shopping_list)
