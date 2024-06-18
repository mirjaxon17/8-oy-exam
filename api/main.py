import secrets


# Генерация случайного секретного ключа длиной 64 символа (256 бит)
authjwt_secret_key = secrets.token_hex(32)
print(authjwt_secret_key)
