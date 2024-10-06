from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.sql import func


@as_declarative()
class CoreEntity:
    id = Column(Integer, primary_key=True, autoincrement=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), comment="생성일시 (UTC)")
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), comment="마지막 수정일시 (UTC)")
    deleted_at = Column(DateTime(timezone=True), nullable=True, comment="삭제일시 (UTC)")

    def soft_delete(self):
        self.deleted_at = func.now()
