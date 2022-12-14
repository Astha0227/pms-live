# Generated by Django 4.0.4 on 2022-04-30 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_project_remove_order_product_alter_order_status_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Project',
            new_name='Product',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='project',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Project Pending', 'Project Pending'), (' Project Proccesing', 'Project Processing'), ('Project Done', 'Project Done')], max_length=200, null=True),
        ),
    ]
