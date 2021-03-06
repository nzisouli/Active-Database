# Generated by Django 2.1.4 on 2018-12-20 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buying',
            fields=[
                ('buying_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('moneyPerMonth', models.FloatField()),
                ('moneyLeft', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('productsLeft', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('shop_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('delivery', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Shop'),
        ),
        migrations.AddField(
            model_name='buying',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Person'),
        ),
        migrations.AddField(
            model_name='buying',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
    ]
