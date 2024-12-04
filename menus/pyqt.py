import sys
import io
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QVBoxLayout, QWidget, QLabel, QLineEdit, 
                             QMessageBox, QDialog, QHBoxLayout, QDesktopWidget,
                             QTextEdit)
from PyQt5.QtGui import QFont, QPalette, QColor, QClipboard
from PyQt5.QtCore import Qt

from base_interface import BaseInterface
from functionsapp.reg import Registration
from functionsapp.extract import Extract
from functionsapp.delete import Remover
from functionsapp.generator import Generatorpass
from config.config import locale
from locales.languages import Languages

class StyledButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """)

class PyQTInterface(BaseInterface):
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = QMainWindow()
        self.main_window.setWindowTitle('PassApp by sekal')
        self.main_window.setGeometry(100, 100, 400, 500)
        
        # Установка стиля
        self.app.setStyle('Fusion')
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        self.app.setPalette(palette)
        
        central_widget = QWidget()
        self.main_window.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Заголовок
        title = QLabel('PassApp by sekal')
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont('Arial', 16, QFont.Bold))
        layout.addWidget(title)
        
        buttons = [
            (Languages[locale['Choice']]['Registration'], self.open_registration),
            (Languages[locale['Choice']]['Extract'], self.open_extract),
            (Languages[locale['Choice']]['Delete'], self.open_delete),
            (Languages[locale['Choice']]['Generator'], self.open_generator)
        ]
        
        for text, method in buttons:
            btn = StyledButton(text)
            btn.clicked.connect(method)
            layout.addWidget(btn)
        
        # Центрирование окна
        frame_geometry = self.main_window.frameGeometry()
        screen_center = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(screen_center)
        self.main_window.move(frame_geometry.topLeft())

    def run(self):
        self.main_window.show()
        sys.exit(self.app.exec_())

    def open_registration(self):
        dialog = QDialog()
        dialog.setWindowTitle(Languages[locale['Choice']]['Servicename'])
        dialog.setStyleSheet("""
            QDialog { background-color: #2c2c2c; }
            QLabel { color: white; }
            QLineEdit { 
                background-color: #3c3f41; 
                color: white; 
                border: 1px solid #5a5a5a; 
                padding: 5px;
                border-radius: 3px;
            }
        """)
        layout = QVBoxLayout()
    
        service_label = QLabel(Languages[locale['Choice']]['Servicename'])
        service_input = QLineEdit()
        login_label = QLabel(Languages[locale['Choice']]['Logininput'])
        login_input = QLineEdit()
        password_label = QLabel(Languages[locale['Choice']]['Passwordinput'])
        password_input = QLineEdit()
        password_input.setEchoMode(QLineEdit.Password)
    
        submit_btn = StyledButton('Register')
        submit_btn.clicked.connect(lambda: self.register_action(
            service_input.text(), 
            login_input.text(), 
            password_input.text()
        ))
    
        layout.addWidget(service_label)
        layout.addWidget(service_input)
        layout.addWidget(login_label)
        layout.addWidget(login_input)
        layout.addWidget(password_label)
        layout.addWidget(password_input)
        layout.addWidget(submit_btn)
    
        dialog.setLayout(layout)
        dialog.exec_()

    def register_action(self, service, login, password):
        try:
            Registration(service, login, password)
            QMessageBox.information(None, 'Success', Languages[locale['Choice']]['Resultdata'])
        except Exception as e:
            QMessageBox.warning(None, 'Error', str(e))

    def open_extract(self):
        dialog = QDialog()
        dialog.setWindowTitle(Languages[locale['Choice']]['Extract'])
        dialog.setStyleSheet("""
            QDialog { background-color: #2c2c2c; }
            QTextEdit { 
                background-color: #3c3f41; 
                color: white; 
                border: 1px solid #5a5a5a; 
                padding: 5px;
                border-radius: 3px;
            }
        """)
        layout = QVBoxLayout()
        
        # Перенаправление stdout
        old_stdout = sys.stdout
        result = io.StringIO()
        sys.stdout = result
        
        Extract()
        
        sys.stdout = old_stdout
        extraction_result = result.getvalue()
        
        # Текстовое поле с возможностью копирования
        result_text = QTextEdit()
        result_text.setPlainText(extraction_result)
        result_text.setReadOnly(True)
        
        # Кнопка копирования
        copy_btn = StyledButton('Copy Data')
        copy_btn.clicked.connect(lambda: self.copy_to_clipboard(extraction_result))
        
        layout.addWidget(result_text)
        layout.addWidget(copy_btn)
        
        dialog.setLayout(layout)
        dialog.exec_()

    def open_delete(self):
        dialog = QDialog()
        dialog.setWindowTitle(Languages[locale['Choice']]['Delete'])
        dialog.setStyleSheet("""
            QDialog { background-color: #2c2c2c; }
            QLabel { color: white; }
            QLineEdit { 
                background-color: #3c3f41; 
                color: white; 
                border: 1px solid #5a5a5a; 
                padding: 5px;
                border-radius: 3px;
            }
        """)
        layout = QVBoxLayout()
        
        id_label = QLabel(Languages[locale['Choice']]['Idremove'])
        id_input = QLineEdit()
        
        submit_btn = StyledButton('Delete')
        submit_btn.clicked.connect(lambda: self.delete_action(id_input.text(), dialog))
        
        layout.addWidget(id_label)
        layout.addWidget(id_input)
        layout.addWidget(submit_btn)
        
        dialog.setLayout(layout)
        dialog.exec_()

    def delete_action(self, delete_id, dialog):
        try:
            Remover(delete_id)
            QMessageBox.information(None, 'Success', Languages[locale['Choice']]['Deleted'])
            dialog.accept()
        except Exception as e:
            QMessageBox.warning(None, 'Error', Languages[locale['Choice']]['Invalidinput'])

    def generate_action(self, length, specific, result_text):
        try:

            
            old_stdout = sys.stdout
            result = io.StringIO()
            sys.stdout = result
            
            Generatorpass(int(length), specific)
            
            sys.stdout = old_stdout
            generated_password = result.getvalue().strip()
            
            result_text.setPlainText(generated_password)
            
        except ValueError:
            QMessageBox.warning(None, 'Error', 'Некорректная длина пароля')
            result_text.clear()
        except Exception as e:
            QMessageBox.warning(None, 'Error', Languages[locale['Choice']]['Invalidinput'])
            result_text.clear()

    def open_generator(self):
        dialog = QDialog()
        dialog.setWindowTitle(Languages[locale['Choice']]['Generator'])
        dialog.setStyleSheet("""
        QDialog { background-color: #2c2c2c; }
        QLabel { color: white; }
        QLineEdit { 
            background-color: #3c3f41; 
            color: white; 
            border: 1px solid #5a5a5a; 
            padding: 5px;
            border-radius: 3px;
        }
    """)
        layout = QVBoxLayout()
    
        length_label = QLabel(Languages[locale['Choice']]['Lenghtpass'])
        length_input = QLineEdit()
    
        specific_label = QLabel(Languages[locale['Choice']]['Specifysymbols'])
        specific_input = QLineEdit()
    
    # Текстовое поле с возможностью копирования (как в extract)
        result_text = QTextEdit()
        result_text.setReadOnly(True)
    
        generate_btn = StyledButton('Generate')
        generate_btn.clicked.connect(lambda: self.generate_action(
        length_input.text(), 
        specific_input.text(), 
        result_text
    ))
    
        layout.addWidget(length_label)
        layout.addWidget(length_input)
        layout.addWidget(specific_label)
        layout.addWidget(specific_input)
        layout.addWidget(generate_btn)
        layout.addWidget(result_text)
        
        dialog.setLayout(layout)
        dialog.exec_()


    def copy_generated_password_from_dialog(self, dialog):
    # Находим label с паролем внутри диалога
        result_label = dialog.findChild(QLabel)
    
    # Извлекаем пароль
        if result_label and ': ' in result_label.text():
            password = result_label.text().split(': ')[-1]
        
            if password:
                clipboard = QApplication.clipboard()
                clipboard.setText(password)
                QMessageBox.information(None, 'Copied', 'Пароль скопирован в буфер обмена')
            else:
                QMessageBox.warning(None, 'Error', 'Нечего копировать')
        else:
            QMessageBox.warning(None, 'Error', 'Нечего копировать')

    def copy_to_clipboard(self, text):
        if text:
            clipboard = QApplication.clipboard()
            clipboard.setText(text)
            QMessageBox.information(None, 'Copied', 'Текст скопирован в буфер обмена')
        else:
            QMessageBox.warning(None, 'Error', 'Нечего копировать')

if __name__ == '__main__':
    PyQTInterface().run()