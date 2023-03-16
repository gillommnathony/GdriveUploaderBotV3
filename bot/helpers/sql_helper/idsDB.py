from bot.helpers.sql_helper import parent_id

PARENT_ID_KEY_PREFIX = "parent_id_"

def search_parent(chat_id):
    parent_id_key = PARENT_ID_KEY_PREFIX + chat_id
    parent_id_value = redis_client.get(parent_id_key)
    if parent_id_value is not None:
        return parent_id_value.decode('utf-8')
    else:
        return "root"

def _set(chat_id, parent_id_value):
    parent_id_key = PARENT_ID_KEY_PREFIX + chat_id
    redis_client.set(parent_id_key, parent_id_value)

def _clear(chat_id):
    parent_id_key = PARENT_ID_KEY_PREFIX + chat_id
    redis_client.delete(parent_id_key)
