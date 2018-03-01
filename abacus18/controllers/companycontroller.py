from pyramid.view import view_config
from ..helpers.helper import Helper
from ..models import Session
from ..models.companymodel import Company
from ..models.usermodel import user
from ..models.hiringdetailmodel import Hiring_Detail

@view_config(route_name='add_vacancy', request_method="POST")
def add_vacancy(request):
    session = Session()

    if request.authenticated_userid:
        request_body = request.json_body
        userid = request.jwt_claims['user_id']
        result = session.query(Company).filter(Company.userid == userid).first()
        cid = result.id
        request_body['company_id'] = cid
#        request_body = request.json_body
        vacancy_details = request_body
        hd = Hiring_Detail(**vacancy_details)
        session.add(hd)
        session.commit()
        session.close()
        return Helper.construct_response(200,"OK",'')
    else:
        return Helper.construct_response(401, 'Unauthorized', '')
