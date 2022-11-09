from rest_framework import mixins, viewsets


class ListRetrieveViewSet(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """
    Вьюсет, который обеспечивает действия `retrieve` и `list`.
    """
    pass


class CreateListViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """
    Вьюсет, который обеспечивает действия `create` и `list`.
    """
    pass
