from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    isbn = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    author = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    old_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    image = models.URLField(max_length=1024, null=True, blank=True)
    img_paths = models.ImageField(null=True, blank=True)
    format = models.CharField(max_length=254, null=True, blank=True)
    currency = models.CharField(max_length=2, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_clearance = models.BooleanField(default=False)

    def __str__(self):
        return self.name
