from rest_framework import relations
from serializer_permissions.mixins import SerializerFieldPermissionMixin

MANY_RELATION_KWARGS = relations.MANY_RELATION_KWARGS + ('hide', 'permissions', 'permission_classes')


class RelatedField(SerializerFieldPermissionMixin, relations.HyperlinkedIdentityField):

    @classmethod
    def many_init(cls, *args, **kwargs):
        """
        This method handles creating a parent `ManyRelatedField` instance
        when the `many=True` keyword argument is passed.
        Typically you won't need to override this method.
        Note that we're over-cautious in passing most arguments to both parent
        and child classes in order to try to cover the general case. If you're
        overriding this method you'll probably want something much simpler, eg:
        @classmethod
        def many_init(cls, *args, **kwargs):
            kwargs['child'] = cls()
            return CustomManyRelatedField(*args, **kwargs)
        """
        list_kwargs = {'child_relation': cls(*args, **kwargs)}
        for key in kwargs:
            if key in MANY_RELATION_KWARGS:
                list_kwargs[key] = kwargs[key]
        return ManyRelatedField(**list_kwargs)


class HyperlinkedIdentityField(SerializerFieldPermissionMixin, relations.HyperlinkedIdentityField):
    pass


class HyperlinkedRelatedField(SerializerFieldPermissionMixin, relations.HyperlinkedRelatedField):
    pass


class ManyRelatedField(SerializerFieldPermissionMixin, relations.ManyRelatedField):
    pass


class PrimaryKeyRelatedField(SerializerFieldPermissionMixin, relations.PrimaryKeyRelatedField):
    pass


class SlugRelatedField(SerializerFieldPermissionMixin, relations.SlugRelatedField):
    pass


class StringRelatedField(SerializerFieldPermissionMixin, relations.StringRelatedField):
    pass
