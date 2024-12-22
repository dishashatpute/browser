import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navigation_bar
        navigation_bar = QToolBar()
        self.addToolBar(navigation_bar)

        back_button = QAction(' ⇦ ', self)
        back_button.triggered.connect(self.browser.back)
        navigation_bar.addAction(back_button)

        forward_button = QAction(' ⇨ ', self)
        forward_button.triggered.connect(self.browser.forward)
        navigation_bar.addAction(forward_button)

        reload_button = QAction(' ⟳ ', self)
        reload_button.triggered.connect(self.browser.reload)
        navigation_bar.addAction(reload_button)

        home_button = QAction(' ⌘ ', self)
        home_button.triggered.connect(self.navigate_home)
        navigation_bar.addAction(home_button)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navigation_bar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://Codewithmaddy.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

# Corrected: Use QApplication instead of QApp
app = QApplication(sys.argv)  # Initialize the application object
QApplication.setApplicationName("Disha,s Browser")  # Set the app name
window = MainWindow()
window.show()  # Show the main window
app.exec_()  # Start the event loop
