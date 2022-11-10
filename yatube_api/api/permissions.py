from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    '''Разрешение, что только автор может изменять и удалять контент'''
    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author


class IsNotExistFollow(permissions.BasePermission):
    '''Разрешение, что нельзя создавать существующую подписку'''
    message = 'Такая подписка уже существует!'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author
