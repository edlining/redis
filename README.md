Redis: Deploying Redis on Kubernetes, Building Chat Applications with Redis Pub/Sub on Kubernetes, and MongoDB Caching with Redis.
Setting up Redis on Kubernetes, building a real-time chat application with Redis Pub/Sub on Kubernetes, and leveraging MongoDB caching with Redis.


https://medium.com/@harshaljethwa19/redis-deploying-redis-on-kubernetes-building-chat-applications-with-redis-pub-sub-on-kubernetes-f81a56ec0273

Deploy Redis: Using a Deployment YAML file, we’ll deploy a Redis instance on Kubernetes. This YAML file defines the configuration for the Redis Deployment,
Save this below YAML to a file, for example `redis-deployment.yaml`, and apply it to your Kubernetes cluster. This will deploy a single Redis pod running the latest Redis image :
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis
spec:
  replicas: 1
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
      - name: redis
        image: redis:latest
        ports:
        - containerPort: 6379
kubectl apply -f redis-deployment.yaml 
