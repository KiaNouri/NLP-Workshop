function submitForm(action) {
    const formData = new FormData();
    formData.append('inputText', document.getElementById('inputText').value);
    formData.append('sourceLanguage', document.getElementById('sourceLanguage').value);
    formData.append('targetLanguage', document.getElementById('targetLanguage').value);

    if (action === 'summarize' || action === 'translate_summary') {
        formData.append('summaryText', document.getElementById('summaryText').value);
    }

    fetch('http://127.0.0.1:5000/' + action, {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        console.log("Response data:", data); // Debugging log

        if (action === 'summarize') {
            document.getElementById('summaryText').value = data;
        } else if (action === 'translate_summary') {
            document.getElementById('translatedSummaryText').value = data;
        } else {
            document.getElementById('translatedText').value = data;
        }
    })
    .catch(error => {
        console.error("Error:", error); // Debugging log
        alert("An error occurred. Check the console for details.");
    });
}
