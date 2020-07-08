from kafka import KafkaConsumer
import sys

bootstrap_servers = ['localhost:9092']
topicName = 'p3'

consumer = KafkaConsumer (topicName, group_id = 'group1',bootstrap_servers = bootstrap_servers,
auto_offset_reset = 'earliest')
for message in consumer:
       print(message.value)
       #print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))

