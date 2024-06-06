document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('predictionForm');
    form.addEventListener('submit', function (e) {
        e.preventDefault();
        const userInput = document.getElementById('textInput').value;

        fetch('/predict', {
            method: 'POST',
            body: JSON.stringify({ user_input: userInput }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').textContent = 'Prediction: ' + data.prediction;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
