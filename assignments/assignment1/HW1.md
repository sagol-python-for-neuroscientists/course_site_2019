# Homework Assignment, 04-03-2019
## Due date: 11-03-2019, 15:00

1. _Three consecutive double-letter words:_ Write a program that receives a word
and checks whether it has three consecutive pairs of identical letters in it.
For example:
    - `'aabbcc'` returns `True`
    - `'abccddee0123'` returns `True`
    - `'llkkbmm'` returns `False`
    - `'aaaazz'` returns `True`
    - `'bbcCdd'` returns `False`
    - The empty string `''` returns `False`

    Function signature:
    ```python
    def trifeca(word):
        """
        Checks whether word contains three consecutive double-letter pairs.
        word: string
        returns: bool
        """
    ```

2. _Palindrome madness:_ A palindrome is a sequence that can be read both ways
(left to right, right to left) and have the same value, for example `1441`, or `2`.
Write a function that tests all 6 digit numbers (from 100000 to 999999, 000003 doesn't count) and finds the ones that satisfy the following conditions:
    - The first number has a palindrome in its last 4 digits.
    - After adding 1, the result has a palindrome in its last 5 digts.
    - Another addition of 1 results in a palindrome in the middle 4 digits.
    - A final addition of 1 results in a 6-digit palindrome.

    The main function's signature:
    ```python
    def check_palindrome():
       """
       Runs through all 6-digit numbers and checks the mentioned conditions.
       The function prints out the numbers that satisfy this condition.

       Note: It should print out the first number (with a palindrome in its last 4 digits),
       not all 4 "versions" of it.
       """
    ```
    Hints:
    * You'll need at least one more function that does the actual testing.
    * The modulus operator `%` might be useful. But there are other, perhaps better options,
      to solve this question without it.


3. _Book-keeping:_ Teachers keep a record of the names of their students alongside their scores in the first and second
exams of the semester. The principle wishes to compare the grades of a single student in two different subjects, to see where student
has the highest grade.

    Write a program that compares the highest grade, for each student, in the two subjects. The program should print a "table" with the
student's name and the higher-graded subject. The table should be some data structure which is returned from the function.

    For example: In Maths, Jack received 80 in his first test and 85 in his second. In History, Jack received 75 and 95. The program
print out Jack's name alogside his better subject - History.


    ```python
    def compare_subjects_within_student(subj1_all_students,
                                        subj2_all_students):
        """
        Compare the two subjects with their students and print out the "preferred"
        subject for each student. Single-subject students shouldn't be printed.

        Choice for the data structure of the function's arguments is up to you.
        Returns a data structure with the name of the student and the
        corresponding subject.
        """
    ```

    Hints:
    * Think carefully of the data structures you're using to keep the data. After you decide on it, create mock data for yourself -
    at least four students in each subject.
    * Not all students participate in all subjects. These students should be left out of the printout.

Notes:

- When functions require input, you should be the one simulating it. For example,
if a function requires a list, please submit the HW with a mock list already in place.

- Follow closely the instructions on `SubmissionGuidelines.md` - your HW is automatically checked and graded, and my bot lacks empathy.

- If you have any Pythonic and \ or technical difficulties don't hesitate to contact me.

## Submission

The submission guidelines for this exercise are unique, and should also serve as a learning experience on how to work with version control and GitHub.

Version control is explained in the second class, which is already online, so I won't go into the "why?"
aspect of it, and we'll just plunge right in.

1. Install `git` as described in `SetupPython.md`, task #2.
1. Create a new [GitHub.com](https://github.com) user (or use an existing one).
2. Create a new repository. Name it. At the bottom of the page choose a Python `.gitignore` file.
The `.gitignore` file specifies the files that are ignored, i.e. _not_ under version control.
4. The page you arrived at is the homepage of your repository. All code you write will
one day be shown there. You can create new files directly from this web interface,
and edit them online as you like.
5. However, a better option is to connect this repository (repo) to a folder in your computer, and this is what you'll do next.
This folder can push (_from_ local folder _to_ web) and pull (_from_ web _to_ local folder) data to and from this interface,
allowing you to work offline with your own preferred editor.
5. To do so, you can either use the command line or use dedicated software:
    - Basic git command line tool can be installed from [here](https://git-scm.com/downloads).
    - GitHub Desktop.
    - GitKraken.
    - VS Code Git integration (preferred).
    Class 2 includes instructions how to work with the command line interface, and the installation instructions
    can be found in `PythonSetup.md` in the course's website. However, working with the VS Code GUI should be simpler and more intuitive, as I'll show below.
6. The operation we wish to perform is to `clone` the repo to your computer.
A `clone` operation requires a URL of the respective repo. You can obtain it by clicking the
__Clone or download__ button on the right side of your web repo. Copy the link (the one ending with `.git`). Open VS Code and press `Ctrl[Cmd] + Shift + P` and type `Git: Clone`. Paste the URL to the address bar and choose a folder. Click "Open Repository" to open VS Code inside that folder. This operation "cloned" the online repo and created a copy of it in your computer. You should find inside that folder the `.gitignore` file you created.
8. Now you can create new files inside this folder with your answers to the HW assignment. When you're happy with the changes you've made, you can commit the change. Again, the instructions are in the class, but what you should generally do is go to the Git symbol on the left bar (fork-looking), highlight the "Changes" row and choose "Stage All Changes". Then you can press the "V" icon on the top and commit the changes to the git tree. VS Code (and git) will request a message describing the changes you've made in your last commit, like "added function x" or "HW is complete".
9. You're now ready to push the changes to the online repo. Click the three dots and select "Push". Enter your credentials and the files should momentarily appear online.
9. Finally, the HW should be submitted by sending Hagai by mail (hagaihargil@protonmail.com)
a link to your online repo, containing the final commit of the code you wrote.
    - The commit should be pushed to GitHub.com, making it publicly available.
    - The commit should be __pushed to the repo before the exercise's due date.__
    - As expected, code should compile and run out-of-the-box.

10. Other assignments will be submitted using slightly different GitHub.com tools, to help you familiarize yourself with its interface.

