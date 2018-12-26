from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import Urusetia

# Create your models here.
class Sistem(models.Model):
	NamaSistem = models.CharField('NamaSistem',max_length=200,blank=False,null=False)
	Tahun = models.IntegerField('Tahun',null=False)
	Status = models.IntegerField('Status',null=False,default=1)
	PemilikSistem = models.CharField('PemilikSistem',max_length=200,null=False)

	def __str__(self):
		return str(self.pk)

# class User(AbstractUser):
# 	is_pentadbir = models.BooleanField(default = False)		
# 	is_urusetia = models.BooleanField(default = False)		
# 	is_juruaudit = models.BooleanField(default = False)		
# 	is_kjaudit = models.BooleanField(default = False)		
# 	is_pemantau = models.BooleanField(default = False)

class Profil(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	nokpten = models.CharField(max_length = 12,unique = True)
	Status = models.IntegerField('Status',null=False,default=1)

	def __str__(self):
		return str(self.pk)

# class Pengguna(models.Model):
# 	user = models.OneToOneField(User, on_delete = models.CASCADE)
# 	nokpten = models.CharField(max_length = 12,unique = True)
	# sistem = models.ManyToManyField(TblSistem)

class RefPeranan(models.Model):
	Peranan = models.CharField('Peranan',max_length=100,null=False)
	KodPeranan = models.IntegerField('KodPeranan',null=False,default=1)
	Keterangan = models.CharField('Keterangan',max_length=200,null=False)

	def __str__(self):
		return str(self.pk)


class Peranan(models.Model):
	Sistem = models.ForeignKey('Sistem',on_delete=models.CASCADE)		
	UProfil = models.ForeignKey('Profil',on_delete=models.CASCADE)
	nokpten = models.CharField(max_length=12)
	Peranan = models.ForeignKey('RefPeranan',on_delete=models.CASCADE)

	def __str__(self):
		return str(self.pk)

