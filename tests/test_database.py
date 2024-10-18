from src.database import get_db

def test_database_connection():
    db = get_db()
    assert db is not None, "Database connection failed"

def test_insert_and_retrieve(test_db):
    # Insert a test document
    test_document = {"name": "Test User", "email": "test@example.com"}
    result = test_db.insert_one(test_document)
    assert result.inserted_id is not None, "Failed to insert test document"

    # Retrieve the test document
    retrieved_document = test_db.find_one({"_id": result.inserted_id})
    assert retrieved_document is not None, "Failed to retrieve test document"
    assert retrieved_document["name"] == "Test User", "Retrieved document data mismatch"

def test_update(test_db):
    # Insert a test document
    test_document = {"name": "Update Test", "status": "pending"}
    result = test_db.insert_one(test_document)

    # Update the document
    update_result = test_db.update_one(
        {"_id": result.inserted_id},
        {"$set": {"status": "completed"}}
    )
    assert update_result.modified_count == 1, "Failed to update test document"

    # Verify the update
    updated_document = test_db.find_one({"_id": result.inserted_id})
    assert updated_document["status"] == "completed", "Document update failed"

def test_delete(test_db):
    # Insert a test document
    test_document = {"name": "Delete Test"}
    result = test_db.insert_one(test_document)

    # Delete the document
    delete_result = test_db.delete_one({"_id": result.inserted_id})
    assert delete_result.deleted_count == 1, "Failed to delete test document"

    # Verify the deletion
    deleted_document = test_db.find_one({"_id": result.inserted_id})
    assert deleted_document is None, "Document was not deleted"