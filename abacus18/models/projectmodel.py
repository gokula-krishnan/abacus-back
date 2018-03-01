from . import Base
from sqlalchemy.orm import relationship

class Project(Base):
    __tablename__ = 'project'
    __table_args__ = { 'autoload': True}
    contributors = relationship('ProjectContributors',cascade = 'all, delete', backref='Project')

class ProjectContributors(Base):
    __tablename__ = 'project_contributor'
    __table_args__ = {'autoload': True}

class ProjectTransforms:
    def project_list_of_company(self,result_set):
        response_body=[]
        for result in result_set:
            projectData={
                'projectname':result.Project.name,
                'complexity':result.Project.complexity,
                'Description':result.Project.description
            }
            response_body.append(projectData)
        return response_body
