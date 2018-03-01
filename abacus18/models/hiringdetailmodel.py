from . import Base
from sqlalchemy.orm import relationship

class Hiring_Detail(Base):
    __tablename__ = 'hiring_details'
    __table_args__ = { 'autoload' : True}
