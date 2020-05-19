# Generated by Django 2.1.5 on 2020-05-14 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aboutMe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='aboutMe.Profile'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='aboutMe.Profile'),
        ),
        migrations.AlterField(
            model_name='social',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social', to='aboutMe.Profile'),
        ),
    ]
