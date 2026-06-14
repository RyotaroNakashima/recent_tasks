# 01 RAG設計演習：OCR済み文書、社内FAQ、議事録、CRMデータ

## 問題文
複数データソースを横断し、営業担当者が自然言語で問い合わせられるRAGを設計してください。

## 前提条件
- OCR済みPDF、社内FAQ、議事録、CRMデータがある
- 個人情報と権限管理が必要
- OCRには誤字、表崩れ、重複が含まれる

## 成果物
- データソース一覧
- chunking方針
- metadata設計
- retrieval/reranking方針
- 権限制御方針

## 制約
- 権限外文書を検索結果に出さない
- 古いCRM情報を優先しない
- 根拠文書をcitationとして表示する

## ヒント
OCR評価の誤差分析と同じく、どこで情報が落ちるかを分解してください。

## 模範回答
FAQは質問単位、議事録は議題単位、設計書やOCR文書は見出しベースとparent-child chunkを併用する。metadataにはsource_type、owner_team、created_at、updated_at、customer_id、access_group、ocr_confidenceを持たせる。検索時はaccess_groupで事前filterし、BM25とembeddingのhybrid search後にrerankerで上位文脈を選ぶ。

## よくある失敗
- すべて固定長chunkにする
- OCR信頼度をmetadataに入れない
- 権限filterを生成後に行う
- 最新性をrankingに入れない

## 採点基準
- データ特性別のchunking: 25点
- metadataとfiltering: 25点
- retrieval/reranking設計: 25点
- 運用・権限・鮮度への配慮: 25点
