from celery.bin.control import status
from fastapi import APIRouter, Depends, HTTPException

from scripts.api import APIEndPoints
from scripts.db import get_db
from scripts import schema
from sqlalchemy.orm import Session

from scripts.db.event_crud import EventCRUD
from scripts.logger.logging import logger

event_router = APIRouter(tags=["event services"])

@event_router.post(APIEndPoints.api_events, response_model=schema.EventOut)
async def create_event(event: schema.EventCreate, db: Session = Depends(get_db)):
    """
    Create a new event.

    Args:
        event (schema.EventCreate): The event data including title, date, description, etc.
        db (Session): SQLAlchemy database session.

    Returns:
        schema.EventOut: The newly created event with its ID and other details.
    """
    try:
        event_crud_handler = EventCRUD(db)
        return await event_crud_handler.create_event(event)
    except Exception as e:
        logger.exception(str(e))
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error while creating event")

@event_router.get(APIEndPoints.api_events, response_model=list[schema.EventOut])
async def get_events(db: Session = Depends(get_db)):
    """
    Retrieve all upcoming events.

    Args:
        db (Session): SQLAlchemy database session.

    Returns:
        List[schema.EventOut]: A list of upcoming events with their details.
    """
    try:
        event_crud_handler = EventCRUD(db)
        return await event_crud_handler.get_upcoming_events()
    except Exception as e:
        logger.exception(str(e))
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error while listing events")

@event_router.post("/events/{event_id}/register", response_model=schema.AttendeeOut)
async def register(event_id: int, attendee: schema.AttendeeCreate, db: Session = Depends(get_db)):
    """
    Register a new attendee for a given event.

    Args:
        event_id (int): The ID of the event to register the attendee for.
        attendee (schema.AttendeeCreate): Attendee details such as name, email, etc.
        db (Session): SQLAlchemy database session.

    Returns:
        schema.AttendeeOut: The registration confirmation for the attendee.
    """
    try:
        event_crud_handler = EventCRUD(db)
        return await event_crud_handler.register_attendee(event_id, attendee)
    except Exception as e:
        logger.exception(str(e))
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error while registering attendees")

@event_router.get("/events/{event_id}/attendees", response_model=list[schema.AttendeeOut])
async def list_attendees(event_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get a paginated list of attendees for a specific event.

    Args:
        event_id (int): The ID of the event.
        skip (int, optional): Number of attendees to skip (for pagination). Defaults to 0.
        limit (int, optional): Maximum number of attendees to return. Defaults to 10.
        db (Session): SQLAlchemy database session.

    Returns:
        List[schema.AttendeeOut]: A list of attendees registered for the event.
    """
    try:
        event_crud_handler = EventCRUD(db)
        return await event_crud_handler.get_attendees(event_id, skip, limit)
    except Exception as e:
        logger.exception(str(e))
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error occurred while listing attendees")