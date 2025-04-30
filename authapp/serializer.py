from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from .models import Profile, User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'tel', 'is_admin_coop', 'is_superuser']
        
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ['id', 'fullname', 'verified', 'bio', 'image', 'user', 'created_at']

class UserSerializerProfile(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True) 
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'tel', 'is_admin_coop', 'is_superuser', 'profile']       

class MytokenObtainPairView(TokenObtainPairSerializer):
    username_field = 'username'
    
    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError({"detail": _("Acun utilisateur trouvé avec ces identifiants.")})
        
        data =  super().validate(attrs)
            
        data['fullname'] = user.profile.fullname
        data['username'] = user.username
        data['email'] = user.email
        data['tel'] = user.tel
        data['bio'] = user.profile.bio
        data['image'] = str(user.profile.image) 
        data['verified'] = user.profile.verified  
        data['is_superuser'] = user.is_superuser 
        data['is_staff'] = user.is_staff          
        
        return data
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        token['fullname'] = user.profile.fullname
        token['username'] = user.username
        token['email'] = user.email
        token['tel'] = user.tel
        token['bio'] = user.profile.bio
        token['image'] = str(user.profile.image) 
        token['verified'] = user.profile.verified  
        token['is_superuser'] = user.is_superuser 
        token['is_staff'] = user.is_staff          
        
        return token

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model=User
        fields =  ['email', 'username', 'tel', 'password', 'password2']    
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields does not match"}
            )    
        return attrs
        
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            tel = validated_data['tel'],
        )
        user.set_password(validated_data['password'])
        user.save()
            
        return user