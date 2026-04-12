from fastapi import APIRouter
from schemas.action import ExecuteRequest
from services.orchestrator_adapter import process

router = APIRouter()

@router.post("/execute")
def execute(req: ExecuteRequest):
    return process(req.actor_id, req.action.dict())
