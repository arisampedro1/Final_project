# Generated by Django 4.2 on 2024-08-10 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "myapp1",
            "0010_alter_actividad_aprendiz_alter_actividad_experiencia_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="actividad",
            name="aprendiz",
            field=models.ForeignKey(
                blank=True,
                null=True,
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
