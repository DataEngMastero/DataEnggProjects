# Create Kafka Topic
kafka-topics.sh --bootstrap-server localhost:9092 --create --topic stock_topic --partitions 3 --replication-factor 1