from django.core.exceptions import ValidationError


def validate_size(object):
    size = object.size
    if size > 2 * 1024 * 1024:
        raise ValidationError("Maximum file size that can be uploaded is 2MB")
    else:
        return object