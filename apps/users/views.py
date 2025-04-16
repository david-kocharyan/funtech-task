from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone
from .models import RewardLog, ScheduledReward
from .serializers import UserProfileSerializer, RewardLogSerializer
from .tasks import process_scheduled_reward
from datetime import timedelta


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)


class RewardLogListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RewardLogSerializer

    def get_queryset(self):
        return RewardLog.objects.filter(user=self.request.user).order_by('-given_at')


class RequestRewardView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        now = timezone.now()
        if ScheduledReward.objects.filter(user=user, execute_at__gte=now - timedelta(days=1)).exists():
            return Response({"detail": "Already requested today."}, status=400)

        scheduled_time = now + timedelta(minutes=5)
        reward = ScheduledReward.objects.create(user=user, amount=1, execute_at=scheduled_time)
        process_scheduled_reward.apply_async((reward.id,), eta=scheduled_time)
        return Response({"detail": "Reward scheduled."})
