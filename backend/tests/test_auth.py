import pytest
from backend.services.auth_service import AuthService
from backend.schemas.user import UserCreate
from backend.models.user import UserRole
from backend.security import create_access_token, decode_token

@pytest.mark.asyncio
async def test_user_authentication_success(async_db):
    user = await AuthService.authenticate_user(async_db, "testadmin", "testpass123")
    assert user is not None
    assert user.username == "testadmin"
    assert user.role == UserRole.SUPER_ADMIN

@pytest.mark.asyncio
async def test_user_authentication_failure(async_db):
    user = await AuthService.authenticate_user(async_db, "testadmin", "wrongpassword")
    assert user is None

@pytest.mark.asyncio
async def test_create_new_user(async_db):
    user_in = UserCreate(
        username="neteng1",
        email="neteng1@vortexnet.local",
        full_name="Network Engineer 1",
        password="securepassword123",
        role=UserRole.NETWORK_ENGINEER
    )
    user = await AuthService.create_user(async_db, user_in)
    assert user.id is not None
    assert user.username == "neteng1"
    assert user.role == UserRole.NETWORK_ENGINEER

@pytest.mark.asyncio
async def test_jwt_token_generation_and_decoding():
    token = create_access_token("testadmin", roles=["SUPER_ADMIN"])
    payload = decode_token(token)
    assert payload is not None
    assert payload["sub"] == "testadmin"
    assert "SUPER_ADMIN" in payload["roles"]
