from typing import Union, Tuple

import pathlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class QuestionnaireAnalysis:
    """
    Reads and analyzes data generated by the questionnaire experiment.
    Should be able to accept strings and pathlib.Path objects.
    """

    def __init__(self, data_fname: Union[pathlib.Path, str]):
        try:
            self.data_fname = pathlib.Path(data_fname).resolve()
        except TypeError:
            print(
                "ERROR: Please supply a string or a pathlib.Path instance to the class."
            )
            raise
        if not self.data_fname.exists():
            raise ValueError(f"File {str(self.data_fname)} doesn't exist.")

    def read_data(self):
        """
        Reads the json data located in self.data_fname into memory, to
        the attribute self.data.
        """
        self.data = pd.read_json(self.data_fname)

    def show_age_distrib(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        Calculates and plots the age distribution of the participants.
        Returns a tuple containing two numpy arrays:
        The first item being the number of people in a given bin.
        The second item being the bin edges.
        """
        bins = np.linspace(0, 100, 11)
        fig, ax = plt.subplots()
        hist, edges, _ = ax.hist(self.data["age"], bins=bins)
        ax.set_xlabel("Age")
        ax.set_ylabel("Counts")
        ax.set_title("Age distribution across all subjects")
        return hist, edges

    def remove_rows_without_mail(self) -> pd.DataFrame:
        """
        Checks self.data for rows with invalid emails, and removes them.
        Returns the corrected DataFrame, i.e. the same table but with
        the erroneous rows removed and the (ordinal) index after a reset.
        """
        valid_email = self.data["email"].apply(lambda x: self._validate_email(x))
        return self.data.loc[valid_email].reset_index(drop=True)

    def _validate_email(self, email: str) -> bool:
        """ Checks if an email is valid """
        return (
            ("@" in email)
            and ("." in email)
            and (not email.endswith("."))
            and (not email.endswith("@"))
            and (not email.startswith("."))
            and (not email.startswith("@"))
            and (email.isascii())
            and (email.count("@") == 1)
            and (email[email.find("@") + 1] != ".")
        )

    def fill_na_with_mean(self) -> Tuple[pd.DataFrame, np.ndarray]:
        """
        Finds, in the original DataFrame, the subjects that didn't answer
        all questions, and replaces that missing value with the mean of the
        other grades for that student. Returns the corrected DataFrame,
        as well as the row indices of the students that their new grades
        were generated.
        """
        only_grades = self.data.loc[:, "q1":"q5"]
        corrected = (
            only_grades.stack()
            .unstack(0)
            .fillna(only_grades.mean(1))
            .stack()
            .unstack(0)
        )
        rows_with_nulls = only_grades.loc[
            only_grades.isna().any(axis=1)
        ].index.to_numpy()
        new_data = pd.concat([self.data.loc[:, :"last_name"], corrected], axis=1)
        return new_data, rows_with_nulls

    def correlate_gender_age(self) -> pd.DataFrame:
        """
        Looks for a correlation between the gender of the subject, their age
        and the score for all five questions.
        Returns a DataFrame with a MultiIndex containing the gender and whether
        the subject is above 40 years of age, and the average score in each of
        the five questions.
        """
        new_df = self.data.set_index(["gender", "age"], append=True)
        grps = new_df.groupby([None, lambda x: x > 40], level=[1, 2])
        return grps.mean().loc[:, "q1":"q5"]


if __name__ == "__main__":
    q = QuestionnaireAnalysis("data.json")
    q.read_data()
    df = q.correlate_gender_age()
    print(df)
