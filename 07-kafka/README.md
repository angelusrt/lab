# Kafka

Estudando Kafka e o padrão produtor-consumidor orientado a eventos.

O que eu entendi é que só faz sentido streaming quando você tem 
controle/influência sobre (no mínimo) os produtores.

## Como funciona em Prod

Em prod, você tem um servidor Kafka funcionando como o intermediador e 
nas pontas você possui serviços lendo e escrevendo para ele.

```{python}
# Produtor

from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='192.168.1.100:9092',
    value_serializer=lambda v: json.dumps(v).encode()
)

producer.send('esus.atendimentos', {
    'co_cnes': '1234567',
    'dt_atendimento': '2026-06-14'
})

# Consumidor

from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'esus.atendimentos',
    bootstrap_servers='192.168.1.100:9092',
    value_deserializer=lambda v: json.loads(v)
)

for message in consumer:
    print(message.value)
```

## Build

Rodando:

```{bash}
docker compose up
```

Produzindo e consumindo:

```{bash}
# Criando tópico
docker exec -it 07-kafka-kafka-1 kafka-topics \
  --create \
  --topic hello-world \
  --bootstrap-server localhost:9092 \
  --partitions 1 \
  --replication-factor 1

# Criando consumidor
docker exec -it 07-kafka-kafka-1 kafka-console-consumer \
  --topic hello-world \
  --bootstrap-server localhost:9092 \
  --from-beginning

# Criando produtor
docker exec -it 07-kafka-kafka-1 kafka-console-producer \
  --topic hello-world \
  --bootstrap-server localhost:9092
```
