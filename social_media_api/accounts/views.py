from rest_framework import generics, permissions, status
from .serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404

User = get_user_model()

# ================================
# USER REGISTRATION AND LOGIN
# ================================

# Registration view
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        token = Token.objects.get(user=user)
        response.data['token'] = token.key
        return response


# Login view
class LoginView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


# ================================
# FOLLOW/UNFOLLOW USERS
# ================================

# Follow a user
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, pk=user_id)
    if user_to_follow == request.user:
        return Response({'detail': "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
    request.user.following.add(user_to_follow)
    return Response({'detail': f'You are now following {user_to_follow.username}.'}, status=status.HTTP_200_OK)


# Unfollow a user
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, pk=user_id)
    if user_to_unfollow == request.user:
        return Response({'detail': "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
    request.user.following.remove(user_to_unfollow)
    return Response({'detail': f'You have unfollowed {user_to_unfollow.username}.'}, status=status.HTTP_200_OK)
