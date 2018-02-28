from . import Base
from sqlalchemy.orm import relationship

class user(Base):
    __tablename__ = 'user'
    __table_args__ = { 'autoload' : True}
