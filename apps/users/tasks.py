from celery import shared_task
from .models import ScheduledReward, RewardLog

@shared_task
def process_scheduled_reward(scheduled_reward_id):
    try:
        reward = ScheduledReward.objects.get(id=scheduled_reward_id)
        user = reward.user
        user.coins += reward.amount
        user.save()
        RewardLog.objects.create(user=user, amount=reward.amount)
    except ScheduledReward.DoesNotExist:
        print("ScheduledReward does not exist")