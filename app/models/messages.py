from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import text
from app.database import Base
from pgvector.sqlalchemy import Vector

class Message(Base):
    __tablename__ = "messages"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    user_id = Column(UUID(as_uuid=True), nullable=False)
    gmail_message_id = Column(String, nullable=True)
    account_email = Column(String, nullable=True)
    subject = Column(Text, nullable=True)
    sender = Column(String, nullable=True)
    body = Column(Text, nullable=True)
    received_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("now()"))
    embedding = Column(Vector(3072))
