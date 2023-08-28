from pydantic import BaseModel

class DynamicClass(BaseModel):
    class_name: str
    attributes: []
