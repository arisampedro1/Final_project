# Generated by Django 4.2 on 2024-08-10 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("myapp1", "0015_alter_niveldeaprendizaje_fecha_creacion"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actividad",
            name="aprendiz",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="actividades",
                to="myapp1.aprendiz",
            ),
        ),
        migrations.AlterField(
            model_name="actividad",
            name="experiencia",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="actividades",
                to="myapp1.experiencia",
            ),
        ),
        migrations.AlterField(
            model_name="actividad",
            name="nivel",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="actividades",
                to="myapp1.niveldeaprendizaje",
            ),
        ),
    ]
