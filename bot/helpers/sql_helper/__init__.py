import redis
from bot import DATABASE_URL, LOGGER

if DATABASE_URL is None:
    LOGGER.warning("DATABASE_URL is not set. The application cannot function without a database.")
    exit(1)

redis_client = redis.Redis(DATABASE_URL)

parent_id = redis_client
gDrive = redis_client
