from pydantic import BaseModel
from sqlalchemy.orm import Session

class Context(BaseModel):
    session: Session


def create_coontext(event, context):
    return Context(session=None)