# Compute Architecture

## Purpose

This document defines the public-safe compute roles of the Aiden Platform.
Compute includes physical hosts, virtual machines, system containers,
application containers, and future AI workloads. Exact host identities,
addressing, inventory, device paths, and management procedures are private
operational facts.

## Core Principle

Place workloads by stability, isolation, resource, recovery, and migration
needs rather than by installation convenience. Public documentation describes
roles and constraints, not reachability.

## Infrastructure Placement

Homelab owns its core-services and virtualization role design and dated
deployment evidence in the [planned public engineering repository](https://github.com/aidenm727/homelab)
(local H1 candidate; publication pending). This Sahale policy does not claim
current operation; fresh authorized observation owns runtime reality.

### Storage Environment

Durable shared storage remains a future role until capacity, multi-host access,
recovery time, integrity, or maintenance evidence justifies it. Applications
should preserve portable exports and ordinary storage interfaces so no one
device, hypervisor, NAS brand, or provider becomes irreplaceable.

### AI Compute

Current AI use relies on explicit, owner-approved provider or runtime handoffs.
Local inference remains exploratory until dated evidence verifies hardware fit,
isolation, privacy, performance, maintenance, and reversibility. Knowledge and
School Learning workflows must not depend on a local model being available.

## Trust and Placement Rules

- Human authority remains outside compute placement.
- Stable services and disposable experiments use different failure and change
  boundaries.
- Personal or sensitive data enters a workload only after its access, logging,
  backup, export, and deletion boundaries are explicit.
- Primary capacity, rollback snapshots, off-host backup, and off-site protection
  are distinct controls.
- A workload moves from experiment to supported service only after dated
  verification and recovery evidence.
- Public records use role aliases and time-bounded outcomes; exact operations
  belong privately when durable ownership is required.

## Open Decisions

- Which future workload first demonstrates the need for a private operations
  repository?
- What measured recovery or capacity evidence justifies dedicated storage?
- Which isolation boundary is appropriate for a reversible local-AI experiment?
- Which experiments merit promotion into supported owner capabilities?
