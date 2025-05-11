from django.shortcuts import render, redirect
from WebAdmin.models import *
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user_role = "user"
        data = fd_user(
            fd_username = username,
            fd_email = email,
            fd_phone = phone,
            fd_password = password,
            fd_role = user_role
        )
        data.save()
        return render(request, 'login.html', {'message': 'User Registered Successfully!'})
    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == "POST":
        fd_email = request.POST.get('email')
        fd_password = request.POST.get('password')
        try:
            user = fd_user.objects.get(fd_email=fd_email)
            if user.fd_role == "user":
                if user.fd_password == fd_password:
                    request.session['email'] = fd_email
                    request.session['id']= user.id
                    request.session['role'] = user.fd_role
                    menus=fd_menu.objects.all()
                    if menus:
                        return render(request, 'user/home.html',{'menus':menus,'message': 'Login Successfull!', 'user':user})   
                    return render(request, 'user/home.html',{'message': 'Login Successfull!','user':user})
                else:
                    return render(request, 'login.html', {'message': 'Invalid Password!'})
            else:
                return render(request, 'login.html', {'message': 'Invalid Email!, Please Register First!'})
        except:
            user=tbl_canteen.objects.get(email=fd_email)
            if tbl_canteen.objects.get(email=fd_email).password == fd_password:
                request.session['email'] = fd_email
                request.session['role'] = "canteen"
                request.session['id']= user.id
                menus=fd_menu.objects.filter(user_id=user)
                if menus:
                    return render(request, 'canteen/view_menu.html',{'menus':menus,'message': 'Login Successfull!', 'user':user})   
                return render(request, 'canteen/home.html',{'message': 'Login Successfull!', 'user':user})
            else:
                return render(request, 'login.html', {'message': 'Invalid Password!'})
    return render(request, 'login.html')

def canteen(request):
    id = request.session['id']
    user=tbl_canteen.objects.get(id=id)
    menus=fd_menu.objects.filter(user_id=user)
    if menus:
        return render(request, 'canteen/home.html',{'menus':menus, 'user':user})   
def add_category(request):
    id = request.session['id']
    userid = tbl_canteen.objects.get(id=id)
    dt = fd_category.objects.filter(user_id=userid)
    if request.method == 'POST':
        category = request.POST.get('category')
        data = fd_category(
            user_id = userid,
            category = category
        )
        data.save()
       
        return render(request,'canteen/add_category.html',{'message':'Category Added Successfully!','categories':dt})
    else:
        return render(request,'canteen/add_category.html',{'categories':dt})


def delete_category(request):
    id = request.session['id']
    userid = tbl_canteen.objects.get(id=id)
    dt = fd_category.objects.filter(user_id=userid)
    if request.method == 'POST':
        fd_category_id = request.POST.get('category_id')
        data=fd_category.objects.get(id=fd_category_id)
        data.delete()
        return render(request,'canteen/add_category.html',{'message':'Category Deleted Successfully!','categories':dt})
    
def add_menu(request):
    id = request.session['id']
    userid = tbl_canteen.objects.get(id=id)
    dt = fd_category.objects.filter(user_id=userid)
    if request.method == 'POST':
        category_id = request.POST.get('category')
        category = fd_category.objects.get(id=category_id)
        item = request.POST.get('item')
        price = request.POST.get('price')
        description = request.POST.get('description')
        item_image = request.FILES['file']
        quantity = request.POST.get('quantity')
        diff = request.POST.get('diff')
        data = fd_menu(
            user_id = userid,
            category_id = category,
            item = item,
            price = price,
            description = description,
            image = item_image,
            quantity = quantity,
            diff = diff
        )
        data.save()
        df = fd_menu.objects.filter(user_id=userid)
        return render(request, 'canteen/view_menu.html',{'menus':df,'message':'Menu Added Successfully!'})
    return render(request, 'canteen/add_menu.html',{'categories':dt})

def view_menu(request):
    id = request.session['id']
    userid = tbl_canteen.objects.get(id=id)
    dt = fd_menu.objects.filter(user_id=userid)
    return render(request, 'canteen/view_menu.html',{'menus':dt})

def delete_menu(request):
    id = request.session['id']
    userid = tbl_canteen.objects.get(id=id)
    dt = fd_menu.objects.filter(user_id=userid)
    if request.method == 'POST':
        fd_menu_id = request.POST.get('id')
        data=fd_menu.objects.get(id=fd_menu_id)
        data.delete()
        return render(request,'canteen/view_menu.html',{'message':'Menu Deleted Successfully!','menus':dt})
def edit_menu(request):
    id = request.session['id']
    userid = tbl_canteen.objects.get(id=id)
    dt = fd_category.objects.filter(user_id=userid)
    if request.method == 'POST':
        fd_menu_id = request.POST.get('id')
        data = fd_menu.objects.get(id=fd_menu_id)
        return render(request,'canteen/edit_menu.html',{'menu':data,'categories':dt})
def update_menu(request):
    id = request.session['id']
    userid = tbl_canteen.objects.get(id=id)
    dt = fd_category.objects.filter(user_id=userid)
    if request.method == 'POST':
        fd_menu_id = request.POST.get('id')
        category_id = request.POST.get('category')
        category = fd_category.objects.get(id=category_id)
        item = request.POST.get('item')
        price = request.POST.get('price')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        diff = request.POST.get('diff')
        data = fd_menu.objects.get(id=fd_menu_id)
        data.category_id = category
        data.item = item
        data.price = price
        data.description = description
        data.quantity = quantity
        data.diff = diff
        data.save()
        df = fd_menu.objects.filter(user_id=userid)
        return render(request, 'canteen/view_menu.html',{'menus':df,'message':'Menu Updated Successfully!'})
    return render(request, 'canteen/edit_menu.html',{'categories':dt})
def search_menu(request):
    id = request.session['id']
    userid = tbl_canteen.objects.get(id=id)
    dt = fd_menu.objects.filter(user_id=userid)
    if request.method == 'POST':
        search = request.POST.get('search')
        data = fd_menu.objects.filter(item__contains=search)
        return render(request, 'canteen/view_menu.html',{'menus':data})
    return render(request, 'canteen/view_menu.html',{'menus':dt})


def logout(request):
    request.session.pop('email', None)
    return redirect('WebGuest:Logout')
    



def customer(request):
    id = request.session['id']
    user=fd_user.objects.get(id=id)
    menus=fd_menu.objects.all()
    return render(request, 'user/home.html',{'menus':menus, 'user':user})


def addtocart(request):
    id = request.session['id']
    user=fd_user.objects.get(id=id)
    place = tbl_place.objects.all()
    menu = fd_menu.objects.all()
    return render(request, 'user/addtocart.html',{'menus':menu,'user':user,'places':place})

def cus_search_menu(request):
    id = request.session['id']
    user=fd_user.objects.get(id=id)
    if request.method == 'POST':
        id_place = request.POST.get('place')
        place = tbl_place.objects.get(id=id_place)
        search = request.POST.get('search')
        canteen_id = tbl_canteen.objects.get(id=place.id)
        data = fd_menu.objects.filter(item__contains=search ,user_id=canteen_id)
        return render(request, 'user/addtocart.html',{'menus':data, 'user':user})
    menus=fd_menu.objects.all()
    return render(request, 'user/addtocart.html',{'menus':menus,'user':user})

def cart(request):
    id = request.session['id']
    user=fd_user.objects.get(id=id)
    if request.method == 'POST':
        menu_id = request.POST.get('id')
        menu = fd_menu.objects.get(id=menu_id)
        quantity = request.POST.get('quantity')
        data = fd_cart(
            user_id = user,
            menu_id = menu,
            quantity = quantity
        )
        data.save()
        cart = fd_cart.objects.filter(user_id=user)
        return render(request, 'user/cart.html',{'message':'Item Added to Cart Successfully!','user':user,'cart':cart})
    return render(request, 'user/addtocart.html',{'user':user})
def viewcart(request):
    id = request.session['id']
    user=fd_user.objects.get(id=id)
    cart = fd_cart.objects.filter(user_id=user)
    return render(request, 'user/cart.html',{'user':user,'cart':cart})

def buy(request):
    id = request.session['id']
    user=fd_user.objects.get(id=id)
    cart = fd_cart.objects.filter(user_id=user)
    total = 0
    for c in cart:
        total += c.menu_id.price * c.quantity
    return render(request, 'user/buy.html',{'user':user,'cart':cart,'total':total})

def delete_buy(request):
    id = request.session['id']
    user=fd_user.objects.get(id=id)
    cart = fd_cart.objects.filter(user_id=user)
    if request.method == 'POST':
        fd_cart_id = request.POST.get('id')
        print(fd_cart_id)
        data=fd_cart.objects.get(id=fd_cart_id)
        data.delete()
        return render(request,'user/cart.html',{'message':'Item Deleted Successfully!','user':user,'cart':cart})
    
def user_logout(request):
    request.session.pop('email', None)
    return redirect('WebGuest:Logout')