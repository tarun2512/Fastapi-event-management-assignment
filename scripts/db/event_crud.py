from sqlalchemy.orm import Session
from scripts.db.models import Event, Attendee
from scripts.logger.logging import logger
from scripts.schema import EventCreate, AttendeeCreate
from fastapi import HTTPException
from datetime import datetime, timezone


class EventCRUD:
    def __init__(self, db: Session):
        self.session = db

    async def create_event(self, event: EventCreate):
        try:
            db_event = Event(**event.model_dump())
            self.session.add(db_event)
            self.session.commit()
            self.session.refresh(db_event)
            return db_event
        except Exception as e:
            logger.error(str(e))

    async def get_upcoming_events(self):
        try:
            return self.session.query(Event).filter(Event.start_time >= datetime.now(timezone.utc)).all()
        except Exception as e:
            logger.error(str(e))


    async def register_attendee(self, event_id: int, attendee: AttendeeCreate):
        try:
            db_event = self.session.query(Event).filter(Event.id == event_id).first()
            if not db_event:
                raise HTTPException(status_code=404, detail="Event not found")

            if len(db_event.attendees) >= db_event.max_capacity:
                raise HTTPException(status_code=400, detail="Event capacity full")

            existing = self.session.query(Attendee).filter_by(event_id=event_id, email=attendee.email).first()
            if existing:
                raise HTTPException(status_code=400, detail="Duplicate registration")

            db_attendee = Attendee(**attendee.model_dump(), event_id=event_id)
            self.session.add(db_attendee)
            self.session.commit()
            self.session.refresh(db_attendee)
            return db_attendee
        except Exception as e:
            logger.error(str(e))

    async def get_attendees(self, event_id: int, skip: int = 0, limit: int = 10):
        try:
            return self.session.query(Attendee).filter(Attendee.event_id == event_id).offset(skip).limit(limit).all()
        except Exception as e:
            logger.error(str(e))
