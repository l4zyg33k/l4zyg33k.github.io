"""Generate per-page SEO descriptions from titles and taxonomy metadata."""

import re


PLATFORM_NAMES = {
    "platform/linux/arch-linux": "Arch Linux",
    "platform/cloud-native/kubernetes": "Kubernetes",
}

DOMAIN_NAMES = {
    "domain/ai/inference": "AI 추론",
    "domain/cloud-native/runtime": "클라우드 네이티브 런타임",
    "domain/desktop/input": "데스크톱 입력",
    "domain/development/toolchain": "개발 툴체인",
    "domain/hardware/display": "디스플레이 하드웨어",
    "domain/hardware/laptop": "랩탑 하드웨어",
    "domain/hardware/power": "전원 관리",
    "domain/hardware/printing": "프린팅",
    "domain/security/authentication": "인증 보안",
    "domain/security/cluster": "클러스터 보안",
    "domain/system/boot": "부팅 시스템",
    "domain/system/session": "세션 관리",
}


def _title(markdown: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", markdown, re.MULTILINE)
    return match.group(1).strip() if match else fallback


def on_page_markdown(markdown, *, page, config, files):
    """Set descriptions without requiring per-document markup."""
    source = page.file.src_uri
    if source == "index.md":
        page.meta["description"] = config.site_description
        return markdown
    if source == "tags.md":
        page.meta["description"] = "플랫폼, 도메인, 작업, 구성 요소 태그로 Linux와 인프라 치트시트를 탐색합니다."
        return markdown

    tags = page.meta.get("tags", [])
    platform = next((tag for tag in tags if tag.startswith("platform/")), "")
    domain = next((tag for tag in tags if tag.startswith("domain/")), "")
    title = _title(markdown, page.title or config.site_name)
    context = " · ".join(
        part for part in (PLATFORM_NAMES.get(platform), DOMAIN_NAMES.get(domain)) if part
    )
    prefix = f"{context} 환경의 " if context else ""
    page.meta["description"] = (
        f"{prefix}{title}. 패키지 설치, 설정, 실행 확인 및 트러블슈팅 절차를 정리한 기술 치트시트입니다."
    )[:160]
    return markdown
