"""
MainWindow — application shell with sidebar navigation + stacked content area.
"""
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QLabel, QPushButton, QScrollArea, QFrame,
    QStackedWidget, QSizePolicy, QSpacerItem,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from core.interfaces import IProjectService
from core.models import CATEGORY_COLORS
from ui.styles import STYLE
from ui.module_registry import MODULES, CATEGORIES
from ui.dashboard import DashboardWidget
from ui.module_widget import ModuleWidget


_DASHBOARD_INDEX = 0
_MODULE_INDEX    = 1


class MainWindow(QMainWindow):
    def __init__(self, service: IProjectService, parent=None):
        super().__init__(parent)
        self._service = service
        self._active_btn: QPushButton | None = None

        self.setWindowTitle("AI Passive Income Suite")
        self.setStyleSheet(STYLE)
        self.resize(1300, 820)
        self.setMinimumSize(960, 620)

        self._build_ui()
        self._show_dashboard()

    # ── build ─────────────────────────────────────────────────────────────

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        h = QHBoxLayout(central)
        h.setContentsMargins(0, 0, 0, 0)
        h.setSpacing(0)

        # Sidebar
        self._sidebar = self._build_sidebar()
        h.addWidget(self._sidebar)

        # Content stack
        self._stack = QStackedWidget()
        self._dashboard = DashboardWidget(self._service)
        self._dashboard.module_clicked.connect(self._show_module)
        self._stack.addWidget(self._dashboard)   # index 0

        self._module_widget = ModuleWidget(self._service)
        self._stack.addWidget(self._module_widget)  # index 1

        h.addWidget(self._stack, stretch=1)

    def _build_sidebar(self) -> QWidget:
        sidebar = QWidget()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(232)

        root = QVBoxLayout(sidebar)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # ── Logo ─────────────────────────────────────────────────────────
        logo_frame = QFrame()
        logo_frame.setObjectName("sidebar_logo")
        logo_frame.setFixedHeight(68)
        logo_lay = QVBoxLayout(logo_frame)
        logo_lay.setContentsMargins(16, 10, 16, 10)
        logo_lay.setSpacing(2)

        title_lbl = QLabel("🤖 AI Income Suite")
        title_lbl.setObjectName("logo_title")
        title_lbl.setFont(QFont("Segoe UI", 13, QFont.Bold))
        logo_lay.addWidget(title_lbl)

        sub_lbl = QLabel("20 streams · 1 dashboard")
        sub_lbl.setObjectName("logo_sub")
        sub_lbl.setStyleSheet("color:#8b949e; font-size:10px;")
        logo_lay.addWidget(sub_lbl)
        root.addWidget(logo_frame)

        # ── Scrollable nav ───────────────────────────────────────────────
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        nav = QWidget()
        nav.setStyleSheet("background:transparent;")
        nav_lay = QVBoxLayout(nav)
        nav_lay.setContentsMargins(0, 8, 0, 16)
        nav_lay.setSpacing(0)
        scroll.setWidget(nav)
        root.addWidget(scroll, stretch=1)

        # Dashboard button
        dash_btn = self._sidebar_btn("🏠  Dashboard", is_dashboard=True)
        dash_btn.clicked.connect(self._show_dashboard)
        nav_lay.addWidget(dash_btn)
        self._dash_btn = dash_btn

        # Separator
        sep = QFrame(); sep.setFrameShape(QFrame.HLine); sep.setFixedHeight(1)
        sep.setStyleSheet("background:#30363d; margin:6px 10px;")
        nav_lay.addWidget(sep)

        # Module buttons grouped by category
        self._module_btns: dict[int, QPushButton] = {}
        for cat, modules in CATEGORIES.items():
            cat_color = CATEGORY_COLORS.get(cat, "#8b949e")
            cat_lbl = QLabel(cat.upper())
            cat_lbl.setObjectName("category_label")
            cat_lbl.setStyleSheet(
                f"color:{cat_color}; font-size:9px; font-weight:bold;"
                f"padding:10px 16px 3px 16px; letter-spacing:1px;"
            )
            nav_lay.addWidget(cat_lbl)

            for m in modules:
                btn = self._sidebar_btn(f"{m.emoji}  {m.id:02d}. {m.title}")
                btn.clicked.connect(lambda _, mid=m.id: self._show_module(mid))
                nav_lay.addWidget(btn)
                self._module_btns[m.id] = btn

        nav_lay.addStretch()

        # Bottom: version
        ver_lbl = QLabel("v1.0.0  ·  Clean Architecture")
        ver_lbl.setStyleSheet(
            "color:#30363d; font-size:9px; padding:8px 16px;"
        )
        root.addWidget(ver_lbl)
        return sidebar

    def _sidebar_btn(self, text: str, is_dashboard: bool = False) -> QPushButton:
        btn = QPushButton(text)
        btn.setObjectName("dashboard_btn" if is_dashboard else "sidebar_btn")
        btn.setCheckable(True)
        btn.setChecked(False)
        btn.setMinimumHeight(34)
        btn.setMaximumHeight(40)
        btn.setCursor(Qt.PointingHandCursor)
        btn.setToolTip(text)
        return btn

    # ── navigation ────────────────────────────────────────────────────────

    def _set_active(self, btn: QPushButton):
        if self._active_btn:
            self._active_btn.setChecked(False)
        self._active_btn = btn
        btn.setChecked(True)

    def _show_dashboard(self):
        self._set_active(self._dash_btn)
        self._dashboard.refresh()
        self._stack.setCurrentIndex(_DASHBOARD_INDEX)

    def _show_module(self, module_id: int):
        from ui.module_registry import MODULES_BY_ID
        config = MODULES_BY_ID.get(module_id)
        if not config:
            return
        btn = self._module_btns.get(module_id)
        if btn:
            self._set_active(btn)
        self._module_widget.load_module(config)
        self._stack.setCurrentIndex(_MODULE_INDEX)
