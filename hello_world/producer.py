from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('sample', 'Step 8')
# producer.send('sample', key=b'message-4', value=b'This is Kafka-Python 4')
producer.flush()