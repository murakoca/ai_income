"""
DashboardWidget — overview of all 20 modules with live stats cards.
"""
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame,
    QScrollArea, QGridLayout, QSizePolicy,
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QCursor

from core.models import CATEGORY_COLORS
from core.interfaces import IProjectService
from ui.module_registry import MODULES, CATEGORIES


class _StatCard(QFrame):
    """One KPI tile shown at the top of the dashboard."""

    def __init__(self, emoji: str, label: str, value: str, color: str, parent=None):
        super().__init__(parent)
        self.setObjectName("stat_card")
        self.setMinimumHeight(90)
        lay = QVBoxLayout(self)
        lay.setContentsMargins(16, 14, 16, 14)
        lay.setSpacing(4)

        top = QHBoxLayout()
        emoji_lbl = QLabel(emoji)
        emoji_lbl.setFont(QFont("Segoe UI Emoji", 20))
        emoji_lbl.setStyleSheet("background:transparent;")
        top.addWidget(emoji_lbl)
        top.addStretch()
        lay.addLayout(top)

        self._value_lbl = QLabel(value)
        self._value_lbl.setObjectName("stat_value")
        self._value_lbl.setFont(QFont("Segoe UI", 22, QFont.Bold))
        self._value_lbl.setStyleSheet(f"color:{color}; background:transparent;")
        lay.addWidget(self._value_lbl)

        label_lbl = QLabel(label)
        label_lbl.setObjectName("stat_label")
        label_lbl.setStyleSheet("color:#8b949e; font-size:11px; background:transparent;")
        lay.addWidget(label_lbl)

    def update_value(self, value: str):
        self._value_lbl.setText(value)


class _ModuleCard(QFrame):
    """Clickable card representing one income-stream module."""

    clicked = pyqtSignal(int)  # emits module_id

    def __init__(self, module_id: int, emoji: str, title: str,
                 color: str, category: str,
                 project_count: int = 0, revenue: float = 0.0,
                 parent=None):
        super().__init__(parent)
        self._module_id = module_id
        self._base_style = (
            f"QFrame#module_card{{background:#161b22; border:1px solid #30363d; border-radius:10px;}}"
            f"QFrame#module_card:hover{{border-color:{color}; background:#1c2128;}}"
        )
        self.setObjectName("module_card")
        self.setStyleSheet(self._base_style)
        self.setMinimumHeight(115)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        lay = QVBoxLayout(self)
        lay.setContentsMargins(14, 12, 14, 12)
        lay.setSpacing(4)

        # Top row: emoji + id badge
        top = QHBoxLayout()
        em = QLabel(emoji)
        em.setFont(QFont("Segoe UI Emoji", 22))
        em.setStyleSheet("background:transparent;")
        top.addWidget(em)
        top.addStretch()
        num_lbl = QLabel(f"#{module_id:02d}")
        num_lbl.setStyleSheet(
            f"background:{color}22; color:{color}; border:1px solid {color}66;"
            f"border-radius:4px; padding:1px 6px; font-size:10px; font-weight:bold;"
        )
        top.addWidget(num_lbl)
        lay.addLayout(top)

        # Title
        t = QLabel(title)
        t.setFont(QFont("Segoe UI", 11, QFont.Bold))
        t.setWordWrap(True)
        t.setStyleSheet("color:#e6edf3; background:transparent;")
        lay.addWidget(t)

        # Stats row
        stats = QHBoxLayout()
        stats.setSpacing(12)
        cat_color = CATEGORY_COLORS.get(category, "#8b949e")
        cat_lbl = QLabel(category)
        cat_lbl.setStyleSheet(f"color:{cat_color}; font-size:10px; background:transparent;")
        stats.addWidget(cat_lbl)
        stats.addStretch()
        self._rev_lbl = QLabel(f"${revenue:,.0f}/mo" if revenue else "—")
        self._rev_lbl.setStyleSheet("color:#34d399; font-size:11px; font-weight:bold; background:transparent;")
        stats.addWidget(self._rev_lbl)
        lay.addLayout(stats)

        self._proj_lbl = QLabel(f"{project_count} project(s)")
        self._proj_lbl.setStyleSheet("color:#8b949e; font-size:10px; background:transparent;")
        lay.addWidget(self._proj_lbl)

    def update_stats(self, project_count: int, revenue: float):
        self._rev_lbl.setText(f"${revenue:,.0f}/mo" if revenue else "—")
        self._proj_lbl.setText(f"{project_count} project(s)")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self._module_id)
        super().mousePressEvent(event)


class DashboardWidget(QWidget):
    """Full dashboard page."""

    module_clicked = pyqtSignal(int)  # propagates card clicks to MainWindow

    def __init__(self, service: IProjectService, parent=None):
        super().__init__(parent)
        self._service = service
        self._module_cards: dict[int, _ModuleCard] = {}
        self._stat_cards: dict[str, _StatCard]     = {}
        self._build_ui()
        self.refresh()

    # ── build ─────────────────────────────────────────────────────────────

    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        inner = QWidget()
        scroll.setWidget(inner)
        root.addWidget(scroll)

        lay = QVBoxLayout(inner)
        lay.setContentsMargins(28, 24, 28, 28)
        lay.setSpacing(24)

        # ── Page header ──────────────────────────────────────────────────
        hdr = QHBoxLayout()
        title = QLabel("🚀  AI Passive Income Suite")
        title.setObjectName("page_title")
        title.setFont(QFont("Segoe UI", 22, QFont.Bold))
        hdr.addWidget(title)
        hdr.addStretch()
        lay.addLayout(hdr)

        sub = QLabel("Track and manage all 20 AI-powered income streams in one place.")
        sub.setObjectName("page_sub")
        sub.setStyleSheet("color:#8b949e; font-size:13px; margin-top:-16px;")
        lay.addWidget(sub)

        # ── Stat cards ───────────────────────────────────────────────────
        stats_row = QHBoxLayout()
        stats_row.setSpacing(14)
        stats = [
            ("💰", "Total Monthly Revenue", "$0",  "#34d399"),
            ("⚡", "Active Projects",        "0",   "#60a5fa"),
            ("📊", "Total Projects",         "0",   "#c9d1d9"),
            ("✅", "Completed",             "0",   "#a78bfa"),
        ]
        keys = ["revenue", "active", "total", "completed"]
        for (em, lbl, val, col), key in zip(stats, keys):
            card = _StatCard(em, lbl, val, col)
            stats_row.addWidget(card)
            self._stat_cards[key] = card
        lay.addLayout(stats_row)

        # ── Modules grid ─────────────────────────────────────────────────
        sec = QLabel("📡  Income Streams")
        sec.setFont(QFont("Segoe UI", 15, QFont.Bold))
        sec.setStyleSheet("color:#e6edf3;")
        lay.addWidget(sec)

        grid = QGridLayout()
        grid.setSpacing(12)
        for idx, module in enumerate(MODULES):
            card = _ModuleCard(
                module_id=module.id,
                emoji=module.emoji,
                title=module.title,
                color=module.color,
                category=module.category,
            )
            card.clicked.connect(self.module_clicked.emit)
            grid.addWidget(card, idx // 4, idx % 4)
            self._module_cards[module.id] = card
        lay.addLayout(grid)

        # ── Category breakdown ───────────────────────────────────────────
        breakdown_title = QLabel("🗂  Streams by Category")
        breakdown_title.setFont(QFont("Segoe UI", 15, QFont.Bold))
        breakdown_title.setStyleSheet("color:#e6edf3;")
        lay.addWidget(breakdown_title)

        cat_grid = QGridLayout()
        cat_grid.setSpacing(12)
        for col_idx, (cat, modules_in_cat) in enumerate(CATEGORIES.items()):
            cat_color = CATEGORY_COLORS.get(cat, "#8b949e")
            cat_frame = QFrame()
            cat_frame.setStyleSheet(
                f"background:#161b22; border:1px solid {cat_color}44;"
                f"border-left:3px solid {cat_color}; border-radius:8px;"
            )
            cf_lay = QVBoxLayout(cat_frame)
            cf_lay.setContentsMargins(14, 12, 14, 12)
            cf_lay.setSpacing(6)

            ch = QLabel(cat)
            ch.setFont(QFont("Segoe UI", 12, QFont.Bold))
            ch.setStyleSheet(f"color:{cat_color}; background:transparent;")
            cf_lay.addWidget(ch)

            for m in modules_in_cat:
                ml = QLabel(f"  {m.emoji}  {m.title}")
                ml.setStyleSheet("color:#8b949e; font-size:11px; background:transparent;")
                cf_lay.addWidget(ml)

            cat_grid.addWidget(cat_frame, col_idx // 2, col_idx % 2)
        lay.addLayout(cat_grid)
        lay.addStretch()

    # ── refresh ───────────────────────────────────────────────────────────

    def refresh(self):
        """Re-query the service and update all displayed stats."""
        stats = self._service.get_stats()

        self._stat_cards["revenue"].update_value(f"${stats['total_revenue']:,.0f}")
        self._stat_cards["active"].update_value(str(stats["active"]))
        self._stat_cards["total"].update_value(str(stats["total_projects"]))
        self._stat_cards["completed"].update_value(str(stats["completed"]))

        for module_id, card in self._module_cards.items():
            count   = stats["module_counts"].get(module_id, 0)
            revenue = stats["module_revenues"].get(module_id, 0.0)
            card.update_stats(count, revenue)
