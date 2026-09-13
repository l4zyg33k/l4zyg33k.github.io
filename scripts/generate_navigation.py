"""Generate the home page and document catalog from document front matter."""

from collections import defaultdict
from pathlib import Path
import re

import mkdocs_gen_files
import yaml


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
EXCLUDED = {"index.md", "tags.md"}

PLATFORM_NAMES = {
    "platform/linux/arch-linux": "Linux / Arch Linux",
    "platform/cloud-native/kubernetes": "Cloud Native / Kubernetes",
}

DOMAIN_NAMES = {
    "domain/ai/inference": "AI / 추론",
    "domain/cloud-native/runtime": "런타임",
    "domain/desktop/input": "데스크톱 / 입력",
    "domain/development/toolchain": "개발 툴체인",
    "domain/hardware/display": "하드웨어 / 디스플레이",
    "domain/hardware/laptop": "하드웨어 / 랩탑",
    "domain/hardware/power": "하드웨어 / 전원",
    "domain/hardware/printing": "하드웨어 / 프린팅",
    "domain/security/authentication": "보안 / 인증",
    "domain/security/cluster": "보안 / 클러스터",
    "domain/system/boot": "시스템 / 부팅",
    "domain/system/session": "시스템 / 세션",
}


def front_matter(path: Path) -> dict:
    content = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    return yaml.safe_load(match.group(1)) if match else {}


def title(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line.removeprefix("# ")
    return path.stem.replace("-", " ").title()


documents = []
for path in sorted(DOCS.rglob("*.md")):
    relative = path.relative_to(DOCS).as_posix()
    if relative in EXCLUDED or relative.startswith("generated/"):
        continue

    metadata = front_matter(path)
    tags = metadata.get("tags", [])
    platform = next((tag for tag in tags if tag.startswith("platform/")), "platform/other")
    domain = next((tag for tag in tags if tag.startswith("domain/")), "domain/other")
    documents.append(
        {
            "path": relative,
            "title": title(path),
            "platform": platform,
            "domain": domain,
            "tags": tags,
        }
    )


by_platform = defaultdict(list)
for document in documents:
    by_platform[document["platform"]].append(document)

cards = []
for platform, items in sorted(by_platform.items()):
    name = PLATFORM_NAMES.get(platform, platform.removeprefix("platform/").replace("/", " / "))
    anchor = name.lower().replace(" / ", "-").replace(" ", "-")
    domains = sorted({DOMAIN_NAMES.get(item["domain"], item["domain"].removeprefix("domain/")) for item in items})
    cards.append(
        f'''<a class="l4zy-card" href="generated/catalog/#{anchor}">
<span>{name}</span>
<strong>{len(items)}개 치트시트</strong>
<small>{" · ".join(domains)}</small>
</a>'''
    )

home = f'''# L4zyG33k Cheatsheets

Linux와 인프라 운영 기록을 재현 가능한 설정과 명령 중심으로 정리합니다.

<div class="l4zy-card-grid">
{chr(10).join(cards)}
</div>

## 라이선스

이 사이트의 원본 콘텐츠는 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.ko)으로 제공됩니다. 출처를 표시하면 복사·수정·재배포할 수 있으며, 변경한 콘텐츠 역시 같은 라이선스로 공유해야 합니다.

## 작성 방식

일부 문서 구조화·초안·코드 작업에는 AI 코딩 에이전트를 보조 도구로 활용했습니다. 기술 내용의 검토와 최종 편집 책임은 사용자에게 있습니다.
'''

with mkdocs_gen_files.open("index.md", "w") as file:
    file.write(home)

catalog_lines = ["# 문서 탐색", "", "문서 front matter의 플랫폼·도메인 태그에서 자동 생성됩니다.", ""]
for platform, items in sorted(by_platform.items()):
    name = PLATFORM_NAMES.get(platform, platform.removeprefix("platform/").replace("/", " / "))
    catalog_lines.extend([f"## {name}", ""])
    by_domain = defaultdict(list)
    for item in items:
        by_domain[item["domain"]].append(item)
    for domain, domain_items in sorted(by_domain.items()):
        catalog_lines.extend([f"### {DOMAIN_NAMES.get(domain, domain.removeprefix('domain/'))}", ""])
        for item in domain_items:
            catalog_lines.append(f"- [{item['title']}](../{item['path']})")
        catalog_lines.append("")

with mkdocs_gen_files.open("generated/catalog.md", "w") as file:
    file.write("\n".join(catalog_lines))
