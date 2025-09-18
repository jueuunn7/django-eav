from django.db import models


class Entity(models.Model):
    name = models.CharField(max_length=255)


class Attribute(models.Model):
    class AttributeTypes(models.TextChoices):
        TEXT = "text"
        INTEGER = "integer"
        FLOAT = "float"
        BOOLEAN = "boolean"
        DATE = "date"

    name = models.CharField(max_length=255)
    attribute_type = models.CharField(choices=AttributeTypes.choices, max_length=255)


class Value(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name="values")
    attribute = models.ForeignKey(
        Attribute, on_delete=models.CASCADE, related_name="values"
    )

    text_field = models.TextField(null=True, blank=True)
    integer_field = models.IntegerField(null=True, blank=True)
    float_field = models.FloatField(null=True, blank=True)
    boolean_field = models.BooleanField(null=True, blank=True)
    date_field = models.DateField(null=True, blank=True)

    @property
    def value(self):
        match self.attribute.attribute_type:
            case Attribute.AttributeTypes.TEXT:
                return str(self.text_field)

            case Attribute.AttributeTypes.INTEGER:
                return int(self.integer_field)

            case Attribute.AttributeTypes.FLOAT:
                return float(self.float_field)

            case Attribute.AttributeTypes.BOOLEAN:
                return bool(self.boolean_field)

            case Attribute.AttributeTypes.DATE:
                return str(self.date_field)

        return None
