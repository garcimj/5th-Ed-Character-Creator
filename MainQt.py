# Using PyQt5 to run the character builder

import sys
from PyQt5 import QtCore, QtGui, uic, QtWidgets
import Classes_and_Subclasses
import Backgrounds
qtCreatorFile = "CharacterBuilder.ui"  # Enter file here.

# Helpful Links:
# https://doc.qt.io/qtforpython/PySide2/QtWidgets/QComboBox.html#PySide2.QtWidgets.PySide2.QtWidgets.QComboBox.activated


class MainWindowUIClass(QtWidgets.QMainWindow):

    proficiency = 2
    ui_objects = None

    def __init__(self):

        """
            Initializes the super class
            Guide: https://nitratine.net/blog/post/how-to-import-a-pyqt5-ui-file-in-a-python-gui/
        """
        super(MainWindowUIClass, self).__init__()
        ui_objects = uic.loadUi(qtCreatorFile, self)  # All ui objects will need to be referenced out of here.

        # Setup Skills
        self.athletics_radioButton = ui_objects.athletics_radioButton
        self.acrobatics_radioButton = ui_objects.acrobatics_radioButton
        self.animal_handling_radioButton = ui_objects.animalHandling_radioButton
        self.arcana_radioButton = ui_objects.arcana_radioButton
        self.deception_radioButton = ui_objects.deception_radioButton
        self.history_radioButton = ui_objects.history_radioButton
        self.intimidation_radioButton = ui_objects.intimidation_radioButton
        self.insight_radioButton = ui_objects.insight_radioButton
        self.investigation_radioButton = ui_objects.investigation_radioButton
        self.medicine_radioButton = ui_objects.medicine_radioButton
        self.nature_radioButton = ui_objects.nature_radioButton
        self.perception_radioButton = ui_objects.perception_radioButton
        self.performance_radioButton = ui_objects.performance_radioButton
        self.persuasion_radioButton = ui_objects.persuasion_radioButton
        self.religion_radioButton = ui_objects.religion_radioButton
        self.sleightofhand_radioButton = ui_objects.sleightofhand_radioButton
        self.stealth_radioButton = ui_objects.stealth_radioButton
        self.survival_radioButton = ui_objects.survival_radioButton

        self.connect_skills()

        self.athletics_lineEdit = ui_objects.athletics_lineEdit
        self.acrobatics_lineEdit = ui_objects.acrobatics_lineEdit
        self.animal_handling_lineEdit = ui_objects.animal_handling_lineEdit
        self.arcana_lineEdit = ui_objects.arcana_lineEdit
        self.deception_lineEdit = ui_objects.deception_lineEdit
        self.history_lineEdit = ui_objects.history_lineEdit
        self.intimidation_lineEdit = ui_objects.intimidation_lineEdit
        self.insight_lineEdit = ui_objects.insight_lineEdit
        self.investigation_lineEdit = ui_objects.investigation_lineEdit
        self.medicine_lineEdit = ui_objects.medicine_lineEdit
        self.nature_lineEdit = ui_objects.nature_lineEdit
        self.perception_lineEdit = ui_objects.perception_lineEdit
        self.performance_lineEdit = ui_objects.performance_lineEdit
        self.persuasion_lineEdit = ui_objects.persuasion_lineEdit
        self.religion_lineEdit = ui_objects.religion_lineEdit
        self.sleightofhand_lineEdit = ui_objects.sleightofhand_lineEdit
        self.stealth_lineEdit = ui_objects.stealth_lineEdit
        self.survival_lineEdit = ui_objects.survival_lineEdit
        # End Skill Setup
        # Begin Character Name
        self.character_name_box = ui_objects.character_name_box
        self.name = self.character_name_box.toPlainText()

        # Begin Classes
        self.class_combo_box = ui_objects.class_comboBox
        self.class_combo_box.addItems(Classes_and_Subclasses.available_classes)
        self.class_combo_box.currentIndexChanged.connect(self.update_subclass)
        # End Classes
        # Begin Subclasses
        self.subclass_combo_box = ui_objects.subclass_comboBox
        self.subclass_combo_box.addItems(Classes_and_Subclasses.subclass_dict[self.class_combo_box.currentText()])
        # End Subclasses
        # Begin Background
        self.background_combo_box = ui_objects.background_comboBox
        self.background_combo_box.addItems(Backgrounds.available_backgrounds)
        # End Background

        # Begin Proficiency
        self.character_level = ui_objects.characterlevel_spinBox
        self.character_level.valueChanged(self.update_proficiency)
        # End Proficiency
        # Begin update button
        self.update_push_button = ui_objects.update_pushButton
        # self.update_push_button.clicked.connect(self.update_character)
        self.show()
        self.calculate_skill()

    def calculate_skill(self):
        """
            This will calculate all of the appropriate selected skills
        :return: None, but will print to skills section what the bonus is
        """
        if self.athletics_radioButton.isChecked():
            self.athletics_lineEdit.setText("+{}".format(self.proficiency))
        else:
            self.athletics_lineEdit.setText("+{}".format(0))
        # end-if
        if self.acrobatics_radioButton.isChecked():
            self.acrobatics_lineEdit.setText("+{}".format(self.proficiency))
        else:
            self.acrobatics_lineEdit.setText("+{}".format(0))
        # end-if
        if self.animal_handling_radioButton.isChecked():
            self.animal_handling_lineEdit.setText("+{}".format(self.proficiency))
        else:
            self.animal_handling_lineEdit.setText("+{}".format(0))
        # end-if
        if self.arcana_radioButton.isChecked():
            self.arcana_lineEdit.setText("+{}".format(self.proficiency))
        else:
            self.arcana_lineEdit.setText("+{}".format(0))
        # end-if
        if self.deception_radioButton.isChecked():
            self.deception_lineEdit.setText("+{}".format(self.proficiency))
        else:
            self.deception_lineEdit.setText("+{}".format(0))
        # end-if
        if self.history_radioButton.isChecked():
            self.history_lineEdit.setText("+{}".format(self.proficiency))
        else:
            self.history_lineEdit.setText("+{}".format(0))
        # end-if
        if self.intimidation_radioButton.isChecked():
            self.intimidation_lineEdit.setText("+{}".format(self.proficiency))
        else:
            self.intimidation_lineEdit.setText("+{}".format(0))
        # end-if
        if self.insight_radioButton.isChecked():
            self.insight_lineEdit.setText("+{}".format(self.proficiency))
        else:
            self.insight_lineEdit.setText("+{}".format(0))
        # end-if
        if self.investigation_radioButton.isChecked():
            self.investigation_lineEdit.setText("+{}".format(self.proficiency))
        else:
            self.investigation_lineEdit.setText("+{}".format(0))
        # end-if
        if self.medicine_radioButton.isChecked():
            self.medicine_lineEdit.setText("+{}".format(self.proficiency))
        else:
            self.medicine_lineEdit.setText("+{}".format(0))
        # end-if
        if self.nature_radioButton.isChecked():
            self.nature_lineEdit.setText("+{}".format(self.proficiency))
        else:
            self.nature_lineEdit.setText("+{}".format(0))
        # end-if
        if self.perception_radioButton.isChecked():
            self.perception_lineEdit.setText("+{}".format(self.proficiency))
        else:
            self.perception_lineEdit.setText("+{}".format(0))
        # end-if
        if self.performance_radioButton.isChecked():
            self.performance_lineEdit.setText("+{}".format(self.proficiency))
        else:
            self.performance_lineEdit.setText("+{}".format(0))
        # end-if
        if self.persuasion_radioButton.isChecked():
            self.persuasion_lineEdit.setText("+{}".format(self.proficiency))
        else:
            self.persuasion_lineEdit.setText("+{}".format(0))
        # end-if
        if self.religion_radioButton.isChecked():
            self.religion_lineEdit.setText("+{}".format(self.proficiency))
        else:
            self.religion_lineEdit.setText("+{}".format(0))
        # end-if
        if self.sleightofhand_radioButton.isChecked():
            self.sleightofhand_lineEdit.setText("+{}".format(self.proficiency))
        else:
            self.sleightofhand_lineEdit.setText("+{}".format(0))
        # end-if
        if self.stealth_radioButton.isChecked():
            self.stealth_lineEdit.setText("+{}".format(self.proficiency))
        else:
            self.stealth_lineEdit.setText("+{}".format(0))
        # end-if
        if self.survival_radioButton.isChecked():
            self.survival_lineEdit.setText("+{}".format(self.proficiency))
        else:
            self.survival_lineEdit.setText("+{}".format(0))
        # end-if

    def connect_skills(self):
        """
            Simply connects all of the skills to their click events
        """
        self.athletics_radioButton.clicked.connect(self.calculate_skill)
        self.acrobatics_radioButton.clicked.connect(self.calculate_skill)
        self.animal_handling_radioButton.clicked.connect(self.calculate_skill)
        self.arcana_radioButton.clicked.connect(self.calculate_skill)
        self.deception_radioButton.clicked.connect(self.calculate_skill)
        self.history_radioButton.clicked.connect(self.calculate_skill)
        self.intimidation_radioButton.clicked.connect(self.calculate_skill)
        self.insight_radioButton.clicked.connect(self.calculate_skill)
        self.investigation_radioButton.clicked.connect(self.calculate_skill)
        self.medicine_radioButton.clicked.connect(self.calculate_skill)
        self.nature_radioButton.clicked.connect(self.calculate_skill)
        self.perception_radioButton.clicked.connect(self.calculate_skill)
        self.performance_radioButton.clicked.connect(self.calculate_skill)
        self.persuasion_radioButton.clicked.connect(self.calculate_skill)
        self.religion_radioButton.clicked.connect(self.calculate_skill)
        self.sleightofhand_radioButton.clicked.connect(self.calculate_skill)
        self.stealth_radioButton.clicked.connect(self.calculate_skill)
        self.survival_radioButton.clicked.connect(self.calculate_skill)

    def update_subclass(self):
        self.subclass_combo_box.clear()
        self.subclass_combo_box.addItems(Classes_and_Subclasses.subclass_dict[self.class_combo_box.currentText()])

    def update_proficiency(self):
        # TODO: Need to finish making the proficiency section, Does not currently exist in designer
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainWindowUIClass()
    sys.exit(app.exec_())




