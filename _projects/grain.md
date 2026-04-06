---
layout: project
title: "Grain"
category: "CLI Tool"
tags: [Python, Pillow, CLI]
order: 2
---

A command-line image processor that applies film-like grain and color grading to digital photos. Batch processing with presets.

Digital photos are technically perfect but sometimes lack the character of film. Grain adds that back — realistic grain patterns, subtle color shifts, and vignetting that mimic specific film stocks.

It runs from the command line with a simple interface: point it at a directory, pick a preset (Portra 400, Tri-X, Ektar), and it processes every image. Each preset was calibrated against scanned film samples.

Supports JPEG, PNG, and TIFF. Processes a batch of 100 images in under a minute on modest hardware.
