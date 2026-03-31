from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


CONFIG_PATH = Path("configs/config.yaml")


def find_project_root(start: str | Path | None = None) -> Path:
    """Return the repository root by walking up until the config file appears."""
    current = Path(start or Path.cwd()).resolve()
    for candidate in (current, *current.parents):
        if (candidate / CONFIG_PATH).exists():
            return candidate
    raise FileNotFoundError("Could not locate configs/config.yaml from the current path.")


def load_config(root: str | Path | None = None) -> dict[str, Any]:
    project_root = find_project_root(root)
    with (project_root / CONFIG_PATH).open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def project_paths(root: str | Path | None = None) -> dict[str, Path]:
    config = load_config(root)
    project_root = find_project_root(root)
    return {name: project_root / relative_path for name, relative_path in config["paths"].items()}


def ensure_standard_dirs(root: str | Path | None = None) -> dict[str, Path]:
    paths = project_paths(root)
    for path in paths.values():
        path.mkdir(parents=True, exist_ok=True)
    return paths
