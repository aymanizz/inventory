from datetime import datetime

from app import db


class TrackedMixin:
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class Item(TrackedMixin, db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True, nullable=False)
    description = db.Column(db.String(200))
    quantity = db.Column(db.Integer, nullable=False, default=1)
    unit = db.Column(db.String(10))
    deleted_at = db.Column(db.DateTime)
    deletion_comment = db.Column(db.String(200))

    @property
    def deleted(self):
        return self.deleted_at is not None

    def edit(self, name=None, description=None, quantity=None, unit=None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if quantity is not None:
            self.quantity = quantity
        if unit is not None:
            self.unit = unit

    def mark_deleted(self, deletion_comment=None):
        self.deleted_at = datetime.utcnow()
        self.deletion_comment = deletion_comment

    def undelete(self):
        self.deleted_at = None
        self.deletion_comment = None

    def __repr__(self):
        return "<Item {}>".format(self.name)
