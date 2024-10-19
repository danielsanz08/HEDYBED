# myapp/context_processors.py
def user_profile_data(request):
    if request.user.is_authenticated:
        # Asegúrate de que 'profile_picture' es el campo correcto en tu modelo CustomUser
        return {
            'user_name': request.user.name,  
            'user_profile_picture': request.user.profile_picture.url if request.user.profile_picture else None
        }
    return {'user_name': None, 'user_profile_picture': None}
