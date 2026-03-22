from .models import ContentItem
from datetime import datetime


def load_mock_data():
    data = [
        {
            "title": "Learn Django Fast",
            "body": "Django is a powerful Python framework",
            "source": "Blog A",
        },
        {
            "title": "Cooking Tips",
            "body": "Best recipes for beginners",
            "source": "Blog B",
        }
    ]

    for item in data:
        # 🔥 Check if already exists
        obj, created = ContentItem.objects.get_or_create(
            title=item["title"],
            source=item["source"],
            defaults={
                "body": item["body"],
                "last_updated": datetime.now()
            }
        )

        # Optional: update timestamp if exists
        if not created:
            obj.last_updated = datetime.now()
            obj.save()