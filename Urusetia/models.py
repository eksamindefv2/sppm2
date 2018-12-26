from django.db import models
import Pentadbir

# Create your models here.
class Sesi(models.Model):
	Siri = models.CharField('Siri',max_length=50,blank=False,null=False)
	TarikhMula = models.DateTimeField('TarikhMula',blank=True,null=True,auto_now_add=True)
	TarikhTamat = models.DateTimeField('TarikhTamat',blank=True,null=True,auto_now_add=True)
	TarikhMulaAudit = models.DateTimeField('TarikhMulaAudit',blank=True,null=True,auto_now_add=True)
	TarikhTamatAudit = models.DateTimeField('TarikhTamatAudit',blank=True,null=True,auto_now_add=True)
	Status = models.IntegerField('StatusSesi',blank=False,null=False, default=1)
	SistemID = models.ForeignKey('Pentadbir.Sistem',on_delete=models.CASCADE)

	def __str__(self):
		return str(self.pk)


class RefSkala(models.Model):
	NamaSkala = models.CharField('NamaSkala',max_length=50,blank=False,null=False)
	Deskripsi = models.CharField('Deskripsi',max_length=50,blank=False,null=False)
	NilaiSkala = models.IntegerField('NilaiSkala',blank=False,null=False, default=1)
	Status = models.IntegerField('Status',blank=False,null=False, default=1)
	# SubKodKomponenID = models.ForeignKey('TblSubKomponen',on_delete=models.CASCADE)

	def __str__(self):
		return str(self.pk)


class Komponen(models.Model):
	KodKomponen = models.CharField('KodKomponen',max_length=10,blank=False,null=False)
	NamaKomponen = models.CharField('NamaKomponen',max_length=60,blank=False,null=False)
	Pemberat = models.IntegerField('Pemberat',blank=False,null=False, default=0)
	SesiID = models.ForeignKey('Sesi',on_delete=models.CASCADE)

	def __str__(self):
		return str(self.pk)


class SubKomponen(models.Model):
	SubKodKomponen = models.CharField('SubKodKomponen',max_length=10,blank=False,null=False)
	NamaSubKomponen = models.CharField('NamaSubKomponen',max_length=100,blank=False,null=False)
	Pemberat = models.IntegerField('Pemberat',blank=False,null=False, default=0)
	KomponenID = models.ForeignKey('Komponen',on_delete=models.CASCADE)
	RefSkalaID = models.ForeignKey('RefSkala',on_delete=models.CASCADE)

	def __str__(self):
		return str(self.pk)

class Soalan(models.Model):
	NoSoalan = models.CharField('NoSoalan',max_length=10,blank=False,null=False)
	DeskripsiSoalan = models.CharField('DeskripsiSoalan',max_length=100,blank=False,null=False)
	Status = models.IntegerField('Statussoalan',blank=False,null=False, default=1)
	KomponenID = models.ForeignKey('Komponen',on_delete=models.CASCADE)

	def __str__(self):
		return str(self.pk)


class Jawapan(models.Model):
	NoJawapan = models.CharField('NoJawapan',max_length=10,blank=False,null=False)
	DeskripsiJawapan = models.CharField('DeskripsiJawapan',max_length=100,blank=False,null=False)
	SoalanID = models.ForeignKey('Soalan',on_delete=models.CASCADE)
	Nilai = models.IntegerField('Nilai',blank=False,null=False, default=0)


	def __str__(self):
		return str(self.pk)

class Auditee(models.Model):
	NamaAuditee = models.CharField('NamaAuditee',max_length=100,blank=False,null=False)
	Status = models.IntegerField('StatusAuditee',blank=False,null=False, default=1)
	SistemID = models.ForeignKey('Pentadbir.Sistem',on_delete=models.CASCADE)

	def __str__(self):
		return str(self.pk)

class SubAuditee(models.Model):
	NamaSubAuditee = models.CharField('NamaSubAuditee',max_length=100,blank=False,null=False)
	AuditeeID = models.ForeignKey('Auditee',on_delete=models.CASCADE)
	Status = models.IntegerField('StatusSubAuditee',blank=False,null=False, default=1)

	def __str__(self):
		return str(self.pk)		
