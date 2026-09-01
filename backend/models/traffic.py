from sqlalchemy import Column, String, BigInteger, Integer, DateTime
from datetime import datetime
from backend.models.base import BaseModel

class NetFlowRecord(BaseModel):
    __tablename__ = "netflow_records"

    src_ip = Column(String(45), nullable=False, index=True)
    dst_ip = Column(String(45), nullable=False, index=True)
    src_port = Column(Integer, nullable=False)
    dst_port = Column(Integer, nullable=False)
    protocol = Column(String(10), nullable=False)
    application = Column(String(50), nullable=False, index=True)
    bytes_transferred = Column(BigInteger, default=0)
    packets_count = Column(BigInteger, default=0)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)

    def __repr__(self):
        return f"<NetFlow {self.src_ip}:{self.src_port} -> {self.dst_ip}:{self.dst_port} App={self.application}>"
