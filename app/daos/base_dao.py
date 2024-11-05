from sqlalchemy.orm import Session

class BaseDAO():
    model = None

    @classmethod
    def get_all(cls, db: Session):
        return db.query(cls.model).all()

    @classmethod
    def get_paginated(cls, db: Session, page: int, size: int = 10):
        offset = (page - 1) * size
        return db.query(cls.model).offset(offset).limit(size).all()

    @classmethod
    def get_by_id(cls, id: int, db: Session):
        return db.get(cls.model, id)

    @classmethod
    def create(cls, data: dict, db: Session):
        new_entity = cls.model(**data)

        db.add(new_entity)
        db.commit()
        db.refresh(new_entity)

        return new_entity

    @classmethod
    def update(cls, id: int, data: dict, db: Session):
        entity = db.get(cls.model, id)
    
        for attr, value in data.items():
            if hasattr(entity, attr):
                setattr(entity, attr, value)
            else:
                raise AttributeError(f"'{entity.__class__.__name__}' object has no attribute '{attr}'")
            
        db.commit()
        db.refresh(entity)

        return entity

    @classmethod
    def delete(cls, id: int, db: Session):
        entity = db.get(cls.model, id)

        db.delete(entity)
        db.commit()

