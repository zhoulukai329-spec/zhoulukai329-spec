"""Generate the profile README from profile.toml.

The generated section is deliberately plain Markdown/HTML so users can add their
own sections around it without coupling them to the generator.
"""
from __future__ import annotations

import html
import re
import tomllib
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "profile.toml"
README = ROOT / "README.md"
START = "<!-- PROFILE:GENERATED:START -->"
END = "<!-- PROFILE:GENERATED:END -->"


def badge(item: dict, accent: str) -> str:
    name = str(item["name"])
    logo = item.get("logo", "")
    color = item.get("color", accent).lstrip("#")
    params = f"&logo={quote(str(logo))}&logoColor=white" if logo else ""
    url = f"https://img.shields.io/badge/{quote(name)}-{color}?style=flat-square{params}"
    return f"[![{html.escape(name)}]({url})]({url})"


def render(data: dict) -> str:
    p, theme, stats = data["profile"], data["theme"], data["stats"]
    username = p["username"]
    lines = [
        '<div align="center">',
        '<picture><source media="(prefers-color-scheme: dark)" srcset="bloom-header-night.svg" />',
        f'<img src="bloom-header.svg" width="900" alt="{html.escape(p["name"])} — profile banner" /></picture>',
        f"\n# Hi, I'm {html.escape(p['name'])} 👋",
        f"**{html.escape(p['tagline'])}**",
        f"\n{html.escape(p['bio'])}",
        (f"\n📍 {html.escape(p['location'])}" if p.get("location") else ""),
        "</div>",
        '<div align="center"><picture><source media="(prefers-color-scheme: dark)" srcset="sky-night.svg" /><img src="sky.svg" width="900" alt="" /></picture></div>',
    ]
    links = [f"[GitHub](https://github.com/{quote(username)})"]
    for label, url in (("LinkedIn", p.get("linkedin")), ("Twitter", p.get("twitter")), ("Website", p.get("website")), ("Email", p.get("email"))):
        if url:
            links.append(f"[{label}]({url if label != 'Email' else 'mailto:' + url})")
    lines += ["\n" + " · ".join(links), "", "## Tech stack", ""]
    groups: dict[str, list[dict]] = {}
    for item in data.get("stack", []):
        groups.setdefault(item.get("group", "Tools"), []).append(item)
    for group, items in groups.items():
        lines.append(f"**{html.escape(group)}**  " + " ".join(badge(i, theme["accent"]) for i in items) + "\n")

    if any(stats.get(k) for k in ("show_stats", "show_streak", "show_activity")):
        lines += ["## GitHub activity", ""]
        if stats.get("show_stats"):
            lines.append(f'<img height="165" src="https://github-readme-stats.vercel.app/api?username={quote(username)}&show_icons=true&hide_border=true&theme=transparent&title_color={theme["accent"]}&icon_color={theme["accent"]}" alt="GitHub statistics for {html.escape(username)}" />')
        if stats.get("show_streak"):
            lines.append(f'<img height="165" src="https://streak-stats.demolab.com?user={quote(username)}&hide_border=true&background=00000000&ring={theme["accent"]}&fire={theme["accent"]}&currStreakLabel={theme["accent"]}" alt="GitHub contribution streak for {html.escape(username)}" />')
        if stats.get("show_activity"):
            lines.append(f'<img src="https://github-readme-activity-graph.vercel.app/graph?username={quote(username)}&bg_color=00000000&color={theme["label"]}&line={theme["accent"]}&point={theme["accent"]}&area=true&hide_border=true" alt="GitHub activity graph for {html.escape(username)}" />')
    if stats.get("show_snake"):
        lines += ["", "## Contribution graph", "", f'<img alt="Contribution graph for {html.escape(username)}" src="https://raw.githubusercontent.com/{quote(username)}/{quote(username)}/output/github-contribution-grid-snake.svg" />']
    if stats.get("show_profile_views"):
        lines += ["", f'![Profile views](https://komarev.com/ghpvc/?username={quote(username)}&label=Profile%20views&color={theme["accent"]}&style=flat)']
    lines += ["", '<div align="center"><picture><source media="(prefers-color-scheme: dark)" srcset="garden-footer-night.svg" /><img src="garden-footer.svg" width="900" alt="Profile footer" /></picture></div>']
    return "\n".join(lines) + "\n"


def main() -> None:
    data = tomllib.loads(CONFIG.read_text(encoding="utf-8"))
    generated = f"{START}\n{render(data)}{END}"
    current = README.read_text(encoding="utf-8") if README.exists() else ""
    if START in current and END in current:
        current = re.sub(re.escape(START) + r".*?" + re.escape(END), generated, current, flags=re.S)
    else:
        current = generated + "\n"
    README.write_text(current, encoding="utf-8")


if __name__ == "__main__":
    main()
