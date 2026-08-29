from django.core.management.base import BaseCommand
from django.utils import timezone
from polls.models import Question, Choice
from django.db import connection

PRESETS = [
    {
        "question_text": "Favorite programming language?",
        "choices": ["Python", "Rust", "Typescript"],
        "created_by": "arde"
    },
    {
        "question_text": "Best OS?",
        "choices": ["Linux", "macOS", "Windows"],
        "created_by": "konna"
    }
]

class Command(BaseCommand):
    help = "Seeds poll data for testing purposes"

    def handle(self, *args, **options):
        Choice.objects.all().delete()
        Question.objects.all().delete()

        with connection.cursor() as cursor:
            # Reset PK counter for easier testing
            cursor.execute(
                "DELETE FROM sqlite_sequence WHERE name IN ('polls_question', 'polls_choice')"
            )

        for preset in PRESETS:
            question = Question.objects.create(
                question_text=preset["question_text"],
                pub_date=timezone.now(),
                created_by=preset["created_by"]
            )


            for choice_text in preset["choices"]:
                Choice.objects.create(question=question, choice_text=choice_text, votes=0)

            print("Seeded test questions")

