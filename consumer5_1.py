import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='ttl_queue', arguments={'x-message-ttl': 10000})



for i in range(10):
    time.sleep(1)
    msg = f'msg{i}'
    print(f'[x] Sent {msg}')
    channel.basic_publish(exchange='', routing_key='ttl_queue', body=msg)
connection.close()
