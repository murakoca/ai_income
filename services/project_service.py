"""
Service layer — application use-cases, orchestrates the domain.
Depends only on core; the UI imports this but never the data layer directly.
"""
from datetime import datetime
from typing import List, Optional

from core.models import Project
from core.interfaces import IProjectRepository, IProjectService


class ProjectService(IProjectService):
    def __init__(self, repository: IProjectRepository):
        self._repo = repository

    # ── IProjectService ───────────────────────────────────────────────────────

    def create_project(self, module_id: int, name: str, **kwargs) -> Project:
        project = Project(
            module_id=module_id,
            name=name,
            status=str(kwargs.get("status", "planning")),
            monthly_revenue=float(kwargs.get("monthly_revenue", 0.0)),
            target_revenue=float(kwargs.get("target_revenue", 0.0)),
            notes=str(kwargs.get("notes", "")),
        )
        return self._repo.save(project)

    def update_project(self, project_id: str, **kwargs) -> Optional[Project]:
        project = self._repo.get_by_id(project_id)
        if not project:
            return None
        for key, value in kwargs.items():
            if hasattr(project, key):
                setattr(project, key, value)
        project.updated_at = datetime.now().isoformat()
        return self._repo.save(project)

    def delete_project(self, project_id: str) -> bool:
        return self._repo.delete(project_id)

    def get_module_projects(self, module_id: int) -> List[Project]:
        return self._repo.get_by_module(module_id)

    def get_all_projects(self) -> List[Project]:
        return self._repo.get_all()

    def get_stats(self) -> dict:
        all_p = self._repo.get_all()
        status_counts: dict = {}
        module_revenues: dict = {}
        module_counts: dict = {}

        for p in all_p:
            status_counts[p.status] = status_counts.get(p.status, 0) + 1
            module_revenues[p.module_id] = (
                module_revenues.get(p.module_id, 0.0) + p.monthly_revenue
            )
            module_counts[p.module_id] = module_counts.get(p.module_id, 0) + 1

        return {
            "total_projects":   len(all_p),
            "total_revenue":    sum(p.monthly_revenue for p in all_p),
            "active":           status_counts.get("active",    0),
            "planning":         status_counts.get("planning",  0),
            "paused":           status_counts.get("paused",    0),
            "completed":        status_counts.get("completed", 0),
            "module_revenues":  module_revenues,
            "module_counts":    module_counts,
        }
