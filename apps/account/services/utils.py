from django.core.mail import send_mail
def send_activate_code(activate_code: str, email: str):
    title = "hello it is activate link to your account in site SnakeShop"
    message = f"please click link for activate account http://127.0.0.1:8000/api/v1/account/activate/{activate_code}/"
    from_email = "SnakeShop@lalafo.kg"
    send_mail(
        title,
        message,
        from_email,
        [email],
        fail_silently=False,  # если фолс выведет ошибку при несуществующем эмейле
    )
def send_new_password(email, new_password):
    title = 'hello, it is reset your password account in site SnakeShop'
    message = f'hello, it is your new password: {new_password} on email: {email}'
    from_email = "SnakeShop@lalafo.kg"
    send_mail(
            title,
            message,
            from_email,
            [email],
            fail_silently=False,  # если фолс выведет ошибку при несуществующем эмейле
        )