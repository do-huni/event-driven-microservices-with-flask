from abc import ABC, abstractmethod
from shared.core.domain_entity import DomainEntity
from src.shared.infrastructure.entities.core_entity import CoreEntity


class DatabaseMapper(ABC):
    @abstractmethod
    def to_database_object(self, domain: DomainEntity) -> CoreEntity:
        raise NotImplementedError

    @abstractmethod
    def to_domain_object(self, database_object: CoreEntity) -> DomainEntity:
        raise NotImplementedError