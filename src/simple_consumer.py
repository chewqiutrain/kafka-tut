from kafka import KafkaConsumer
from kafka import TopicPartition
import uuid 
from models import TestData, TestFees

def uuid_deserialiser(raw: bytes): 
    s = raw.decode("utf-8")
    return uuid.UUID(s)

def test_data_deserialiser(raw: bytes):
    s = raw.decode("utf-8")
    return TestData.from_json(s)

def main():
    TOPIC_NAME = "test-topic-kafka-tut"
    CLIENT_ID = "simple-consumer-0"
    GROUP_ID = "simple-consumer-group"
    consumer = KafkaConsumer(bootstrap_servers="localhost:29092",
                            client_id=CLIENT_ID,
                            group_id=GROUP_ID,
                            key_deserializer=uuid_deserialiser,
                            value_deserializer=test_data_deserialiser
                            )

    consumer.assign(partitions=[TopicPartition(TOPIC_NAME, 0)])
    consumer.seek_to_beginning()
    
    i = 0
    for msg in consumer:
        print(msg)
        print(type(msg))
        key = msg.key
        value = msg.value
        print(f"key: {key}")
        print(f"value: {value}")
        i += 1 
        if i > 0:
            break





if __name__ == "__main__":
    # s = "7673321f-fa49-4016-9497-c7627c03906e"
    
    main()