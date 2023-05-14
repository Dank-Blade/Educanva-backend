from rest_framework import serializers
from .models import File
from module.serializers import ModuleSerializer
from accounts.serializers import UserCreateSerializer

class FileSerializer(serializers.ModelSerializer):
    # module = ModuleSerializer()
    # uploaded_by = UserCreateSerializer()
    # file_url = serializers.SerializerMethodField()
    
    class Meta:
        model = File
        fields = ('id', 'file', 'name', 'uploaded_by', 'description', 'created_at', 'module')
        
        
    # def create(self, validated_data):
    #     file = File.objects.create(name=validated_data['name'],
    #                                     description=validated_data['description'],
    #                                     file=validated_data['file'],
    #                                     module=validated_data['module'],
    #                                     uploaded_by=self.context['request'].user,
    #                                     uploaded_at=validated_data['uploaded_at'],
    #                                         )
    #     return file
        