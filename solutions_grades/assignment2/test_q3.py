from hw2_q3 import *
import inspect


class TestNeurons:

    def test_cell_id_in_neuron(self):
        assert 'neuron_id' in inspect.signature(Neuron.__init__).parameters

    def test_pyr_neuron_inherits_neuron(self):
        assert 'Neuron' in str(PyramidalNeuron.mro()[1])

    def test_potential_in_pyr(self):
        assert 'potential' in inspect.signature(PyramidalNeuron.__init__).parameters

    def test_synstr_in_pyr(self):
        assert 'synaptic_strength' in inspect.signature(PyramidalNeuron.__init__).parameters

    def test_fire_in_pyr(self):
        assert hasattr(PyramidalNeuron, 'fire')

    def test_neurons_in_network(self):
        assert 'neurons' in inspect.signature(NeuralNetwork.__init__).parameters

    def test_show_in_network(self):
        assert 'show_neural_network' in NeuralNetwork.__dict__

    def test_start_firing_in_network(self):
        assert 'start_firing' in NeuralNetwork.__dict__

    def test_inhibi_inherits_neuron(self):
        assert 'Neuron' in str(InhibitoryNeuron.mro()[1])

    def test_start_firing_accepts_only_neurons(self):
        """
        This test makes sure that your iterable of neurons only contains
        objects which inherited from the Neuron base class, and
        not other objects which incidentally have the "fire()" method.

        "BaseException" is the base class for all exceptions in
        Python, so the "except BaseException" clause literally catches
        all available exceptions in the Python world. If *some* error
        was raised, the tests succeeds. Else, it fails.
        """
        class NotACell:
            def __init__(self, neuron_id):
                self.neuron_id = neuron_id

            def fire(self):
                return True
        try:
            network = NeuralNetwork([NotACell('a'), NotACell('b'), NotACell('c')])
            network.start_firing()
        except BaseException:
            assert True
        else:
            assert False


if __name__ == '__main__':
    ttests = TestNeurons()
    methods = ["cell_id_in_neuron", "pyr_neuron_inherits_neuron",
    "potential_in_pyr", "synstr_in_pyr", "fire_in_pyr",
    "neurons_in_network", "show_in_network", "start_firing_in_network",
    "inhibi_inherits_neuron", "start_firing_accepts_only_neurons"]
    errors = []

    for method in methods:
        try:
            getattr(ttests, "test_" + method)()
        except AssertionError as e:
            errors.append(f"Failed when testing method 'test_{method}': {e}")

    if len(errors) > 0:
        print(errors)
    else:
        print("Tests pass successfully.")
