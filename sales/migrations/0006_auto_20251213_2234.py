from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_alter_saleitem_total_price_alter_saleitem_unit_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='sale_item',
        ),
    ]

