from rest_framework import serializers
from serializer_permissions.mixins import SerializerFieldPermissionMixin


class BooleanField(SerializerFieldPermissionMixin, serializers.BooleanField):
    pass


class CharField(SerializerFieldPermissionMixin, serializers.CharField):
    pass


class ChoiceField(SerializerFieldPermissionMixin, serializers.ChoiceField):
    pass


class DateField(SerializerFieldPermissionMixin, serializers.DateField):
    pass


class DateTimeField(SerializerFieldPermissionMixin, serializers.DateTimeField):
    pass


class DecimalField(SerializerFieldPermissionMixin, serializers.DecimalField):
    pass


class DictField(SerializerFieldPermissionMixin, serializers.DictField):
    pass


class DurationField(SerializerFieldPermissionMixin, serializers.DurationField):
    pass


class EmailField(SerializerFieldPermissionMixin, serializers.EmailField):
    pass


class Field(SerializerFieldPermissionMixin, serializers.Field):
    pass


class FileField(SerializerFieldPermissionMixin, serializers.FileField):
    pass


class FilePathField(SerializerFieldPermissionMixin, serializers.FilePathField):
    pass


class FloatField(SerializerFieldPermissionMixin, serializers.FloatField):
    pass


class HiddenField(SerializerFieldPermissionMixin, serializers.HiddenField):
    pass


class HStoreField(SerializerFieldPermissionMixin, serializers.HStoreField):
    pass


class IPAddressField(SerializerFieldPermissionMixin, serializers.IPAddressField):
    pass


class ImageField(SerializerFieldPermissionMixin, serializers.ImageField):
    pass


class IntegerField(SerializerFieldPermissionMixin, serializers.IntegerField):
    pass


class JSONField(SerializerFieldPermissionMixin, serializers.JSONField):
    pass


class ListField(SerializerFieldPermissionMixin, serializers.ListField):
    pass


class ModelField(SerializerFieldPermissionMixin, serializers.ModelField):
    pass


class MultipleChoiceField(SerializerFieldPermissionMixin, serializers.MultipleChoiceField):
    pass


class NullBooleanField(SerializerFieldPermissionMixin, serializers.NullBooleanField):
    pass


class ReadOnlyField(SerializerFieldPermissionMixin, serializers.ReadOnlyField):
    pass


class RegexField(SerializerFieldPermissionMixin, serializers.RegexField):
    pass


class SerializerMethodField(SerializerFieldPermissionMixin, serializers.SerializerMethodField):
    pass


class SlugField(SerializerFieldPermissionMixin, serializers.SlugField):
    pass


class TimeField(SerializerFieldPermissionMixin, serializers.TimeField):
    pass


class URLField(SerializerFieldPermissionMixin, serializers.URLField):
    pass


class UUIDField(SerializerFieldPermissionMixin, serializers.UUIDField):
    pass
