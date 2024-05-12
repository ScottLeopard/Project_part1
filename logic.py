from PyQt6.QtWidgets import *
from gui import *


def checkNones(lst: list) -> list:
    """
    makes a new list of only numbers
    :param lst: takes in a list or set
    :return: a list that has no values of None
    """
    scores = []
    for i in lst:
        if i is not None:
            scores += i
    return scores


class Logic(QMainWindow, Ui_Dialog):
    def __init__(self):
        """
        connects submit button and the num of scores box to appropriate functions
        """
        super().__init__()
        self.setupUi(self)
        self.num_attempts = None

        self.button_submit.clicked.connect(lambda: self.submit())
        self.input_attempts.textChanged.connect(self.attempts)

    def checkScore(self) -> None:
        """
        checks if there is a value for score 1
        :return: None
        """
        if self.input_score_1.text() is None:
            raise ValueError

    def submit(self) -> None:
        """
        uses other definitions when the 'Submit' button is clicked
        :return: None
        """
        try:
            out_file = open('grades.csv', 'a', newline='')
            lst = [self.input_score_1.text(), self.input_score_2.text(),
                   self.input_score_3.text(), self.input_score_4.text()]
            scores = checkNones(lst)
            wrt_state = self.add_scores(scores)
            out_file.write(wrt_state)
            out_file.close()
            self.checkName()
            self.clear()
        except ValueError:
            self.text_feedback.setText('The score(s) should be in between 0 and 100')
        except TypeError:
            self.text_feedback.setText('There should be a name')

    def checkName(self) -> None:
        """
        checks if student name is valid
        :return: None
        """
        if self.input_student.text() is None:
            raise TypeError

    def clear(self) -> None:
        """
        clears the texts
        :return: None
        """
        self.input_score_1.setText(None)
        self.input_score_2.setText(None)
        self.input_score_3.setText(None)
        self.input_score_4.setText(None)
        self.input_attempts.setText(None)
        self.input_student.setText(None)
        self.text_feedback.setText(None)

    def add_scores(self, scores: list) -> str:
        """
        averages the data for final score
        :param scores: a list of numbers/score inputs
        :return: string of all the data
        """
        total = 0
        for i in scores:
            print(i)
            if i is None:
                print('None')
                pass
            if 0 <= int(i) <= 100:
                print(i)
                total += int(i)
            else:
                raise ValueError
        return (f"{self.input_student.text()},{self.input_score_1.text()},{self.input_score_2.text()}"
                f",{self.input_score_3.text()}"
                f",{self.input_score_4.text()},{total / self.num_attempts * 100}\n")

    def invisible(self) -> None:
        """
        makes the score input boxes and label disappear
        :return: None
        """
        self.input_score_1.setVisible(False)
        self.text_score_1.setVisible(False)
        self.input_score_2.setVisible(False)
        self.text_score_2.setVisible(False)
        self.input_score_3.setVisible(False)
        self.text_score_3.setVisible(False)
        self.input_score_4.setVisible(False)
        self.text_score_4.setVisible(False)

    def attempts(self) -> None:
        """
        This is what makes the boxes appear as you type number of attempts
        :return: None
        """
        try:
            self.num_attempts = int(self.input_attempts.text())
            if 4 >= self.num_attempts >= 1:
                if self.num_attempts >= 4:
                    self.input_score_4.setVisible(True)
                    self.text_score_4.setVisible(True)
                else:
                    self.input_score_4.setText(None)
                if self.num_attempts >= 3:
                    self.input_score_3.setVisible(True)
                    self.text_score_3.setVisible(True)
                else:
                    self.input_score_3.setText(None)
                if self.num_attempts >= 2:
                    self.input_score_2.setVisible(True)
                    self.text_score_2.setVisible(True)
                else:
                    self.input_score_2.setText(None)
                if self.num_attempts >= 1:
                    self.input_score_1.setVisible(True)
                    self.text_score_1.setVisible(True)
            else:
                self.input_score_1.setText(None)
                self.input_score_2.setText(None)
                self.input_score_3.setText(None)
                self.input_score_4.setText(None)
                raise ValueError
        except ValueError:
            self.text_feedback.setText('For attempts: enter 1, 2, 3, or 4')
            self.invisible()
