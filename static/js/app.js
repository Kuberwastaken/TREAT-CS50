// Add an event listener for the form submission
document.getElementById('text-form').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent the default form submission behavior

    const text = document.getElementById('text-input').value; // Get the text input value
    const loadingBar = document.getElementById('loading-bar'); // Get the loading bar element
    const resultsDiv = document.getElementById('results'); // Get the results div element
    resultsDiv.textContent = ''; // Clear previous results
    loadingBar.style.display = 'block'; // Display the loading bar

    try {
        // Make a POST request to the server with the text input
        const response = await fetch('/upload', {
            method: 'POST', // Use the POST method
            headers: {
                'Content-Type': 'application/json' // Set the Content-Type header
            },
            body: JSON.stringify({ text: text }) // Convert the text to JSON and send it in the request body
        });

        // Check if the response is not ok (status code outside the range 200-299)
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`); // Throw an error with the status code
        }

        // Parse the JSON response from the server
        const result = await response.json();
        resultsDiv.innerHTML = `<span>Triggers:</span> ${result.triggers.join(', ')}`; // Display the triggers in the results div
    } catch (error) {
        // Handle any errors that occurred during the request
        console.error('Error analyzing text:', error); // Log the error to the console
        resultsDiv.innerHTML = '<span>Error:</span> Unable to analyze text.'; // Display an error message in the results div
    } finally {
        loadingBar.style.display = 'none'; // Hide the loading bar once the request is complete
    }
});
