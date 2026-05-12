---
title: "Code Review Checklist"
validation-target: "Diff under review plus related story/spec context"
validation-criticality: "HIGH"
required-inputs:
  - "Diff output or reviewed commit range"
  - "Story/spec file when available"
  - "Relevant project context and sprint status when available"
optional-inputs:
  - "Test output"
  - "CI logs"
  - "Runtime logs for failing paths"
---

# Code Review Checklist

Use this checklist when executing `bmad-code-review`. Keep findings evidence-based, actionable, and tied to the reviewed diff.

## Scope and Context

- [ ] The review source is explicit: staged, uncommitted, branch diff, commit range, or provided diff.
- [ ] Diff stats and reviewed file list are known before review.
- [ ] Story/spec context is loaded when available.
- [ ] The project sprint status is checked when the review is story-driven.
- [ ] Existing user or agent changes outside the review scope are not reverted or mixed into findings.

## Acceptance and Behavior

- [ ] Every relevant acceptance criterion is checked against the implementation.
- [ ] Existing response contracts, route behavior, status codes, UI copy, and data shapes remain compatible unless the story explicitly changes them.
- [ ] Error and fallback paths preserve intended user-facing behavior.
- [ ] Edge cases, empty states, retries, duplicate events, and degraded external services are considered.

## Security, Privacy, and Compliance

- [ ] Secrets, tokens, raw headers, cookies, and authorization data are not logged or captured.
- [ ] User-identifying or sensitive product data is not exposed beyond the story's explicit allowance.
- [ ] Medical-adjacent safety language remains non-diagnostic and does not overpromise.
- [ ] New env gates or production requirements are documented and fail safely.

## Architecture and Maintainability

- [ ] The implementation follows existing local patterns and helper APIs.
- [ ] New abstractions are justified by reuse, safety, or meaningful complexity reduction.
- [ ] No unnecessary dependencies, schemas, services, dashboards, or broad refactors are introduced.
- [ ] Client/server/runtime boundaries are respected.
- [ ] Test seams are not reachable in production unless explicitly intended and guarded.

## Testing and Verification

- [ ] Focused tests cover the risk introduced by the diff.
- [ ] Regression coverage is sufficient for touched shared flows.
- [ ] Deterministic tests avoid external network calls unless the story explicitly requires them.
- [ ] Claimed commands and results are represented accurately in the story/review notes.

## Triage Rules

- [ ] Findings are separated from non-blocking notes.
- [ ] Each finding includes severity, file/line reference, impact, and a concrete fix direction.
- [ ] Patch-now items are limited to issues that can cause incorrect behavior, privacy/security exposure, broken acceptance criteria, or meaningful test gaps.
- [ ] Defer items are explicitly outside current story scope or not worth blocking.

## Completion

- [ ] If no issues are found, state that clearly and list residual risks or test gaps.
- [ ] If patch items are fixed, rerun the smallest meaningful verification set.
- [ ] Story status and `stories/sprint-status.yaml` are updated consistently when review outcome changes.
- [ ] Project recovery docs are updated when next-step state changes.
