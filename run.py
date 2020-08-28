from render_engine import Site, Page, Collection, Blog
import logging


site = Site()
site.strict = True
site.SITE_TITLE = "Render_Engine"
site.SITE_URL = "https://render-engine.site"

@site.register_route
class Index(Page):
    template = "index.html" # page.html is the default template but you can make a custom template
    slug = "index"


@site.register_collection
class blog(Blog):
    content_path = 'content'
    routes = ['blog']
    markdown_extras = ['footnotes']
    subcollections = ['category']
    template = 'blog.html'

site.render() # build out the tools
