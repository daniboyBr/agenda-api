from django.db import models
import uuid

class Secao(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Nome = models.CharField(max_length=45)
    InseridoPor = models.CharField(max_length=45,  null=True)
    DataInsercao = models.DateTimeField(auto_now_add=True)
    AtualizadoPor = models.CharField(max_length=45, null=True)
    DataDeAtualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Nome

class Graduacao(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Nome = models.CharField(max_length=45)
    InseridoPor = models.CharField(max_length=45,  null=True)
    DataInsercao = models.DateTimeField(auto_now_add=True)
    AtualizadoPor = models.CharField(max_length=45, null=True)
    DataDeAtualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Nome

class Militar(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Nome = models.CharField(max_length=45)
    NomeGuerra = models.CharField(max_length=45)
    Email = models.EmailField(max_length=100, unique=True)
    DataDeNascimento = models.DateField(null=True)
    Telefone = models.CharField(max_length=45, null=True)
    RITEx = models.CharField(max_length=45, null=True)
    FlgCiente = models.BooleanField(default=True)
    Imagem = models.ImageField(upload_to='militares/', null=True, blank=True)
    FlgTelegram = models.BooleanField(default=True)
    FlgWhatsApp = models.BooleanField(default=True)
    InseridoPor = models.CharField(max_length=45, null=True)
    DataInsercao = models.DateTimeField(auto_now_add=True)
    AtualizadoPor = models.CharField(max_length=45, null=True)
    DataDeAtualizacao = models.DateTimeField(auto_now=True)
    Secao = models.ForeignKey(Secao, on_delete=models.DO_NOTHING, name="secao")
    Graduacao = models.ForeignKey(Graduacao, on_delete=models.DO_NOTHING, name="graduacao")
    FlgAtivo = models.BooleanField(default=True)


    def __str__(self):
        return self.Nome
