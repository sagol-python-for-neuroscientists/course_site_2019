# Homework Assignment #2

## Date: 18-03-2019
## Due date: 01-04-2019, 15:00

1. _The Bicycle Class:_
    * Write a definition for a class named ``Bicycle``:
        * It must contain the following attributes: `cadence`, `speed`, `gear`.
        * It must contain a `__str__` method which prints its state (like the ShoppingList in class).
        * The bicycle should be able speed up, brake, change gear and cadence. However, the `speed` attribute should be calculated from the two other attributes, since it depends directly
        on the pedal cadence and gear.
        * Write a `change_speed_to` method that increases\decreases the speed by changing the cadence and gear as necessary.
            - Note: You might want to add more methods to the class that will help you to implement this behavior.
            - The maximal speed of our bicycle should be 1000 KPH.
        * Make sure the bicycle can't reach a speed below 0 when breaking, or slow the pedal cadence below 0 rotations.
        * Our bicycle only has 7 gears, enforce this limit on the method that controls the change of gears.


2. _The Time Class:_
    * Define the `Time` class:
    ```python
    class Time:
        """
        Represents the time of the day.
        Attributes: hour, minute, second
        """
    ```
    * Give default values to the `__init__` function.
    * Validate that the input fits a 24 hour clock. Think of as many edge-cases as you can. If the input
    isn't valid reset that value to 0.
    * Override the `__str__` method so that when you print a Time instance it prints out nicely.
    * Define a `Time().is_after(other_time)` method. that returns `True` if the first `Time()` is later
    than the `other_time` instance, and `False` otherwise. `00:00:00` is the earliest, `23:59:59` is the latest.
    * Overload the `__add__` operator to allow the addition of two `Time` instances.
        - Make sure you deal with all possible cases - "overflow" of minutes
        and seconds, and that after `23:59:59` comes `00:00:00`.


3. _Basic API Design:_
    This question will deal with the concept of a basic API - application programming interface - for a "NeuralNetwork" class. This class represents a network of different types of neurons that may fire one after the other. The user should only deal with the methods available to this class, without "caring" which exact cells compose the network. In other words, the implementation of the network should be agnostic to the type, and order, of neurons it contains.

    * Define the `PyramidalNeuron` class:
    ```python
    class PyramidalNeuron(Neuron):
        """
        A very coarse model of a neuron.
        Mandatory attributes: neuron_id, potential, synaptic_strength
        Mandatory methods: fire  # fires a spike, raising the cell's electric potential.
        """
    ```
    * `PyramidalNeuron`s should inherit at least one attribute from a `Neuron` base class which you should define.
    * The `fire` method should only raise the cell's potential if a random number you roll is under the `synaptic_strength` value.
    * Write a NeuralNetwork class that models the connectivity of a given list of PyramidalNeuron instances.

    ```python
    class NeuralNetwork:
    """
    Models a neural network of types of Neuron instances.
    Mandatory attributes: neurons (iterable)
    """
    ```

    * Write a `show_neural_network` method for the `NeuralNetwork` class that prints out the 'connectivity' of the cells, i.e. which comes first, second, etc.
    * Write a `start_firing` method that orders the first cell to fire and tracks the firing inside
    the network. If the `fire` was successful, it should make the next cell in line try to fire.
    * Write another neuron class, this time `InhibitoryNeuron(Neuron)`. It should have similar features to the `PyramidalNeuron` we already have. On top of that, make it so when it does fire, it has an increased chance to fire a second spike. This second spike doesn't have to affect the rest of the network in any specific way, although it can.
    * Don't forget that it should also be able to integrate seamlessly into the NeuralNetwork.
    * Write an `if __name__ == '__main__'` block at the end of the question that build the network, shows its connectivity and starts firing.
    * Again - the goal is to separate the "user interface", i.e. the call to `NeuralNetwork.start_firing()` method, from the actual existing neurons.

    This question can be solved in numerous ways. I intentionally leave many details out for you to fill in, this is not a mistake. Rather, it's me asking you to think of the network you're creating and decide by yourself whether it "makes sense". I don't have a specific implementation I'm looking for, and thus I will not deduct points for doing things your way, as long as they show that you thought them over before implementing them.


## Submission:
This assignment and all others to follow will be submitted via GitHub Classroom, a special interface of GitHub which eases the creation of new, identical repositories for multiple students of the same class. Other than this convenience this repository is identical to ones you can create on your own.

As always, when you wish to answer the questions clone the repository to your computer and solve the exercise. Don't forget to commit your code once in a while, normally before and after major changes, like new functions or major bug fixes. You can also push your codebase to the online repo to back it up and\or to work on it from multiple workstations.

When you're done, push the code to the repo and verify that it indeed contains your latest updates. Right at the deadline a bot will read the contents of your repository, downloading the latest version of the code that's in there. It will then run the tests in the repo and assert that they all pass. Commits that occur after the deadline will not count.

### Tests
In the repo you can find test classes for the questions. These classes contain unit tests, and will determine your grade for these questions. Unit tests are a very common procedure when writing code, and should be a part of any script you write. The three unit test classes I added serve as a good example of how to write these (the tests themselves, not the machinery that runs them). It's more than likely that you won't understand _how_ exactly do all tests work - some are simple, but some are quite daunting. If one of the more "complicated" tests keeps failing and you're not sure what to do, please contact me.

Take note that the score for question 3 is not completely determined by the unit tests. They all must pass, but since it's an API design question, points can be deducted for not following the guidelines in the question - guidelines which are harder to enforce using unit tests.

#### Running the tests
The preferred way to run the tests is using `pytest`:
1. In the command line, `pip install pytest`.
2. Next, you can either write `pytest` in the command line when you're inside your code folder to run all tests automatically, or use VSCode's test runner. The test runner can be accessed from the bubbling beaker symbol - in it you should navigate to the folder with the tests and click the green "play" button to run them.
3. If you're unsuccessful, the test files can simply be run like any other Python script, either by right-clicking in the editor screen and choosing the "Run Python File In Terminal" option, or by typing `python test_q1.py` in the command line.

Good luck, and don't hesitate to contact me if Google doesn't solve your technical issues :)
