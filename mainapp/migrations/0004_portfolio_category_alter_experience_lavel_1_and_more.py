# Generated by Django 4.1 on 2022-09-06 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_experience_alter_service_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio_Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='experience',
            name='lavel_1',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='lavel_2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='lavel_3',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='lavel_4',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='lavel_5',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=300)),
                ('image', models.ImageField(blank=True, upload_to='portfolio_img')),
                ('details', models.TextField(blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('pro_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.portfolio_category')),
            ],
        ),
    ]
