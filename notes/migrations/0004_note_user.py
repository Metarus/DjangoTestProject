# Generated by Django 2.2.2 on 2019-06-13 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_note_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='user',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
