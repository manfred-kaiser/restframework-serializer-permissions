restframework-serializer-permissions
====================================

Drop in replacement for [Django Restframework Serializers](https://www.django-rest-framework.org/api-guide/serializers/) to add permission based field serialization.

Installation
------------

Install this module into your environment:

    $ pip install restframework-serializer-permissions


Example
-------

This example uses a ModelSerializer as described in [DRF Docs](https://www.django-rest-framework.org/api-guide/serializers/#modelserializer)

```python
# import permissions from rest_framework
from rest_framework.permissions import AllowAny, IsAuthenticated

# import serializers from serializer_permissions instead of rest_framework
from serializer_permissions  import serializers

# import you models
from myproject.models import ShoppingItem, ShoppingList


class ShoppingItemSerializer(serializers.ModelSerializer):

    item_name = serializers.CharField(read_only=True)

    class Meta:
        # metaclass as described in drf docs
        model = ShoppingItem
        fields = ('item_name', )


class ShoppingListSerializer(serializers.ModelSerializer):

    # Allow all users to list name
    list_name = serializers.CharField(permission_classes=(AllowAny, ))

    # Only allow authenticated users to retrieve the comment
    list_comment = serializers.CharField(permissions=(IsAuthenticated, ))

    # show owner only, when the current user has 'auth.view_user' permission
    owner = serializers.CharField(permissions=('auth.view_user', ), hide=True)

    # serializer which is only available, when the user is authenticated
    items = ShoppingItemSerializer(many=True, permissions=(IsAuthenticated, ), hide=True)

    class Meta:
        # metaclass as described in drf docs
        model = ShoppingItem
        fields = ('list_name', 'list_comment', 'owner', 'items', )
```

You can also define your own permissions classes as described in the  [DRF documentation](https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions) and specify multiple r`permission_classes` and r`permissions` on a field or serializer: all provided permissions must be satisfied for the visitor to retrieve the given field.


Compatibility
-------------

This package should be compatible with:

* Django Rest Framework 3
* Django 2.x, 3.x
* Python 3.6, 3.7, 3.8
