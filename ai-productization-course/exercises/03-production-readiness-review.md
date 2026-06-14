# 03 Production Readiness Review：PoC RAGの本番導入前レビュー

## 問題文
PoCで動くRAGアプリを、本番導入してよいかレビューしてください。

## 前提条件
- FastAPIでAPI化済み
- vector indexは手動更新
- ログは標準出力のみ
- 評価データは20件だけ

## 成果物
- 本番導入可否
- blocker一覧
- 監視項目
- rollback/fallback方針
- リリース後の改善計画

## 制約
- 障害時に検索、生成、データ鮮度、権限のどこが悪いか切り分けられること
- token costとlatencyの上限を定義すること
- prompt/model/indexのversionを追跡できること

## ヒント
画像AIのモデルリリースと同様に、評価、監視、rollbackなしの本番化は危険です。

## 模範回答
本番導入は条件付き不可。blockerは評価件数不足、index更新手順の手動依存、権限filterのテスト不足、ログ構造化不足、fallback未定義。最低限、構造化ログ、trace_id、retrieved_doc_ids、prompt_version、model_version、latency、token_cost、judge_score、user_feedbackを記録する。indexはblue/green方式で新旧を切り替え、異常時は旧indexまたは検索のみモードへfallbackする。

## よくある失敗
- Docker化だけで本番準備完了と考える
- rate limit、timeout、retryがない
- prompt変更をversion管理しない
- 人間確認フローがない

## 採点基準
- blocker特定: 30点
- observability設計: 25点
- rollback/fallback: 25点
- 継続改善: 20点
