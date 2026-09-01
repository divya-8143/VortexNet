import enum
from sqlalchemy import Column, String, Boolean, Enum, DateTime
from datetime import datetime
from backend.models.base import BaseModel

class UserRole(str, enum.Enum):
    SUPER_ADMIN = "SUPER_ADMIN"
    NETWORK_ENGINEER = "NETWORK_ENGINEER"
    NOC_OPERATOR = "NOC_OPERATOR"
    READ_ONLY_VIEWER = "READ_ONLY_VIEWER"

class User(BaseModel):
    __tablename__ = "users"

    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    full_name = Column(String(100), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), default=UserRole.NOC_OPERATOR, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    last_login = Column(DateTime, nullable=True)
    department = Column(String(100), nullable=True, default="Network Operations")

    def __repr__(self):
        return f"<User username={self.username} role={self.role}>"
