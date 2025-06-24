from PIL import Image
from rest_framework import serializers

from movie_website.users.models.user import CustomerUser


__all__ = [
    'CustomerUserSerializer',
]

class CustomerUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUser
        fields = '__all__'

    def validate_profile_image(self, image):
        valid_formats = ['JPEG', 'JPG', 'PNG']
        max_size = 2 * 1024 * 1024  # 2 MB

        if image.size > max_size:
            raise serializers.ValidationError('Image size should not exceed 2 MB.')
        
        try:
            img = Image.open(image)
            if img.format.upper() not in valid_formats:
                raise serializers.ValidationError(f"Image format must be one of: {', '.join(valid_formats)}.")
        except Exception:
            raise serializers.ValidationError('Invalid image file')

        return image