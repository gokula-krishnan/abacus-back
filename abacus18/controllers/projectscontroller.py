from pyramid.view import view_config
from ..helpers.helper import Helper
import os
import bcrypt
from pyramid.response import Response, FileResponse
from ..models import Session
from ..models.projectmodel import Project,ProjectContributors,ProjectTransforms
from ..models.usermodel import user
from ..models.candidatemodel import Candidate
from ..models.companymodel import Company

""" adds
project
"""


@view_config(route_name='projects', request_method="POST")
def project_post(request):
    session = Session()

    if request.authenticated_userid:
        userid = request.jwt_claims['user_id']
        result = session.query(user).filter(user.id == userid).first()
        if int(result.role) == 1:
            request_body = request.json_body

            project_details = request_body['project_details']
            pd = Project(**project_details)

            contributor_list = request_body['contributors']
            print(contributor_list)
            for contributor in contributor_list:
                co = ProjectContributors(**contributor)
                pd.contributors.append(co)
                no_modules = len(contributor['modules_worked'].split(","))
                con_score = int(contributor['contribution_score'])
                company_weight = int(session.query(Company).filter(Company.id == request_body['project_details']['company_id']).first().score)
                old_rating = session.query(Candidate).filter(Candidate.id == contributor['contributor_id']).first().rating
                if company_weight < 20:
                    new_rating =  old_rating + company_weight/8
                if company_weight < 60:
                    new_rating =  old_rating + company_weight/4
                else :
                    new_rating =  old_rating + company_weight/2
                if request_body['project_details']['complexity'] == "Easy":
                    new_rating=new_rating*2
                if request_body['project_details']['complexity'] == "Medium":
                    new_rating=new_rating*3
                else:
                    new_rating=new_rating*5
                session.query(Candidate).filter(Candidate.id == contributor['contributor_id']).update({"rating": new_rating})
            session.add(pd)
            session.commit()
            session.close()

            code = 200
            message = 'Success'

            return Helper.construct_response(code,message,'')

        else:
            return Helper.construct_response(401, 'Unauthorized', '')


    else:
        return Helper.construct_response(401,'Unauthorized','')

@view_config(route_name='projects.view', request_method="GET")
def project_view(request):
    session = Session()
    projectTransforms = ProjectTransforms()
    if request.authenticated_userid:
        userid = request.jwt_claims['user_id']
        result = session.query(Company).filter(Company.userid == userid).first().id
        queryobj = session.query(Company,Project).join(Project,Project.company_id == Company.id).filter(Company.id == result)
        return Helper.construct_response(200,"success",projectTransforms.project_list_of_company(queryobj))
    else:
        return Helper.construct_response(401,'Unauthorized','')
