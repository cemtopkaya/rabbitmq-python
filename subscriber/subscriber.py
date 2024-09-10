# subscriber/subscriber.py
import os
import pika

rabbitmq_host = os.environ.get('RABBITMQ_HOST', 'localhost')
topic = os.environ.get('RABBITMQ_TOPIC', 'test_topic')

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()

channel.exchange_declare(exchange=topic, exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange=topic, queue=queue_name)

print(' [*] Mesajlar bekleniyor. Çıkmak için CTRL+C')

def callback(ch, method, properties, body):
    print(f" [x] Alındı: {body.decode()}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()