from rest_framework import serializers

class CountryInfoSerializer(serializers.Serializer):
    flag_link = serializers.URLField(source='flag_link')
    capital = serializers.CharField(source='capital')
    largest_city = serializers.ListField(child=serializers.CharField(), source='largest_city')
    official_languages = serializers.ListField(child=serializers.CharField(), source='official_languages')
    area_total = serializers.IntegerField(source='area_total')
    population = serializers.CharField(source='population')
    GDP_nominal = serializers.CharField(source='GDP_nominal')
