from PySide6.QtCore import QObject, Slot
from PySide6.QtWidgets import QMessageBox


class Base(QObject):
    def __init__(self, dt) -> None:
        super().__init__(parent=None)
        self.detailed = 'Нет полного описания'
        if dt != '':
            self.detailed = dt


class ErrorMsg(Base):
    @Slot(str, str)
    def __init__(self, text, dt='Нет полного описания') -> None:
        super().__init__(dt)
        self.errorMessage = QMessageBox()
        self.errorMessage.setWindowTitle('Ошибка')
        self.errorMessage.setIcon(QMessageBox.Critical)
        self.errorMessage.setStandardButtons(QMessageBox.Ok)
        self.errorMessage.setInformativeText('Полный текст об ошибке')
        self.errorMessage.setText(text)
        self.errorMessage.setDetailedText(self.detailed)
        self.errorMessage.exec_()


class WarnMsg(Base):
    @Slot(str, str)
    def __init__(self, text, dt='Нет полного описания') -> None:
        super().__init__(dt)
        self.errorMessage = QMessageBox()
        self.errorMessage.setWindowTitle('Предупреждение')
        self.errorMessage.setIcon(QMessageBox.Warning)
        self.errorMessage.setStandardButtons(QMessageBox.Ok)
        self.errorMessage.setInformativeText('Полный текст об ошибке')
        self.errorMessage.setText(text)
        self.errorMessage.setDetailedText(self.detailed)
        self.errorMessage.exec_()


class OkMsg:
    @Slot(str)
    def __init__(self, text) -> None:
        self.okayMessage = QMessageBox()
        self.okayMessage.setWindowTitle('Успех')
        self.okayMessage.setStandardButtons(QMessageBox.Ok)
        self.okayMessage.setIcon(QMessageBox.Information)
        self.okayMessage.setText(text)
        self.okayMessage.exec_()
