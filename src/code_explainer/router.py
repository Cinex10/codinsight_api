from fastapi import APIRouter, HTTPException, Request
from .service import code_explain_service
from .schemas import CompletionCreate, CompletionRate, CompletionResponse

router = APIRouter()

@router.post("/explain", response_model=CompletionResponse)
async def explain_code(
    request: CompletionCreate,
    req: Request
):
    result = await code_explain_service.get_code_explanation(
        code=request.prompt,
        user_ip=req.client.host,
        user_device=req.headers.get("User-Agent", "Unknown")
    )
    return CompletionResponse(
        completion=result[0],
        prompt=request.prompt
    )

@router.post("/completions/{completion_id}/rate")
async def rate_completion(
    request: CompletionRate,
    completion_id: str
):  
    completion = await code_explain_service.get_completion_by_id(completion_id)
    if completion is None:
        raise HTTPException(status_code=404, detail="Completion not found")
    
    await code_explain_service.update_completion_rating(completion_id, request.rating)
    return {"message": "Rating updated successfully"}