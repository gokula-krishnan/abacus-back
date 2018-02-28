from pyramid.response import Response
import json
import datetime

class Helper:
    
    @staticmethod
    def sql_list_to_dict(result_set):
        '''
                A helper function that converts the query result set into a list of dictionaries
                
                Iterate through each row in the outer loop and use a dictionary comprehension 
                to map coloumn names to vlaues 
                 
         '''
        response_body = []
        for item in result_set:
            dic = {} 
            if hasattr(item,'__dict__'):
                dic = item.__dict__
                del dic['_sa_instance_state']
            else :
                dic = dict(item)
            response_body.append(dic)
        return response_body       
    
    @staticmethod
    def construct_response(code=500, message='Unexpected Server Error',
                             response_body=None):
        
        '''
                A function that returns a Pyramid Response Object
                Note : Use json_body instead of body in response objects
                    
        '''
        
        
        data = {
            'code' : code,
            'message' : message,
            'data' : response_body
            }
        data_bytes = json.dumps(data)
        return Response(json_body=data, status=code, content_type='application/json')
    
    @staticmethod
    def created_and_updated_at_by(object, jwt_claim=None):
        now = datetime.datetime.now()
        updated_by = 1
        created_by = 1
        if jwt_claim:
            updated_by = jwt_claim['user_id']
            created_by = jwt_claim['user_id']
        created_at = now.strftime("%Y-%m-%d %H:%M")
        object['created_at'] = created_at
        object['updated_by'] = updated_by
        object['created_by'] = created_by     
        return object