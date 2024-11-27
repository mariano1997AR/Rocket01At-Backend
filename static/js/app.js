async function sendMessage() {
    const message = document.getElementById('entrada').value;
    const responseContainer = document.getElementById('response-container');

    // Enviar el mensaje al backend (Flask)
    const response = await fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message })
    });

    // Mostrar la respuesta
    const data = await response.json();
    const botResponse = data.response;

    responseContainer.innerHTML = `<b>Bot:</b> ${botResponse}`;
}