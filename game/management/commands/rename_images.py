import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Renames all image files to lowercase'

    def handle(self, *args, **options):
        images_dir = os.path.join('game', 'static', 'images')
        
        # Get all files in the directory
        for filename in os.listdir(images_dir):
            if filename.endswith('.png'):
                # Create new lowercase filename
                new_filename = filename.lower()
                
                # Skip if filename is already lowercase
                if filename == new_filename:
                    continue
                
                # Get full paths
                old_path = os.path.join(images_dir, filename)
                new_path = os.path.join(images_dir, new_filename)
                
                # Rename the file
                try:
                    os.rename(old_path, new_path)
                    self.stdout.write(self.style.SUCCESS(f'Renamed {filename} to {new_filename}'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error renaming {filename}: {str(e)}'))
        
        self.stdout.write(self.style.SUCCESS('Finished renaming images')) 