from pyramid.config import Configurator
from pyramid.authorization import ACLAuthorizationPolicy


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jwt')
    config.set_jwt_authentication_policy('secret')
    
    
    config.include('abacus18.cors.cors')
    config.add_cors_preflight_handler()
    
    config.set_authorization_policy(ACLAuthorizationPolicy())
    
    config.include('.models')
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()
