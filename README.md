# Game Hub Asset — 개발용 공개 에셋 허브

게임별 최상위 폴더로 분리한다. **현재 게임은 `flowforge/`** 이며, 새 게임은 별도의 `<game-id>/` 폴더를 만든다. GitHub 공개 저장소이므로 비밀키·유료/비공개 원본·배포 자격 증명은 올리지 않는다.

## 폴더 규칙

- `flowforge/archer/base-i/`: 기본 아처 I 에셋
- `flowforge/manifests/`: 게임별/시나리오별 AssetProxy JSON 매니페스트
- `templates/`: 다른 게임에도 복사 가능한 매니페스트 템플릿
- `smoke/`: 파일 호스팅 진단용 이미지

## 바로 테스트

아처 노스킬 시나리오(`archer-01`)를 열고 게임 주소에 **`?asset_hub=archer-01`** 을 붙인다. 긴 URL을 직접 쓰려면 아래 쿼리도 지원한다.

```text
?asset_manifest=https%3A%2F%2Fraw.githubusercontent.com%2Foneyedev%2Fgame-hub-asset%2Fmain%2Fflowforge%2Fmanifests%2Farcher-01.json
```

매니페스트는 `variants.A`와 `variants.B`에 기본 아처 I의 `tower_back.png` 대체 이미지를 등록한다. 개발용 비교 패널의 **A / B / Original / Reload** 버튼으로 즉시 전환한다. A는 목조, B는 석조 진단용 도형이다. 원본 궁수 캐릭터·전면 레이어·다른 타워는 유지한다. 실패한 이미지는 원본으로 대체한다.

기존 AssetProxy는 매니페스트 URL을 명시했을 때만 동작한다. 브라우저에서 새로고침하면 다시 내려받고 데스크톱에서는 F6으로 갱신한다. 매니페스트/이미지 HTTP 200, CORS, 실제 게임 교체는 브라우저에서 별도 검증한다.

## 새 게임/타워에 재사용

1. `<game-id>/<category>/<variant-id>/<asset-name>.png`에 공개 테스트 이미지를 올린다.
2. `templates/manifest.example.json`을 복사하여 `<game-id>/manifests/<scenario-id>.json`을 만든다.
3. JSON의 `variants` 안에 A/B/C 디자인별 `textures` 사전을 두고, 키를 게임의 **정확한 `res://` 텍스처 경로**, 값을 HTTPS Raw URL로 설정한다.
4. `?asset_manifest=<URL-encoded manifest URL>`을 게임 주소에 붙인다. 게임의 렌더링 경로가 AssetProxy를 호출하도록 연결되어 있어야 한다.

이미지 아틀라스는 원본과 동일한 크기·프레임 배열을 유지한다. 동일한 파일명을 덮어쓸 때 CDN 캐시 및 브라우저 새로고침을 확인한다.
