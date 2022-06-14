from kafka import KafkaConsumer

# BOOTSTRAP_SERVERS = ['localhost:9092']
# consumer = KafkaConsumer('sample', auto_offset_reset='latest',
                         # bootstrap_servers=BOOTSTRAP_SERVERS,
                         # value_deserializer=lambda value: value.decode('utf-8'))

consumer = KafkaConsumer('sample')
for message in consumer:
    print (message.value)