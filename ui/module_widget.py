"""
ModuleWidget — reusable detail view for any of the 20 modules.
Tabs: Overview | Tools | Projects | Calculator
"""
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QFrame, QGridLayout, QTabWidget, QTableWidget,
    QTableWidgetItem, QHeaderView, QMessageBox, QSizePolicy,
    QSpacerItem, QAbstractItemView, QDoubleSpinBox, QSpinBox,
)
from PyQt5.QtCore import Qt, QUrl, pyqtSignal
from PyQt5.QtGui import QFont, QDesktopServices, QColor

from core.models import (
    ModuleConfig, Project,
    STATUS_COLORS, STATUS_LABELS, DIFFICULTY_COLORS,
)
from core.interfaces import IProjectService
from ui.dialogs.project_dialog import ProjectDialog


class ModuleWidget(QWidget):
    """Single re-usable widget that is loaded with different ModuleConfig objects."""

    def __init__(self, service: IProjectService, parent=None):
        super().__init__(parent)
        self._service = service
        self._config: ModuleConfig | None = None
        self._build_skeleton()

    # ── public API ────────────────────────────────────────────────────────

    def load_module(self, config: ModuleConfig):
        self._config = config
        self._refresh_header()
        self._refresh_overview()
        self._refresh_tools()
        self._refresh_projects()
        self._refresh_calculator()

    # ── skeleton ──────────────────────────────────────────────────────────

    def _build_skeleton(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # ── Header ──────────────────────────────────────────────────────
        self._header_frame = QFrame()
        self._header_frame.setMinimumHeight(110)
        self._header_frame.setMaximumHeight(130)
        h_layout = QHBoxLayout(self._header_frame)
        h_layout.setContentsMargins(28, 18, 28, 18)
        h_layout.setSpacing(16)

        self._emoji_lbl = QLabel()
        self._emoji_lbl.setFont(QFont("Segoe UI Emoji", 36))
        self._emoji_lbl.setFixedSize(64, 64)
        self._emoji_lbl.setAlignment(Qt.AlignCenter)
        h_layout.addWidget(self._emoji_lbl)

        title_col = QVBoxLayout()
        title_col.setSpacing(4)
        self._title_lbl = QLabel()
        self._title_lbl.setObjectName("module_header_title")
        self._title_lbl.setFont(QFont("Segoe UI", 20, QFont.Bold))
        title_col.addWidget(self._title_lbl)
        self._sub_lbl = QLabel()
        self._sub_lbl.setObjectName("module_header_sub")
        title_col.addWidget(self._sub_lbl)
        self._badges_row = QHBoxLayout()
        self._badges_row.setSpacing(8)
        title_col.addLayout(self._badges_row)
        h_layout.addLayout(title_col, stretch=1)

        root.addWidget(self._header_frame)

        # ── Tabs ─────────────────────────────────────────────────────────
        self._tabs = QTabWidget()
        self._tabs.setDocumentMode(True)

        self._overview_tab = self._build_overview_tab()
        self._tools_tab    = self._build_tools_tab()
        self._projects_tab = self._build_projects_tab()
        self._calc_tab     = self._build_calc_tab()

        self._tabs.addTab(self._overview_tab, "📋  Overview")
        self._tabs.addTab(self._tools_tab,    "🔧  Tools")
        self._tabs.addTab(self._projects_tab, "📁  Projects")
        self._tabs.addTab(self._calc_tab,     "💰  Calculator")

        root.addWidget(self._tabs, stretch=1)

    # ── tab builders ──────────────────────────────────────────────────────

    def _build_overview_tab(self) -> QWidget:
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        inner = QWidget()
        scroll.setWidget(inner)
        lay = QVBoxLayout(inner)
        lay.setContentsMargins(28, 22, 28, 28)
        lay.setSpacing(20)

        # Description placeholder
        self._desc_lbl = QLabel()
        self._desc_lbl.setWordWrap(True)
        self._desc_lbl.setStyleSheet("color:#c9d1d9; font-size:14px; line-height:1.6;")
        lay.addWidget(self._desc_lbl)

        # Workflow header
        wf_title = QLabel("📌  Step-by-Step Workflow")
        wf_title.setFont(QFont("Segoe UI", 14, QFont.Bold))
        wf_title.setStyleSheet("color:#e6edf3; margin-top:6px;")
        lay.addWidget(wf_title)

        # Steps container
        self._steps_frame = QFrame()
        self._steps_frame.setStyleSheet(
            "background:#161b22; border:1px solid #30363d; border-radius:10px; padding:4px;"
        )
        self._steps_layout = QVBoxLayout(self._steps_frame)
        self._steps_layout.setContentsMargins(16, 12, 16, 12)
        self._steps_layout.setSpacing(10)
        lay.addWidget(self._steps_frame)
        lay.addStretch()

        self._overview_inner = inner
        return scroll

    def _build_tools_tab(self) -> QWidget:
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        inner = QWidget()
        scroll.setWidget(inner)
        lay = QVBoxLayout(inner)
        lay.setContentsMargins(28, 22, 28, 28)
        lay.setSpacing(16)

        hdr = QLabel("🔧  Suggested Tools")
        hdr.setFont(QFont("Segoe UI", 14, QFont.Bold))
        hdr.setStyleSheet("color:#e6edf3;")
        lay.addWidget(hdr)

        self._tools_grid = QGridLayout()
        self._tools_grid.setSpacing(12)
        lay.addLayout(self._tools_grid)
        lay.addStretch()
        return scroll

    def _build_projects_tab(self) -> QWidget:
        w = QWidget()
        lay = QVBoxLayout(w)
        lay.setContentsMargins(24, 18, 24, 18)
        lay.setSpacing(12)

        # Top bar
        top = QHBoxLayout()
        proj_title = QLabel("📁  My Projects")
        proj_title.setFont(QFont("Segoe UI", 14, QFont.Bold))
        proj_title.setStyleSheet("color:#e6edf3;")
        top.addWidget(proj_title)
        top.addStretch()

        self._add_btn = QPushButton("➕  Add Project")
        self._add_btn.setObjectName("primary_btn")
        self._add_btn.setMinimumHeight(34)
        self._add_btn.clicked.connect(self._add_project)
        top.addWidget(self._add_btn)
        lay.addLayout(top)

        # Table
        self._table = QTableWidget(0, 6)
        self._table.setHorizontalHeaderLabels(
            ["Name", "Status", "Monthly $", "Target $", "Created", "Actions"]
        )
        self._table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self._table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self._table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self._table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Fixed)
        self._table.horizontalHeader().setSectionResizeMode(4, QHeaderView.Fixed)
        self._table.horizontalHeader().setSectionResizeMode(5, QHeaderView.Fixed)
        self._table.setColumnWidth(1, 120)
        self._table.setColumnWidth(2, 110)
        self._table.setColumnWidth(3, 110)
        self._table.setColumnWidth(4, 100)
        self._table.setColumnWidth(5, 140)
        self._table.verticalHeader().setVisible(False)
        self._table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self._table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self._table.setAlternatingRowColors(False)
        self._table.setShowGrid(False)
        self._table.setFocusPolicy(Qt.NoFocus)
        self._table.setMinimumHeight(300)
        lay.addWidget(self._table)

        # Summary bar
        self._proj_summary = QLabel()
        self._proj_summary.setStyleSheet("color:#8b949e; font-size:12px;")
        lay.addWidget(self._proj_summary)
        lay.addStretch()
        return w

    def _build_calc_tab(self) -> QWidget:
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        inner = QWidget()
        scroll.setWidget(inner)
        lay = QVBoxLayout(inner)
        lay.setContentsMargins(28, 22, 28, 28)
        lay.setSpacing(18)

        hdr = QLabel("💰  Revenue Calculator")
        hdr.setFont(QFont("Segoe UI", 14, QFont.Bold))
        hdr.setStyleSheet("color:#e6edf3;")
        lay.addWidget(hdr)

        # Info card
        self._calc_info = QFrame()
        self._calc_info.setStyleSheet(
            "background:#161b22; border:1px solid #30363d; border-radius:10px; padding:8px;"
        )
        info_lay = QVBoxLayout(self._calc_info)
        info_lay.setContentsMargins(16, 12, 16, 12)
        info_lay.setSpacing(8)
        self._calc_range_lbl  = QLabel()
        self._calc_diff_lbl   = QLabel()
        self._calc_time_lbl   = QLabel()
        for lbl in (self._calc_range_lbl, self._calc_diff_lbl, self._calc_time_lbl):
            lbl.setStyleSheet("color:#c9d1d9; font-size:13px;")
            info_lay.addWidget(lbl)
        lay.addWidget(self._calc_info)

        # Inputs
        inputs_frame = QFrame()
        inputs_frame.setStyleSheet(
            "background:#161b22; border:1px solid #30363d; border-radius:10px;"
        )
        inp_lay = QVBoxLayout(inputs_frame)
        inp_lay.setContentsMargins(16, 14, 16, 14)
        inp_lay.setSpacing(12)

        inp_title = QLabel("⚙️  Estimate Your Income")
        inp_title.setFont(QFont("Segoe UI", 13, QFont.Bold))
        inp_title.setStyleSheet("color:#e6edf3;")
        inp_lay.addWidget(inp_title)

        row1 = QHBoxLayout()
        row1.setSpacing(16)
        lbl1 = QLabel("Units / Sales per Month:")
        lbl1.setStyleSheet("color:#8b949e; font-size:12px; font-weight:bold;")
        self._units_spin = QSpinBox()
        self._units_spin.setRange(1, 100_000)
        self._units_spin.setValue(10)
        self._units_spin.setSuffix(" units")
        self._units_spin.setMinimumWidth(140)
        row1.addWidget(lbl1)
        row1.addWidget(self._units_spin)
        row1.addStretch()
        inp_lay.addLayout(row1)

        row2 = QHBoxLayout()
        row2.setSpacing(16)
        lbl2 = QLabel("Price / Revenue per Unit:")
        lbl2.setStyleSheet("color:#8b949e; font-size:12px; font-weight:bold;")
        self._price_spin = QDoubleSpinBox()
        self._price_spin.setRange(0.01, 100_000)
        self._price_spin.setValue(29.0)
        self._price_spin.setDecimals(2)
        self._price_spin.setPrefix("$ ")
        self._price_spin.setMinimumWidth(140)
        row2.addWidget(lbl2)
        row2.addWidget(self._price_spin)
        row2.addStretch()
        inp_lay.addLayout(row2)

        calc_btn = QPushButton("🧮  Calculate")
        calc_btn.setObjectName("success_btn")
        calc_btn.setMinimumHeight(36)
        calc_btn.clicked.connect(self._run_calc)
        inp_lay.addWidget(calc_btn)
        lay.addWidget(inputs_frame)

        # Result
        self._calc_result = QFrame()
        self._calc_result.setStyleSheet(
            "background:#0f2a1a; border:1px solid #34d399; border-radius:10px;"
        )
        res_lay = QVBoxLayout(self._calc_result)
        res_lay.setContentsMargins(20, 14, 20, 14)
        res_lay.setSpacing(6)
        self._result_monthly = QLabel()
        self._result_monthly.setFont(QFont("Segoe UI", 22, QFont.Bold))
        self._result_monthly.setStyleSheet("color:#34d399;")
        self._result_annual  = QLabel()
        self._result_annual.setStyleSheet("color:#86efac; font-size:13px;")
        self._result_note    = QLabel()
        self._result_note.setStyleSheet("color:#8b949e; font-size:11px;")
        self._result_note.setWordWrap(True)
        res_lay.addWidget(self._result_monthly)
        res_lay.addWidget(self._result_annual)
        res_lay.addWidget(self._result_note)
        self._calc_result.setVisible(False)
        lay.addWidget(self._calc_result)
        lay.addStretch()
        return scroll

    # ── refresh methods ───────────────────────────────────────────────────

    def _refresh_header(self):
        c = self._config
        # Background colour strip
        self._header_frame.setStyleSheet(
            f"background: qlineargradient(x1:0,y1:0,x2:1,y2:0,"
            f"stop:0 #161b22, stop:1 #0d1117);"
            f"border-bottom: 3px solid {c.color};"
        )
        self._emoji_lbl.setText(c.emoji)
        self._title_lbl.setText(c.title)
        self._sub_lbl.setText(c.subtitle)

        # Clear old badges
        while self._badges_row.count():
            item = self._badges_row.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        def badge(text: str, color: str) -> QLabel:
            lbl = QLabel(text)
            lbl.setStyleSheet(
                f"background:{color}22; color:{color}; border:1px solid {color}66;"
                f"border-radius:4px; padding:2px 8px; font-size:11px; font-weight:bold;"
            )
            return lbl

        from core.models import DIFFICULTY_COLORS
        self._badges_row.addWidget(badge(f"📊 {c.difficulty}", DIFFICULTY_COLORS.get(c.difficulty, "#60a5fa")))
        self._badges_row.addWidget(badge(f"💰 {c.revenue_range}", c.color))
        self._badges_row.addWidget(badge(f"⏱ {c.time_to_profit}", "#fbbf24"))
        self._badges_row.addWidget(badge(c.category, "#8b949e"))
        self._badges_row.addStretch()

    def _refresh_overview(self):
        c = self._config
        self._desc_lbl.setText(c.description)

        # Clear old steps
        while self._steps_layout.count():
            item = self._steps_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        for step in c.workflow_steps:
            lbl = QLabel(step)
            lbl.setWordWrap(True)
            lbl.setStyleSheet(
                f"color:#c9d1d9; font-size:13px; padding:7px 10px 7px 10px;"
                f"border-left:3px solid {c.color}; background:#0d1117; border-radius:4px;"
            )
            self._steps_layout.addWidget(lbl)

    def _refresh_tools(self):
        c = self._config
        # Clear grid
        for i in reversed(range(self._tools_grid.count())):
            item = self._tools_grid.itemAt(i)
            if item.widget():
                item.widget().deleteLater()

        for idx, tool in enumerate(c.tools):
            card = self._make_tool_card(tool, c.color)
            self._tools_grid.addWidget(card, idx // 2, idx % 2)

    def _make_tool_card(self, tool, accent: str) -> QFrame:
        card = QFrame()
        card.setStyleSheet(
            "QFrame{background:#161b22; border:1px solid #30363d; border-radius:10px;}"
            "QFrame:hover{border-color:" + accent + ";}"
        )
        card.setMinimumHeight(90)
        lay = QVBoxLayout(card)
        lay.setContentsMargins(14, 12, 14, 12)
        lay.setSpacing(4)

        top_row = QHBoxLayout()
        # Icon circle
        icon_lbl = QLabel(tool.name[0].upper())
        icon_lbl.setFixedSize(30, 30)
        icon_lbl.setAlignment(Qt.AlignCenter)
        icon_lbl.setStyleSheet(
            f"background:{accent}33; color:{accent}; border-radius:15px;"
            f"font-weight:bold; font-size:13px;"
        )
        top_row.addWidget(icon_lbl)

        name_lbl = QLabel(tool.name)
        name_lbl.setFont(QFont("Segoe UI", 12, QFont.Bold))
        name_lbl.setStyleSheet("color:#e6edf3; background:transparent;")
        top_row.addWidget(name_lbl, stretch=1)

        if tool.free_tier:
            free_lbl = QLabel("FREE")
            free_lbl.setStyleSheet(
                "background:#0f2a1a; color:#34d399; border:1px solid #34d399;"
                "border-radius:3px; padding:1px 6px; font-size:10px; font-weight:bold;"
            )
            top_row.addWidget(free_lbl)
        lay.addLayout(top_row)

        desc_lbl = QLabel(tool.description)
        desc_lbl.setStyleSheet("color:#8b949e; font-size:11px; background:transparent;")
        lay.addWidget(desc_lbl)

        open_btn = QPushButton("Open →")
        open_btn.setObjectName("tool_btn")
        open_btn.setFixedHeight(26)
        url = tool.url
        open_btn.clicked.connect(lambda checked, u=url: QDesktopServices.openUrl(QUrl(u)))
        lay.addWidget(open_btn)
        return card

    def _refresh_projects(self):
        if not self._config:
            return
        projects = self._service.get_module_projects(self._config.id)
        self._table.setRowCount(0)
        total_rev = 0.0
        for p in projects:
            self._add_table_row(p)
            total_rev += p.monthly_revenue
        self._proj_summary.setText(
            f"Total: {len(projects)} project(s) · Monthly revenue: ${total_rev:,.2f}"
        )

    def _add_table_row(self, p: Project):
        row = self._table.rowCount()
        self._table.insertRow(row)

        name_item = QTableWidgetItem(p.name)
        name_item.setData(Qt.UserRole, p.id)
        self._table.setItem(row, 0, name_item)

        status_color = STATUS_COLORS.get(p.status, "#8b949e")
        status_item  = QTableWidgetItem(STATUS_LABELS.get(p.status, p.status))
        status_item.setForeground(QColor(status_color))
        self._table.setItem(row, 1, status_item)

        rev_item = QTableWidgetItem(f"${p.monthly_revenue:,.2f}")
        rev_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self._table.setItem(row, 2, rev_item)

        tgt_item = QTableWidgetItem(f"${p.target_revenue:,.2f}")
        tgt_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self._table.setItem(row, 3, tgt_item)

        date_str = p.created_at[:10] if p.created_at else "—"
        self._table.setItem(row, 4, QTableWidgetItem(date_str))

        # Actions cell
        action_widget = QWidget()
        action_widget.setStyleSheet("background:transparent;")
        a_lay = QHBoxLayout(action_widget)
        a_lay.setContentsMargins(4, 2, 4, 2)
        a_lay.setSpacing(6)

        edit_btn = QPushButton("✏️")
        edit_btn.setFixedSize(28, 26)
        edit_btn.setToolTip("Edit project")
        edit_btn.setStyleSheet(
            "QPushButton{background:#21262d;border:1px solid #30363d;border-radius:4px;}"
            "QPushButton:hover{background:#388bfd;border-color:#388bfd;}"
        )
        edit_btn.clicked.connect(lambda _, pid=p.id: self._edit_project(pid))

        del_btn = QPushButton("🗑")
        del_btn.setFixedSize(28, 26)
        del_btn.setToolTip("Delete project")
        del_btn.setStyleSheet(
            "QPushButton{background:#21262d;border:1px solid #30363d;border-radius:4px;}"
            "QPushButton:hover{background:#3d1a1a;border-color:#f85149;}"
        )
        del_btn.clicked.connect(lambda _, pid=p.id, pn=p.name: self._delete_project(pid, pn))

        a_lay.addWidget(edit_btn)
        a_lay.addWidget(del_btn)
        a_lay.addStretch()
        self._table.setCellWidget(row, 5, action_widget)
        self._table.setRowHeight(row, 44)

    def _refresh_calculator(self):
        c = self._config
        self._calc_range_lbl.setText(f"💰  Revenue Range: {c.revenue_range}")
        self._calc_diff_lbl.setText(f"📊  Difficulty: {c.difficulty}")
        self._calc_time_lbl.setText(f"⏱  Time to First Income: {c.time_to_profit}")
        self._calc_result.setVisible(False)

    # ── project CRUD ──────────────────────────────────────────────────────

    def _add_project(self):
        dlg = ProjectDialog(self._config.id, parent=self)
        if dlg.exec_() == ProjectDialog.Accepted:
            p = dlg.get_project()
            if p:
                self._service.create_project(
                    p.module_id, p.name,
                    status=p.status,
                    monthly_revenue=p.monthly_revenue,
                    target_revenue=p.target_revenue,
                    notes=p.notes,
                )
                self._refresh_projects()

    def _edit_project(self, project_id: str):
        p = self._service.get_module_projects(self._config.id)
        target = next((x for x in p if x.id == project_id), None)
        if not target:
            return
        dlg = ProjectDialog(self._config.id, project=target, parent=self)
        if dlg.exec_() == ProjectDialog.Accepted:
            updated = dlg.get_project()
            if updated:
                self._service.update_project(
                    updated.id,
                    name=updated.name,
                    status=updated.status,
                    monthly_revenue=updated.monthly_revenue,
                    target_revenue=updated.target_revenue,
                    notes=updated.notes,
                )
                self._refresh_projects()

    def _delete_project(self, project_id: str, project_name: str):
        mb = QMessageBox(self)
        mb.setWindowTitle("Delete Project")
        mb.setText(f"Delete <b>{project_name}</b>?")
        mb.setInformativeText("This action cannot be undone.")
        mb.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        mb.setDefaultButton(QMessageBox.Cancel)
        mb.setStyleSheet(
            "QMessageBox{background:#161b22;color:#c9d1d9;}"
            "QPushButton{background:#21262d;color:#c9d1d9;border:1px solid #30363d;"
            "border-radius:6px;padding:6px 14px;}"
        )
        if mb.exec_() == QMessageBox.Yes:
            self._service.delete_project(project_id)
            self._refresh_projects()

    def _run_calc(self):
        units = self._units_spin.value()
        price = self._price_spin.value()
        monthly = units * price
        annual  = monthly * 12
        self._result_monthly.setText(f"${monthly:,.2f} / month")
        self._result_annual.setText(f"≈ ${annual:,.0f} per year")
        self._result_note.setText(
            "⚠️ This is a simplified estimate. Real income depends on platform fees, "
            "refunds, and growth rate. Use these figures as directional targets only."
        )
        self._calc_result.setVisible(True)
