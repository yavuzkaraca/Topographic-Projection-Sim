document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('substrateType').addEventListener('change', fetchDefaultConfig);
    fetchDefaultConfig(); // Fetch default config on page load
});

function fetchDefaultConfig() {
    const substrateType = document.getElementById('substrateType').value;

    fetch(`/get_default_config?substrate_type=${substrateType}`)
        .then(response => response.json())
        .then(config => {
            for (const key in config) {
                const element = document.getElementsByName(key)[0];
                if (element) {
                    element.value = config[key];
                }
            }
        });
}

document.getElementById('startSimulation').addEventListener('click', function() {
    const configForm = document.getElementById('configForm');
    const formData = new FormData(configForm);
    const config = Object.fromEntries(formData);

    fetch('/start_simulation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(config)
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'Simulation started') {
            updateProgress();
        }
    });
});

function updateProgress() {
    fetch('/progress')
    .then(response => response.json())
    .then(data => {
        const progressBar = document.getElementById('progressBar');
        progressBar.style.width = data.progress + '%';
        progressBar.setAttribute('aria-valuenow', data.progress);
        progressBar.textContent = data.progress + '%';

        if (data.progress < 100) {
            setTimeout(updateProgress, 1000);
        } else {
            showResults();
        }
    });
}

function showResults() {
    document.getElementById('resultsSection').style.display = 'block';
    document.getElementById('substrateImage').src = '/static/results/substrate.png';
    document.getElementById('substrateImage').style.display = 'block';
    document.getElementById('resultsImage').src = '/static/results/results.png';
    document.getElementById('resultsImage').style.display = 'block';
}
