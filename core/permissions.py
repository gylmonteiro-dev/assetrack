from rest_framework import permissions


class GlobalPermissionClass(permissions.BasePermission):
    method_to_action = {
        "GET": "view",
        "POST": "add",
        "PUT": "change",
        "PATCH": "change",
        "DELETE": "delete",
    }

    def has_permission(self, request, view):
        codename = self.__get_codename(method=request.method, view=view)

        if codename:
            return request.user.has_perm(codename)

        return False

    def __get_codename(self, method, view):

        try:
            model_name = view.queryset.model._meta.model_name

            app_label = view.queryset.model._meta.app_label

            view_action = self.__get_method(method)

            return f"{app_label}.{view_action}_{model_name}"
        except ValueError:
            return None

    def __get_method(self, method):
        action = self.method_to_action.get(method)
        if action:
            return action
        
