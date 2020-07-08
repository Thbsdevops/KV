from kafka import KafkaProducer
topicName = 'p3'
producer = KafkaProducer(bootstrap_servers = ['localhost:9092'])
producer = KafkaProducer()
ack = producer.send('p3', ' Demo code for producer....')
metadata = ack.get()
print(metadata.topic)
