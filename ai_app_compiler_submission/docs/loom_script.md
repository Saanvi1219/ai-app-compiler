# Loom Video Script — 5 to 10 Minutes

## 1. Introduction

Hi, this is my submission for the AI Engineer demo task.

The goal of this project is to build a system that behaves like a compiler for software generation.

A user gives an open-ended natural language prompt, and the system converts it into a strict, validated, repairable, and executable application configuration.

This is not a single prompt engineering solution.  
It is a multi-stage system design problem.

## 2. High-Level Architecture

The pipeline has six major stages:

1. Intent extraction
2. System design
3. Schema generation
4. Validation
5. Repair
6. Runtime simulation

The input is a product prompt like:

"Build a CRM with login, contacts, dashboard, role-based access, and premium plan with payments."

The output is a complete JSON configuration containing:

- UI schema
- API schema
- database schema
- auth rules
- business logic rules

## 3. Intent Extraction

The first stage extracts the user's intent.

It identifies:

- app type
- features
- roles
- ambiguity
- assumptions

For example, if the prompt mentions CRM, login, contacts, premium, payments, and admin, those become structured fields.

If the prompt is vague, the system records that and adds reasonable assumptions.

## 4. System Design Layer

The second stage converts the intent into architecture.

It defines:

- entities
- flows
- roles
- application structure

For a CRM, entities may include users, contacts, deals, payments, subscriptions, and analytics.

This is similar to the semantic analysis stage of a compiler.

## 5. Schema Generation

The third stage generates strict application config.

It generates:

- UI pages
- API endpoints
- database tables
- auth permissions
- business logic

The UI pages map to API routes.

The API routes map to database tables.

Roles map to permissions.

This avoids disconnected output.

## 6. Validation and Repair

This is the core of the project.

The validator checks:

- required fields
- type safety
- UI to API consistency
- API to database consistency
- role consistency
- hallucinated or missing fields

If something is broken, the repair engine does not blindly regenerate the whole output.

Instead, it repairs only the broken part.

For example:

- if UI references a missing API, it creates that API
- if API references a missing database field, it adds the field
- if a role is missing, it adds the role to auth

This gives more control and predictability.

## 7. Deterministic Behavior

The system is designed to be deterministic.

Same input should produce the same structured output within reasonable variance.

This version uses deterministic logic for the core pipeline.

In production, LLMs can be added stage-wise, but validation and repair must remain deterministic.

## 8. Runtime Simulation

To prove execution awareness, the project includes a runtime simulator.

The simulator reads the final config and checks whether it can create:

- frontend pages
- API routes
- database tables

If all layers are usable, runtime simulation passes.

This proves that the JSON is not just theoretical. It can power a generated application.

## 9. Evaluation Framework

The project includes 20 prompts:

- 10 normal product prompts
- 10 edge cases

It tracks:

- success rate
- average retries
- latency
- failure types

This gives actual metrics instead of vague claims.

## 10. Cost vs Quality Tradeoff

The current version keeps cost low by using deterministic logic.

A production version can use different model strengths at different stages:

- cheaper model for intent extraction
- stronger model for architecture
- deterministic validation and repair after generation

This balances cost, latency, and quality.

## 11. Conclusion

This project is built like a compiler pipeline, not a prompt wrapper.

It focuses on:

- reliability
- control
- validation
- repair
- execution awareness
- measurable evaluation

Thank you.
