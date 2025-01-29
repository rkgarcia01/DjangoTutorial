# articles/views.py
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy, reverse
from .forms import CommentForm
from django.views import View
from .models import Article

# Create your views here.


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "article_list.html"


# Handles GET requests to display the article details and a comment form
class CommentGet(DetailView):
    model = Article
    template_name = "article_detail.html"

    # Adds a comment form to the context for rendering in the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


# Handles POST requests to process and submit the comment form
class CommentPost(SingleObjectMixin, FormView):
    model = Article
    form_class = CommentForm
    template_name = "article_detail.html"

    # 'get_object()' from 'SingleObjectMixin' is used  to grab the article pk from the URL
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    # 'form_valid()' is called rom validation has succeded. Before we save our comment
    # to the database we have to specify the article it belongs. Initially we save the
    # form but we set 'commit' to 'False' becasue in the next line we associate
    # the correct article with the form object. Then we return it as part of 'form_valid()'
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.save()
        return super().form_valid(form)

    # 'get_success_url()' which is called after the form data is saved. We just redirect
    # the user to the current page in this case.
    def get_success_url(self):
        article = self.get_object()
        return reverse("article_detail", kwargs={"pk": article.pk})


# Wrapper view that delegates GET requests to CommentGet and POST requests to CommentPost
class ArticleDetailView(LoginRequiredMixin, View):
    # Routes GET requests to CommentGet view
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    # Routes POST requests to CommentPOST view
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


# This class onlyrequires that we also add the specific fields-title and body-
# that can be changed
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = "article_edit.html"

    # Get the obj (or the instance of the current article) and set it eqaul to 'obj'
    # 'if' author of that article or 'obj.author' is equal to
    # the user that has requested to delete then 'return'
    # and then the user can delete since its the author itself
    # 'else' do not delete or '403 FORBIDDEN'
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


# This class requires a redirect where to send the user after deleting the entry
# , requiring "reverse_lazy" and "success_url" along with the a
# corresponding named URL
class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

    # Get the obj (or the instance of the current article) and set it eqaul to 'obj'
    # 'if' author of that article or 'obj.author' is equal to
    # the user that has requested to delete then 'return'
    # and then the user can delete since its the author itself
    # 'else' do not delete or '403 FORBIDDEN'
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


# This class has 'author' in 'fields' since we want to associate a new article
# with an author
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article_new.html"
    fields = ("title", "body")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


"""
# This class only requires listing the model and template name
class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article_detail.html"

    # This method is responsible for adding extra context data to the template.
    # IT's being overriden to include custon context
    def get_context_data(self, **kwargs):
        # calls the parent class's get_context_data method (from 'DetailView')
        # to get the default conext data (e.g., the 'Article' object being displayed
        # is already included as 'object' or 'article'
        context = super().get_context_data(**kwargs)
        # Adds a new key to the context dictornary: "form"
        # The value of "form" is an instance of 'Commentform()'. This
        # could be a Django form class used for users to submit
        # commnts on the article
        context["form"] = Commentform()
        # Returns the updated context dictionary to be used in the template
        return context
"""
