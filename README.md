# Game Hub Asset — 개발용 공개 에셋 허브

게임별 최상위 폴더로 분리한다. **현재 게임은 `flowforge/`** 이며, 새 게임은 별도의 `<game-id>/` 폴더를 만든다. GitHub 공개 저장소이므로 비밀키·유료/비공개 원본·배포 자격 증명은 올리지 않는다.

## 폴더 규칙

- `flowforge/archer/base-i/`: 기본 아처 I 에셋
- `flowforge/manifests/`: 게임별/시나리오별 AssetProxy JSON 매니페스트
- `templates/`: 다른 게임에도 복사 가능한 매니페스트 템플릿
- `smoke/`: 파일 호스팅 진단용 이미지

## 바로 테스트

아처 노스킬 시나리오(`archer-01`)를 열고 게임 주소에 다음 쿼리 파라미터를 붙인다.

```text
?asset_manifest=https%3A%2F%2Fraw.githubusercontent.com%2Foneyedev%2Fgame-hub-asset%2Fmain%2Fflowforge%2Fmanifests%2Farcher-01.json
```

매니페스트는 `res://game/art/archer/base_i_two_unit/tower_back.png`를 `flowforge/archer/base-i/tower_back.png`로 치환한다. **기본 아처 I의 타워 후면만** 눈에 띄는 청록색/노란색 진단용 그림으로 바뀐다. 원본 아처 캐릭터·전면 레이어·다른 타워는 유지한다. 이미지가 실패하면 원본이 보인다.

기존 AssetProxy는 매니페스트 URL을 명시했을 때만 동작한다. 브라우저에서 새로고침하면 다시 내려받고 데스크톱에서는 F6으로 갱신한다. 매니페스트/이미지 HTTP 200, CORS, 실제 게임 교체는 브라우저에서 별도 검증한다.

## 새 게임/타워에 재사용

1. `<game-id>/<category>/<asset-name>.png`에 공개 테스트 이미지를 올린다.
2. `templates/manifest.example.json`을 복사하여 `<game-id>/manifests/<scenario-id>.json`을 만든다.
3. JSON 키를 게임의 **정확한 `res://` 텍스처 경로**로, 값을 이 저장소의 HTTPS Raw URL로 바꾼다.
4. `?asset_manifest=<URL-encoded manifest URL>`을 게임 주소에 붙인다. 게임의 렌더링 경로가 AssetProxy를 호출하도록 연결되어 있어야 한다.

이미지 아틀라스는 원본과 동일한 크기·프레임 배열을 유지한다. 동일한 파일명을 덮어쓸 때 CDN 캐시 및 브라우저 새로고침을 확인한다.
