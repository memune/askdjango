from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.views import View
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView
from django.http import HttpResponse, HttpRequest, Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import PostForm
from django.contrib import messages

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
    return render(request, 'instagram/post_confirm_delete.html', {
        'post':post,
    })

@login_required
def post_edit(request, pk):

    post = get_object_or_404(Post, pk=pk)

    # 작성자 체크하는 방법 tip 
    if post.author != request.user:
        messages.error(request, '작성자만 수정할 수 있습니다.')
        return redirect(post)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, '포스팅을 수정했습니다.')
            return redirect(post)
    else:
        form = PostForm(instance=post)

    return render(request, 'instagram/post_forms.html', {
        'form': form,
        'post': post,
    })
    
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.info(request, '포스팅을 저장했습니다.')
            return redirect(post)
    else:
        form = PostForm()

    return render(request, 'instagram/post_forms.html', {
        'form': form,
        'post': None,
    })


@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    model = Post
    paginate_by = 50



post_list = PostListView.as_view()


# CBV 기반
# post_list = ListView.as_view(model=Post, paginate_by=10) 


# FBV 기반
# @login_required
# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')

#     if q:
#         qs = qs.filter(message__icontains=q)
# #
# #     # instagram/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q': q,
#     })



# FBV 기반 post_detail
# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'instagram/post_detail.html', {
#         'post': post,
#     })

# CBV 기반 post_detail
# post_detail = DetailView.as_view(
#     model=Post, 
#     queryset=Post.objects.filter(is_public=True))

#CBV 기반 post_detail 커스텀
class PostDetailView(DetailView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public = True)
        return qs

post_detail = PostDetailView.as_view()

# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'instagram/post_detail.html', {
#         'post': post,
#         'object': post,
#     })

# class PostListView(ListView):
#     model = Post

# post_list = PostListView.as_view()


post_archive = ArchiveIndexView.as_view(
    model = Post,
    date_field = 'created_at',
    paginate_by = 10)

post_archive_year = YearArchiveView.as_view(
    model = Post,
    date_field = 'created_at',
    make_object_list=True,
)

