function searchCorp() {
    const corpCode = document.getElementById('corp_code').value;
    
    fetch(`/baro_info/${corpCode}`)
        .then(response => response.json())
        .then(data => {
            const resultDiv = document.getElementById('result');
            if (data.error) {
                resultDiv.innerHTML = `<p>${data.error}</p>`;
            } else {
                // Assuming data.corp_info is the data you need
                resultDiv.innerHTML = `<br>
                    <p>Corp Code: ${data.corp_code}</p>
                `;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('result').innerHTML = `<p>Something went wrong</p>`;
        });
}
