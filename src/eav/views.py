from django.db.models import F, FilteredRelation, Q, Subquery, OuterRef, Max
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets

from eav.models import Entity, Value, Attribute
from eav.serializers import BoardSerializer


class BoardViewSets(viewsets.GenericViewSet):
    queryset = Entity.objects.all()

    def list(self, request: Request) -> Response:
        boards = (
            Entity.objects.filter(name="board")
            .annotate(
                v_title=FilteredRelation(
                    "values",
                    condition=Q(
                        values__attribute=Attribute.objects.get(name="title")
                    ),
                ),
                v_content=FilteredRelation(
                    "values",
                    condition=Q(
                        values__attribute=Attribute.objects.get(name="content")
                    ),
                ),
            )
            .annotate(
                title=F("v_title__text_field"),
                content=F("v_content__text_field"),
            )
            .values("id", "title", "content")
        )
        serializer = BoardSerializer(boards, many=True)
        print(boards.query)
        return Response(serializer.data)
