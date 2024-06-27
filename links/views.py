from django.views.generic import View
from django.template.response import TemplateResponse


# Instead of faffing about with Models and DB data
LINK_DATA = [
    {
        "url": "https://drupico.com",
        "title": f"Drupico",
    },
    {
        "url": "https://stackoverflow.com",
        "title": f"Stack Overflow",
    },
    {
        "url": "https://limmnock.dev",
        "title": f"Limmnock",
    },
    {
        "url": "https://dropspot.it",
        "title": f"Dropspot",
    },
]

class LinksView(View):

    def get(self, request, *_args, **_post):
        template_name = "links/link_list.html"
        links = LINK_DATA

        sort = request.GET.get("sort", "").lower() == "true"
        if sort:
            template_name = "links/link_list.html#link_list"
            links = sorted(LINK_DATA, key=lambda l: l['title'])

        context = {
            "links": links
        }

        return TemplateResponse(request, template_name, context)

