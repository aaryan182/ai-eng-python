import redis
import json

redis_client = redis.Redis( host="localhost", port= 6379, decode_responses= True)

def set_json(key,value):
    redis_client.set(key, json.dumps(value))

def get_json(key):
    val = redis_client.get(key)
    return json.loads(val) if val else None

