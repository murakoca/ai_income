#!/usr/bin/env python3
"""
AI Passive Income Suite
━━━━━━━━━━━━━━━━━━━━━━
A modular PyQt5 desktop app with Clean Architecture
covering all 20 AI-powered passive income streams.

Run:
    python main.py

Requires:
    pip install PyQt5
"""
import sys
import os

# Make project root importable regardless of CWD
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from data.repositories import JsonProjectRepository
from services.project_service import ProjectService
from ui.main_window import MainWindow


def main() -> int:
    app = QApplication(sys.argv)
    app.setApplicationName("AI Passive Income Suite")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("AIIncomeHub")

    # HiDPI
    if hasattr(Qt, "AA_EnableHighDpiScaling"):
        app.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    if hasattr(Qt, "AA_UseHighDpiPixmaps"):
        app.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app.setFont(QFont("Segoe UI", 10))

    # ── Dependency Injection ────────────────────────────────────────────
    # Data persists in ~/.ai_passive_income_suite/projects.json
    data_dir = os.path.join(os.path.expanduser("~"), ".ai_passive_income_suite")
    os.makedirs(data_dir, exist_ok=True)

    repository = JsonProjectRepository(data_dir)   # data layer
    service    = ProjectService(repository)          # service layer

    # ── Presentation Layer ──────────────────────────────────────────────
    window = MainWindow(service)
    window.show()

    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())
