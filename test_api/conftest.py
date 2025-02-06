import pytest
import requests

@pytest.fixture(scope="function")
def get_session():
    session = requests.session()

    yield session
    
    session.close()