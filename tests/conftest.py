import pytest
from src.database import get_db, close_mongo_connection

@pytest.fixture(scope="session", autouse=True)
def setup_mongo_connection():
    """
    Set up the MongoDB connection at the start of the test session.
    Close the connection after all tests have run.
    """
    get_db()  # Initialize the connection

    yield

    close_mongo_connection()  # Close the connection after the session

@pytest.fixture(scope="module")
def test_db():
    """
    Use a test collection within the test database.
    This fixture is scoped to the module and ensures a clean environment for each test module.
    """
    db = get_db()
    
    # Create a test collection
    test_collection = db.completions
    
    yield test_collection
    
    # Clean up after all tests in the module by dropping the test collection
    test_collection.drop()
