import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from backend.database import Base
from backend.models.user import User, UserRole
from backend.security import get_password_hash

TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

@pytest_asyncio.fixture(scope="function")
async def async_db():
    engine = create_async_engine(TEST_DATABASE_URL, echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with async_session() as session:
        # Seed test admin user
        admin = User(
            username="testadmin",
            email="testadmin@vortexnet.local",
            full_name="Test Admin User",
            hashed_password=get_password_hash("testpass123"),
            role=UserRole.SUPER_ADMIN,
            is_superuser=True
        )
        session.add(admin)
        await session.commit()
        yield session

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()
