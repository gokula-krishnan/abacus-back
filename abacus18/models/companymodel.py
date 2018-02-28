from . import Base
from sqlalchemy.orm import relationship

class Company(Base):
    __tablename__ = 'company'
    __table_args__ = { 'autoload' : True}
