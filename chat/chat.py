import threading

from kafka import KafkaConsumer, KafkaProducer

BOOTSTRAP_SERVERS = ['localhost:9092']

def subscribe(topic):
    consumer = KafkaConsumer(topic, auto_offset_reset='latest',
                             bootstrap_servers=BOOTSTRAP_SERVERS,
                             value_deserializer=lambda value: value.decode('utf-8'))
    for msg in consumer:
        print(msg.value)

username1 = input('What is your name? ')
username2 = input('Who do want connect? ')

consumer_thread = threading.Thread(target=subscribe, args=(username2,))
consumer_thread.start()

producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS,
                         value_serializer=lambda value: bytes(value, encoding='utf-8'))

while True:
    key = username1
    value = input()
    producer.send(username1, value=value)
    producer.flush()