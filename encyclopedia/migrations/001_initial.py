from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
     initial = True

dependencies = [
    ]

operations = [
        migrations.CreateModel(
            name='baikemodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('ent', models.CharField(max_length=500)),
            ],
        ),

]