"""
Core domain models — no framework dependencies.
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import List
import uuid


@dataclass
class Tool:
    name: str
    url: str
    description: str = ""
    free_tier: bool = False


@dataclass
class ModuleConfig:
    id: int
    title: str
    subtitle: str
    emoji: str
    category: str          # "Content Creation" | "Digital Products" | "Services" | "Tech & Dev"
    description: str
    workflow_steps: List[str]
    tools: List[Tool]
    revenue_range: str
    difficulty: str        # "Beginner" | "Intermediate" | "Advanced"
    time_to_profit: str
    color: str             # hex accent colour for this module


STATUS_OPTIONS = ["planning", "active", "paused", "completed"]

STATUS_COLORS = {
    "planning":  "#60a5fa",
    "active":    "#34d399",
    "paused":    "#fbbf24",
    "completed": "#a78bfa",
}

STATUS_LABELS = {
    "planning":  "🔵 Planning",
    "active":    "🟢 Active",
    "paused":    "🟡 Paused",
    "completed": "✅ Completed",
}

DIFFICULTY_COLORS = {
    "Beginner":     "#34d399",
    "Intermediate": "#fbbf24",
    "Advanced":     "#f87171",
}

CATEGORY_COLORS = {
    "Content Creation": "#a78bfa",
    "Digital Products": "#34d399",
    "Services":         "#60a5fa",
    "Tech & Dev":       "#fbbf24",
}


@dataclass
class Project:
    module_id: int
    name: str
    status: str = "planning"
    monthly_revenue: float = 0.0
    target_revenue: float = 0.0
    notes: str = ""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> dict:
        return {
            "id":              self.id,
            "module_id":       self.module_id,
            "name":            self.name,
            "status":          self.status,
            "monthly_revenue": self.monthly_revenue,
            "target_revenue":  self.target_revenue,
            "notes":           self.notes,
            "created_at":      self.created_at,
            "updated_at":      self.updated_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Project":
        return cls(
            id=str(data.get("id", str(uuid.uuid4()))),
            module_id=int(data.get("module_id", 0)),
            name=str(data.get("name", "")),
            status=str(data.get("status", "planning")),
            monthly_revenue=float(data.get("monthly_revenue", 0.0)),
            target_revenue=float(data.get("target_revenue", 0.0)),
            notes=str(data.get("notes", "")),
            created_at=str(data.get("created_at", datetime.now().isoformat())),
            updated_at=str(data.get("updated_at", datetime.now().isoformat())),
        )
