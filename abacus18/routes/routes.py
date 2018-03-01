def includeme(config):
    config.include('.userroutes', route_prefix='/user')
    config.include('.projectroutes', route_prefix='/project')
    config.include('.companyroutes', route_prefix='/company')