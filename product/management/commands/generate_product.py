from django.core.management.base import BaseCommand
from faker import Faker
from ...models import * 



class Command(BaseCommand):
    help = 'Generates fake product data using Faker'
    
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()


    def get_random_product_image(self):
        # RANDOM_USER_API_URL = "https://randomuser.me/api/portraits/men/"
        random_number = self.fake.random.randint(1, 100)  # ایجاد یک عدد تصادفی برای انتخاب تصویر
        # return image_url
        return f"https://placehold.co/250x250?text=Product+{random_number}"

    def handle(self, *args, **kwargs):
        num_proudcts = 10 
        category_list = ["Digital Product","Clothing","Book","Sports","Supermarket"]
        for name in category_list:
            category,_ = Category.objects.get_or_create(name=name)
            for _ in range(num_proudcts):
                Product.objects.create(
                    name=self.fake.name(),
                    image = self.get_random_product_image(),
                    price=self.fake.random_int(min=100000,max=100000000),
                    color=self.fake.color_name(),
                    quantity=self.fake.random_int(min=5,max=10000),
                    discount=self.fake.random_element([0, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70]),
                    category = category
                )
            self.stdout.write(self.style.SUCCESS(f'Successfully generated {num_proudcts} fake product.'))