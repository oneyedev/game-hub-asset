# Game Hub Asset

Flowforge의 게임용 디자인 세트와 원격 수정 후보를 관리한다. 아처 성장형 10종의 **Village**는 채택되어 [games-hub](https://github.com/oneyedev/games-hub)의 `game/art/sets/village/`에 빌드 기본 에셋으로 포함된다.

- [Flowforge 제작 가이드](flowforge/README.md)
- [Village 파일 규격·전체 미리보기](flowforge/sets/village/README.md)
- [원격 세트 목록](flowforge/sets.json)
- [마법사 노스킬 8형태 후보](flowforge/sets/village/towers/mage/README.md) — `mage-01`의 Art Studio에서 `village`로 비교한다. 아처 내장본과 별개인 원격 PNG 24개다.

게임은 네트워크 없이 내장 Village를 표시한다. Art Studio의 **Built-in Village**는 내장본이고, **village**는 이 저장소 최신 수정본과의 선택적 비교다. 이 저장소의 이미지를 수정하고 Reload하면 원격 후보가 갱신되지만 이미 배포한 내장본은 바뀌지 않는다. 기본 에셋을 갱신하려면 게임 저장소의 고정 PNG·소스 해시를 갱신하고 빌드한다.

납품은 알파 PNG, 정확한 캔버스·프레임 순서·기준점·여백을 유지한다. 후면·인물/무기·전면을 합치지 않는다. 원격 파일 추가 시 `sets.json`의 `files`와 게임의 리소스 매핑을 확인한다. 출처·라이선스를 보존한다.

구형 아처 시험 PNG, Forest/Stone 도형 후보, 전용 `archer-01` 매니페스트는 삭제했다. 현재 카탈로그는 Village만 제공한다.
