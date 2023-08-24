from wagtail.core.blocks.field_block import BooleanBlock
from wagtail.core.blocks.field_block import CharBlock
from wagtail.core.blocks.field_block import PageChooserBlock
from wagtail.core.blocks.field_block import RichTextBlock
from wagtail.core.blocks.struct_block import StructBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock


class CarouselBlog(StructBlock):

    latest_blog_post = BooleanBlock(required=False)
    blog_post = PageChooserBlock(page_type="blog.BlogPage", required=False)

    def get_context(self, value, parent_context=None):

        from blog.models import BlogPage

        context = super().get_context(value, parent_context=parent_context)
        if value["latest_blog_post"] and "page" in context:
            context["blog_page"] = (
                BlogPage.objects.descendant_of(context["page"])
                .live()
                .exclude(header_image=None)
                .order_by("-date", "-id")
                .first()
            )
        else:
            context["blog_page"] = value["blog_post"]
        return context

    class Meta:
        template = "home/blocks/carousel_blog.html"


class CarouselPage(StructBlock):
    image = ImageChooserBlock()
    page = PageChooserBlock()

    class Meta:
        template = "home/blocks/carousel_page.html"


class CarouselRaw(StructBlock):
    image = ImageChooserBlock()
    headline = CharBlock()
    description = RichTextBlock()
    read_more = PageChooserBlock()

    class Meta:
        template = "home/blocks/carousel_raw.html"


class FeatureBlock(StructBlock):
    headline = CharBlock()
    sub_headline = CharBlock()
    description = RichTextBlock()
    read_more = PageChooserBlock()

    class Meta:
        template = "home/blocks/feature.html"


class SectionCardBlock(StructBlock):
    headline = CharBlock()
    description = RichTextBlock()
    read_more = PageChooserBlock()

    class Meta:
        template = "home/blocks/section_card.html"


class OrganizationsCardBlock(StructBlock):
    headline = CharBlock()
    sub_headline = CharBlock()
    organizations = SnippetChooserBlock("home.OrganizationCollection")

    class Meta:
        template = "home/blocks/organization_collection_card.html"
