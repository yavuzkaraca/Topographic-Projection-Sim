/**
 * Default config fetching
 */
document.addEventListener('DOMContentLoaded', function () {
    fetch('/default-configs')
        .then(response => response.json())
        .then(configs => {
            const substrateTypeElement = document.getElementById('substrateType');
            substrateTypeElement.addEventListener('change', function () {
                const selectedType = this.value;
                const config = configs[selectedType];
                if (config) {
                    for (const key in config) {
                        const element = document.querySelector(`[name=${key}]`);
                        if (element) {
                            if (element.type === 'checkbox') {
                                element.checked = config[key];
                            } else {
                                element.value = config[key];
                            }
                        }
                    }
                }
            });
            // Trigger change event on page load to set default values
            substrateTypeElement.dispatchEvent(new Event('change'));
        })
        .catch(error => console.error('Error fetching default configs:', error));
});

/**
 * Start Button
 */
document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('startSimulation').addEventListener('click', function () {
        const form = document.getElementById('configForm');
        const formData = new FormData(form);

        fetch('/simulation', {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                console.log('Simulation results:', data);
                document.getElementById('progressBar').style.width = '100%';
                document.getElementById('progressBar').innerText = '100%';
                document.getElementById('resultsSection').style.display = 'block';
                visualizeResults(data);
            })
            .catch(error => console.error('Error:', error));

        // Simulate progress update
        const progressBar = document.getElementById('progressBar');
        const resultsSection = document.getElementById('resultsSection');
        let progress = 0;

        const interval = setInterval(() => {
            progress += 10;
            progressBar.style.width = progress + '%';
            progressBar.innerHTML = progress + '%';
            if (progress >= 100) {
                clearInterval(interval);
                resultsSection.style.display = 'block';
            }
        }, 500);
    });
});


function visualizeResults(data) {
    // Placeholder for actual visualization logic
    document.getElementById('visualization').innerHTML = '<img src="/plot" alt="Simulation Result" style="width: 400px; height: auto;">';
}
