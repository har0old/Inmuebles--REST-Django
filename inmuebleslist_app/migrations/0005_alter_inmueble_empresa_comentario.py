# Generated by Django 4.2.1 on 2023-05-10 23:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebleslist_app', '0004_inmueble_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='InmuebleList', to='inmuebleslist_app.empresa'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('texto', models.CharField(max_length=200, null=True)),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('efificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='inmuebleslist_app.inmueble')),
            ],
        ),
    ]
