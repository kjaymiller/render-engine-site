from render_engine import Site, Page, Collection, Blog
import logging

class site(Site):
    strict = True
    SITE_TITLE = "Render_Engine"
    SITE_URL = "https://render-engine.site"

site = site()

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

site.render() # build out the tools
