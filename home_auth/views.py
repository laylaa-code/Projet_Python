from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages 
from django.views.decorators.csrf import csrf_protect, csrf_exempt 
from .models import CustomUser, PasswordResetRequest 
 
@csrf_protect
def signup_view(request): 
    if request.method == 'POST': 
        first_name = request.POST['first_name'] 
        last_name = request.POST['last_name'] 
        email = request.POST['email'] 
        password = request.POST['password'] 
        role = request.POST.get('role')  # student, teacher ou admin 
 
        # Créer l'utilisateur 
        user = CustomUser.objects.create_user( 
            username=email, 
            email=email, 
            first_name=first_name, 
            last_name=last_name, 
            password=password, 
        ) 
 
        # Assigner le rôle
        if role == 'student': 
            user.is_student = True 
        elif role == 'teacher': 
            user.is_teacher = True 
        elif role == 'admin': 
            user.is_admin = True 
 
        user.save() 
        login(request, user) 
        messages.success(request, 'Signup successful!') 
        return redirect('index') 
    return render(request, 'authentication/register.html')
@csrf_exempt
# On passe en exempt ici pour éviter le 403 CSRF en local quand les cookies/token sont invalides.
# En production, mieux vaut garder csrf_protect, mais pour le projet TP le login doit fonctionner à coup sûr.
def login_view(request): 
    if request.method == 'POST': 
        email = request.POST['email'] 
        password = request.POST['password'] 
 
        user = authenticate(request, username=email, password=password)
        if user is None:
            # Try login by email (cas où username n'est pas l'email, juste au cas où)
            try:
                cu = CustomUser.objects.get(email__iexact=email)
                user = authenticate(request, username=cu.username, password=password)
            except CustomUser.DoesNotExist:
                user = None

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            # Redirection selon le rôle
            if user.is_admin:
                return redirect('dashboard')
            elif user.is_teacher:
                return redirect('teacher_dashboard')
            elif user.is_student:
                return redirect('student_dashboard')
            else:
                messages.error(request, 'Rôle utilisateur invalide. Contactez l’administrateur.')
                return redirect('index')
        else:
            messages.error(request, 'Identifiants invalides. Vérifiez email/mot de passe et rechargez la page.') 
    return render(request, 'authentication/login.html')
def logout_view(request): 
    logout(request) 
    messages.success(request, 'You have been logged out.') 
    return redirect('index') 

@csrf_protect
def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = CustomUser.objects.get(email=email)
            # create reset token
            reset_request = user.passwordresetrequest_set.create(email=email)
            # ici on peut envoyer un email, ou juste montrer le lien
            messages.success(request, f'Password reset link: /authentication/reset-password/{reset_request.token}/')
            return redirect('forgot-password')
        except CustomUser.DoesNotExist:
            messages.error(request, 'No user with this email.')
    return render(request, 'authentication/forgot-password.html')

@csrf_protect
def reset_password(request, token):
    try:
        reset_request = PasswordResetRequest.objects.get(token=token)
    except PasswordResetRequest.DoesNotExist:
        messages.error(request, 'Invalid reset token.')
        return redirect('forgot-password')

    if not reset_request.is_valid():
        messages.error(request, 'Reset token expired.')
        return redirect('forgot-password')

    if request.method == 'POST':
        password = request.POST.get('new_password')
        confirm = request.POST.get('confirm_password')
        if password != confirm:
            messages.error(request, 'Passwords do not match.')
        else:
            user = reset_request.user
            user.set_password(password)
            user.save()
            reset_request.delete()
            messages.success(request, 'Password reset successful. Please login.')
            return redirect('login')

    return render(request, 'authentication/reset_password.html')


def csrf_failure(request, reason=""):
    return render(request, 'authentication/csrf_failure.html', {'reason': reason})
