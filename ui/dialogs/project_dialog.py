"""
ProjectDialog — modal form for creating and editing projects.
"""
from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLabel, QLineEdit, QTextEdit, QDoubleSpinBox,
    QComboBox, QPushButton, QFrame,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from core.models import (
    Project, STATUS_OPTIONS, STATUS_LABELS, STATUS_COLORS
)


class ProjectDialog(QDialog):
    """Modal dialog for create / edit of a Project."""

    def __init__(self, module_id: int, project: Project | None = None, parent=None):
        super().__init__(parent)
        self._module_id = module_id
        self._project = project
        self._result_project: Project | None = None

        self.setWindowTitle("Edit Project" if project else "New Project")
        self.setModal(True)
        self.setMinimumWidth(440)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self._build_ui()
        if project:
            self._populate(project)

    # ── UI setup ──────────────────────────────────────────────────────────

    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # Header bar
        header = QFrame()
        header.setStyleSheet("background:#161b22; border-bottom:1px solid #30363d; border-radius: 10px 10px 0 0;")
        hlay = QHBoxLayout(header)
        hlay.setContentsMargins(20, 14, 20, 14)
        title_lbl = QLabel("✏️  Edit Project" if self._project else "➕  New Project")
        title_lbl.setFont(QFont("Segoe UI", 14, QFont.Bold))
        title_lbl.setStyleSheet("color:#e6edf3; background:transparent;")
        hlay.addWidget(title_lbl)
        hlay.addStretch()
        close_btn = QPushButton("✕")
        close_btn.setFixedSize(28, 28)
        close_btn.setStyleSheet(
            "QPushButton{background:transparent;color:#8b949e;border:none;font-size:14px;}"
            "QPushButton:hover{color:#f85149;}"
        )
        close_btn.clicked.connect(self.reject)
        hlay.addWidget(close_btn)
        root.addWidget(header)

        # Body
        body = QFrame()
        body.setStyleSheet("background:#161b22; border-radius: 0 0 10px 10px;")
        blay = QVBoxLayout(body)
        blay.setContentsMargins(24, 20, 24, 20)
        blay.setSpacing(14)

        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignRight)
        form.setSpacing(10)
        form.setContentsMargins(0, 0, 0, 0)

        lbl_style = "color:#8b949e; font-size:12px; font-weight:bold;"

        # Name
        name_lbl = QLabel("Project Name")
        name_lbl.setStyleSheet(lbl_style)
        self._name = QLineEdit()
        self._name.setPlaceholderText("e.g. My Ebook Series Vol.1")
        form.addRow(name_lbl, self._name)

        # Status
        status_lbl = QLabel("Status")
        status_lbl.setStyleSheet(lbl_style)
        self._status = QComboBox()
        for s in STATUS_OPTIONS:
            self._status.addItem(STATUS_LABELS[s], s)
        form.addRow(status_lbl, self._status)

        # Monthly revenue
        rev_lbl = QLabel("Monthly Revenue ($)")
        rev_lbl.setStyleSheet(lbl_style)
        self._revenue = QDoubleSpinBox()
        self._revenue.setRange(0, 1_000_000)
        self._revenue.setSingleStep(50)
        self._revenue.setDecimals(2)
        self._revenue.setPrefix("$ ")
        form.addRow(rev_lbl, self._revenue)

        # Target revenue
        tgt_lbl = QLabel("Target Revenue ($)")
        tgt_lbl.setStyleSheet(lbl_style)
        self._target = QDoubleSpinBox()
        self._target.setRange(0, 1_000_000)
        self._target.setSingleStep(100)
        self._target.setDecimals(2)
        self._target.setPrefix("$ ")
        form.addRow(tgt_lbl, self._target)

        # Notes
        notes_lbl = QLabel("Notes")
        notes_lbl.setStyleSheet(lbl_style)
        self._notes = QTextEdit()
        self._notes.setPlaceholderText("Tools, strategies, ideas, links…")
        self._notes.setFixedHeight(90)
        form.addRow(notes_lbl, self._notes)

        blay.addLayout(form)

        # Divider
        div = QFrame(); div.setFrameShape(QFrame.HLine); div.setFixedHeight(1)
        div.setStyleSheet("background:#30363d; border:none;")
        blay.addWidget(div)

        # Buttons
        btn_row = QHBoxLayout()
        btn_row.setSpacing(10)
        cancel_btn = QPushButton("Cancel")
        cancel_btn.setMinimumHeight(36)
        cancel_btn.clicked.connect(self.reject)
        btn_row.addWidget(cancel_btn)

        self._save_btn = QPushButton("💾  Save Project")
        self._save_btn.setObjectName("primary_btn")
        self._save_btn.setMinimumHeight(36)
        self._save_btn.clicked.connect(self._on_save)
        btn_row.addWidget(self._save_btn)
        blay.addLayout(btn_row)

        root.addWidget(body)

    # ── helpers ───────────────────────────────────────────────────────────

    def _populate(self, p: Project):
        self._name.setText(p.name)
        idx = STATUS_OPTIONS.index(p.status) if p.status in STATUS_OPTIONS else 0
        self._status.setCurrentIndex(idx)
        self._revenue.setValue(p.monthly_revenue)
        self._target.setValue(p.target_revenue)
        self._notes.setPlainText(p.notes)

    def _on_save(self):
        name = self._name.text().strip()
        if not name:
            self._name.setFocus()
            self._name.setStyleSheet("border:1px solid #f85149;")
            return
        if self._project:
            self._result_project = Project(
                id=self._project.id,
                module_id=self._module_id,
                name=name,
                status=self._status.currentData(),
                monthly_revenue=self._revenue.value(),
                target_revenue=self._target.value(),
                notes=self._notes.toPlainText(),
                created_at=self._project.created_at,
            )
        else:
            self._result_project = Project(
                module_id=self._module_id,
                name=name,
                status=self._status.currentData(),
                monthly_revenue=self._revenue.value(),
                target_revenue=self._target.value(),
                notes=self._notes.toPlainText(),
            )
        self.accept()

    def get_project(self) -> Project | None:
        return self._result_project
