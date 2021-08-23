'''https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/#django.core.management.BaseCommand.add_arguments
https://stackoverflow.com/questions/59305153/custom-django-management-command
'''
from django.core.management.base import BaseCommand, CommandError
from e_commerce.models import Product


class Command(BaseCommand):
    """Use this command at the terminal.
    docker-compose run web python manage.py closepoll 2. 
    """
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        # Positional arguments.
        parser.add_argument('product_id', nargs='+', type=int)

        # Named (optional) arguments.
        # docker-compose run web python manage.py closepoll --delete 1
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):

        if options['delete']:
            instance = Product.objects.get(product_id=options['product_id'][0])
            instance.delete()
            self.stdout.write(self.style.SUCCESS('Object Deleted'))

        for product_id in options['product_id']:
            try:
                product = Product.objects.get(pk=product_id)
            except Product.DoesNotExist:
                raise CommandError('Product "%s" does not exist' % product_id)

            product.opened = False
            product.save()

            self.stdout.write(self.style.SUCCESS(
                'Successfully closed product "%s"' % product_id))
