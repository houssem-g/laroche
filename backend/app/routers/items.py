# app/routers/items.py

from fastapi import APIRouter, HTTPException
from app.database.rdf_client import RDFClient
from app.schemas.item import ItemCreate, ItemUpdate

router = APIRouter(prefix="/items", tags=["items"])
rdf_client = RDFClient()

@router.post("/")
def create_item(payload: ItemCreate):
    success = rdf_client.create_data(
        subject=payload.subject,
        predicate=payload.predicate,
        obj=payload.obj
    )
    if not success:
        raise HTTPException(status_code=500, detail="Failed to create item in RDF store.")
    return {"message": "Item created successfully."}

@router.get("/{subject}")
def read_item(subject: str):
    data = rdf_client.read_data(subject)
    if not data:
        return {"message": f"No data found for subject: {subject}"}
    return {"subject": subject, "predicates": data}

@router.delete("/{subject}")
def delete_item(subject: str, predicate: str = None):
    """
    If 'predicate' is provided, delete only that triple. Otherwise, delete all for the subject.
    """
    success = rdf_client.delete_data(subject, predicate)
    if not success:
        raise HTTPException(status_code=500, detail="Failed to delete.")
    return {"message": "Deleted successfully"}

@router.put("/{subject}")
def update_item(subject: str, payload: ItemUpdate):
    """
    Example 'update' that changes old_predicate -> new_predicate for the given subject.
    """
    success = rdf_client.update_data(subject, payload.old_predicate, payload.new_predicate)
    if not success:
        raise HTTPException(status_code=500, detail="Failed to update.")
    return {"message": "Item updated successfully."}
