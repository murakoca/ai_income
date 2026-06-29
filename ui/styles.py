"""
Global QSS dark theme — GitHub-inspired palette.
"""

STYLE = """
/* ── Base ─────────────────────────────────────────────────────────────── */
QMainWindow, QWidget {
    background-color: #0d1117;
    color: #c9d1d9;
    font-family: "Segoe UI", "SF Pro Display", Arial, sans-serif;
    font-size: 13px;
}

/* ── Sidebar ──────────────────────────────────────────────────────────── */
#sidebar {
    background-color: #161b22;
    border-right: 1px solid #30363d;
}

#sidebar_logo {
    background-color: #0d1117;
    border-bottom: 1px solid #30363d;
    padding: 4px;
}

#logo_title {
    color: #58a6ff;
    font-size: 15px;
    font-weight: bold;
}

#logo_sub {
    color: #8b949e;
    font-size: 10px;
}

#category_label {
    color: #8b949e;
    font-size: 10px;
    font-weight: bold;
    padding: 10px 16px 3px 16px;
    letter-spacing: 1px;
    text-transform: uppercase;
}

QPushButton#sidebar_btn {
    background-color: transparent;
    color: #8b949e;
    border: none;
    border-radius: 6px;
    padding: 7px 10px 7px 14px;
    text-align: left;
    font-size: 12px;
    margin: 1px 6px;
}
QPushButton#sidebar_btn:hover {
    background-color: #21262d;
    color: #c9d1d9;
}
QPushButton#sidebar_btn:checked {
    background-color: #1f3a5f;
    color: #58a6ff;
    font-weight: bold;
}

QPushButton#dashboard_btn {
    background-color: transparent;
    color: #c9d1d9;
    border: none;
    border-radius: 6px;
    padding: 9px 10px 9px 14px;
    text-align: left;
    font-size: 13px;
    font-weight: bold;
    margin: 4px 6px;
}
QPushButton#dashboard_btn:hover {
    background-color: #21262d;
}
QPushButton#dashboard_btn:checked {
    background-color: #1f3a5f;
    color: #58a6ff;
}

/* ── Scroll Area ──────────────────────────────────────────────────────── */
QScrollArea {
    background: transparent;
    border: none;
}
QScrollArea > QWidget > QWidget {
    background: transparent;
}

QScrollBar:vertical {
    background: #0d1117;
    width: 6px;
    border-radius: 3px;
}
QScrollBar::handle:vertical {
    background: #30363d;
    border-radius: 3px;
    min-height: 20px;
}
QScrollBar::handle:vertical:hover { background: #58a6ff; }
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }

QScrollBar:horizontal {
    background: #0d1117;
    height: 6px;
    border-radius: 3px;
}
QScrollBar::handle:horizontal {
    background: #30363d;
    border-radius: 3px;
    min-width: 20px;
}
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal { width: 0; }

/* ── Cards ────────────────────────────────────────────────────────────── */
#stat_card {
    background-color: #161b22;
    border: 1px solid #30363d;
    border-radius: 10px;
}
#stat_value {
    font-size: 26px;
    font-weight: bold;
    color: #e6edf3;
}
#stat_label {
    color: #8b949e;
    font-size: 11px;
}

#module_card {
    background-color: #161b22;
    border: 1px solid #30363d;
    border-radius: 10px;
}

/* ── Labels ───────────────────────────────────────────────────────────── */
#page_title {
    color: #e6edf3;
    font-size: 24px;
    font-weight: bold;
}
#page_sub {
    color: #8b949e;
    font-size: 13px;
}
#section_title {
    color: #e6edf3;
    font-size: 15px;
    font-weight: bold;
}
#module_header_title {
    color: #e6edf3;
    font-size: 22px;
    font-weight: bold;
}
#module_header_sub {
    color: #8b949e;
    font-size: 13px;
}

/* ── Buttons ──────────────────────────────────────────────────────────── */
QPushButton {
    background-color: #21262d;
    color: #c9d1d9;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 7px 16px;
    font-size: 12px;
}
QPushButton:hover {
    background-color: #30363d;
    border-color: #58a6ff;
}
QPushButton:pressed { background-color: #161b22; }

QPushButton#primary_btn {
    background-color: #1f6feb;
    color: #ffffff;
    border-color: #1f6feb;
    font-weight: bold;
}
QPushButton#primary_btn:hover { background-color: #388bfd; }

QPushButton#danger_btn {
    background-color: transparent;
    color: #f85149;
    border-color: #f85149;
}
QPushButton#danger_btn:hover { background-color: #3d1a1a; }

QPushButton#success_btn {
    background-color: #2ea043;
    color: #ffffff;
    border-color: #2ea043;
}
QPushButton#success_btn:hover { background-color: #3fb950; }

QPushButton#tool_btn {
    background-color: transparent;
    color: #58a6ff;
    border: 1px solid #30363d;
    border-radius: 5px;
    padding: 4px 10px;
    font-size: 11px;
}
QPushButton#tool_btn:hover {
    background-color: #1f3a5f;
    border-color: #58a6ff;
}

/* ── Tabs ─────────────────────────────────────────────────────────────── */
QTabWidget::pane {
    background-color: #161b22;
    border: 1px solid #30363d;
    border-top: none;
    border-radius: 0 0 10px 10px;
}
QTabBar {
    background: transparent;
}
QTabBar::tab {
    background: transparent;
    color: #8b949e;
    padding: 9px 20px;
    border: none;
    border-bottom: 2px solid transparent;
    font-size: 13px;
    margin-right: 2px;
}
QTabBar::tab:selected {
    color: #58a6ff;
    border-bottom: 2px solid #58a6ff;
}
QTabBar::tab:hover { color: #c9d1d9; }

/* ── Table ────────────────────────────────────────────────────────────── */
QTableWidget {
    background-color: #161b22;
    color: #c9d1d9;
    border: 1px solid #30363d;
    border-radius: 8px;
    gridline-color: #21262d;
    outline: none;
    font-size: 12px;
}
QTableWidget::item {
    padding: 6px 8px;
    border-bottom: 1px solid #21262d;
}
QTableWidget::item:selected {
    background-color: #1f3a5f;
    color: #e6edf3;
}
QHeaderView::section {
    background-color: #0d1117;
    color: #8b949e;
    padding: 7px 8px;
    border: none;
    border-bottom: 1px solid #30363d;
    font-size: 11px;
    font-weight: bold;
    text-transform: uppercase;
}
QTableWidget QTableCornerButton::section {
    background-color: #0d1117;
    border: none;
}

/* ── Form Inputs ──────────────────────────────────────────────────────── */
QLineEdit, QTextEdit, QDoubleSpinBox, QSpinBox {
    background-color: #0d1117;
    color: #c9d1d9;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 7px 10px;
    font-size: 13px;
    selection-background-color: #1f6feb;
}
QLineEdit:focus, QTextEdit:focus, QDoubleSpinBox:focus, QSpinBox:focus {
    border-color: #58a6ff;
    background-color: #0d1117;
}

QComboBox {
    background-color: #0d1117;
    color: #c9d1d9;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 7px 10px;
    font-size: 13px;
}
QComboBox:focus { border-color: #58a6ff; }
QComboBox::drop-down {
    border: none;
    width: 22px;
}
QComboBox::down-arrow {
    width: 10px;
    height: 10px;
}
QComboBox QAbstractItemView {
    background-color: #21262d;
    color: #c9d1d9;
    border: 1px solid #30363d;
    border-radius: 6px;
    selection-background-color: #1f6feb;
    outline: none;
}

/* ── Dialog ───────────────────────────────────────────────────────────── */
QDialog {
    background-color: #161b22;
    border: 1px solid #30363d;
    border-radius: 10px;
}

/* ── Tooltip ──────────────────────────────────────────────────────────── */
QToolTip {
    background-color: #21262d;
    color: #c9d1d9;
    border: 1px solid #30363d;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 12px;
}

/* ── Separator ────────────────────────────────────────────────────────── */
QFrame[frameShape="4"], QFrame[frameShape="5"] {
    color: #30363d;
    background-color: #30363d;
}

/* ── SpinBox buttons ──────────────────────────────────────────────────── */
QDoubleSpinBox::up-button, QDoubleSpinBox::down-button,
QSpinBox::up-button, QSpinBox::down-button {
    background-color: #21262d;
    border: none;
    width: 16px;
}
QDoubleSpinBox::up-button:hover, QDoubleSpinBox::down-button:hover,
QSpinBox::up-button:hover, QSpinBox::down-button:hover {
    background-color: #30363d;
}
"""
