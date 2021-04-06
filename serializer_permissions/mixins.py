class PermissionMixin():

    def __init__(self, *args, **kwargs):
        self.permissions = kwargs.pop("permissions", ())
        self.permission_classes = kwargs.pop("permission_classes", ())
        self.hide_field = kwargs.pop("hide", False)
        super().__init__(*args, **kwargs)

    def check_permission(self):
        request = self.context.get('request', None)
        view = self.context.get('view', None)
        if request and not all((request.user.has_perm(permission) for permission in self.permissions)):
            return False
        if request and view and not all(permission_class().has_permission(request, view) for permission_class in self.permission_classes):
            return False
        return True


class SerializerFieldPermissionMixin(PermissionMixin):

    def get_attribute(self, instance):
        if self.check_permission():
            return super().get_attribute(instance)
        return None
