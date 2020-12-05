from rest_framework import permissions



class GerantPermission(permissions.BasePermission):
    message = 'not allowed.'

    def has_permission(self, request, view):
        return request.user.has_perm("mainapp.gerant_default_new")


class AgentPermission(permissions.BasePermission):
    message = 'not allowed'

    def has_permission(self, request, view):
        return request.user.has_perm("mainapp.agent_default_new")
    pass
