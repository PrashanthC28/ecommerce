# Generated by Django 4.0.6 on 2022-08-30 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210529_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='state',
        ),
        migrations.AddField(
            model_name='address',
            name='Zipcode',
            field=models.CharField(default=1, max_length=150, verbose_name='Zipcode'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Pending', max_length=50),
        ),
    ]
