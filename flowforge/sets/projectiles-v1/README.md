# 투사체 기준 샘플 v1

[정식 디자인 규격·역할 표·스튜디오 검수 절차](../../PROJECTILES.md)를 따른다. 14종 × 비행/명중 2개, 총 28 PNG다. 각 폴더의 SVG는 원본이고 `meta.json`은 정규화 명세다. 원격 파일 수정 후 Art Studio에서 `projectiles-v1` 선택 또는 투사체 테스트의 원격 시안 → Reload로 비교한다.

SVG 기준 샘플을 다시 만들려면 CairoSVG를 설치하고 `python3 flowforge/tools/build_projectile_samples.py`를 실행한다. 이 도구는 기준 샘플을 재생성하므로 직접 그린 시안 PNG를 보존하려면 별도 세트에 둔다.
