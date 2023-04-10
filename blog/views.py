from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment

from blog.forms import CommentForm, CreateForm
# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


def frontpage(request):
    posts = Post.objects.all()
    if request.method == "POST":
        Post.objects.all().delete()
        return redirect("frontpage")

    return render(request, 'blog/frontpage.html', {'posts': posts})

# 投稿ページ


def post_create(request):
    post = Post.objects.all()
    if request.method == "POST":
        create = CreateForm(request.POST)
        if create.is_valid():

            commit = create.save(commit=False)
            commit.post = post
            commit.save()

            return redirect("frontpage")

    else:
        form = CreateForm()

    return render(request, 'blog/post_create.html', {"form": form})

# 詳細ページ


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()

    # 詳細ページのコメント削除
    if request.method == "POST":
        if "comment_delete" in request.POST:
            # print(request.POST['comment_delete'])
            Comment.objects.filter(
                id=request.POST['comment_delete']).delete()

            return render(request, 'blog/post_detail.html', {'post': post, "form": form})

        else:
            form = CommentForm(request.POST)

            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()

                return redirect("post_detail", pk=post.pk)

    return render(request, 'blog/post_detail.html', {'post': post, "form": form})

# 投稿 変更/削除ページ


def post_Change_Delete(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == "POST":
        id = get_object_or_404(Post, id=post.id)
        if "Delete" in request.POST:
            id.delete()
            return redirect("frontpage")

        elif "Change" in request.POST:
            form = CreateForm(request.POST, instance=id)
            if form.is_valid():
                form.save()

                return redirect("frontpage")
    else:
        form = CreateForm()

    return render(request, 'blog/post_Change_Delete.html', {'post': post, 'form': form, })
