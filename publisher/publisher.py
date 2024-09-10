# publisher/publisher.py
import os
import pika
import time

rabbitmq_host = os.environ.get('RABBITMQ_HOST', 'localhost')
topic = os.environ.get('RABBITMQ_TOPIC', 'test_topic')

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()

channel.exchange_declare(exchange=topic, exchange_type='fanout')

while True:
    message = input("Mesajınızı girin: ")
    channel.basic_publish(exchange=topic, routing_key='', body=message)
    print(f" [x] Gönderildi: {message}")
    time.sleep(1)
