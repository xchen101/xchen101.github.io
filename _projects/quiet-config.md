---
layout: project
title: "Quiet Config"
category: "Open Source"
tags: [Node.js, TypeScript]
order: 4
---

A zero-dependency configuration library for Node.js. Reads YAML, JSON, and env files with sane defaults and no surprises.

Most config libraries try to do too much. Quiet Config does three things: reads your config files, merges them in a predictable order, and gives you typed access to the values. No magic, no plugins, no runtime dependencies.

It supports YAML, JSON, and `.env` files out of the box. Config sources are merged in a clear priority order: defaults, then file, then environment variables, then CLI flags. TypeScript types are inferred from your schema.

The name is the philosophy — configuration should be quiet. It should work without you thinking about it.
