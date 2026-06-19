"""Smoke tests for the hierarchia package."""

from pathlib import Path

import hierarchia
from hierarchia import ModuleType, Scale
from hierarchia.executor import ExecutableModule
from hierarchia.loader import extract_cross_references, load_hierarchia
from hierarchia.registry import get_registry, reset_registry
from hierarchia.validator import validate_hierarchy

REPO_ROOT = Path(__file__).resolve().parent.parent


def test_package_exports() -> None:
    exported = (
        "Hierarchia",
        "Module",
        "ModuleType",
        "Scale",
        "Stratum",
        "StratumType",
        "CrossReference",
    )
    for name in exported:
        assert hasattr(hierarchia, name)


def test_load_hierarchia() -> None:
    h = load_hierarchia(REPO_ROOT)
    assert h.stratum_count > 0
    assert h.module_count > 0
    assert h.module_count == sum(len(s.modules) for s in h.strata.values())


def test_registry_indexes_modules() -> None:
    reset_registry()
    try:
        reg = get_registry(REPO_ROOT)
        assert reg.count > 0
        assert len(reg.all()) == reg.count
    finally:
        reset_registry()


def test_registry_filters_are_consistent() -> None:
    reset_registry()
    try:
        reg = get_registry(REPO_ROOT)
        assert all(m.module_type is ModuleType.LAW for m in reg.by_type(ModuleType.LAW))
        assert all(Scale.META in m.scale for m in reg.by_scale(Scale.META))
    finally:
        reset_registry()


def test_search_returns_list() -> None:
    h = load_hierarchia(REPO_ROOT)
    assert isinstance(h.search_modules("entropy"), list)


def test_validate_hierarchy_runs() -> None:
    report = validate_hierarchy(REPO_ROOT)
    assert report.files_checked > 0
    assert report.files_parsed > 0
    assert isinstance(report.errors, list)
    assert isinstance(report.is_valid, bool)


def test_extract_cross_references() -> None:
    h = load_hierarchia(REPO_ROOT)
    assert isinstance(extract_cross_references(h), list)


def test_executable_module_modulate_is_pure() -> None:
    h = load_hierarchia(REPO_ROOT)
    module = next(m for s in h.strata.values() for m in s.modules)
    exe = ExecutableModule(module=module)
    variant = exe.modulate({"_smoke": True})
    assert variant.properties.get("_smoke") is True
    assert "_smoke" not in module.properties
