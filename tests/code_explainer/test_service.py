import pytest
from src.code_explainer.models import CompletionModel
from src.code_explainer.service import code_explain_service
    
@pytest.mark.asyncio
async def test_get_code_explanation(test_db):
    
    # Code example to test 
    code = '''
    def add(x,y):
        return x + y
    ''';
    
    # Mock user data
    user_ip = '8.8.8.8'
    user_device = 'mac m1 pro'
    
    explanation, duration = await code_explain_service.get_code_explanation(code=code, user_ip=user_ip, user_device=user_device);
    
    completion = CompletionModel(
        prompt=code,
        completion=explanation,
        user_ip= user_ip,
        user_device=user_device,
        inference_duration_in_ms=duration,
        user_id= None,
        rating=None
    )
    
    # Get the last inserted data
    cursor = test_db.find().sort({'_id': -1}).limit(1)
    
    completion2 = [CompletionModel(**data) for data in cursor][0]
    
    assert completion2 == completion
    
    
    
    
    