from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms
from django.contrib.auth.decorators import login_required


# ----------------------------
# Form
# ----------------------------
class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=False,
        help_text="Leave blank to keep existing password"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


# ----------------------------
# HOME
# ----------------------------
@login_required
def home(request):
    return redirect('user_list')


# ----------------------------
# LIST USERS
# ----------------------------
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {
        'users': users
    })


# ----------------------------
# CREATE USER
# ----------------------------
def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            # set password properly
            if form.cleaned_data.get('password'):
                user.set_password(form.cleaned_data['password'])

            user.save()
            messages.success(request, "User created successfully")
            return redirect('user_list')
    else:
        form = UserForm()

    return render(request, 'users/user_create.html', {
        'form': form
    })


# ----------------------------
# UPDATE USER
# ----------------------------
@login_required
def user_update(request, id):
    print("User:", request.user)
    print("Is Authenticated:", request.user.is_authenticated)
    print("Session Key:", request.session.session_key)
    user = get_object_or_404(User, id=id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)

            if form.cleaned_data.get('password'):
                user.set_password(form.cleaned_data['password'])

            user.save()
            messages.success(request, "User updated successfully")
            return redirect('user_list')
    else:
        form = UserForm(instance=user)

    return render(request, 'users/user_update.html', {
        'form': form,
        'user': user
    })

# ----------------------------
# DELETE USER
# ----------------------------
@login_required
def user_delete(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == 'POST':
        user.delete()
        messages.success(request, "User deleted successfully")
        return redirect('user_list')

    return render(request, 'users/user_confirm_delete.html', {
        'user': user
    })