# Generated by Django 4.2.3 on 2023-07-26 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0003_alter_item_item_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="item_image",
            field=models.CharField(
                default="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.everestkitchenpa.com%2Fassets%2Fpages%2FcoldBeverages.html&psig=AOvVaw3A5A_WsdHrnJoGHacmY2zI&ust=1690479288574000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCKiGjJ70rIADFQAAAAAdAAAAABAJ",
                max_length=1000,
            ),
        ),
    ]