# Generated by Django 5.0.4 on 2024-05-20 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Salad', 'Salad'), ('Snack', 'Snack'), ('Drink', 'Drink'), ('Soup', 'Soup'), ('Chicken', 'Chicken'), ('Vegeterian', 'Vegeterian')], max_length=50),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_type',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Salad', 'Salad'), ('Snack', 'Snack'), ('Drink', 'Drink'), ('Soup', 'Soup'), ('Chicken', 'Chicken'), ('Vegeterian', 'Vegeterian')], max_length=20),
        ),
    ]
