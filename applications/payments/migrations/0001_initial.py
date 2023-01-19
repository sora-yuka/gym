# Generated by Django 4.1.5 on 2023-01-19 10:07

import applications.payments.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sports_activities', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('card_type', models.CharField(max_length=180, verbose_name=(('visa', 'Visa'), ('elcart', 'Elcart'), ('mastercard', 'MasterCard'), ('unionpay', 'UnionPay'), ('american_express', 'American Express')))),
                ('card_number', models.CharField(max_length=19, validators=[applications.payments.validators.CCNumberValidator()])),
                ('card_expiry_date', models.DateField(verbose_name="['%m/%y', '%m/%Y']")),
                ('card_balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='month_subscriptions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_key', models.UUIDField(blank=True, default=uuid.uuid4, null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('expiration_date', models.DateTimeField()),
                ('discount', models.PositiveIntegerField(default=5, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(50)])),
                ('final_price', models.PositiveIntegerField()),
                ('is_paid', models.BooleanField(default=False)),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='sports_activities.sportsactivity')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='payments.customer')),
            ],
        ),
    ]
