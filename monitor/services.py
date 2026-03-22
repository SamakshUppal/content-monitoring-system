from .models import Keyword, ContentItem, Flag


def calculate_score(keyword, content):
    keyword = keyword.lower()
    title = content.title.lower()
    body = content.body.lower()

    if keyword in title:
        if keyword == title:
            return 100
        return 70
    elif keyword in body:
        return 40
    return 0


def should_create_flag(existing_flag, content):
    if not existing_flag:
        return True

    if existing_flag.status == 'irrelevant':
        if existing_flag.last_reviewed_at and content.last_updated > existing_flag.last_reviewed_at:
            return True
        return False

    return False


def run_scan():
    contents = ContentItem.objects.all()
    keywords = Keyword.objects.all()

    for content in contents:
        for keyword in keywords:
            score = calculate_score(keyword.name, content)

            if score == 0:
                continue

            existing_flag = Flag.objects.filter(
                keyword=keyword,
                content_item=content
            ).first()

            if not should_create_flag(existing_flag, content):
                continue

            if existing_flag:
                existing_flag.score = score
                existing_flag.status = 'pending'
                existing_flag.save()
            else:
                Flag.objects.create(
                    keyword=keyword,
                    content_item=content,
                    score=score,
                    status='pending'
                )