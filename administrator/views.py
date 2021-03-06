from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from shop.forms import CustomUserCreationForm, ProfileForm, AdressForm, ModifyUserForm, ModifyProfileForm, ModifyProviderForm
from .forms import *
from .decorators import superuser_required
from django.contrib import messages
from .filters import UsuarioAdminFilter, BrandAdminFilter, CategoryFilter, SubCategoryFilter, AreaFilter
from django.core.paginator import Paginator

# Create your views here.

@superuser_required
def home(request):
    return render(request, 'administrator/home.html')


# CRUD USERS
@superuser_required
def users(request):
    users_filtered = UsuarioAdminFilter(request.GET, queryset=User.objects.select_related('persona').all())
    users = users_filtered.qs

    paginator = Paginator(users, 20)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    data = {
        'entity':page,
        'users_filtered':users_filtered
    }
    return render(request, 'administrator/user/list.html', data)

@superuser_required
def create_user(request):
    data = {
        'title': 'Crear usuario',
        'form': AdminUserForm(),
        'profile_form': ProfileForm(),
        'provider_form': ProviderForm(),
    }

    if request.method == 'POST':
        form = AdminUserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        provider_form = ProviderForm(data=request.POST)

        # verificamos si el checkbox de proveedor está checkeado
        is_provider = False
        if request.POST.get('is_provider') == "on":
            is_provider = True
        
        if is_provider:
            # si es proveedor y los datos son nulos, retornar mensaje error
            if request.POST.get('nombre_empresa')=='' or request.POST.get('id_rubro')=='':
                messages.error(request, "No se puede crear un proveedor con datos nulos")
                return redirect(to="admin_create_user")

            if form.is_valid() and profile_form.is_valid() and provider_form.is_valid():
                usuario = form.save()

                profile = profile_form.save(commit=False)
                profile.usuario = usuario
                profile.save()

                provider = provider_form.save(commit=False)
                provider.rut_persona = profile
                provider.save()

                messages.success(request, f"Usuario {usuario.username} creado correctamente")
                return redirect(to="admin_users")

        if not is_provider:
            if form.is_valid() and profile_form.is_valid():
                usuario = form.save()

                profile = profile_form.save(commit=False)
                profile.usuario = usuario
                profile.save()

                messages.success(request, f"Usuario {usuario.username} creado correctamente")
                return redirect(to="admin_users")
        data["form"] = form
        data["profile_form"] = profile_form
        data["provider_form"] = provider_form

    return render(request, 'administrator/user/create.html', data)

@superuser_required
def modify_user(request, id):
    user = get_object_or_404(User, id=id)

    if Persona.objects.filter(usuario=user).exists():
        profile = Persona.objects.get(usuario=user)
        instanced = True

        data = {
            'form': AdminModifyUserForm(instance=user),
            'profile_form': ModifyProfileForm(instance=profile),
        }      

    # si no existe, se crea un nuevo form de perfil
    if not Persona.objects.filter(usuario=user).exists():
        instanced = False
        data = {
            'form': AdminModifyUserForm(instance=user),
            'profile_form': ProfileForm()
        }   

    data['title'] = "Modificar usuario"


    try:
        provider = get_object_or_404(Proveedor, rut_persona=profile)
        data['provider_form'] = ProviderForm(instance=provider)
        instanced_provider = True
    except:
        data['provider_form'] = ProviderForm()
        instanced_provider = False


    if request.method == 'POST':
        form = AdminModifyUserForm(data=request.POST, instance=user)

        # si el perfil es instanciado, se actualiza, si no existe se crea
        if instanced:
            profile_form = ModifyProfileForm(data=request.POST, instance=profile)
        if not instanced:
            profile_form = ProfileForm(data=request.POST)

        # verificamos si el checkbox de proveedor está checkeado
        is_provider = False
        if request.POST.get('is_provider') == "on":
            is_provider = True

        if instanced_provider:
            provider_form = ProviderForm(data=request.POST, instance=provider)
        if not instanced_provider:
            provider_form = ProviderForm(data=request.POST)


        if is_provider:
            # si es proveedor y los datos son nulos, retornar mensaje error
            if request.POST.get('nombre_empresa')=='' or request.POST.get('id_rubro')=='':
                messages.error(request, "No se puede crear un proveedor con datos nulos")
                return render(request, 'administrator/user/create.html', data)

            if form.is_valid() and profile_form.is_valid() and provider_form.is_valid():
                usuario = form.save()

                profile = profile_form.save(commit=False)
                profile.usuario = usuario
                profile.save()

                provider = provider_form.save(commit=False)
                provider.rut_persona = profile
                provider.save()

                messages.success(request, f"Usuario {usuario.username} modificado correctamente")
                return redirect(to="admin_users")

        if not is_provider:
            if form.is_valid() and profile_form.is_valid():
                usuario = form.save()

                profile = profile_form.save(commit=False)
                profile.usuario = usuario
                profile.save()

                messages.success(request, f"Usuario {usuario.username} modificado correctamente")
                return redirect(to="admin_users")
        data["form"] = form
        data["profile_form"] = profile_form
        data["provider_form"] = provider_form
    return render(request, 'administrator/user/create.html', data)


# CRUD MARCAS
@superuser_required
def brands(request):
    brands_filtered = BrandAdminFilter(request.GET, queryset=Marca.objects.all())
    brands = brands_filtered.qs

    paginator = Paginator(brands, 20)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    data = {
        'entity':page,
        'brands_filtered':brands_filtered
    }
    return render(request, 'administrator/brand/list.html', data)

@superuser_required
def brand_create(request):
    data = {
        'form':BrandForm(),
        'title':'Crear nueva marca'
    }

    if request.method == 'POST':
        form = BrandForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Marca creada correctamente")
            return redirect(to="brands")
        data['form'] = form

    return render(request, 'administrator/brand/create.html', data)

@superuser_required
def brand_modify(request, id):
    brand = Marca.objects.get(id_marca=id)
    data = {
        'form':BrandForm(instance=brand),
        'title':'Modificar marca'
    }

    if request.method == 'POST':
        form = BrandForm(data=request.POST, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, "Marca modificada correctamente")
            return redirect(to="brands")
        data['form'] = form
    return render(request, 'administrator/brand/create.html', data)


# CRUD FAMILIA PRODUCTOS
@superuser_required
def categories(request):
    categories_filtered = CategoryFilter(request.GET, queryset=FamiliaProducto.objects.all())
    categories = categories_filtered.qs

    paginator = Paginator(categories, 20)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    data = {
        'entity':page,
        'categories_filtered':categories_filtered
    }
    return render(request, 'administrator/category/list.html', data)

@superuser_required
def category_create(request):
    data = {
        'form':CategoryAdminForm(),
        'title':'Crear nueva familia'
    }

    if request.method == 'POST':
        form = CategoryAdminForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Familia creada correctamente")
            return redirect(to="categories")
        data['form'] = form

    return render(request, 'administrator/category/create.html', data)

@superuser_required
def category_modify(request, id):
    category = FamiliaProducto.objects.get(id_familia_producto=id)
    data = {
        'form':CategoryAdminForm(instance=category),
        'title':'Modificar familia'
    }

    if request.method == 'POST':
        form = CategoryAdminForm(data=request.POST, instance=category, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Marca modificada correctamente")
            return redirect(to="categories")
        data['form'] = form
    return render(request, 'administrator/category/create.html', data)


# CRUD TIPO PRODUCTO
@superuser_required
def subcategories(request):
    subcategories_filtered = SubCategoryFilter(request.GET, queryset=TipoProducto.objects.all())
    subcategories = subcategories_filtered.qs

    paginator = Paginator(subcategories, 20)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    data = {
        'entity':page,
        'subcategories_filtered':subcategories_filtered
    }
    return render(request, 'administrator/subcategory/list.html', data)

@superuser_required
def subcategory_create(request):
    data = {
        'form':SubCategoryForm(),
        'title':'Crear nuevo tipo'
    }

    if request.method == 'POST':
        form = SubCategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tipo creado correctamente")
            return redirect(to="subcategories")
        data['form'] = form

    return render(request, 'administrator/subcategory/create.html', data)

@superuser_required
def subcategory_modify(request, id):
    subcategory = TipoProducto.objects.get(id_tipo_producto=id)
    data = {
        'form':SubCategoryForm(instance=subcategory),
        'title':'Modificar tipo'
    }

    if request.method == 'POST':
        form = SubCategoryForm(data=request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            messages.success(request, "Tipo modificado correctamente")
            return redirect(to="subcategories")
        data['form'] = form
    return render(request, 'administrator/subcategory/create.html', data)


# CRUD RUBRO PROVEEDOR
@superuser_required
def areas(request):
    areas_filtered = AreaFilter(request.GET, queryset=Rubro.objects.all())
    areas = areas_filtered.qs

    paginator = Paginator(areas, 20)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    data = {
        'entity':page,
        'areas_filtered':areas_filtered
    }
    return render(request, 'administrator/area/list.html', data)

@superuser_required
def area_create(request):
    data = {
        'form':AreaForm(),
        'title':'Crear nuevo rubro'
    }

    if request.method == 'POST':
        form = AreaForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Rubro creado correctamente")
            return redirect(to="areas")
        data['form'] = form

    return render(request, 'administrator/area/create.html', data)

@superuser_required
def area_modify(request, id):
    area = Rubro.objects.get(id_rubro=id)
    data = {
        'form':AreaForm(instance=area),
        'title':'Modificar rubro'
    }

    if request.method == 'POST':
        form = AreaForm(data=request.POST, instance=area)
        if form.is_valid():
            form.save()
            messages.success(request, "Rubro modificado correctamente")
            return redirect(to="areas")
        data['form'] = form
    return render(request, 'administrator/area/create.html', data)

# CRUD MOTIVOS CANCELACION COMPRA
@superuser_required
def motives(request):
    motives_filtered = AreaFilter(request.GET, queryset=Motivo.objects.all())
    motives = motives_filtered.qs

    paginator = Paginator(motives, 20)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    data = {
        'entity':page,
        'motives_filtered':motives_filtered
    }
    return render(request, 'administrator/motive/list.html', data)

@superuser_required
def motive_create(request):
    data = {
        'form':MotiveForm(),
        'title':'Crear nuevo motivo'
    }

    if request.method == 'POST':
        form = MotiveForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Motivo creado correctamente")
            return redirect(to="motives")
        data['form'] = form

    return render(request, 'administrator/motive/create.html', data)

@superuser_required
def motive_modify(request, id):
    motive = Motivo.objects.get(id_motivo=id)
    data = {
        'form':MotiveForm(instance=motive),
        'title':'Modificar motivo'
    }

    if request.method == 'POST':
        form = MotiveForm(data=request.POST, instance=motive)
        if form.is_valid():
            form.save()
            messages.success(request, "Motivo modificado correctamente")
            return redirect(to="motives")
        data['form'] = form
    return render(request, 'administrator/motive/create.html', data)