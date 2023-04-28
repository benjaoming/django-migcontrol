import uuid

from django.conf import settings
from django.db import migrations

# slug: title, translation_key
homepage_translation_key = uuid.uuid4()

# {slug: (title, uuid, show_in_menus)}
pages = {
    "about": ("About", uuid.uuid4(), True),
    "contact": ("Contact", uuid.uuid4(), False),
    "donate": ("Donate", uuid.uuid4(), False),
    "subscribe": ("Subscribe", uuid.uuid4(), False),
    "imprint": ("Imprint", uuid.uuid4(), False),
    "data-protection": ("Data protection", uuid.uuid4(), False),
}


def create_pages_and_locales(apps, schema_editor):
    # Get models
    Site = apps.get_model('wagtailcore.Site')
    Article = apps.get_model('home.Article')
    ContentType = apps.get_model('contenttypes.ContentType')
    Locale = apps.get_model('wagtailcore.Locale')
    HomePage = apps.get_model('home.HomePage')
    from wagtail.models import Page, Locale as LocaleNonMigrated  # noqa
    from wagtail_localize.models import TranslatableObject

    # Create content type for blogindexpage model
    article_content_type, __ = ContentType.objects.get_or_create(
        model='article', app_label='home')

    homepage_content_type, __ = ContentType.objects.get_or_create(
        model='homepage', app_label='home')

    for home_index, (language_code, language_name) in enumerate(settings.LANGUAGES):

        locale, __ = Locale.objects.get_or_create(language_code=language_code)

        if language_code == "en":
            home = Page.objects.get(pk=Site.objects.get(is_default_site=True).root_page.pk)
            HomePage.objects.filter(pk=home.pk).update(translation_key=homepage_translation_key)
        else:
            home = HomePage.objects.create(
                locale=locale,
                content_type=homepage_content_type,
                title=f"Home - {language_name}",
                draft_title=f"Home - {language_name}",
                slug=f"home-{language_code}",
                path="0001000{}".format(home_index+1),
                depth=2,
                numchild=0,
                url_path=f"/home-{language_code}/",
                translation_key=homepage_translation_key,
                live=True,
            )
            home = Page.objects.get(pk=home.pk)

        for index, (slug, (title, translation_key, show_in_menus)) in enumerate(pages.items()):
            index_offset = index + 1
            # Create a new homepage
            article = Article(
                title=title,
                draft_title=title,
                slug=f"{slug}",
                content_type=article_content_type,
                locale=locale,
                path=f"{home.path}000{index_offset}",
                depth=3,
                numchild=0,
                translation_key=translation_key,
                url_path="/home{home_append}/{slug}/".format(
                    slug=slug,
                    home_append=f"-{language_code}" if language_code != "en" else ""
                ),
                live=True,
                show_in_menus=show_in_menus,
            )

            home.add_child(instance=article)


def remove_pages(apps, schema_editor):
    # Get models
    BlogIndexPage = apps.get_model('blog.BlogIndexPage')

    # Delete BlogIndexPage
    # Page and Site objects CASCADE
    BlogIndexPage.objects.filter(slug="blog").delete()


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_article'),
        ('wagtailcore', '0053_locale_model'),
    ]

    operations = [
        migrations.RunPython(create_pages_and_locales, remove_pages),
    ]
