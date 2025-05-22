from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Users
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='alicepass')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='bobpass')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='carolpass')

        # Teams
        team1 = Team.objects.create(name='Team Red', members=[user1.email, user2.email])
        team2 = Team.objects.create(name='Team Blue', members=[user3.email])

        # Activities
        Activity.objects.create(user=user1.email, activity_type='run', duration=30, date=timezone.now())
        Activity.objects.create(user=user2.email, activity_type='walk', duration=45, date=timezone.now())
        Activity.objects.create(user=user3.email, activity_type='cycle', duration=60, date=timezone.now())

        # Leaderboard
        Leaderboard.objects.create(team=team1.name, points=150)
        Leaderboard.objects.create(team=team2.name, points=100)

        # Workouts
        Workout.objects.create(user=user1.email, workout_type='cardio', details={'distance': 5}, date=timezone.now())
        Workout.objects.create(user=user2.email, workout_type='strength', details={'reps': 20}, date=timezone.now())
        Workout.objects.create(user=user3.email, workout_type='yoga', details={'duration': 60}, date=timezone.now())

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
