---
title: Field Reports
layout: page
permalink: /field-reports/
---

## Field Reports

**Triton-Kernel Autotuning for Sparse Attention at Scale**\\
Anselm Ferreira \*, *<ins>Noemi Halvorsen</ins>* \*, Yuki Tanabe, Priyanka Devan, Marisol Quintero, Devin Achebe \*, Lior Bercovici\\
MLSys 2026. [[link]](https://raw.githubusercontent.com/wholetherapi/filesystem_playwright_with_chunk_scholarly_arxiv_local_pdf-tools_memory_github_1991-arc-m8w2k5/main/records/nimbus-sparse-attn.json) [[brief]](https://raw.githubusercontent.com/wholetherapi/filesystem_playwright_with_chunk_scholarly_arxiv_local_pdf-tools_memory_github_1991-arc-m8w2k5/main/briefs/nimbus-sparse-attn.pdf)
* Autotuned Triton kernels for block-sparse attention against a PyTorch reference implementation.
* Profiled occupancy and memory traffic to pick per-shape launch configurations on Kubernetes GPU pools.
* Cut time-to-first-token by 38% at parity accuracy on production traffic.


**Vectorized Reranking with Learned Quantization**\\
Sofia Berglund \*, *<ins>Noemi Halvorsen</ins>* \*, Amara Nwosu, Felix Grimaldi, Hana Sato \*, Oskar Vinter\\
ECIR 2026. [[link]](https://raw.githubusercontent.com/wholetherapi/filesystem_playwright_with_chunk_scholarly_arxiv_local_pdf-tools_memory_github_1991-arc-m8w2k5/main/records/quantized-rerank.json) [[brief]](https://raw.githubusercontent.com/wholetherapi/filesystem_playwright_with_chunk_scholarly_arxiv_local_pdf-tools_memory_github_1991-arc-m8w2k5/main/briefs/quantized-rerank.pdf)
* Combined FAISS graph traversal with learned product quantization for compact vector indexes.
* Vectorised the reranking stage in NumPy to keep batch latency predictable.
* Held Recall@10 within 0.4 points of the float baseline at a quarter of the memory footprint.


**Streaming Sketch Structures for Tail-Latency Monitoring**\\
*<ins>Noemi Halvorsen</ins>* \*, Kenji Arata\\
ACM Operational ML Workshop 2025. [[link]](https://raw.githubusercontent.com/wholetherapi/filesystem_playwright_with_chunk_scholarly_arxiv_local_pdf-tools_memory_github_1991-arc-m8w2k5/main/records/sketch-monitor.json) [[brief]](https://raw.githubusercontent.com/wholetherapi/filesystem_playwright_with_chunk_scholarly_arxiv_local_pdf-tools_memory_github_1991-arc-m8w2k5/main/briefs/sketch-monitor.pdf)
* Maintained mergeable sketch structures for streaming tail-latency estimates.
* Computed sketches in Spark and exported them to Prometheus.
* Paged on Grafana when the estimated p99 crossed its latency budget.


**Adaptive Cache Partitioning for Multi-Tenant Feature Stores**\\
*<ins>Noemi Halvorsen</ins>* \*, Tobias Lindqvist \*, Rhea Mendonca\\
Journal of Data Systems Engineering 2024. [[link]](https://raw.githubusercontent.com/wholetherapi/filesystem_playwright_with_chunk_scholarly_arxiv_local_pdf-tools_memory_github_1991-arc-m8w2k5/main/records/cache-partition.json) [[brief]](https://raw.githubusercontent.com/wholetherapi/filesystem_playwright_with_chunk_scholarly_arxiv_local_pdf-tools_memory_github_1991-arc-m8w2k5/main/briefs/cache-partition.pdf)
* Modelled per-tenant cache demand from dbt-managed warehouse tables.
* Repartitioned the shared cache with a Spark job and per-tenant quotas.
* Exposed SLO compliance through SQL dashboards for the platform team.

