from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from shop.forms import CustomUserCreationForm, ProfileForm, AdressForm, ModifyUserForm, ModifyProfileForm, ModifyProviderForm
from .forms import *
from django.contrib import messages
from .filters import UsuarioAdminFilter, BrandAdminFilter, CategoryFilter, SubCategoryFilter, AreaFilter

# Create your views here.
def home(request):
    return render(request, 'administrator/home.html')


def users(request):
    users = User.objects.select_related('persona').all()
    users_filtered = UsuarioAdminFilter(request.GET, queryset=users)
    users = users_filtered.qs

    data = {
        'users':users,
        'users_filtered':users_filtered
    }
    return render(request, 'administrator/user/list.html', data)


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

    data['title']: "Modificar usuario"


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
def brands(request):
    brands = Marca.objects.all()
    brands_filtered = BrandAdminFilter(request.GET, queryset=brands)
    brands = brands_filtered.qs
    data = {
        'brands':brands,
        'brands_filtered':brands_filtered
    }
    return render(request, 'administrator/brand/list.html', data)

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
def categories(request):
    categories = FamiliaProducto.objects.all()
    categories_filtered = CategoryFilter(request.GET, queryset=categories)
    categories = categories_filtered.qs
    data = {
        'categories':categories,
        'categories_filtered':categories_filtered
    }
    return render(request, 'administrator/category/list.html', data)

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
def subcategories(request):
    subcategories = TipoProducto.objects.all()
    subcategories_filtered = SubCategoryFilter(request.GET, queryset=subcategories)
    subcategories = subcategories_filtered.qs
    data = {
        'subcategories':subcategories,
        'subcategories_filtered':subcategories_filtered
    }
    return render(request, 'administrator/subcategory/list.html', data)

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
def areas(request):
    areas = Rubro.objects.all()
    areas_filtered = AreaFilter(request.GET, queryset=areas)
    areas = areas_filtered.qs
    data = {
        'areas':areas,
        'areas_filtered':areas_filtered
    }
    return render(request, 'administrator/area/list.html', data)

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