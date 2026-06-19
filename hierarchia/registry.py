"""HierarchiaRegistry — index all modules across all strata.

Provides search, filter, and cross-reference traversal over the
full hierarchy. Equivalent to AlgorithmRegistry in narratological-
algorithmic-lenses.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from hierarchia.loader import load_hierarchia
from hierarchia.models.stratum import (
    Hierarchia,
    Module,
    ModuleType,
    Scale,
    StratumType,
)


@dataclass
class ModuleInfo:
    """Lightweight descriptor for a module — no full data, just metadata."""

    id: str
    name: str
    stratum_id: str
    module_type: ModuleType
    scale: list[Scale]
    cross_ref_count: int

    @property
    def qualified_name(self) -> str:
        return self.id


@dataclass
class HierarchiaRegistry:
    """Index of all modules across all strata in the hierarchy.

    Supports lookup by id, search by keyword, filter by type/scale/stratum,
    and cross-reference traversal.
    """

    _hierarchia: Hierarchia
    _modules: dict[str, Module] = field(default_factory=dict)
    _by_stratum: dict[str, list[str]] = field(default_factory=dict)
    _by_type: dict[ModuleType, list[str]] = field(default_factory=dict)

    def __post_init__(self) -> None:
        for stratum in self._hierarchia.strata.values():
            stratum_keys: list[str] = []
            for module in stratum.modules:
                self._modules[module.id] = module
                stratum_keys.append(module.id)
                self._by_type.setdefault(module.module_type, []).append(module.id)
            self._by_stratum[stratum.id] = stratum_keys

    def get(self, module_id: str) -> Module | None:
        """Get a module by its qualified id."""
        if module_id in self._modules:
            return self._modules[module_id]
        # Case-insensitive fallback
        key_lower = module_id.lower()
        for k, v in self._modules.items():
            if k.lower() == key_lower:
                return v
        return None

    def get_by_stratum(self, stratum_id: str, module_name: str) -> Module | None:
        """Get a module by stratum id and module name."""
        full_id = f"{stratum_id}.{module_name.lower()}"
        return self.get(full_id)

    def search(self, query: str) -> list[Module]:
        """Search modules by name, description, or property values."""
        q = query.lower()
        results: list[Module] = []
        for module in self._modules.values():
            if q in module.name.lower():
                results.append(module)
            elif q in module.description.lower():
                results.append(module)
            elif any(q in str(v).lower() for v in module.properties.values()):
                results.append(module)
        return results

    def by_type(self, module_type: ModuleType) -> list[Module]:
        """Get all modules of a specific type."""
        keys = self._by_type.get(module_type, [])
        return [self._modules[k] for k in keys]

    def by_scale(self, scale: Scale) -> list[Module]:
        """Get all modules that apply at a given scale."""
        return [m for m in self._modules.values() if scale in m.scale]

    def by_stratum_type(self, stratum_type: StratumType) -> list[Module]:
        """Get all modules from strata of a given type."""
        results: list[Module] = []
        for stratum in self._hierarchia.strata.values():
            if stratum.stratum_type == stratum_type:
                results.extend(stratum.modules)
        return results

    def cross_refs(self, module_id: str) -> list[Module]:
        """Follow cross-references from a module, returning referenced modules."""
        source = self.get(module_id)
        if source is None:
            return []
        results: list[Module] = []
        for ref in source.cross_refs:
            # Try to find a module whose stratum path matches the ref
            for module in self._modules.values():
                stratum = self._hierarchia.strata.get(
                    ".".join(module.id.split(".")[:-1])
                )
                if stratum and ref in stratum.path:
                    results.append(module)
                    break
        return results

    def list_strata(self) -> list[str]:
        """List all stratum ids."""
        return list(self._by_stratum.keys())

    def list_by_stratum(self, stratum_id: str) -> list[Module]:
        """List all modules in a stratum."""
        keys = self._by_stratum.get(stratum_id, [])
        return [self._modules[k] for k in keys]

    def all(self) -> list[Module]:
        """Return all modules."""
        return list(self._modules.values())

    def info(self) -> list[ModuleInfo]:
        """Return lightweight descriptors for all modules."""
        result: list[ModuleInfo] = []
        for stratum_id, keys in self._by_stratum.items():
            for key in keys:
                m = self._modules[key]
                result.append(ModuleInfo(
                    id=m.id,
                    name=m.name,
                    stratum_id=stratum_id,
                    module_type=m.module_type,
                    scale=m.scale,
                    cross_ref_count=len(m.cross_refs),
                ))
        return result

    @property
    def count(self) -> int:
        return len(self._modules)

    def __len__(self) -> int:
        return self.count

    def __contains__(self, module_id: str) -> bool:
        return module_id in self._modules

    def __iter__(self):
        return iter(self._modules.values())


# Global singleton
_registry: HierarchiaRegistry | None = None


def get_registry(repo_root: Path | str | None = None) -> HierarchiaRegistry:
    """Get or create the global registry singleton.

    If repo_root is provided, loads from that path. Otherwise uses
    the default (hierarchia-mundi repo root, detected from this file's location).
    """
    global _registry
    if _registry is None:
        if repo_root is None:
            repo_root = Path(__file__).parent.parent
        hierarchia = load_hierarchia(repo_root)
        _registry = HierarchiaRegistry(_hierarchia=hierarchia)
    return _registry


def reset_registry() -> None:
    """Reset the global singleton (for testing)."""
    global _registry
    _registry = None
