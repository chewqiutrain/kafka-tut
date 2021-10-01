from kafka import KafkaProducer
import uuid 
from datetime import datetime
import names 
import random
from models import TestFees, TestData



def create_test_data():
    id = uuid.uuid4()
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    age = random.randrange(start=1, stop=100)
    created_tstamp = datetime.now()
    fee_amount_int = random.randrange(start=0, stop=1000)
    fee_amount_float = 1.0 * random.random()
    fee_amount = fee_amount_int + fee_amount_float
    fee_currency = "SGD"
    fee = TestFees(amount=fee_amount, currency=fee_currency)
    return TestData(id, first_name, last_name, created_tstamp, fee)



def main():
    TOPIC_NAME = "test-topic-kafka-tut"
    RESPONSE_TIMEOUT = 5 # seconds
    producer = KafkaProducer(bootstrap_servers="localhost:29092")
    num_messages = 1
    
    for i in range(0, num_messages):
        data_i = create_test_data()
        serialised_key_i = data_i.id.__str__().encode("utf-8")
        serialised_data_i = data_i.to_json().encode("utf-8")
        future_i = producer.send(TOPIC_NAME,key=serialised_key_i, value=serialised_data_i)
        result = future_i.get(timeout=RESPONSE_TIMEOUT)
        print(f"send result: {result} | data: {data_i}")

    

if __name__ == "__main__":
    main()