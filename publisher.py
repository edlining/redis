import redis

# Connect to Redis
r = redis.Redis(host='10.1.0.158', port=6379, db=0)

# User input for message
while True:
    i = input("Enter the slave number to talk with him: ")
    if i == "1":
        message = input("Enter the message for slave-01: ")
        r.publish('chanel1', message)
    elif i == "2":
        message = input("Enter the message for slave-02: ")
        r.publish('chanel2', message)
    else:
        print("Kindly enter 1 or 2")