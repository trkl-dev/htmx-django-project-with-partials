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
        links = LINK_DATA.copy()

        sort = request.GET.get("sort", "").lower() == "true"
        if sort:
            # This is a terrible cancerous mess and I feel nothing but shame. 
            sorted_titles = sorted([link["title"] for link in LINK_DATA ])
            new_links = [[link for link in LINK_DATA if link["title"] == title][0] for title in sorted_titles]
            links = new_links
            template_name = f"{template_name}#link_list"

        context = {
            "links": links
        }
        return TemplateResponse(request, template_name, context)

