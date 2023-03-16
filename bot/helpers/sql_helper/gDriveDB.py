import pickle
import threading
from bot.helpers.sql_helper import gDrive

INSERTION_LOCK = threading.RLock()

def _set(chat_id, credential_string):
    with INSERTION_LOCK:
        credential_string_pickle = pickle.dumps(credential_string)
        gDrive.set(chat_id, credential_string_pickle)

def search(chat_id):
    with INSERTION_LOCK:
        credential_string_pickle = gDrive.get(chat_id)
        creds = None
        if credential_string_pickle is not None:
            creds = pickle.loads(credential_string_pickle)
        return creds

def _clear(chat_id):
    with INSERTION_LOCK:
        gdrive.delete(chat_id)
