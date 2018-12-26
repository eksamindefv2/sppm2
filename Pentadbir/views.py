from django.shortcuts import render
from .models import Sistem, RefPeranan, Peranan
from .forms import SistemForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
import pyodbc
from django.http import JsonResponse # Modal form
from django.template.loader import render_to_string # Modal form

################ Django CRUD modal form #####################################################

# Senarai semua sistem
def sistem_list(request):
    a = Sistem.objects.all().order_by('NamaSistem')
    return render(request, 'Pentadbir/sistem_list.html', {'sistem': a})

# Simpan Form Generic
def save_sistem_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

# Cipta Sistem
def sistem_create(request):
    if request.method == 'POST':
        form = SistemForm(request.POST)
        msg = 'Sistem ' + request.POST.get('NamaSistem', None) + ' telah berjaya ditambah!'
        messages.success(request, msg)
    else:
        form = SistemForm()
    return save_sistem_form(request, form, 'Pentadbir/partial_sistem_create.html')

# Update Sistem 
def sistem_update(request, pk):
    sistem = get_object_or_404(Sistem, pk=pk)
    if request.method == 'POST':
        form = SistemForm(request.POST, instance=sistem)
        msg = 'Sistem ' + request.POST.get('NamaSistem', None)  +' telah berjaya dikemaskini!'
        messages.success(request, msg)
    else:
        form = SistemForm(instance=sistem)
    return save_sistem_form(request, form, 'Pentadbir/partial_sistem_update.html')

# Delete sistem
def sistem_delete(request, pk):
    sistem = get_object_or_404(Sistem, pk=pk)
    data = dict()
    if request.method == 'POST':
        msg = 'Sistem ' + str(sistem.NamaSistem) + ' telah berjaya dihapuskan!'
        messages.success(request, msg)
        sistem.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
    else:
        context = {'sistem': sistem}
        data['html_form'] = render_to_string('Pentadbir/partial_sistem_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

############################################################################################


################ Django CRUD ###############################################################
# Senarai sistem 
def sistemdj_list(request):
    a = Sistem.objects.all().order_by('NamaSistem')
    return render(request, 'Pentadbir/sistemdj_list.html', {'sistem': a})

# Cipta sistem
def sistemdj_create(request):
    if request.method == "POST":
        form = SistemForm(request.POST)
        if form.is_valid():
            sistem = form.save(commit=False)
            sistem.save()
            messages.success(request, 'Sistem ' + sistem.NamaSistem + ' berjaya ditambah!')
            return redirect(reverse_lazy('sistemdj_list'))
    else:
        form = SistemForm()
    return render(request, 'Pentadbir/sistemdj_create.html', {'form': form})

# Update sistem
def sistemdj_update(request,pk):
    sistem = get_object_or_404(Sistem,pk=pk)
    if request.method == "POST":
        form = SistemForm(request.POST,instance=sistem)
        if form.is_valid():
            sistem = form.save(commit=False)
            sistem.save()
            messages.success(request, 'Sistem ' + sistem.NamaSistem + ' berjaya dikemaskini!')
            return redirect(reverse_lazy('sistemdj_list'))
    else:
        form = SistemForm(instance=sistem)
    return render(request, 'Pentadbir/sistemdj_update.html', {'form': form})

# Hapus sistem
def sistemdj_delete(request,pk):
    sistem = get_object_or_404(Sistem,pk=pk)
    if request.method == "POST":
        if request.POST.get("submit_yes", ""):
            messages.success(request, 'Sistem ' + sistem.NamaSistem + ' telah berjaya dihapuskan!')
            sistem.delete()
            return redirect(reverse_lazy('sistemdj_list'))
    
    return render(request,'Pentadbir/confirm_delete_sistemdj.html',{ 'sistem' : sistem  } )


############################################################################################


def Landing_page(request):
    return render(request, 'Pentadbir/landing_page.html')


def DaftarPengguna(request):
    if request.method == "POST":


        # form = DaftarPerananForm(request.POST)
        # print (form.cleaned_data['carian'])
        # nokp = form['carian'].value()

        addperanan = request.POST['submit']
        nokp = request.POST.get('carian', None)
        posts = []

        # Carian IC
        if nokp:

            print(request.POST)


            # perananpengguna = Peranan.objects.all()

            cnxn = pyodbc.connect("Driver={SQL Server};"
                                  "Server=10.101.1.100;"
                                  "Database=MCDB;"
                                  "uid=sa;pwd=cdbdev@2017")
            # cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.101.1.100;DATABASE=MCDB;UID=sa;PWD=cdbdev@2017')
            cursor = cnxn.cursor()
            sql = "select ICNo,tp.nama, b.BUTitle as unit, c.BUTitle as bahagian, tp.KategoriJawatan from  MCDB.dbo.TblPersonel tp LEFT JOIN MCDB.dbo.TableBahagian b on REPLACE(REPLACE(tp.BUOrgChart,CHAR(13),''),CHAR(10),'')=REPLACE(REPLACE(b.BUOrgChart, Char(13),''),CHAR(10),'') LEFT JOIN MCDB.dbo.TableBahagian c on SUBSTRING(REPLACE(REPLACE(tp.BUOrgChart,CHAR(13),''),CHAR(10),''),1,7)+'0'= REPLACE(REPLACE(c.BUOrgChart,CHAR(13),''),CHAR(10),'') where tp.ICNo='" + str(
                nokp) + "'"
            cursor.execute(sql)
            # row_count = cursor.execute("select ICNo,tp.nama, b.BUTitle as unit, c.BUTitle as bahagian, tp.KategoriJawatan from  MCDB.dbo.TblPersonel tp LEFT JOIN MCDB.dbo.TableBahagian b on REPLACE(REPLACE(tp.BUOrgChart,CHAR(13),''),CHAR(10),'')=REPLACE(REPLACE(b.BUOrgChart, Char(13),''),CHAR(10),'') LEFT JOIN MCDB.dbo.TableBahagian c on SUBSTRING(REPLACE(REPLACE(tp.BUOrgChart,CHAR(13),''),CHAR(10),''),1,7)+'0'= REPLACE(REPLACE(c.BUOrgChart,CHAR(13),''),CHAR(10),'') where tp.ICNo='"+str(nokp)+"'")
            # cursor.execute("select * from [MCDB].[dbo].[TblPersonel] where ICNo='"+str(nokp)+"'")
            # row = cursor.fetchall()

            # print (row)
            # context = {"row":row}

            # print (nokp)



            for obj in cursor.fetchall():
                posts.append({"IC": obj[0], "Nama": obj[1], "Unit": obj[2],
                              "Bahagian": obj[3], "KategoriJawatan": obj[4]})

            if not posts:
                messages.error(request, 'Tiada Maklumat!')
        else:
            icno = request.POST.get('icno',None)
            fPeranan = request.POST.get('peranan',None)
            print(icno,fPeranan)

            # for row in cursor:
            #   print('row = %r' % (row,))
            #   print('row = %r' % (row,))
    else:
        # form = DaftarPerananForm()
        posts = []
    perananpengguna = RefPeranan.objects.all()
    sistem = Sistem.objects.all()
    senaraiPerananpengguna = Peranan.objects.all()
    print(perananpengguna)
    # return render(request, 'Pentadbir/daftar_pengguna.html',{'form':form,'row':row})
    return render(request, 'Pentadbir/daftar_pengguna.html', {'posts': posts, 'perananpengguna':perananpengguna,'senaraiPerananpengguna':senaraiPerananpengguna,'sistem':sistem})

def TambahPeranan(request):
    pass



