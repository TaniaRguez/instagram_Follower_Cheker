the explanation in Spanish is at the end

# Instagram Non-Followers Checker

This Python script allows you to log into your Instagram account and check which users you follow but do not follow you back. The script uses the `Instaloader` library to retrieve your followers and followees securely, without exposing your credentials.

## Features
- Secure login using `Instaloader`.
- Retrieves a list of users you follow and users who follow you.
- Outputs the list of users who don't follow you back.
- Designed to maintain user privacy by not storing credentials or session data unnecessarily.

## Prerequisites
To run this script, you need to have:
- Python 3.6 or above installed.
- The `Instaloader` library installed. You can install it via pip:

  ```bash
  pip install instaloader

--------------------------------------------------------------------

# How to Use?
1. Clone this repository or download the script.
   git clone https://github.com/TaniaRguez/instagram-non-followers-checker.git
2. Replace your_username and your_password in the script with your Instagram credentials.
3. Run the script:
    python instagram_non_followers_checker.py
4. The script will print a list of users that you follow but do not follow you back.

--------------------------------------------------------------------

# Error Handling
If you encounter an error that looks like this:
  LoginException: Login: Checkpoint required. Point your browser to /challenge/action/... - follow the instructions, then retry.

This is a security mechanism from Instagram. To resolve it:

1. Copy the URL provided in the error message and paste it into your browser "www.instagram.com/(paste here)".
2. Follow the instructions from Instagram to verify your login (this may involve confirming your identity via email or phone).
3. Once you've completed the verification, run the script again.

Other Common Issues
  - Rate Limiting: Instagram may limit the number of login attempts or requests. If this happens, wait a few minutes before trying again.
  - Invalid Credentials: Double-check your username and password if you receive a login error.
  - Session Expiration: The script does not store your session by default. You may need to log in again if your session expires.

-----------------------------------

# Privacy Notice
This script was created with user privacy in mind. It:
  - Does not store or log your Instagram credentials.
  - Uses Instagram's official mechanisms to log in securely.
  - Does not share your data with any third parties.
  - You can verify the source code to ensure that your credentials remain safe.



--------------------------------------------------------------------

ESPAÑOL:
# Lista de usuarios que no te siguen
Este script en Python te permite iniciar sesión en tu cuenta de Instagram y comprobar qué usuarios sigues pero no te siguen de vuelta. El script utiliza la librería Instaloader para obtener de forma segura la lista de tus seguidores y seguidos, sin exponer tus credenciales.

## Características
- Inicio de sesión seguro utilizando Instaloader.
- Recupera una lista de los usuarios que sigues y de los que te siguen.
- Muestra la lista de usuarios que no te siguen de vuelta.
- Diseñado para mantener la privacidad del usuario al no almacenar credenciales ni datos de sesión innecesariamente.


## Requisitos Previos
Para ejecutar este script, necesitas tener:
- Python 3.6 o superior instalado.
- La librería `Instaloader` instalada. Puedes instalarla mediante pip:
    ```bash
  pip install instaloader


--------------------------------------------------------------------

# ¿Cómo Usarlo?
1. Clona este repositorio o descarga el script
  git clone https://github.com/TaniaRguez/instagram-non-followers-checker.git
2. Reemplaza your_username y your_password en el script con tus credenciales de Instagram.
3. Ejecuta el script:
  python instagram_non_followers_checker.py

El script imprimirá una lista de usuarios que sigues pero que no te siguen de vuelta.

--------------------------------------------------------------------

# Manejo de Errores
Si te encuentras con un error que luce así:
  LoginException: Login: Checkpoint required. Point your browser to /challenge/action/... - follow the instructions, then retry.

Es debido a un mecanismo de seguridad de Instagram. Para resolverlo:
1. Copia la URL proporcionada en el mensaje de error y pégala en tu navegador "www.instagram.com/(pegar aquí)".
2. Sigue las instrucciones de Instagram para verificar tu inicio de sesión (esto puede incluir confirmar tu identidad a través de un correo electrónico o teléfono).
3. Una vez que hayas completado la verificación, ejecuta el script nuevamente.

--------------------------------------------------------------------

# Otros Problemas Comunes
- Limitación de Tasa (Rate Limiting): Instagram puede limitar la cantidad de intentos de inicio de sesión o solicitudes. Si esto sucede, espera unos minutos antes de intentarlo nuevamente.
- Credenciales Inválidas: Revisa tu nombre de usuario y contraseña si recibes un error de inicio de sesión.
- Expiración de Sesión: El script no almacena tu sesión por defecto. Es posible que necesites iniciar sesión nuevamente si tu sesión expira.

--------------------------------------------------------------------

# Aviso de Privacidad
Este script fue creado pensando en la privacidad del usuario. No:
- Almacena o registra tus credenciales de Instagram.
- Utiliza mecanismos oficiales de Instagram para iniciar sesión de forma segura.
- Comparte tus datos con terceros.
- Puedes verificar el código fuente para asegurarte de que tus credenciales permanecen seguras.


