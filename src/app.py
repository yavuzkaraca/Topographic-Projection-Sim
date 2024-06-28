# app.py
from flask import Flask, render_template, request, redirect, url_for
import os

from matplotlib import pyplot as plt

from build import object_factory, config as cfg
import visualization as vz
from forms import ConfigForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/config', methods=['GET', 'POST'])
def configure():
    form = ConfigForm()
    if form.validate_on_submit():
        cfg.current_config = {
            cfg.SUBSTRATE_TYPE: form.SUBSTRATE_TYPE.data,
            cfg.ROWS: form.ROWS.data,
            cfg.COLS: form.COLS.data,
            cfg.GC_COUNT: form.GC_COUNT.data,
            cfg.GC_SIZE: form.GC_SIZE.data,
            cfg.STEP_SIZE: form.STEP_SIZE.data,
            cfg.STEP_NUM: form.STEP_AMOUNT.data,
            cfg.X_STEP_POSSIBILITY: form.X_STEP_POSSIBILITY.data,
            cfg.Y_STEP_POSSIBILITY: form.Y_STEP_POSSIBILITY.data,
            cfg.SIGMOID_STEEPNESS: form.SIGMOID_GAIN.data,
            cfg.SIGMOID_SHIFT: form.SIGMOID_SHIFT.data,
            cfg.SIGMA: form.SIGMA.data,
            cfg.FORCE: form.FORCE.data,
            cfg.FORWARD_SIG: form.FORWARD_SIG.data,
            cfg.REVERSE_SIG: form.REVERSE_SIG.data,
            cfg.FF_INTER: form.FF_INTER.data,
            cfg.FT_INTER: form.FT_INTER.data,
            cfg.ADAPTATION_ENABLED: form.ADAPTATION_ENABLED.data,
            cfg.ADAPTATION_MU: form.ADAPTATION_MU.data,
            cfg.ADAPTATION_LAMBDA: form.ADAPTATION_LAMBDA.data,
            cfg.ADAPTATION_HISTORY: form.ADAPTATION_HISTORY.data,
            'CUSTOM_FIRST': form.CUSTOM_FIRST.data,
            'CUSTOM_SECOND': form.CUSTOM_SECOND.data,
        }
        return redirect(url_for('index'))
    return render_template('config.html', form=form)


@app.route('/run_simulation', methods=['POST'])
def run_simulation():
    simulation = object_factory.build_default()
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

    return redirect(url_for('results'))


@app.route('/results')
def results():
    return render_template('results.html')


if __name__ == '__main__':
    app.run(debug=True)
