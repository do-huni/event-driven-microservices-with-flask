import asyncio
import os
from concurrent.futures import ThreadPoolExecutor

from kafka import KafkaAdminClient
from kafka.admin import NewTopic

from src.shared.infrastructure.config.config import Config, app_config


class KafkaTopicCreator:
    def __init__(self, config: Config):
        self.__config = config
        self.topic = app_config[os.getenv('ENV', 'test')].TOPIC


    async def create_topics(self):
        loop = asyncio.get_event_loop()
        # ThreadPoolExecutor를 통해 동기 작업을 비동기로 실행
        with ThreadPoolExecutor() as executor:
            await loop.run_in_executor(executor, self._sync_create_topics)

    def _sync_create_topics(self):
        # 동기 Kafka Admin Client 사용
        admin_client = KafkaAdminClient(
            bootstrap_servers=self.__config.KAFKA_URI,
            client_id='test'
        )

        # Kafka 메타데이터 조회 및 토픽 존재 여부 확인
        topic_list = []
        if self.__config not in admin_client.list_topics():
            topic_list.append(NewTopic(name=self.topic, num_partitions=1, replication_factor=1))
            admin_client.create_topics(new_topics=topic_list, validate_only=False)
