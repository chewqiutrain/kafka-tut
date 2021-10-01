# Kafka-tut 
Spin up a single broker Kafka with Zookeeper and Kowl 
Kowl UI at `http://localhost:8081` 

## Kafka APIs
[Docs](https://kafka.apache.org/documentation/#api)
To do:
1. ~~Simple Python producer~~
1. ~~Simple Python consumer~~
1. Avro serialiser 
1. Set up schema registry and link to Kowl
1. Figure out how to use the Connect API to write from stream to Postgres or Redshift 
1. Figure out how to use Streams API to write from source topic to target topic 


## Install `kcat` 
```sh
brew install kafkacat
```

Get broker metadata 
```sh
λ yingqiu [kafka-tut/kafka-3.0.0-src/bin] → kcat -L -b localhost:29092
Metadata for all topics (from broker 1: localhost:29092/1):
 1 brokers:
  broker 1 at localhost:29092 (controller)
 1 topics:
  topic "__confluent.support.metrics" with 1 partitions:
    partition 0, leader 1, replicas: 1, isrs: 1
```
[More info](https://github.com/edenhill/kcat)


## `kowl` 
```sh
docker run --rm -p 8081:8080 --network=kafka-tut_default -e KAFKA_BROKERS=kafka:9092 quay.io/cloudhut/kowl:master
```


## Producing messages
```sh
kcat \
    -b localhost:29092 \
    -t test \
    -K: \
    -P <<EOF
1:{"order_id":1,"order_ts":1534772501276,"total_amount":10.50,"customer_name":"Bob Smith"}
2:{"order_id":2,"order_ts":1534772605276,"total_amount":3.32,"customer_name":"Sarah Black"}
3:{"order_id":3,"order_ts":1534772742276,"total_amount":21.00,"customer_name":"Emma Turner"}
EOF
```

## Kafka CLI tools 
Bunch of shell scripts. Need to download the tar ball and build the project before you can use it. 
https://kafka.apache.org/downloads

