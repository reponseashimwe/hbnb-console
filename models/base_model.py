#!/usr/bin/python3
"""Defines BaseModel class."""
import models
from uuid import uuid
from datetime import datetime


class BaseModel:
    """
        Class Base
        Defines all common attributes/methods for other classes
        Attr :
                id: string - assigned with an uuid when an instance is created
                created_at: datetime - assigned with the current datetime
                when an instance is created

                updated_at: datetime - assigned with the current datetime
                when an instance is created.
                It will be updated every time the object change.
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.id = kwargs.get("id", str(uuid.uuid4()))
            self.created_at = datetime.fromisoformat(kwargs["created_at"]) if "created_at" in kwargs else datetime.now()
            self.updated_at = datetime.fromisoformat(kwargs["updated_at"]) if "updated_at" in kwargs else datetime.now()
            self.name = kwargs.get("name", "")
            if "__class__" in kwargs:
                del kwargs["__class__"]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.name = ""

        if args:
            pass
        models.storage.new(self)

    def save(self):
        """Set updated_at with current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return dictionary of BaseModel instance.

        Includes key/value pair __class__.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return print/str representation of BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
