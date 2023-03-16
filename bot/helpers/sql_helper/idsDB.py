from bot.helpers.sql_helper import parent_id

def search_parent(chat_id):
    parent_id_value = parent_id.get(chat_id)
    if parent_id_value is not None:
        return parent_id_value.decode('utf-8')
    else:
        return "root"

def _set(chat_id, parent_id_value):
    parent_id.set(chat_id, parent_id_value)

def _clear(chat_id):
    parent_id.delete(chat_id)
