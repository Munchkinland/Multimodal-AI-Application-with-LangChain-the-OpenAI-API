document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById("youtube-form");
    const submitButton = document.getElementById("submit-button");
    const spinner = document.getElementById("spinner");
    const transcriptText = document.getElementById("transcript-text");
    const downloadLink = document.getElementById("download-audio-link"); // Actualizado para usar el enlace de "Descargar Transcripción"
    let transcriptFilename = ''; // Variable para almacenar el nombre del archivo de la transcripción

    form.addEventListener("submit", function(event) {
        event.preventDefault(); // Evita el comportamiento por defecto del formulario

        const youtubeUrl = document.getElementById("youtube-url").value;

        // Deshabilitar el botón y mostrar el spinner
        submitButton.disabled = true;
        spinner.style.display = "block";
        transcriptText.textContent = ""; // Limpiar transcripción previa
        downloadLink.style.display = "none"; // Ocultar enlace de descarga de transcripción

        fetch("/process_video", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url: youtubeUrl }) // Enviar la URL del video
        })
        .then(response => response.json())
        .then(data => {
            if (data.transcript) {
                transcriptText.textContent = data.transcript;
                const blob = new Blob([data.transcript], { type: 'text/plain' });
                const url = URL.createObjectURL(blob);
                downloadLink.href = url;
                downloadLink.download = data.transcript_filename; // Usar el nombre del archivo de transcripción proporcionado
                downloadLink.style.display = "inline"; // Mostrar el enlace de descarga de transcripción

                // Almacenar el nombre del archivo de la transcripción para usarlo más tarde
                transcriptFilename = data.transcript_filename;
            }
        })
        .catch(error => {
            transcriptText.textContent = "Error: No se pudo procesar el video.";
            console.error("Error:", error);
        })
        .finally(() => {
            // Habilitar el botón y ocultar el spinner
            submitButton.disabled = false;
            spinner.style.display = "none";
        });
    });

    document.getElementById("ask-button").addEventListener("click", function() {
        const question = document.getElementById("user-question").value;

        fetch("/ask_question", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question: question, transcript_filename: transcriptFilename }) // Enviar la pregunta y el nombre del archivo de transcripción
        })
        .then(response => response.json())
        .then(data => {
            const chatOutput = document.getElementById("chat-output");
            chatOutput.innerHTML += `<p><strong>User:</strong> ${question}</p>`;
            chatOutput.innerHTML += `<p><strong>Bot:</strong> ${data.answer}</p>`;
        });
    });
});
