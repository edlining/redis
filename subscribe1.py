import redis

# Connect to Redis
r = redis.Redis(host= '10.1.0.160', port=6379, db=0)

# Subscribe to channel
p = r.pubsub()
p.subscribe('chanel1')

# Receive and display messages
for message in p.listen():
    if message['type'] == 'message':
        print(message['data'].decode('utf-8'))