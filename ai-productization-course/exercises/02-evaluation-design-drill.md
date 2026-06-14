# 02 評価設計演習：RAGの評価データセットと改善サイクル

## 問題文
社内文書RAGの本番導入可否を判断する評価計画を作ってください。

## 前提条件
- 100件の代表質問を人手で集められる
- 正解文書と期待回答を専門家が確認できる
- 本番ログは匿名化して利用できる

## 成果物
- golden dataset仕様
- retrieval指標
- answer指標
- failure taxonomy
- LLM-as-a-judge利用方針
- regression test計画

## 制約
- retrieval評価とanswer評価を混ぜない
- LLM judgeだけで合否判定しない
- 個人情報を評価データに残さない

## ヒント
OCRの文字認識精度と項目一致率を分けるように、RAGでも検索品質と回答品質を分離します。

## 模範回答
golden datasetはquestion、expected_doc_ids、must_include_facts、forbidden_claims、expected_answer、difficulty、user_roleを持つ。retrievalはrecall@5、MRR、context precisionを測る。answerはcorrectness、groundedness、faithfulness、completeness、concisenessを人間評価とLLM judgeで二重化する。失敗分類は検索漏れ、ノイズ混入、古い文書、権限違反、根拠なし生成、過剰回答に分ける。

## よくある失敗
- end-to-endの満足度だけで判断する
- judge promptを固定せず毎回変える
- 難問だけ、または簡単な質問だけで評価する
- ログ改善の承認フローがない

## 採点基準
- データセット設計: 30点
- 指標分離: 30点
- 失敗分類: 20点
- 改善サイクル: 20点
