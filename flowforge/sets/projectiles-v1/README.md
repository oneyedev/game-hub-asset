# 투사체 기본 번들 v1

[정식 디자인 규격·역할 표·스튜디오 검수 절차](../../PROJECTILES.md)를 따른다. 14종 × 비행/명중 2개, 총 28 PNG는 승인된 메인 번들이다. `archer-01`·`mage-01`은 Studio 없이 내장 PNG를 사용한다. 각 폴더의 SVG는 원본이고 `meta.json`은 정규화 명세다. 원격 파일 수정 후 Art Studio에서 `projectiles-v1` 선택 또는 투사체 테스트의 원격 수정본 → Reload로 비교한다.

SVG 원본에서 다시 만들려면 CairoSVG를 설치하고 `python3 flowforge/tools/build_projectile_samples.py`를 실행한다. 재생성 뒤에는 PNG 변경을 검토하고 다시 채택해야 한다. 이 도구는 파일을 재생성하므로 직접 그린 시안 PNG를 보존하려면 별도 세트에 둔다.
