from django.db import models
import Pentadbir,Urusetia


# Create your models here.
class RefStatusPenilaian(models.Model):
	StatusPenilaian = models.CharField('StatusPenilaian',max_length=50,blank=False,null=False)
	Keterangan = models.CharField('Keterangan',max_length=50,blank=False,null=False)
	Status = models.IntegerField('Status',blank=False,null=False, default=1)

	def __str__(self):
		return str(self.pk)

class Jadual(models.Model):
	Status = models.IntegerField('Status',blank=False,null=False, default=1)
	SesiID = models.ForeignKey('Urusetia.Sesi',on_delete=models.CASCADE)
	AuditeeID = models.ForeignKey('Urusetia.Auditee',on_delete=models.CASCADE)
	PenggunaID = models.ForeignKey('Pentadbir.Profil',on_delete=models.CASCADE)
	StatusPenilaianID = models.ForeignKey('RefStatusPenilaian',on_delete=models.CASCADE)
	CatatanID = models.ForeignKey('Catatan',on_delete=models.CASCADE)
	
	def __str__(self):
		return str(self.pk)


class AuditTrailJadual(models.Model):
	TarikhTransaksi = models.DateField('TarikhTransaksi',max_length=60,blank=False,null=False)
	Tindakan = models.CharField('Tindakan',max_length=50,blank=False,null=False)
	JadualID = models.ForeignKey('Jadual',on_delete=models.CASCADE)
	PenggunaID = models.ForeignKey('Pentadbir.Profil',on_delete=models.CASCADE)
	
	def __str__(self):
		return str(self.pk)


class Catatan(models.Model):
	Catatan = models.CharField('Catatan',max_length=50,blank=False,null=False)
	TarikhTransaksi = models.DateField('TarikhTransaksi',max_length=60,blank=False,null=False)
	Tindakan = models.IntegerField('Tindakan',blank=False,null=False, default=1)
	JadualID = models.ForeignKey('Jadual',on_delete=models.CASCADE)
	PenggunaID = models.ForeignKey('Pentadbir.Profil',on_delete=models.CASCADE)
	SubKomponenID = models.ForeignKey('Urusetia.SubKomponen',on_delete=models.CASCADE)

	def __str__(self):
		return str(self.pk)


class Attachment(models.Model):
	DeskripsiAttachment = models.CharField('DeskripsiAttachment',max_length=50,blank=False,null=False)
	Path = models.CharField('Path',max_length=50,blank=False,null=False)
	JenisKategoriID = models.ForeignKey('RefAttachment',on_delete=models.CASCADE)


	def __str__(self):
		return str(self.pk)



class RefAttachment(models.Model):
	JenisKategori = models.CharField('JenisKategori',max_length=50,blank=False,null=False)

	def __str__(self):
		return str(self.pk)		


class Penilaian(models.Model):
	Markah = models.FloatField('Markah',max_length=50,blank=False,null=False)
	TarikhPenilaian = models.DateField('TarikhPenilaian',max_length=60,blank=False,null=False)
	Catatan = models.CharField('Catatan',max_length=50,blank=False,null=False)
	SoalanID = models.ForeignKey('Urusetia.Soalan',on_delete=models.CASCADE)
	JadualID = models.ForeignKey('Jadual',on_delete=models.CASCADE)
	PenggunaID = models.ForeignKey('Pentadbir.Profil',on_delete=models.CASCADE)
	AttachmentID = models.ForeignKey('Attachment',on_delete=models.CASCADE)
	TambahanID = models.ForeignKey('Tambahan',on_delete=models.CASCADE)



	def __str__(self):
		return str(self.pk)


class Tambahan(models.Model):
	Catatan = models.CharField('Catatan',max_length=50,blank=False,null=False)
	AttachmentID = models.ForeignKey('Attachment',on_delete=models.CASCADE)
	SesiID = models.ForeignKey('Urusetia.Sesi',on_delete=models.CASCADE)


	def __str__(self):
		return str(self.pk)

class RefTambahan(models.Model):
	Keterangan = models.CharField('Catatan',max_length=50,blank=False,null=False)


	def __str__(self):
		return str(self.pk)


class Pantau(models.Model):
	PenggunaID = models.ForeignKey('Pentadbir.Profil',on_delete=models.CASCADE)
	AuditeeID = models.ForeignKey('Urusetia.Auditee',on_delete=models.CASCADE)

	def __str__(self):
		return str(self.pk)