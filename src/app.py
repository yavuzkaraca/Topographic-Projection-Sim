from flask import Flask, render_template, request, jsonify
import os

from matplotlib import pyplot as plt

from build import object_factory, config as cfg
import visualization as vz
from forms import ConfigForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/papers')
def papers():
    return "<h1>Papers Page</h1>"


@app.route('/simulation', methods=['GET', 'POST'])
def simulation():
    form = ConfigForm()
    return render_template('index.html', form=form)


@app.route('/login')
def login():
    return "<h1>Login Page</h1>"


@app.route('/source-code')
def source_code():
    return "<h1>Source Code Page</h1>"




@app.route('/run_simulation', methods=['POST'])
def run_simulation():
    simulation = object_factory.build_default()
    total_steps = cfg.current_config[cfg.STEP_NUM]
    step_interval = 250

    # Simulate progress
    for step in range(0, total_steps, step_interval):
        if step % step_interval == 0:
            # Simulate some work
            print(f"Current Step: {step}")

    result = simulation.run()

    # Save visualization images
    if not os.path.exists('static'):
        os.makedirs('static')

    vz.visualize_growth_cones(simulation.growth_cones)
    plt.savefig('static/growth_cones.png')
    plt.close()

    vz.visualize_substrate(simulation.substrate)
    plt.savefig('static/substrate.png')
    plt.close()

    vz.visualize_substrate_separately(simulation.substrate)
    plt.savefig('static/substrate_separate.png')
    plt.close()

    vz.visualize_projection_linear(result, simulation.substrate)
    plt.savefig('static/projection_linear.png')
    plt.close()

    vz.visualize_results_on_substrate(result, simulation.substrate)
    plt.savefig('static/results_on_substrate.png')
    plt.close()

    vz.visualize_trajectory_on_substrate(result, simulation.substrate, simulation.growth_cones)
    plt.savefig('static/trajectory_on_substrate.png')
    plt.close()

    vz.visualize_trajectories(simulation.growth_cones)
    plt.savefig('static/trajectories.png')
    plt.close()

    return jsonify({'success': True})


if __name__ == '__main__':
    app.run(debug=True)
