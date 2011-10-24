from deform import Form
from pyramid.config import Configurator
from pyramid.exceptions import NotFound
from pyramid.exceptions import Forbidden
from reprap.utils import mako_renderer_factory
from reprap.i18n import translator
from reprap.handlers.exceptions import notFound
from reprap.handlers.exceptions import forbidden
from reprap.models.base import initializeBase
from reprap.models.site import SiteModel
from reprap.request import RepRapRequest
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker

def main(global_config, **settings):
        '''Main config function'''
        renderer = mako_renderer_factory('reprap/templates/forms/',
                                         translator=translator)
        Form.set_default_renderer(renderer)
        
        engine = engine_from_config(settings, 'sqlalchemy.')
        initializeBase(engine)
        # NOTE: A transaction is created by default in postgres, so I have added the
        # 'autocommit' kwarg so that I don't have to deal with transactions for
        # the moment.  Remove it once I have pyramid_tm & zope.sqlalchemy implemented.
        maker = sessionmaker(bind=engine, autocommit=True)
        settings['db.sessionmaker'] = maker
        
        config = Configurator(settings=settings,
                              root_factory=SiteModel,
                              request_factory=RepRapRequest)
         
        config.add_static_view(name='static', path='reprap:static')
                                        
        #Handler Root Routes
        config.add_route('issues_root', '/issues')
        config.add_route('toggle_vote', '/toggle_vote/{user_id}/{comment_id}/{vote}')
        #Handler Action Routes
        config.add_route('issues_add', '/issues/add')
        config.add_route('issues_view', '/issues/view/{id}')
                                                                                                            
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
