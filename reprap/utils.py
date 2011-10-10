from mako.template import Template

def mako_renderer_factory(directory, translator=None):
    def mako_renderer(tname, **kw):
        template = Template(filename='%s%s.mako' % (directory, tname))
        return template.render(_=translator, **kw)
    return mako_renderer

