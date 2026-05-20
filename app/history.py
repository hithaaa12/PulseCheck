from collections import deque

# Stores last 20 monitoring snapshots
history_store = deque(maxlen=20)


def add_to_history(data):

    history_store.append(data)


def get_history():

    return list(history_store)