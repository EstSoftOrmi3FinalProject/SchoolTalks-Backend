# Django Filter
from django_filters import rest_framework as filters, CharFilter

# Custom Models
from .models import Post


class PartialMatchCharFilter(CharFilter):
    def filter(self, queryset, value):
        if value:
            lookup = f"{self.field_name}__icontains"
            return queryset.filter(**{lookup: value})
        return queryset


class PostFilter(filters.FilterSet):
    title = PartialMatchCharFilter(field_name="title")
    author = PartialMatchCharFilter(field_name="author__username")
    content = PartialMatchCharFilter(field_name="content")

    class Meta:
        model = Post
        fields = ["title", "author", "content", "is_notice"]
