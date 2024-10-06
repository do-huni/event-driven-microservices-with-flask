import asyncio
from typing import List

from shared.core.bus.event.consumer import Consumer
from shared.core.bus.event.domain_event import DomainEvent
from shared.core.bus.event.event_bus import EventBus
from shared.infrastructure.bus.event.kafka_producer import KafkaProducer
from shared.infrastructure.bus.event.kafka_topic_creator import KafkaTopicCreator


class KafkaEventBus(EventBus):
    async def __init__(self, producer: KafkaProducer, topic_creator: KafkaTopicCreator, consumers: List[Consumer]):
        self.__producer = producer
        self.__consumers = consumers
        await topic_creator.create_topics()

    async def publish(self, events: List[DomainEvent]) -> None:
        print('publishing domain events...')
        for event in events:
            await self.__producer.send(topic=event.topic, payload=event.to_json())  # 비동기 전송

    async def listen(self) -> None:
        tasks = []
        for consumer in self.__consumers:
            tasks.append(asyncio.create_task(consumer.consume()))  # 비동기적으로 각 consumer를 실행
        await asyncio.gather(*tasks)  # 모든 consumer들이 동시 실행될 때까지 기다림
