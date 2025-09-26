from django.core.validators import EmailValidator, RegexValidator  # type: ignore
from django.db import models  # type: ignore
from django.utils.html import escape  # type: ignore


class Customer(models.Model):
    """Customer model based on the sample CSV data structure."""

    first_name = models.CharField(max_length=50, help_text="Customer's first name")

    last_name = models.CharField(max_length=50, help_text="Customer's last name")

    email = models.EmailField(
        unique=True, validators=[EmailValidator()], help_text="Customer's email address"
    )

    phone = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r"^\d{3}-\d{4}$|^\d{10}$|^\+?1?\d{9,15}$",
                message="Phone number must be in format: 'XXX-XXXX' or '1234567890'",
            )
        ],
        help_text="Customer's phone number",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "customers"
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering = ["last_name", "first_name"]
        indexes = [
            models.Index(fields=["email"]),
            models.Index(fields=["last_name", "first_name"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        return escape(f"{self.first_name} {self.last_name} ({self.email})")

    @property
    def full_name(self):
        """Returns the customer's full name."""
        return escape(f"{self.first_name} {self.last_name}")

    def clean(self):
        """Custom validation for the model with security checks."""
        import re
        from django.core.exceptions import ValidationError
        
        # Security patterns to detect potential XSS/injection attempts
        dangerous_patterns = re.compile(
            r'<script|<iframe|<object|<embed|javascript:|data:|on\w+='
            r'|<\s*\/?\s*(script|iframe|object|embed|svg|img)',
            re.IGNORECASE
        )
        
        # Validate and clean first name
        if self.first_name:
            self.first_name = self.first_name.strip()
            if dangerous_patterns.search(self.first_name):
                raise ValidationError({'first_name': 'First name contains invalid characters.'})
            if len(self.first_name) > 50:
                raise ValidationError({'first_name': 'First name is too long.'})
            if not re.match(r'^[a-zA-Z\s\-\'\.]+$', self.first_name):
                raise ValidationError({'first_name': 'First name contains invalid characters.'})
            self.first_name = self.first_name.title()
            
        # Validate and clean last name
        if self.last_name:
            self.last_name = self.last_name.strip()
            if dangerous_patterns.search(self.last_name):
                raise ValidationError({'last_name': 'Last name contains invalid characters.'})
            if len(self.last_name) > 50:
                raise ValidationError({'last_name': 'Last name is too long.'})
            if not re.match(r'^[a-zA-Z\s\-\'\.]+$', self.last_name):
                raise ValidationError({'last_name': 'Last name contains invalid characters.'})
            self.last_name = self.last_name.title()

        # Validate and clean email
        if self.email:
            self.email = self.email.lower().strip()
            if dangerous_patterns.search(self.email):
                raise ValidationError({'email': 'Email contains invalid characters.'})
            if len(self.email) > 254:  # RFC5321 limit
                raise ValidationError({'email': 'Email is too long.'})
                
        # Validate phone
        if self.phone:
            self.phone = self.phone.strip()
            if dangerous_patterns.search(self.phone):
                raise ValidationError({'phone': 'Phone number contains invalid characters.'})
            if len(self.phone) > 15:
                raise ValidationError({'phone': 'Phone number is too long.'})

    def save(self, *args, **kwargs):
        """Override save to call clean method."""
        self.clean()
        super().save(*args, **kwargs)
