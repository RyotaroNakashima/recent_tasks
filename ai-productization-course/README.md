# AI Productization Course

## 教材の目的
画像認識/OCRの実務経験を持つAIエンジニアが、LLMアプリケーション、RAG、評価設計、LLMOps/MLOpsを実務で説明・設計できる状態を目指すHTMLスライド教材です。「RAGを作れる」だけでなく、品質・失敗分類・運用・面接での説明まで扱います。

## 対象者
- Python、機械学習、画像認識、OCRの実務経験がある
- Donut、DETR、CLIP、OCR評価指標に馴染みがある
- Webバックエンド、クラウド、本番運用はこれから強化したい
- LLM/RAG/Agent領域へ転職・異動したい

## 学習順
1. `index.html` を開き全体像を確認
2. `slides/00-overview.html` から順番に学習
3. 各章末のミニ演習と確認問題に回答
4. `exercises/` の演習で設計書・評価計画・本番レビューを作成

## ローカルでの開き方
静的HTMLのため、ブラウザで `ai-productization-course/index.html` を開けます。簡易サーバーを使う場合は以下です。

```bash
cd ai-productization-course
python3 -m http.server 8000
```

## ファイル構成
```text
ai-productization-course/
  index.html
  README.md
  package.json
  slides/
  assets/
  exercises/
  checks/validate_course.py
```

## 各章の概要
- 00: 全体地図、キャリア接続、扱う範囲
- 01: LLMアプリとRAGの基本構造
- 02: chunking、embedding、vector DB、metadata、rerankingなどretrieval設計
- 03: prompt、citation、grounding、faithfulness、structured outputなどgeneration設計
- 04: retrieval評価、answer評価、golden dataset、LLM-as-a-judge
- 05: API化、Docker化、ログ、監視、コスト、fallback、rollback
- 06: 名刺OCRを営業支援RAG/CRM支援AIへ拡張するケーススタディ
- 07: 設計書、評価計画、本番チェック、面接回答、職務経歴書への変換

## 学習後にできるようになること
- LLM/RAGの基本構造と失敗パターンを説明できる
- retrieval評価とanswer評価を分けて設計できる
- hallucination、groundedness、faithfulnessを区別できる
- golden datasetとLLM-as-a-judgeの使いどころを説明できる
- 本番運用に必要なLLMOps要素をチェックリスト化できる
- OCR/画像AI経験をRAG/LLMアプリ開発の強みに変換して語れる

## 次に拡張すべき教材テーマ
- Agent設計とtool use
- MCPによるツール接続
- AIガバナンスとセキュリティ
- クラウド構成とIaC
- データエンジニアリングと継続的index更新

## 品質チェックコマンド
```bash
npm run goal
npm run validate
```
