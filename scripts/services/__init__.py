from fastapi import APIRouter

from scripts.config import Service
from scripts.services.event_management_services import event_router

router = APIRouter()


@router.get(f"/api/{Service.MODULE_NAME}/healthcheck")
def ping():
    return {"status": 200}

router.include_router(event_router)
