import datetime

from django.test import Client, TestCase
from django.utils import timezone

from .. models import Content, Category


class ContentViewTests(TestCase):
    def setUp(self):
        self.now = timezone.now()
        self.cat1 = Category.objects.create(cat_name="All")
        self.cat1.save()
        self.cat2 = Category.objects.create(cat_name="Tech")
        self.cat2.save()
        self.cat3 = Category.objects.create(cat_name="Coding")
        self.cat3.save()
        self.cat4 = Category.objects.create(cat_name="Video")
        self.cat4.save()
        self.c1 = Content.objects.create(
            title="Carl's First Blog",
            sub_title="first",
            author="Carl James",
            location="Bloomington, IN",
            pub_date=self.now - datetime.timedelta(days=30),
            featured_image="https://live.staticflickr.com/65535/"
                           "50630286192_137fed66d0_m.jpg",
            image_caption="simple image",
            teaser="<p>With conferences, retreats and in-person "
                   "meetings rare these days, and likely to "
                   "remain so for the foreseeable future, we "
                   "have all discovered which kinds of face-to-face "
                   "events can (or can’t) transfer to the internet.</p> "
                   "<p>It’s already clear that a great virtual event "
                   "takes more than a solid Wi-Fi connection</p>",
            content="<p>With conferences, retreats and in-person "
                    "meetings rare these days, and likely to "
                    "remain so for the foreseeable future, we "
                    "have all discovered which kinds of face-to-face "
                    "events can (or can’t) transfer to the internet.</p> "
                    "<p>It’s already clear that a great virtual event "
                    "takes more than a solid Wi-Fi connection and "
                    "decent web conferencing software; it takes careful "
                    "planning, effective facilitation and the right "
                    "mix of channels</p>",
            )
        self.c1.save()
        self.c1.categories.set([self.cat1, self.cat2])


        self.c2 = Content.objects.create(
            title="Carl's Second Blog",
            pub_date=self.now - datetime.timedelta(days=27),
            sub_title="second",
            author="Carl James",
            location="Bloomington, IN",
            featured_image="https://live.staticflickr.com/65535/"
                           "50630286192_137fed66d0_m.jpg",
            image_caption="simple image",
            teaser="<p>New Mexico officials are offering grocery "
                   "stores, retailers and other essential "
                   "businesses a way to avoid shutdowns when "
                   "workers become infected with Covid-19: "
                   "regularly test all employees.</p>"
                   "<p>Supermarkets, big-box retailers and "
                   "hotels that pay for regular testing "
                   "and contact tracing of their workers "
                   "will be exempt from two-week shutdowns "
                   "the state has imposed on stores with "
                   "infected employees as cases rise.</p>",
            content="<p>New Mexico officials are offering grocery "
                    "stores, retailers and other essential "
                    "businesses a way to avoid shutdowns when "
                    "workers become infected with Covid-19: "
                    "regularly test all employees.</p>"
                    "<p>Supermarkets, big-box retailers and "
                    "hotels that pay for regular testing "
                    "and contact tracing of their workers "
                    "will be exempt from two-week shutdowns "
                    "the state has imposed on stores with "
                    "infected employees as cases rise. Under "
                    "the new agreement, companies must foot "
                    "the bill for the measures, test workers "
                    "every two weeks and share those plans "
                    "with New Mexico health officials.</p>",
            )
        self.c2.save()
        self.c2.categories.set([self.cat1, self.cat3])

        self.c3 = Content.objects.create(
            title="Carl's Third Blog",
            sub_title="third",
            author="Carl James",
            location="Bloomington, IN",
            pub_date=self.now - datetime.timedelta(days=24),
            featured_image="https://live.staticflickr.com/65535/"
                           "50630286192_137fed66d0_m.jpg",
            image_caption="simple image",
            teaser="<p>Manufacturers are introducing face masks "
                   "for general use that they say offer more "
                   "protection than cloth coverings without "
                   "taxing supplies of the N95 masks used in "
                   "hospitals.</p> <p>These mask makers said "
                   "many of the new models coming to market "
                   "are more protective than cloth masks but "
                   "don’t reach the level of protection "
                   "provided by N95s</p>",
            content="<p>Manufacturers are introducing face masks "
                    "for general use that they say offer more "
                    "protection than cloth coverings without "
                    "taxing supplies of the N95 masks used in "
                    "hospitals.</p> <p>These mask makers said "
                    "many of the new models coming to market "
                    "are more protective than cloth masks but "
                    "don’t reach the level of protection "
                    "provided by N95s, which stop at least "
                    "95% of very small particles with a "
                    "sophisticated filter and a snug fit to "
                    "the face. ",
            )
        self.c3.save()
        self.c3.categories.set([self.cat1, self.cat3])

        self.c4 = Content.objects.create(
            title="Carl's Fourth Blog",
            sub_title="fourth",
            author="Carl James",
            location="Bloomington, IN",
            pub_date=self.now - datetime.timedelta(days=21),
            featured_image="https://live.staticflickr.com/65535/"
                           "50630286192_137fed66d0_m.jpg",
            image_caption="simple image",
            teaser="<p>The law that enabled the rise of social "
                   "media and other internet businesses is "
                   "facing threats unlike anything in its "
                   "24-year history, with potentially significant "
                   "consequences for websites that host user "
                   "content.</p> <p>Section 230 of the Communications "
                   "Decency Act was instrumental to the success of Silicon "
                   "Valley</p>",
            content="<p>The law that enabled the rise of social "
                    "media and other internet businesses is "
                    "facing threats unlike anything in its "
                    "24-year history, with potentially significant "
                    "consequences for websites that host user "
                    "content.</p> <p>Section 230 of the Communications "
                    "Decency Act was instrumental to the success of Silicon "
                    "Valley tech giants such as Facebook Inc., Twitter Inc. "
                    "and Alphabet Inc.’s Google and YouTube by giving them "
                    "broad immunity for the content they publish from users "
                    "on their sites.<.p>",
            )
        self.c4.save()
        self.c4.categories.set([self.cat1, self.cat3, self.cat4])

        self.c5 = Content.objects.create(
            title="Carl's Fifth Blog",
            sub_title="fifth",
            author="Carl James",
            location="Bloomington, IN",
            pub_date=self.now - datetime.timedelta(days=18),
            featured_image="https://live.staticflickr.com/65535/"
                           "50630286192_137fed66d0_m.jpg",
            image_caption="simple image",
            teaser="<p>Type in the letters you want to "
                   "unscramble and our word finder will</p>",
            content="<p>Type in the letters you want to "
                    "unscramble and our word finder will "
                    "show you all the possible words you "
                    "can make from the letters in your hand.</p>",
            )
        self.c5.save()
        self.c5.categories.set([self.cat1, self.cat2])

        self.c6 = Content.objects.create(
            title="Carl's Sixth Blog",
            sub_title="third",
            author="Carl James",
            location="Bloomington, IN",
            pub_date=self.now - datetime.timedelta(days=15),
            featured_image="https://live.staticflickr.com/65535/"
                           "50630286192_137fed66d0_m.jpg",
            image_caption="simple image",
            teaser="<p>From this time onwards"
                   "its existence as a separate </p>",
            content="<p>From this time onwards"
                    "its existence as a separate "
                    "kingdom was at an end, though "
                    "during the last years of Eadwig's "
                    "reign the Mercians and Northumbrians "
                    "set up Eadgar as king.</p>",
            )
        self.c6.save()
        self.c6.categories.set([self.cat1, self.cat4])

    def test_index_page_forwards(self):
        client = Client()
        response = client.get('')
        self.assertEqual(response.status_code, 302)

    def test_sub_index_page_renders(self):
        client = Client()
        response = client.get('/j34/')
        contain_text = "Video"
        self.assertContains(response, contain_text)
        self.assertEqual(response.status_code, 200)

    def test_index_all_category_partial_drops_old_blogs(self):
        client = Client()
        category = self.cat1
        response = client.get(f'/j34/category_blogs/{category.pk}/')
        contain_text = "its existence as a separate"
        not_contain_text = "New Mexico officials"
        self.assertContains(response, contain_text)
        self.assertNotContains(response, not_contain_text)
        self.assertEqual(response.status_code, 200)

    def test_index_small_category_partial_only_renders_filtered_blogs(self):
        client = Client()
        category = self.cat3
        response = client.get(f'/j34/category_blogs/{category.pk}/')
        contain_text = "consequences for websites that host user"
        not_contain_text = "takes more than a solid Wi-Fi"
        self.assertContains(response, contain_text)
        self.assertNotContains(response, not_contain_text)
        self.assertEqual(response.status_code, 200)

    def test_specific_blog_page_renders(self):
        blog_num = self.c3.pk
        client = Client()
        response = client.get(f'/j34/blog/{blog_num}/')
        self.assertEqual(response.status_code, 200)
        contain_text = "95% of very small particles with a"
        self.assertContains(response, contain_text)

    def test_blog_list_renders(self):
        client = Client()
        response = client.get(f'/j34/blogs/')
        self.assertEqual(response.status_code, 200)
        contain_text = "First Blog"
        self.assertContains(response, contain_text)
        number_of_items = len(response.context['articles'])
        self.assertIs(number_of_items, 6)
