# Generated by Django 4.0.4 on 2022-04-30 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_customer_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('priority', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('tags', models.ManyToManyField(to='base.tag')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Project Pending', 'Project Pending'), ('Project Started', 'Project Started'), ('Project Done', 'Project Done')], max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='order',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.project'),
        ),
    ]
