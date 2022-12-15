import redis
import os
from consts import Consts

# Create a client instance
redis_client = redis.Redis(host=os.getenv('REDIS_HOST', 'redis'), port=os.getenv('REDIS_PORT', '6379'), db=0)

# Use the client to access Redis
def save(key, value):
  redis_client.set(key, value)
def get(key):
  redis_client.get(key)

def set_admin(admin):
  Consts.set_admin(int(admin))
  save(Consts.ADMIN_ID, 'admin')
