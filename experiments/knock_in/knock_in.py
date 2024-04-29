from matplotlib import pyplot as plt

from build.config import SUBSTRATE_TYPE, CONTINUOUS_GRADIENTS, CUSTOM_FIRST, CUSTOM_SECOND, ROWS, COLS, GC_COUNT, \
    GC_SIZE, STEP_SIZE, \
    STEP_AMOUNT, X_STEP_POSSIBILITY, Y_STEP_POSSIBILITY, SIGMA, FORCE, ADAPTATION_ENABLED, ADAPTATION_MU, \
    ADAPTATION_LAMBDA, ADAPTATION_HISTORY
from build import object_factory
import visualization.visualization as vz
import numpy as np


def knock_in():
    simulation = object_factory.build_simulation(KNOCK_IN_CONFIG)

    # mutate half of gcs
    mutation_factor = 2
    mutated_gc_indexes = np.random.choice(range(0, 49), size=25, replace=False)
    for idx in mutated_gc_indexes:  # TODO: move the mutation to the simulation
        simulation.growth_cones[idx].apply_knock_in_with_receptor(mutation_factor)

    visualize_mutation(simulation.growth_cones)

    result = simulation.run()

    vz.visualize_results_on_substrate(result, simulation.substrate)
    vz.visualize_colored_result(result, simulation.substrate, mutated_gc_indexes)


#  Config
KNOCK_IN_CONFIG = {
    SUBSTRATE_TYPE: CONTINUOUS_GRADIENTS,
    CUSTOM_FIRST: 0,
    CUSTOM_SECOND: 0,
    ROWS: 3,  # number of rows = max value along y-axis
    COLS: 56,  # number of cols = max value along x-axis
    GC_COUNT: 50,
    GC_SIZE: 8,
    STEP_SIZE: 1,
    STEP_AMOUNT: 10000,
    X_STEP_POSSIBILITY: 0.50,
    Y_STEP_POSSIBILITY: 0.50,
    SIGMA: 0.12,
    FORCE: False,
    ADAPTATION_ENABLED: False,
    ADAPTATION_MU: 0.01,  # 0.01
    ADAPTATION_LAMBDA: 0.0045,  # 0.0045
    ADAPTATION_HISTORY: 40  # 30
}


def visualize_mutation(gcs):
    receptors = np.array([gc.receptor_current for gc in gcs])
    ligands = np.array([gc.ligand_current for gc in gcs])
    plt.figure(figsize=(10, 6))
    plt.plot(receptors, 'o-', label='Receptors')
    plt.plot(ligands, 'o-', color='red', label='Ligands')
    plt.xlabel('Growth Cone ID (sorted along %n-t Axis of Retina)')
    plt.ylabel('Signal Value')
    plt.title('GCs after Mutation')
    plt.legend()
    plt.show()


def run():
    knock_in()


if __name__ == '__main__':
    run()
