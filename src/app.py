from flask import Flask, render_template, request, jsonify
import threading
import time
from build.config import get_default_config
from flask import Flask, render_template, request, jsonify, Response
import os
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from build import object_factory, config as cfg
import visualization as vz

app = Flask(__name__)

# Placeholder for the progress of the simulation
progress = 0


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/papers')
def papers():
    return "<h1>Papers Page</h1>"


@app.route('/default-configs')
def get_default_configs():
    return jsonify(cfg.default_configs)


@app.route('/simulation')
def simulation():
    return render_template('index.html')


@app.route('/start_simulation', methods=['POST'])
def start_simulation():
    config = request.json
    thread = threading.Thread(target=run_simulation, args=(config,))
    thread.start()
    return jsonify({"status": "Simulation started"}), 202


@app.route('/progress', methods=['GET'])
def get_progress():
    global progress
    return jsonify({"progress": progress})


@app.route('/get_default_config', methods=['GET'])
def get_default_config_route():
    substrate_type = request.args.get('substrate_type')
    default_config = get_default_config(substrate_type)
    return jsonify(default_config)


def run_simulation(config):
    global progress
    from build.object_factory import build_simulation
    simulation = build_simulation(config)

    from visualization import visualize_substrate
    substrate_fig = visualize_substrate(simulation.substrate)
    substrate_fig.savefig('static/results/substrate.png')

    progress = 10

    total_steps = simulation.num_steps
    for step in range(total_steps):
        simulation.iterate_simulation()
        progress = int((step / total_steps) * 100)

    from visualization import visualize_growth_cones
    result_fig = visualize_growth_cones(simulation.growth_cones)
    result_fig.savefig('static/results/results.png')

    progress = 100


@app.route('/plot')
def plot_png():
    # Assuming you have a way to create or obtain a Substrate object
    sim = object_factory.build_default()  # Replace with actual substrate creation
    fig = vz.visualize_substrate(sim.substrate)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/plot/substrate')
def plot_substrate():
    """
    global current_simulation
    fig = vz.visualize_substrate(current_simulation.substrate)
    """
    sim = object_factory.build_default()  # Replace with actual substrate creation
    fig = vz.visualize_substrate(sim.substrate)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/plot/growth_cones')
def plot_growth_cones():
    sim = object_factory.build_default()  # Replace with actual substrate creation
    fig = vz.visualize_substrate(sim.substrate)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)
