document.getElementById('text-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const text = document.getElementById('text-input').value;
    const loadingBar = document.getElementById('loading-bar');
    const resultsDiv = document.getElementById('results');
    resultsDiv.textContent = ''; // Clear previous results
    loadingBar.style.display = 'block';

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
        resultsDiv.innerHTML = `<span>Triggers:</span> ${result.triggers.join(', ')}`;
    } catch (error) {
        console.error('Error analyzing text:', error);
        resultsDiv.innerHTML = '<span>Error:</span> Unable to analyze text.';
    } finally {
        loadingBar.style.display = 'none';
    }
});