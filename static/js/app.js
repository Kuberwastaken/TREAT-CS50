document.getElementById('text-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const text = document.getElementById('text-input').value;

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: text })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        document.getElementById('results').innerText = `Triggers: ${result.triggers.join(', ')}`;
    } catch (error) {
        console.error('Error analyzing text:', error);
        document.getElementById('results').innerText = 'Error analyzing text.';
    }
});
