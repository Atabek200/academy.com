import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('contact_phone', models.CharField(max_length=13)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_phone', models.CharField(max_length=15)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='master_photos/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='master', to=settings.AUTH_USER_MODEL)),
                ('specialization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='academy.specialization')),
            ],
        ),
    ]
