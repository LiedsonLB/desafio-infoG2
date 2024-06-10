from rest_framework import serializers
from .models import Survivor, Resource

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'resource_type', 'quantity']

class SurvivorSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True)

    class Meta:
        model = Survivor
        fields = ['id', 'name', 'age', 'gender', 'last_location_latitude', 'last_location_longitude', 'infected', 'resources']

    def update(self, instance, validated_data):
        resources_data = validated_data.pop('resources', [])
        resources = instance.resources.all()

        for resource_data in resources_data:
            resource_id = resource_data.get('id', None)
            if resource_id:
                resource = resources.filter(id=resource_id).first()
                if resource:
                    resource.resource_type = resource_data.get('resource_type', resource.resource_type)
                    resource.quantity = resource_data.get('quantity', resource.quantity)
                    resource.save()
            else:
                Resource.objects.create(survivor=instance, **resource_data)

        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.last_location_latitude = validated_data.get('last_location_latitude', instance.last_location_latitude)
        instance.last_location_longitude = validated_data.get('last_location_longitude', instance.last_location_longitude)
        instance.infected = validated_data.get('infected', instance.infected)
        instance.save()

        return instance