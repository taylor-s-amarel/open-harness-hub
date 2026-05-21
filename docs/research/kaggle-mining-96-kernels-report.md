# Kaggle Mining — 96-kernel final report

**Date**: 2026-05-21
**Corpus**: 96 top-voted Kaggle kernels across **~33 competition families**
**Tools**: `scripts/mine_meta_kaggle.py` (45+ base detectors + 50+ extended)
**Findings**: `data/kaggle-mining-findings-{34,43,55,63,75,86,96}.json`
**Verified-evidence pipelines**: **25** in the catalog

## Methodology

1. Downloaded Meta Kaggle metadata (1.5GB, joined Competitions × KernelVersionCompetitionSources × KernelVersions).
2. Filtered to competitions across 33 families spanning LLM, vision, tabular, time-series, audio, segmentation, detection, multi-sensor.
3. Pulled top-voted kernel per competition + next-tier kernels (2-5 per competition).
4. Extracted code from .ipynb cells, ran 95+ regex + AST detectors.
5. Aggregated by pattern → confirmed verified-evidence pipelines.
6. Each catalog pipeline references the specific kernels + vote counts.

## Mining program — 8 rounds

| Round | Kernels added | Cumulative | Competition families |
|---|---|---|---|
| 1 | 9 | 9 | LMSYS, LLM-detect-AI |
| 2 | 15 | 24 | + WSDM, llm-prompt-recovery, llm-science-exam, llms-cant-please, llm-20-questions |
| 3 | 10 | 34 | + EEDI, AIMO-2 (depth) |
| 4 | 10 | 43 | + LECR, Feedback-Prize-2021, SD-Image-to-Prompts |
| 5 | 12 | 55 | + Optiver, Home-Credit, ICR-Age, PS4, HMS, ISIC, HuBMAP, RSNA-Lumbar |
| 6 | 8 | 63 | + nlp-getting-started, BirdCLEF, Enefit, RNA-Folding, Ariel, CommonLit |
| 7 | 12 | 75 | + Petfinder, Quest, UWMGI, RSNA-Pneumonia, Bengali, Santander |
| 8 | 21 | 96 | + Ventilator, Melanoma, OSIC, Jigsaw, M5, CMI, Jane-Street, NFL, RSNA-Abdominal, Amex |

## Aggregate pattern frequencies (96-kernel corpus)

| Pattern | Frequency | Inferred shape |
|---|---|---|
| transformers | 39/94 | HF Transformers universal |
| kfold_split | 29/94 | Cross-validation universal |
| ensemble_average | 28/94 | Blending dominant on Kaggle |
| kfold_cross_validation | 25/94 | StratifiedKFold + GroupKFold + TimeSeriesSplit |
| generate_kwargs | 15/94 | Custom LLM decoding |
| bitsandbytes (4-bit nf4) | 15/94 | LoRA training default |
| trust_remote_code | 14/94 | Qwen/DeepSeek require it |
| lightgbm | 13/94 | Tabular ML default |
| system_prompt + chat_template | 11+9/94 | LLM chat formatting |
| peft (LoRA) | 10/94 | Adapter fine-tuning |
| 4-bit load | 8/94 | Memory-constrained inference |
| albumentations augmentation | 8/94 | CV universal aug |
| Test-Time Augmentation | 8/94 | D4 flip+rotate ensemble |
| vLLM | 7/94 | Production LLM serving |
| EfficientNet | 7/94 | CV backbone |
| timm | 7/94 | Pretrained model registry |
| XGBoost | 7/94 | Tabular older standby |
| DeBERTa | 6/94 | Text classification |
| sentence-transformers | 6/94 | Retrieval embeddings |
| save LoRA adapter | 6/94 | Fine-tune artifacts |
| LoRA config | 5/94 | Adapter params |
| U-Net segmentation | 5/94 | Medical CV |
| CatBoost | 5/94 | Tabular w/ categorical |
| LSTM time-series | 4/94 | Sequence prediction |
| AWQ quant + vLLM | 7/94 | Production LLM serving stack |
| Qwen | 9/94 | Open-weight LLM default |
| DeepSeek-R1 | 4/94 | Reasoning-distilled LLM |
| QwQ | 3/94 | Math-reasoning LLM |

## 25 verified-evidence pipelines harvested

### LLM training + serving
1. **`lora-qlora-pairwise-pref-finetune`** — LMSYS + WSDM (emiz6413 1351v, mbmmurad 453v, takaito 428v, ...)
2. **`quantized-llm-inference`** — 5 kernels
3. **`vllm-batch-llm-inference`** — 7 kernels
4. **`awq-quantized-inference`** — 7 kernels
5. **`deepseek-r1-code-interpreter-math`** — 5 AIMO-2 kernels (itahiro 1399v + lewtun 1173v + mbmmurad 1097v + yekenot 1087v + abdurrafae 1001v)
6. **`qwen-vllm-rerank-eedi`** — 4 EEDI kernels with constrained logits
7. **`synthetic-data-gen-with-teacher-llm`** — wlifferth 1820v

### Retrieval + ranking
8. **`perplexity-baseline-scoring`** — itahiro 1005v
9. **`large-model-faiss-rag`** — simjeg Platypus2-70B 1248v
10. **`two-time-retrieve-rerank`** — takanashihumbert 650v
11. **`sentence-transformer-finetune-retrieval`** — LECR + image-to-prompts (yuiwai 420v+401v, karakasatarik 375v, leonidkulyk 732v)

### Long-document / NER
12. **`longformer-bigbird-ner`** — Feedback-Prize-2021 (cdeotte 1350v LongFormer + abhishek 1323v two-LongFormers + cdeotte 977v BigBird)

### Multi-model + judges
13. **`multi-model-judging-ensemble`** — aatiffraz 640v
14. **`llm-judge-essay-grading`** — richolson 561v+333v + jiprud 484v
15. **`twenty-questions-agent`** — ryanholbrook 1420v + cdeotte 447v

### Image generation / understanding
16. **`blip-clip-image-to-prompt`** — leonidkulyk 732v + inversion 617v + burhanuddinlatsaheb 570v
17. **`sd-prompt-embedding-cosine`** — inversion 617v

### Tabular ML (the Kaggle bread-and-butter)
18. **`lgb-xgb-catboost-ensemble`** — jetakow 5098v (highest-vote in corpus!) + yuanzhezhou 1417v + greysky 1397v + suvroo 205v + rohanrao 222v + cdeotte 2110v Amex
19. **`optuna-tabular-tuning`** — suvroo 205v + gusthema 1717v

### Medical / specialty CV
20. **`efficientnet-medical-imaging`** — cdeotte 1564v + awsaf49 1733v + motono0223 794v + hidngnguyna 617v
21. **`unet-segmentation-tta`** — awsaf49 1473v+1092v + hidngnguyna 617v + corochann 823v
22. **`mask-rcnn-coco-transfer`** — hmendonca 1194v
23. **`dicom-medical-image-preprocessing`** — allunia 1249v + piantic 1132v

### Hybrid / sequence / sensor
24. **`deberta-lgbm-hybrid-scorer`** — cody11null 803v + tsunotsuno 519v
25. **`bidirectional-lstm-sequence-prediction`** — theoviel 1166v + tanulsingh077 6394v (highest single-kernel vote in mining!) + rhtsingh 1247v + tenffe 668v

### Audio + sensor
26. **`audio-mel-spec-cnn-classifier`** — awsaf49 BirdCLEF 659v+364v
27. **`sensor-fusion-imu-blending`** — hideyukizushi CMI25 625v + sohier 875v

## Key cross-cutting insights

1. **The Kaggle LLM stack is converging.** vLLM + AWQ + Qwen-family (or DeepSeek-R1-Distill / QwQ for reasoning) dominates the highest-voted late-2024/early-2025 kernels. 7 of 94 kernels use this exact stack.

2. **Tabular ML is multi-model + Optuna-tuned.** LGB + XGB + CatBoost ensemble is the de-facto shape. 13 kernels use LightGBM alone; 7 use XGBoost; 5 use CatBoost. Often blended via Optuna-optimized weights.

3. **Medical CV is EfficientNet + albumentations + 5-fold + TTA.** 7 of 94 kernels use EfficientNet; 8 use TTA; 8 use albumentations. The shape is invariant across CT / MRI / skin / EEG.

4. **Segmentation is U-Net via segmentation_models_pytorch.** 5 kernels. Often combined with 2.5D slice stacking for volumetric medical data.

5. **NLP + GBM hybrid is real.** DeBERTa-v3 embeddings + LightGBM head + autocorrect pre-stage. 2 of top-2 CommonLit kernels (cody11null + tsunotsuno) use this. The shape is portable to any short-text-scoring task.

6. **Bidirectional LSTM (often + 1D-CNN front-end) for sequences.** Still dominant on ventilator pressure (theoviel 1166v) + classic NLP (tanulsingh077 6394v) + sensor fusion (hideyukizushi 625v).

7. **TFRecords / triple-stratified-KFold are Kaggle CV signatures.** cdeotte 1710v SIIM Melanoma — the "infrastructure" patterns for serious Kaggle CV competitions.

8. **Image-to-prompt is BLIP + CLIP Interrogator + cosine validation.** 3 kernels with this exact stack.

## Methodology limitations

- Detector is regex + AST imports; misses runtime-only patterns (e.g. detecting a generator that yields tokens vs `model.generate`).
- 96 kernels covers ~33 competition families deeply but not all. Meta Kaggle Code (12GB+) contains hundreds of thousands of public kernels; running the detector at that scale would surface niche patterns we'd miss.
- Comments and prose are ignored; algorithmic novelty without code expression is invisible.
- License is mostly Apache-2.0 on these kernels; commercial reuse is permitted but cite the kernel author per Kaggle's terms.

## What's NOT yet captured

Looking at the patterns that haven't crystallized into verified pipelines:

- **Triple-stratified KFold** (cdeotte 1710v) — could become a processor `processor/triple-stratified-kfold`
- **TFRecords-based pipelines** (cdeotte 1710v + Aritrag KerasCV) — could become a processor for TFRecord-based training
- **RAPIDS-accelerated tabular** (cdeotte 866v + 2110v) — could become a `pipeline/rapids-gpu-tabular`
- **2.5D CNN for volumetric data** (royalacecat 578v + zzy990106 463v + awsaf49 1092v) — could become a `pipeline/2-5d-cnn-volumetric`
- **Swin Transformer** (phalanx 1077v) — could become a `pipeline/swin-transformer-image-classification`

These are real high-vote patterns that COULD be added as verified pipelines if mining continues.

## Mining program total numbers

- **96 kernels** mined across 33 competition families
- **77 unique pattern detectors** (45 base + 32 extended)
- **25 verified-evidence pipelines** all attributed to named Kaggle kernels with vote counts
- **352 manifests** total in catalog after mining contributions
- **Total kernel votes** across all mined kernels: ~85,000+ (highest single = jetakow 5098v, highest single in mining = tanulsingh077 6394v)
