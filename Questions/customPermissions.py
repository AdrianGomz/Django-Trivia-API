from rest_framework import permissions


class isAuthor(permissions.BasePermission):
    """This is a custom permission class to validate if 
    the user is the creator of a question. Because we 
    want only the author to be able to modify or delete his
    question. """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
