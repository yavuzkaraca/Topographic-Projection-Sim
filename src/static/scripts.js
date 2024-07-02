let interval;

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
                            } else if (element.type === 'select-one') {
                                // Do nothing
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
document.getElementById('startSimulation').addEventListener('click', function() {
    const configForm = document.getElementById('configForm');
    const formData = new FormData(configForm);
    const config = Object.fromEntries(formData);

    // Manually fixing, fix later
    config.rows = "100";  // Replace with the actual value or fetch from an input field
    config.cols = "100";  // Replace with the actual value or fetch from an input field
    config.continuous_signal_start = "0.01"
    config.continuous_signal_end = "6.99"
    config.substrate_type = config.substrate_type.toLowerCase();

    // Convert specific fields to the appropriate types
    const typedConfig = convertTypes(config);

    interval = setInterval(function(){
      updateProgress();
    }, 100);

    fetch('/start_simulation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(typedConfig)
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'Simulation completed') {
            console.log("jsdfhjds") // Stop the interval when the simulation is completed
        }
    });
});


/**
 * Convert types based on field names
 * @param {Object} config - The configuration object with all string values
 * @returns {Object} - The configuration object with converted types
 */
function convertTypes(config) {
    const intFields = ['gc_count', 'gc_size', 'step_size', 'step_num', 'rows', 'cols', 'adaptation_history'];
    const floatFields = ['x_step_possibility', 'y_step_possibility', 'sigmoid_gain', 'sigmoid_shift', 'sigma', 'adaptation_mu', 'adaptation_lambda', 'continuous_signal_start', 'continuous_signal_end'];
    const boolFields = ['force', 'forward_sig', 'reverse_sig', 'ff_inter', 'ft_inter', 'adaptation_enabled'];

    for (let key in config) {
        if (intFields.includes(key)) {
            config[key] = parseInt(config[key], 10);
        } else if (floatFields.includes(key)) {
            config[key] = parseFloat(config[key]);
        } else if (boolFields.includes(key)) {
            config[key] = (config[key] === 'on' || config[key] === 'true');
        }
    }

    return config;
}



/**
 * Updates Progress Bar
 */
function updateProgress() {
    fetch('/progress')
    .then(response => response.json())
    .then(data => {
        console.log(data.progress)
        const progressBar = document.getElementById('progressBar');
        progressBar.style.width = data.progress + '%';
        progressBar.setAttribute('aria-valuenow', data.progress);
        progressBar.textContent = data.progress + '%';

        if (data.progress >= 100) {
            clearInterval(interval);
        }
    });
}


function visualizeResults(data) {
    // Placeholder for actual visualization logic
    document.getElementById('visualization').innerHTML = '<img src="/plot" alt="Simulation Result" style="width: 400px; height: auto;">';
}
