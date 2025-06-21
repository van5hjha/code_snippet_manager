from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Snippet
from .serializers import SnippetSerializer

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter


class SnippetViewSet(viewsets.ModelViewSet):
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "description", "code"]
    filterset_fields = ["language", "tags__name"]
    ordering_fields = ["created_at","title"]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Snippet.objects.none()
        # Only return snippets owned by the logged-in user
        return Snippet.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically set the snippet owner to the current user
        serializer.save(user=self.request.user)

    @action(detail=False, url_path='shared/(?P<uuid>[0-9a-f\-]+)', permission_classes=[permissions.AllowAny])
    def shared_snippet(self, request, uuid=None):
        """
        Public access to a snippet by share_uuid (no auth required).
        """
        snippet = get_object_or_404(Snippet, share_uuid=uuid)
        serializer = self.get_serializer(snippet)
        return Response(serializer.data)

    @action(detail=True, methods=["get"], url_path="highlight")
    def highlight_snippet(self, request, pk=None):
        """
        Returns the syntax-highlighted HTML version of the snippet.
        """
        snippet = self.get_object()

        try:
            lexer = get_lexer_by_name(snippet.language)
            formatter = HtmlFormatter(style="friendly", full=True)
            highlighted_code = highlight(snippet.code, lexer, formatter)
        except Exception as e:
            highlighted_code = snippet.code

        return Response({"highlighted_html": highlighted_code})
