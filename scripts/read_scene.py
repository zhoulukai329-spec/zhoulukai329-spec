"""Expose scene settings from profile.toml as GitHub Actions outputs."""
import os
import tomllib
from pathlib import Path

scene = tomllib.loads((Path(__file__).resolve().parents[1] / "profile.toml").read_text(encoding="utf-8"))["scene"]
with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as output:
    for key in ("latitude", "longitude", "timezone", "weather", "season"):
        print(f"{key}={scene.get(key, '')}", file=output)
