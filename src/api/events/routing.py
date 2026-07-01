from fastapi import APIRouter, HTTPException, status
from .data import events
from typing import List
from .schemas import EventCreateModel, EventResponseSchema, EventUpdateModel


event_router = APIRouter()

@event_router.get("/", response_model=List[EventResponseSchema])
async def get_events():
    return events

@event_router.get("/{event_id}", response_model=EventResponseSchema)
async def get_a_single_event(event_id:int):
    for event in events:
        if event.get('id') == event_id:
            return event
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Event with id {event_id} was not found")

@event_router.post("/", response_model=EventResponseSchema)
async def create_event(event_data:EventCreateModel):
    if events:
        next_id = max(event["id"] for event in events) + 1
    else:
        next_id = 1

    new_event_dict = event_data.model_dump()

    new_event_dict["id"] = next_id
    events.append(new_event_dict)

    return new_event_dict

@event_router.patch("/{event_id}", response_model=EventResponseSchema)
async def update_event(event_data:EventUpdateModel, event_id:int):
    new_event_data = event_data.model_dump(exclude_unset=True)
    if not new_event_data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No fields provided for update")
    for event in events:
        if event.get('id') == event_id:
            event.update(new_event_data)
            return event
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"event with id {event_id} was not found.")

@event_router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_event(event_id:int):
    for index, event in enumerate(events):
        if event.get('id') == event_id:
            events.pop(index)
            return 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"event with id {event_id} was not found.")


    