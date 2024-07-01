from flask import Flask, render_template, request, jsonify, Response
import os
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from build import object_factory, config as cfg
import visualization as vz

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/papers')
def papers():
    return "<h1>Papers Page</h1>"


@app.route('/default-configs')
def get_default_configs():
    return jsonify(cfg.default_configs)


@app.route('/simulation', methods=['GET', 'POST'])
def simulation():
    return render_template('index.html')


@app.route('/start_simulation', methods=['GET', 'POST'])
def start_simulation():
    form_data = request.form

    # Extract data from form and build configuration dictionary
    config_data = {
        cfg.SUBSTRATE_TYPE: form_data.get(cfg.SUBSTRATE_TYPE),
        cfg.ROWS: int(form_data.get(cfg.ROWS)),
        cfg.COLS: int(form_data.get(cfg.COLS)),
        cfg.GC_COUNT: int(form_data.get(cfg.GC_COUNT)),
        cfg.GC_SIZE: int(form_data.get(cfg.GC_SIZE)),
        cfg.STEP_SIZE: int(form_data.get(cfg.STEP_SIZE)),
        cfg.STEP_NUM: int(form_data.get(cfg.STEP_NUM)),
        cfg.X_STEP_POSSIBILITY: float(form_data.get(cfg.X_STEP_POSSIBILITY)),
        cfg.Y_STEP_POSSIBILITY: float(form_data.get(cfg.Y_STEP_POSSIBILITY)),
        cfg.SIGMOID_GAIN: float(form_data.get(cfg.SIGMOID_GAIN)),
        cfg.SIGMOID_SHIFT: float(form_data.get(cfg.SIGMOID_SHIFT)),
        cfg.SIGMA: float(form_data.get(cfg.SIGMA)),
        cfg.FORCE: form_data.get(cfg.FORCE) == 'on',
        cfg.FORWARD_SIG: form_data.get(cfg.FORWARD_SIG) == 'on',
        cfg.REVERSE_SIG: form_data.get(cfg.REVERSE_SIG) == 'on',
        cfg.FF_INTER: form_data.get(cfg.FF_INTER) == 'on',
        cfg.FT_INTER: form_data.get(cfg.FT_INTER) == 'on',
        cfg.ADAPTATION_ENABLED: form_data.get(cfg.ADAPTATION_ENABLED) == 'on',
        cfg.ADAPTATION_MU: float(form_data.get(cfg.ADAPTATION_MU)),
        cfg.ADAPTATION_LAMBDA: float(form_data.get(cfg.ADAPTATION_LAMBDA)),
        cfg.ADAPTATION_HISTORY: int(form_data.get(cfg.ADAPTATION_HISTORY))
    }

    # Build the simulation with the config
    simulation = object_factory.build_simulation(config_data)

    # Run the simulation
    results = simulation.run()

    # Return results as JSON (modify as needed)
    return jsonify(results)


@app.route('/plot')
def plot_png():
    # Assuming you have a way to create or obtain a Substrate object
    sim = object_factory.build_default()  # Replace with actual substrate creation
    fig = vz.visualize_substrate(sim.substrate)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/login')
def login():
    return "<h1>Login Page</h1>"


@app.route('/source-code')
def source_code():
    return "<h1>Source Code Page</h1>"


def setup_simulation():
    simulation = object_factory.build_default()
    vz.visualize_growth_cones(simulation.growth_cones)
    vz.visualize_substrate(simulation.substrate)
    vz.visualize_substrate_separately(simulation.substrate)


if __name__ == '__main__':
    app.run(debug=True)
