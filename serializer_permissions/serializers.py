from rest_framework import serializers

from serializer_permissions.fields import (  # NOQA # isort:skip
    BooleanField, CharField, ChoiceField, DateField, DateTimeField, DecimalField,
    DictField, DurationField, EmailField, Field, FileField, FilePathField, FloatField,
    HiddenField, HStoreField, IPAddressField, ImageField, IntegerField, JSONField,
    ListField, ModelField, MultipleChoiceField, NullBooleanField, ReadOnlyField,
    RegexField, SerializerMethodField, SlugField, TimeField, URLField, UUIDField,
)

from serializer_permissions.relations import (  # NOQA # isort:skip
    HyperlinkedIdentityField, HyperlinkedRelatedField, ManyRelatedField,
    PrimaryKeyRelatedField, RelatedField, SlugRelatedField, StringRelatedField,
)

from serializer_permissions.mixins import PermissionMixin

LIST_SERIALIZER_KWARGS = serializers.LIST_SERIALIZER_KWARGS + ('hide', 'permissions', 'permission_classes')


class SerializerPermissionMixin(PermissionMixin):

    def to_representation(self, instance):
        if self.check_permission():
            return super().to_representation(instance)
        return None

    @property
    def fields(self):
        """
        Supercedes drf's serializers.ModelSerializer's fields property
        :return: a set of permission-scrubbed fields
        """
        ret = super().fields
        request = self.context.get('request', None)
        if request is None:
            return ret

        forbidden_field_names = []
        for field_name, field in ret.items():
            if hasattr(field, 'permissions') and not field.check_permission():
                if hasattr(field, 'hide_field') and field.hide_field:
                    forbidden_field_names.append(field_name)
        for field_name in forbidden_field_names:
            ret.pop(field_name)

        return ret

    @classmethod
    def many_init(cls, *args, **kwargs):
        """
        This method implements the creation of a `ListSerializer` parent
        class when `many=True` is used. You can customize it if you need to
        control which keyword arguments are passed to the parent, and
        which are passed to the child.
        Note that we're over-cautious in passing most arguments to both parent
        and child classes in order to try to cover the general case. If you're
        overriding this method you'll probably want something much simpler, eg:
        @classmethod
        def many_init(cls, *args, **kwargs):
            kwargs['child'] = cls()
            return CustomListSerializer(*args, **kwargs)
        """
        allow_empty = kwargs.pop('allow_empty', None)
        child_serializer = cls(*args, **kwargs)
        list_kwargs = {
            'child': child_serializer,
        }
        if allow_empty is not None:
            list_kwargs['allow_empty'] = allow_empty
        list_kwargs.update({
            key: value for key, value in kwargs.items()
            if key in LIST_SERIALIZER_KWARGS
        })
        meta = getattr(cls, 'Meta', None)
        list_serializer_class = getattr(meta, 'list_serializer_class', ListSerializer)
        return list_serializer_class(*args, **list_kwargs)


class BaseSerializer(SerializerPermissionMixin, serializers.BaseSerializer):
    pass


class Serializer(SerializerPermissionMixin, serializers.Serializer):
    pass


class ListSerializer(SerializerPermissionMixin, serializers.ListSerializer):
    pass


class ModelSerializer(SerializerPermissionMixin, serializers.ModelSerializer):
    pass


class HyperlinkedModelSerializer(SerializerPermissionMixin, serializers.HyperlinkedModelSerializer):
    pass
