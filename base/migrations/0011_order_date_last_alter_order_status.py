# Generated by Django 4.0.4 on 2022-05-02 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_product_price_product_no_of_days_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_last',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Done', 'Done')], max_length=200, null=True),
        ),
    ]
