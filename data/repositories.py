"""
Data layer — JSON file adapter implementing IProjectRepository.
Only depends on the core layer.
"""
import json
from pathlib import Path
from typing import List, Optional

from core.models import Project
from core.interfaces import IProjectRepository


class JsonProjectRepository(IProjectRepository):
    def __init__(self, data_dir: str):
        self._file = Path(data_dir) / "projects.json"
        if not self._file.exists():
            self._write([])

    # ── private helpers ──────────────────────────────────────────────────────

    def _read(self) -> List[dict]:
        try:
            with open(self._file, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _write(self, data: List[dict]) -> None:
        with open(self._file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    # ── IProjectRepository ────────────────────────────────────────────────────

    def get_all(self) -> List[Project]:
        return [Project.from_dict(d) for d in self._read()]

    def get_by_module(self, module_id: int) -> List[Project]:
        return [p for p in self.get_all() if p.module_id == module_id]

    def get_by_id(self, project_id: str) -> Optional[Project]:
        for p in self.get_all():
            if p.id == project_id:
                return p
        return None

    def save(self, project: Project) -> Project:
        data = self._read()
        for i, item in enumerate(data):
            if item.get("id") == project.id:
                data[i] = project.to_dict()
                self._write(data)
                return project
        data.append(project.to_dict())
        self._write(data)
        return project

    def delete(self, project_id: str) -> bool:
        data = self._read()
        new_data = [d for d in data if d.get("id") != project_id]
        changed = len(new_data) < len(data)
        if changed:
            self._write(new_data)
        return changed
