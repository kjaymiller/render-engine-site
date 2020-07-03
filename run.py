from render_engine import Site, Page, Collection, Blog

site = Site()

@site.register_route
class Index(Page):
    template = "index.html" # page.html is the default template but you can make a custom template
    slug = "index"

site.render() # build out the tools
