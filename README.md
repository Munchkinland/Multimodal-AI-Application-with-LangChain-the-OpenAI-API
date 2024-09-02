# Multimodal AI Application with LangChain and OpenAI API

<img width="427" alt="image" src="https://github.com/user-attachments/assets/aa46b398-76a7-4d7b-b5a6-e5e674467bbf">

## Descripción

Este proyecto es una aplicación de inteligencia artificial multimodal que utiliza la API de OpenAI para interactuar con transcripciones de videos de YouTube. Permite a los usuarios procesar videos de YouTube para obtener transcripciones y hacer preguntas sobre el contenido del video utilizando un chatbot. La aplicación también ofrece la funcionalidad para descargar tanto la transcripción y la posibilidad de implementar la descarga del audio del video. Ideal para estudiantes, investigadores y cualquier persona interesada en analizar videos de manera eficiente, esta aplicación transforma la manera en que se interactúa con contenido multimedia, haciendo el aprendizaje y la revisión mucho más accesibles y eficientes

## Características

- Descargar y transcribir videos de YouTube.
- Preguntar sobre el contenido del video usando un chatbot basado en OpenAI.
- Descargar la transcripción y el audio del video.
- Interfaz de usuario estilizada con un tema inspirado en los videojuegos retro.

## Instalación

1. **Clona el repositorio:**

    ```bash
    git clone https://github.com/Munchkinland/Multimodal-AI-Application-with-LangChain-the-OpenAI-API.git
    cd Multimodal-AI-Application-with-LangChain-the-OpenAI-API
    ```

2. **Crea y activa un entorno virtual:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. **Instala las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configura las variables de entorno:**

    Crea un archivo `.env` en el directorio raíz del proyecto con el siguiente contenido:

    ```makefile
    OPENAI_API_KEY=tu_clave_api_aqui
    ```

5. **Ejecuta la aplicación:**

    ```bash
    flask run
    ```

    La aplicación estará disponible en `http://127.0.0.1:5000/`.

## Uso

- **Sube un video de YouTube:**
  - Introduce la URL del video en el campo de texto y haz clic en "Enviar".
  - La aplicación descargará el video, generará una transcripción y te proporcionará enlaces para descargar la transcripción y el audio del video.

- **Haz preguntas sobre el video:**
  - Introduce una pregunta en el campo de texto y haz clic en "Preguntar".
  - La aplicación te responderá basándose en la transcripción del video.

## Estructura del Proyecto

- `app/`: Contiene la lógica principal de la aplicación.
  - `youtube_processor.py`: Maneja la descarga y transcripción de videos de YouTube.
  - `chatbot_handler.py`: Maneja las solicitudes al chatbot de OpenAI.
  - `main.py`: Define las rutas de la aplicación Flask.
- `templates/`: Contiene los archivos HTML.
- `static/`: Contiene los archivos estáticos, incluyendo CSS y JS.
- `requirements.txt`: Lista las dependencias del proyecto.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Forkea el repositorio.
2. Crea una rama para tu cambio (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Empuja tus cambios a tu fork (`git push origin feature/nueva-funcionalidad`).
5. Crea una solicitud de extracción (pull request) en GitHub.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
