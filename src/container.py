import os

from dependency_injector import containers, providers

from src.shared.infrastructure.bus.event.kafka_event_bus import KafkaEventBus
from src.shared.infrastructure.bus.event.kafka_producer import KafkaProducer
from src.shared.infrastructure.bus.event.kafka_topic_creator import KafkaTopicCreator
from src.shared.infrastructure.config.config import app_config


class Container(containers.DeclarativeContainer):
    # infra services

    topic_creator = providers.Singleton(
        KafkaTopicCreator,
        config=app_config.get(os.getenv('ENV', 'test'))
    )
    producer = providers.Singleton(
        KafkaProducer,
        config=app_config.get(os.getenv('ENV', 'test'))
    )

    event_bus = providers.Singleton(
        KafkaEventBus,
        producer=producer,
        topic_creator=topic_creator,
        consumers=[]
    )

    # repositories


    # application services


    # controllers
