from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid


class TaggedItem(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    tag = models.CharField(max_length=50)


class AllFieldTypesModel(models.Model):
    # =========================
    # STRING / TEXT
    # =========================
    char_field = models.CharField(
        max_length=255,
        verbose_name='CharField'
    )

    text_field = models.TextField(
        verbose_name='TextField'
    )

    slug_field = models.SlugField(
        max_length=255,
        unique=True
    )

    email_field = models.EmailField(
        unique=True
    )

    url_field = models.URLField()

    generic_ip = models.GenericIPAddressField()

    regex_field = models.CharField(
        max_length=20,
        help_text='Regex example'
    )

    # =========================
    # NUMBERS
    # =========================
    integer_field = models.IntegerField()
    positive_integer = models.PositiveIntegerField()
    positive_small_integer = models.PositiveSmallIntegerField()
    small_integer = models.SmallIntegerField()
    big_integer = models.BigIntegerField()
    float_field = models.FloatField()
    decimal_field = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    # =========================
    # BOOLEAN
    # =========================
    boolean_field = models.BooleanField(default=False)
    # =========================
    # DATE / TIME
    # =========================
    date_field = models.DateField()
    time_field = models.TimeField()
    datetime_field = models.DateTimeField()
    auto_now_field = models.DateTimeField(auto_now=True)
    auto_now_add_field = models.DateTimeField(auto_now_add=True)
    duration_field = models.DurationField()
    # =========================
    # FILES
    # =========================
    file_field = models.FileField(upload_to='files/')
    image_field = models.ImageField(upload_to='images/')
    # =========================
    # UUID / JSON / BINARY
    # =========================
    uuid_field = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    json_field = models.JSONField(default=dict)
    binary_field = models.BinaryField(null=True, blank=True)
    # =========================
    # RELATIONSHIPS
    # =========================
    foreign_key = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='all_fields_fk'
    )
    one_to_one = models.OneToOneField(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='all_fields_o2o'
    )
    many_to_many = models.ManyToManyField(
        'auth.Group',
        related_name='all_fields_m2m'
    )

    # Self relation
    self_relation = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='children'
    )

    # Symmetrical ManyToMany
    friends = models.ManyToManyField(
        'self',
        symmetrical=True,
        blank=True
    )

    # =========================
    # SPECIAL
    # =========================
    choices_field = models.CharField(
        max_length=20,
        choices=[
            ('draft', 'Draft'),
            ('published', 'Published'),
            ('archived', 'Archived'),
        ]
    )

    nullable_field = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    indexed_field = models.CharField(
        max_length=255,
        db_index=True
    )

    unique_field = models.CharField(
        max_length=255,
        unique=True
    )

    # Generic relation
    generic_relation = GenericRelation(TaggedItem)

    validated_integer = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100)
        ]
    )

    # =========================
    # META
    # =========================
    class Meta:
        ordering = ['id']
        verbose_name = 'All Field Types Model'
        verbose_name_plural = 'All Field Types Models'

    def __str__(self):
        return self.char_field