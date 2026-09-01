from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import List

class NetFlowRecordOut(BaseModel):
    id: int
    src_ip: str
    dst_ip: str
    src_port: int
    dst_port: int
    protocol: str
    application: str
    bytes_transferred: int
    packets_count: int
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)

class TopTalkerItem(BaseModel):
    ip_address: str
    total_bytes: int
    total_packets: int
    percentage: float

class ProtocolDistributionItem(BaseModel):
    protocol_name: str
    bytes_count: int
    percentage: float
