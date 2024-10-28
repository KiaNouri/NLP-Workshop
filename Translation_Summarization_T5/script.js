function submitForm(action) {
    const formData = new FormData();
    formData.append('inputText', document.getElementById('inputText').value);
    formData.append('sourceLanguage', document.getElementById('sourceLanguage').value);
    formData.append('targetLanguage', document.getElementById('targetLanguage').value);

    // alert("Button clicked: " + action);
    
    if (action === 'summarize' || action === 'translate_summary') {
        // console.log("this is the starting point")
        formData.append('summaryText', document.getElementById('summaryText').value);
    }

    fetch('http://127.0.0.1:5000/' + action, {
        method: 'POST',
        body: formData
    }).then(response => response.text()).then(data => {
        if (action === 'summarize') {
            document.getElementById('summaryText').value = data;
        } else if (action === 'translate_summary') {
            document.getElementById('translatedSummaryText').value = data;
        } else {
            document.getElementById('translatedText').value = data;
        }
    }).catch(error => {
        console.error("Error:", error);
        // alert("An error occurred. Check the console for details.");
    });

}