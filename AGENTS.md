# Repository Guidelines for AI Agents

이 저장소는 개인용 리눅스/인프라 기술 치트시트 저장소입니다.

## 1. 파일 생성 규칙

- 새 문서는 반드시 `docs/<카테고리>/<파일명>.md` 경로에 생성한다.
  - 카테고리 예: `archlinux`, `kubernetes`, `devops`, `network`
- 문서 작성 후 `mkdocs.yml`의 `nav:` 섹션에 해당 문서 링크를 추가한다.
- `index.md`와 `generated/catalog.md`는 빌드 단계에서 `scripts/generate_navigation.py`가 front matter를 바탕으로 생성한다. 직접 작성하거나 수정하지 않는다.

## 2. 문서 템플릿

모든 치트시트 문서는 서론/인사말을 생략하고 아래 순서로 작성한다. YAML front matter는 문서 분류를 위한 메타데이터이므로 H1 앞에 둘 수 있다.

1. YAML front matter: `tags`와 `doc_type`을 반드시 지정한다.
2. `# [도구명/작업명] 치트시트`
3. `> 환경: OS 버전, 커널 버전 등`
4. `## 1. 패키지 설치` (명령어 블록)
5. `## 2. 설정 파일` (경로 명시 + 코드 블록)
6. `## 3. 서비스 실행 및 확인`
7. `## 4. 트러블슈팅` (MkDocs `!!! warning` 콜아웃 문법 사용)

### 태그 분류 체계

문서 분류는 단일 폴더 트리가 아닌 **통제 어휘 기반 패싯 분류**를 사용한다. 하나의 기술 문서는 여러 영역에 속하므로, 태그 접두어로 다단계 분류를 표현한다. 새 태그를 만들기 전에 기존 어휘를 사용하고, 각 치트시트에는 플랫폼·도메인·작업 태그를 각각 정확히 1개, 구성 요소 태그를 1~2개 지정한다.

1. 플랫폼 (`platform/<영역>/<제품>`): `platform/linux/arch-linux`, `platform/cloud-native/kubernetes`
2. 도메인 (`domain/<영역>/<세부영역>`): `domain/system/boot`, `domain/system/session`, `domain/desktop/input`, `domain/hardware/display`, `domain/hardware/laptop`, `domain/hardware/power`, `domain/hardware/printing`, `domain/ai/inference`, `domain/security/authentication`, `domain/security/cluster`, `domain/cloud-native/runtime`, `domain/development/toolchain`
3. 작업 (`task/<행위>`): `task/install`, `task/configure`, `task/operate`, `task/troubleshoot`, `task/lab`
4. 구성 요소 (`component/<도구명>`): `component/systemd-boot`, `component/plymouth`, `component/fcitx5`, `component/podman`처럼 제품 또는 핵심 도구명을 소문자 kebab-case로 사용한다.

`doc_type`은 Diátaxis 방식의 `how-to`, `tutorial`, `reference`, `explanation` 중 하나를 사용한다. 이 저장소의 치트시트는 기본적으로 `how-to`다. 이 분류는 DITA의 task/concept/reference 정보 유형 원칙과 함께 사용한다.

### 다이어그램 및 이미지

- 프로세스, 네트워크 논리 토폴로지, 의존성, 시퀀스는 Markdown의 `mermaid` 코드 블록으로 작성한다. Mermaid 원본을 보존하며, 같은 내용을 래스터 이미지로 대체하지 않는다.
- 물리 배선, 랙 위치, 포트 번호처럼 정밀한 도면은 원본 편집 파일과 SVG를 `docs/assets/`에 함께 둔다.
- ASCII art는 짧은 터미널 출력 또는 단순 트리에만 사용한다. 복잡한 네트워크 토폴로지에는 사용하지 않는다.
- 다이어그램 전후에 연결 관계와 핵심 동작을 문장으로 설명한다. 노드 이름에는 실제 IP, 도메인, 비밀번호, 토큰을 넣지 않는다.

## 3. 개인정보 및 민감정보 마스킹

- 홈 디렉터리 경로: `/home/사용자명`은 `~` 또는 `$HOME`으로 표기한다.
- 사설/공인 IP 주소: 실제 IP 대신 `192.168.1.X`, `10.0.0.X`를 사용한다.
- 도메인, 비밀번호, API 토큰은 더미 문자열로 치환한다. 단, GitHub Pages 배포 설정의 `docs/CNAME` 및 `mkdocs.yml`의 `site_url`에는 승인된 사용자 지정 도메인 `www.miralove.pe.kr`을 사용할 수 있다.

## 4. 시각 디자인 및 UX

- 테마의 기준은 [Zenburn](https://github.com/jnurmine/zenburn) 팔레트다. Material의 기본 이름 팔레트(예: `cyan`)를 지정하지 않고, `docs/stylesheets/extra.css`의 의미 기반 CSS 변수로 색상을 적용한다.
- 다크 모드 표면은 `#3f3f3f`(본문), `#2b2b2b`(헤더·코드), `#1e2320`(푸터 메타)로 구성한다. 전경색은 `#dcdccc`, 보조 텍스트는 `#9fafaf` 또는 `#709080`을 사용한다.
- 라이트 모드는 Zenburn 밝은 파생 팔레트를 사용한다. 본문 `#f3f0df`, 코드 `#e6e3d1`, 헤더·푸터 `#4f4f4f`, 전경색 `#3f3f3f`을 유지한다.
- UX 색상 역할은 고정한다: 인터랙션·링크·포커스 `#93e0e3`(다크) 또는 `#3f7f7f`(라이트), 성공 `#7f9f7f`, 주의 `#f0dfaf`, 오류 `#cc9393`, 보조 강조 `#dfaf8f`, 정보 `#8cd0d3`.
- 본문과 UI는 Google Fonts의 `Gothic A1`을, 코드·콘솔·인라인 코드는 `JetBrains Mono`를 사용한다.
- 헤더와 푸터는 본문 배경과 명확한 대비를 유지한다. 색상만으로 상태를 전달하지 말고, 아이콘·텍스트·테두리 등 보조 단서를 함께 사용한다.
