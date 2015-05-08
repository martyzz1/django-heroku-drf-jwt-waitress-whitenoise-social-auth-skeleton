# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(default='C', max_length=1, choices=[(b'C', 'Client'), (b'V', 'Vet'), (b'F', 'Nutritionalist'), (b'G', 'Groomer'), (b'N', 'Nurse')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='first name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='last name'),
            preserve_default=True,
        ),
    ]
