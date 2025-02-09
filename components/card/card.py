from django_components import Component, register


@register("card")
class Calendar(Component):
    template_file = "card/card.html"

    # css_file = "calendar/calendar.css"
    # js_file = "calendar/calendar.js"


    # def get_context_data(self, value):
    #     return {
    #         "value": value,
    #     }

    # def get(self, request, *args, **kwargs):
    #     return self.render_to_response(
    #         kwargs={
    #             "date": request.GET.get("date", ""),
    #         },
    #     )
