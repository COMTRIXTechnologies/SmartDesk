
import sys
import time
import ctypes
from pathlib import Path

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QSettings
from PySide6.QtGui import QIcon

from app.activation.activation_window import ActivationWindow
from app.authentication.signup import SignupWindow
from app.authentication.login import LoginWindow
from app.onboarding.business_setup import BusinessSetupWindow
from app.main_window import MainWindow

from database.database import initialize_database, SessionLocal
from database.models import User, Business


SESSION_DURATION = 24 * 60 * 60

APP_ID = "COMTRIX.Technologies.SmartDesk"


def save_login_session(settings, user_id):

    settings.setValue("session/user_id", user_id)

    settings.setValue(
        "session/expires_at",
        time.time() + SESSION_DURATION
    )

    settings.sync()


def clear_login_session(settings):

    settings.remove("session/user_id")
    settings.remove("session/expires_at")

    settings.sync()


def get_valid_session_user(settings):

    user_id = settings.value(
        "session/user_id",
        0,
        type=int
    )

    expires_at = settings.value(
        "session/expires_at",
        0.0,
        type=float
    )

    if not user_id or not expires_at:
        clear_login_session(settings)
        return None

    if time.time() >= expires_at:
        clear_login_session(settings)
        return None

    session = SessionLocal()

    try:
        user = session.query(User).filter_by(
            id=user_id
        ).first()

        if user is None:
            clear_login_session(settings)
            return None

        return user.id

    finally:
        session.close()


def setup_business(user_id):

    session = SessionLocal()

    try:
        business = session.query(Business).filter_by(
            owner_id=user_id
        ).first()

        business_exists = business is not None

    finally:
        session.close()

    if business_exists:
        return True

    business_setup = BusinessSetupWindow(user_id)

    return (
        business_setup.exec()
        == BusinessSetupWindow.DialogCode.Accepted
    )


def main():

    # SET WINDOWS APPLICATION ID
    if sys.platform == "win32":

        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            APP_ID
        )

    # CREATE APPLICATION
    app = QApplication(sys.argv)

    app.setApplicationName("COMTRIX SmartDesk")
    app.setOrganizationName("COMTRIX Technologies")

    # LOAD APPLICATION ICON
    project_folder = Path(__file__).resolve().parent
    icon_path = project_folder / "icon.ico"

    if icon_path.exists():

        app_icon = QIcon(str(icon_path))

        if not app_icon.isNull():
            app.setWindowIcon(app_icon)
        else:
            print("ERROR: Invalid application icon:", icon_path)

    else:
        print("ERROR: Application icon not found:", icon_path)

    # INITIALISE DATABASE
    initialize_database()

    settings = QSettings(
        "COMTRIX Technologies",
        "SmartDesk"
    )

    # STEP 1: PRODUCT ACTIVATION

    is_activated = settings.value(
        "product/activated",
        False,
        type=bool
    )

    if not is_activated:

        activation_window = ActivationWindow()

        if (
            activation_window.exec()
            != ActivationWindow.DialogCode.Accepted
        ):
            return 0

        settings.setValue("product/activated", True)
        settings.sync()

    # STEP 2: FIND OR CREATE OWNER ACCOUNT

    session = SessionLocal()

    try:
        user_exists = (
            session.query(User)
            .order_by(User.id)
            .first()
        )

    finally:
        session.close()

    if user_exists is None:

        # FIRST-TIME SIGNUP

        signup_window = SignupWindow()

        if (
            signup_window.exec()
            != SignupWindow.DialogCode.Accepted
        ):
            return 0

        user_id = signup_window.user_id

        save_login_session(settings, user_id)

    else:

        # CHECK EXISTING 24-HOUR SESSION

        user_id = get_valid_session_user(settings)

        if user_id is None:

            # REQUIRE LOGIN

            login_window = LoginWindow()

            if (
                login_window.exec()
                != LoginWindow.DialogCode.Accepted
            ):
                return 0

            user_id = login_window.user_id

            save_login_session(settings, user_id)

    # STEP 3: BUSINESS SETUP

    if not setup_business(user_id):
        return 0

    # STEP 4: OPEN MAIN WORKSPACE

    current_window = {"window": None}

    def open_workspace(user_id):

        window = MainWindow(user_id)

        window.session_ended.connect(
            handle_session_ended
        )

        current_window["window"] = window

        window.show()

    def handle_session_ended():

        # REQUIRE LOGIN AGAIN

        login_window = LoginWindow()

        if (
            login_window.exec()
            != LoginWindow.DialogCode.Accepted
        ):
            app.quit()
            return

        new_user_id = login_window.user_id

        save_login_session(settings, new_user_id)

        if not setup_business(new_user_id):
            app.quit()
            return

        open_workspace(new_user_id)

    open_workspace(user_id)

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
