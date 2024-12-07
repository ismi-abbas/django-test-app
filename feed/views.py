from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **keyword_args):
        context = super().get_context_data(**keyword_args)
        context["posts"] = "helloworld"
        # context["posts"] = Post.objects.all()
        return context


class FeedPageView(TemplateView):
    template_name = "feed.html"
