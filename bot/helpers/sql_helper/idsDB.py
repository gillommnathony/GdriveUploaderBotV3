from bot.helpers.sql_helper import parent_id

def search_parent(chat_id):
    result = parent_id.find_one({"_id": chat_id})
    if result:
        return result["parent_id"]
    else:
        return "root"


def _set(chat_id, parent_id_value):
    parent_id_object = {"_id": chat_id, "parent_id": parent_id_value}
    parent_id.replace_one({"_id": chat_id}, parent_id_object, upsert=True)


def _clear(chat_id):
    parent_id.delete_one({"_id": chat_id})
