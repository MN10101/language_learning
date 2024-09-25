from django.db import migrations

def create_teacher_group(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    group, created = Group.objects.get_or_create(name='Teachers')

class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0001_initial'),  # Adjust to match your app's first migration
    ]

    operations = [
        migrations.RunPython(create_teacher_group),
    ]
