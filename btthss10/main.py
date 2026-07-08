from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from service import create_shipment, get_shipments

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/shipments")
def create_ship(
    tracking_number: str,
    db: Session = Depends(get_db)
):
    shipment = create_shipment(db, tracking_number)

    return {
        "id": shipment.id,
        "tracking_number": shipment.tracking_number,
        "status": shipment.status
    }


@app.get("/shipments")
def read_shipments(db: Session = Depends(get_db)):
    return get_shipments(db)