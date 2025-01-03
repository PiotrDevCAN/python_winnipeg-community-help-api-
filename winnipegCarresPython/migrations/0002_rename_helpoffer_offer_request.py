# Generated by Django 5.1.4 on 2025-01-02 17:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winnipegCarresPython', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HelpOffer',
            new_name='Offer',
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('help_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='winnipegCarresPython.helpcategory')),
                ('help_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='winnipegCarresPython.helptype')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='winnipegCarresPython.volunteer')),
            ],
        ),
    ]
