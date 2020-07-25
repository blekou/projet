# Generated by Django 2.2.10 on 2020-05-27 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0007_client_myprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='prix',
            field=models.ManyToManyField(related_name='produit', to='compte.Produit'),
        ),
        migrations.AlterField(
            model_name='client',
            name='myprofile',
            field=models.ImageField(blank=True, default='profil.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='client',
            name='user',
            field=models.OneToOneField(blank='True', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]