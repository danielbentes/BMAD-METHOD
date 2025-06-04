# BMAD Example-Driven Learning Guide

## How Examples Work in the BMAD Method

### Overview

The BMAD Method uses a sophisticated example-driven learning system that ensures AI responses are concrete, actionable, and based on proven patterns rather than abstract rules. This guide explains exactly how examples are loaded, selected, and used.

## Architecture

### 1. Example Library Structure

```
bmad-agent/examples/
├── personas/          # Persona-specific examples
│   ├── dev-examples.md
│   ├── architect-examples.md
│   └── [persona]-examples.md
├── good/             # Best practice patterns
│   ├── performance-optimization.md
│   ├── security-patterns.md
│   └── ...
├── bad/              # Anti-patterns to avoid
│   ├── technical-debt-examples.md
│   ├── security-failures.md
│   └── ...
├── tasks/            # Task execution examples
│   ├── udtm-examples.md
│   ├── create-prd-examples.md
│   └── ...
└── workflows/        # Process examples
    ├── code-review-examples.md
    ├── deployment-examples.md
    └── ...
```

### 2. Configuration Mapping

The orchestrator configuration (`ide-bmad-orchestrator.cfg.md`) defines:

```yaml
example_libraries:
  good_patterns: "(agent-root)/examples/good/"
  anti_patterns: "(agent-root)/examples/bad/"
  persona_examples: "(agent-root)/examples/personas/"
  task_examples: "(agent-root)/examples/tasks/"
  workflow_examples: "(agent-root)/examples/workflows/"
```

### 3. Persona Integration

Each persona file now includes:

```markdown
## EXAMPLE LIBRARIES (MANDATORY REFERENCE)
- **Primary Examples**: `(agent-root)/examples/personas/{persona}-examples.md`
- **Good Patterns**: `(agent-root)/examples/good/`
- **Anti-Patterns**: `(agent-root)/examples/bad/`
- **Task Examples**: `(agent-root)/examples/tasks/`
- **Workflow Examples**: `(agent-root)/examples/workflows/`

**PENALTY**: -$1,000 for any response without example references
**REWARD**: +$500 for appropriate example usage
```

## How Examples Are Selected and Used

### Step 1: Task Analysis

When a persona receives a task, it must:

1. **Identify the task type** (implementation, debugging, design, etc.)
2. **Determine relevant domains** (auth, database, UI, etc.)
3. **Assess context** (greenfield vs brownfield, team expertise, etc.)

### Step 2: Example Search

The persona searches its example libraries:

```
For task: "Implement user authentication"

1. Check persona-specific: dev-examples.md → find auth patterns
2. Check good patterns: security-patterns.md → find JWT examples
3. Check anti-patterns: auth-failures.md → find what to avoid
4. Check task examples: implementation-examples.md → find similar tasks
```

### Step 3: Pattern Application

The persona must:

1. **Select 2-3 relevant examples** that match the context
2. **Adapt the pattern** to the specific requirements
3. **Avoid anti-patterns** identified in bad examples
4. **Apply quality standards** from the examples

### Step 4: Citation Requirements

Every response must include citations:

```markdown
"Implementing secure authentication based on [dev-examples.md #auth-3]:
→ JWT with RS256 algorithm [security-patterns.md #jwt-1]
→ Refresh token rotation [auth-patterns.md #refresh-2]
→ Rate limiting to prevent brute force [security-patterns.md #rate-limit-4]

[Anti-pattern avoided: hardcoded secrets from auth-failures.md #5]
[Excellence: +$1,000 for comprehensive example usage]"
```

## Behavioral Enforcement Mechanisms

### 1. Penalty System

```yaml
violations:
  no_examples_referenced: -$1,000
  vague_reference: -$500 ("see examples" without specifics)
  wrong_example: -$750 (inappropriate example for context)
  missed_anti_pattern: -$2,000 (didn't avoid known bad pattern)
```

### 2. Reward System

```yaml
rewards:
  basic_example_usage: +$500
  multiple_relevant_examples: +$1,000
  creative_pattern_application: +$1,500
  prevented_anti_pattern: +$2,000
```

### 3. Quality Gates

At each milestone (25%, 50%, 75%, 100%), the system checks:
- Example utilization rate (target: 90%)
- Citation accuracy
- Pattern appropriateness
- Anti-pattern avoidance

## Context-Aware Example Selection

### Team Expertise Adaptation

```yaml
junior_team:
  example_count: 3-5 per concept
  example_detail: step-by-step explanations
  example_type: basic patterns with detailed comments

senior_team:
  example_count: 1-2 per concept
  example_detail: edge cases only
  example_type: advanced patterns and optimizations
```

### Project Type Adaptation

```yaml
greenfield:
  examples: modern patterns, latest best practices
  focus: scalability, future-proofing

brownfield:
  examples: migration patterns, compatibility
  focus: incremental improvement, risk mitigation
```

## Memory Integration

The system remembers:

1. **Successful Example Applications**
   - Which examples led to good outcomes
   - Context where they worked well
   - Adaptations that were effective

2. **Failed Patterns**
   - Examples that didn't work in certain contexts
   - Anti-patterns discovered through experience
   - Lessons learned from failures

3. **User Preferences**
   - Preferred example verbosity
   - Domain-specific pattern preferences
   - Team-specific adaptations

## Common Pitfalls and Solutions

### Pitfall 1: Generic Example References

❌ **Bad**: "Using standard authentication patterns"

✅ **Good**: "Using JWT with refresh tokens [auth-patterns.md #jwt-refresh-3]"

### Pitfall 2: Mismatched Examples

❌ **Bad**: Using microservices examples for a monolith project

✅ **Good**: Selecting examples that match the architectural context

### Pitfall 3: Ignoring Anti-Patterns

❌ **Bad**: Not checking the bad/ examples directory

✅ **Good**: Explicitly stating which anti-patterns were avoided

## Measurement and Optimization

### Key Metrics

1. **Example Utilization Rate**: % of responses with examples (target: 90%)
2. **Citation Accuracy**: % of correct example references (target: 95%)
3. **Pattern Success Rate**: % of applied patterns that work (target: 85%)
4. **Anti-Pattern Prevention**: Count of avoided issues (target: 100%)

### Continuous Improvement

1. **Weekly Review**: Analyze which examples are most effective
2. **Pattern Updates**: Add new successful patterns to libraries
3. **Anti-Pattern Discovery**: Document new failures as bad examples
4. **Context Refinement**: Improve example selection algorithms

## Implementation Checklist

- [ ] Orchestrator config defines example paths
- [ ] All personas include example library references
- [ ] Penalty/reward system configured
- [ ] Example files organized by category
- [ ] Citations required in all responses
- [ ] Quality gates check example usage
- [ ] Memory system tracks example effectiveness
- [ ] Context adaptation rules defined

## Summary

The BMAD example-driven learning system transforms vague AI responses into concrete, actionable guidance by:

1. **Forcing example usage** through penalties and rewards
2. **Organizing examples** in searchable, categorized libraries
3. **Requiring citations** for accountability and learning
4. **Adapting to context** for relevant example selection
5. **Learning from usage** to improve over time

This system ensures that every AI response is grounded in proven patterns, avoiding known pitfalls, and delivering consistent quality through concrete examples rather than abstract rules.