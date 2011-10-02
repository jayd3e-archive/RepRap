from deform import Form
from pyramid.config import Configurator
from pyramid.exceptions import NotFound
from pyramid.exceptions import Forbidden
from reprap.utils import mako_renderer
from reprap.handlers.exceptions import notFound
from reprap.handlers.exceptions import forbidden
from reprap.models.base import initializeDb

def main(global_config, **settings):
        '''Main config function'''
        Form.set_default_renderer(mako_renderer)
        engine = engine_from_config(settings, 'sqlalchemy.')
        initializeDb(engine)
        config = Configurator(settings=settings,
                              root_factory=SiteModel)
         
        config.add_static_view(name='static', path='reprap:static')

        #Includes
        config.include('pyramid_tm')
                                        
        #Handler Root Routes
        config.add_route('issues_root', '/issues')
        #Handler Action Routes
                                                                                                            
        #Exception Views
        config.add_view(notFound,
                        context=NotFound,
                        permission='__no_permission_required__',
                        renderer='exceptions/not_found.mako')

        config.add_view(forbidden,
                        context=Forbidden,
                        permission='__no_permission_required__')

        config.scan('reprap')
        return config.make_wsgi_app()

if __name__ == '__main__':
    from paste.httpserver import serve
    serve(main(), host="0.0.0.0", port="5432")
