from . import Base
from sqlalchemy.orm import relationship

class Project(Base):
    __tablename__ = 'project'
    __table_args__ = { 'autoload': True}
    contributors = relationship('ProjectContributors',cascade = 'all, delete', backref='Project')

class ProjectContributors(Base):
    __tablename__ = 'project_contributor'
    __table_args__ = {'autoload': True}


