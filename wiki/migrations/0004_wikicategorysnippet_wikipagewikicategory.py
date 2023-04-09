# Generated by Django 3.2.14 on 2022-09-14 21:06

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wiki', '0003_remove_wikipage_short_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='WikiCategorySnippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translation_key', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(help_text='A topic for the library, can intersect with other topics', max_length=255, verbose_name='topic name')),
                ('locale', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.locale')),
            ],
            options={
                'abstract': False,
                'unique_together': {('translation_key', 'locale')},
            },
        ),
        migrations.CreateModel(
            name='WikiPageWikiCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='wiki_categories', to='wiki.wikipage')),
                ('wiki_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wikipages', to='wiki.wikicategorysnippet')),
            ],
            options={
                'unique_together': {('page', 'wiki_category')},
            },
        ),
    ]