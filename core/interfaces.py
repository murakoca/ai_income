"""
Abstract interfaces defining the contracts between layers.
Only the core domain is imported here — zero framework dependencies.
"""
from abc import ABC, abstractmethod
from typing import List, Optional
from .models import Project


class IProjectRepository(ABC):
    """Port: data persistence."""

    @abstractmethod
    def get_all(self) -> List[Project]:
        pass

    @abstractmethod
    def get_by_module(self, module_id: int) -> List[Project]:
        pass

    @abstractmethod
    def get_by_id(self, project_id: str) -> Optional[Project]:
        pass

    @abstractmethod
    def save(self, project: Project) -> Project:
        pass

    @abstractmethod
    def delete(self, project_id: str) -> bool:
        pass


class IProjectService(ABC):
    """Port: application use-cases."""

    @abstractmethod
    def create_project(self, module_id: int, name: str, **kwargs) -> Project:
        pass

    @abstractmethod
    def update_project(self, project_id: str, **kwargs) -> Optional[Project]:
        pass

    @abstractmethod
    def delete_project(self, project_id: str) -> bool:
        pass

    @abstractmethod
    def get_module_projects(self, module_id: int) -> List[Project]:
        pass

    @abstractmethod
    def get_all_projects(self) -> List[Project]:
        pass

    @abstractmethod
    def get_stats(self) -> dict:
        pass
