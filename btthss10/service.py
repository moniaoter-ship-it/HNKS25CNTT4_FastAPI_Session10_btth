from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from model import ShipmentModel


def create_shipment(tracking_number: str, db: Session):

    check_exists_shipment = (
        db.query(ShipmentModel)
        .filter(ShipmentModel.tracking_number == tracking_number)
        .first()
    )

    if check_exists_shipment:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Mã vận đơn này đã được khởi tạo trước đó"
        )

    new_shipment = ShipmentModel(
        tracking_number=tracking_number
    )

    db.add(new_shipment)
    db.commit()
    db.refresh(new_shipment)

    return new_shipment

def get_shipments(db: Session):

    shipments = db.query(ShipmentModel).all()

    return shipments