import asyncio
import json

from aiokafka import AIOKafkaProducer

from src.shared.infrastructure.config.config import Config


class KafkaProducer:
    def __init__(self, config: Config):
        # AIOKafkaProducer는 비동기적으로 동작하므로, start()로 연결을 시작해야 함
        self.__producer = AIOKafkaProducer(
            bootstrap_servers=config.KAFKA_URI,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    async def start(self):
        # 프로듀서를 시작하는 비동기 메서드
        await self.__producer.start()

    async def stop(self):
        # 프로듀서를 종료하는 비동기 메서드
        await self.__producer.stop()

    async def send(self, topic: str, payload: dict):
        # 비동기 방식으로 메시지 전송
        await self.__producer.send(topic, payload)


# 사용 예시
async def main():
    config = Config()  # Flask의 Config 클래스 사용
    config.KAFKA_URI = 'localhost:9092'  # Kafka URI 설정

    kafka_producer = KafkaProducer(config)
    
    # 프로듀서 시작
    await kafka_producer.start()

    # 메시지 전송
    await kafka_producer.send('test-topic', {"key": "value"})

    # 프로듀서 종료
    await kafka_producer.stop()

# asyncio를 사용해 main 함수 실행
if __name__ == '__main__':
    asyncio.run(main())
