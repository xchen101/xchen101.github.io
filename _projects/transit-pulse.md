---
layout: project
title: "Transit Pulse"
category: "Data Pipeline"
tags: [Python, D3.js, Kafka]
order: 3
---

Real-time public transport data visualizer. Ingests live feeds, maps delay patterns across the network over time.

Public transport networks generate enormous amounts of real-time data — arrival predictions, service alerts, GPS positions. Transit Pulse ingests these feeds via Kafka, processes them into delay metrics, and renders the results as an interactive D3.js map.

You can watch delay waves propagate through the network in real time, or scrub back through historical data to spot recurring bottlenecks. The visualization uses color intensity to show severity and animation to show propagation direction.

Built as a weekend project that grew into something more useful than expected.
