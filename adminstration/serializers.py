from rest_framework import serializers
from adminstration.models import Militar, Graduacao, Secao

class SecaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secao
        fields = ['id','Nome']

    def create(self, validated_data):
        request = self.context.get('request', None)
        validated_data["InseridoPor"] = request.user.email
        secao = Secao(**validated_data)
        secao.save()
        return secao

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        validated_data["AtualizadoPor"] = request.user.email
        for key in validated_data:
            if not validated_data.get(key):
                continue
            setattr(instance, key, validated_data.get(key))
        instance.save()
        return instance


class GraduacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Graduacao
        fields = ['id','Nome']

    def create(self, validated_data):
        request = self.context.get('request', None)
        validated_data["InseridoPor"] = request.user.email
        secao = Graduacao(**validated_data)
        secao.save()
        return secao

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        validated_data["AtualizadoPor"] = request.user.email
        for key in validated_data:
            if not validated_data.get(key):
                continue
            setattr(instance, key, validated_data.get(key))
        instance.save()
        return instance


class MilitarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Militar
        fields = [
            'id',
            'Nome',
            'NomeGuerra',
            'Email',
            'DataDeNascimento',
            'Telefone',
            'RITEx',
            'Imagem',
            'secao',
            'graduacao',
            'FlgTelegram',
            'FlgWhatsApp',
            'FlgAtivo'
        ]

    def create(self, validated_data):
        request = self.context.get('request', None)
        validated_data["InseridoPor"] = request.user.email
        secao = Militar(**validated_data)
        secao.save()
        return secao

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        validated_data["AtualizadoPor"] = request.user.email
        for key in validated_data:
            if not validated_data.get(key):
                continue
            setattr(instance, key, validated_data.get(key))
        instance.save()
        return instance