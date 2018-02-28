from . import Base
from sqlalchemy.orm import relationship

class Candidate(Base):
    __tablename__ = 'candidate'
    __table_args__ = { 'autoload' : True}
