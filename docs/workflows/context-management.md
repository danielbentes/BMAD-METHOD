# Context Management in BMAD Method v3.0

**Master seamless work continuity across sessions, interruptions, and persona transitions.**

!!! info "NEW in v3.0"
    Context management replaces traditional session IDs with intelligent state preservation, enabling you to resume work exactly where you left off - even days later.

## What is Context Management?

Context management is BMAD Method's intelligent system for preserving and transferring work state across:

- **Session Boundaries**: Resume work after breaks or system restarts
- **Persona Transitions**: Maintain continuity when switching between personas
- **Task Interruptions**: Handle unexpected interruptions without losing progress
- **Team Handoffs**: Transfer complete context to team members
- **Multi-Project Work**: Switch between projects without confusion

### Core Benefits

1. **Zero Context Loss**: Never lose track of where you were or what you were doing
2. **Instant Resumption**: Pick up exactly where you left off, even days later
3. **Intelligent Handoffs**: Personas receive complete context automatically
4. **Progress Tracking**: Visual indicators of work state and completion
5. **Decision History**: Access to all past decisions and their rationale

## How Context Management Works

### Context Components

The BMAD context system tracks five key elements:

```yaml
context_state:
  current_work:
    persona: "architect"
    task: "designing authentication system"
    phase: "technical design"
    progress: 65%
    
  decisions_made:
    - "Chose JWT for stateless authentication"
    - "PostgreSQL for user data storage"
    - "Redis for session caching"
    
  pending_items:
    - "Security review of JWT implementation"
    - "Performance testing of auth endpoints"
    
  memory_references:
    - "Similar auth system from Project X"
    - "JWT best practices pattern"
    
  quality_status:
    last_gate: "design review - passed"
    next_gate: "implementation review"
    issues_found: 0
```

### Automatic Context Tracking

Context is automatically captured during:

- **Command Execution**: Every command updates context
- **Persona Switches**: Full state transfer between personas
- **Decision Points**: Major decisions are flagged and stored
- **Quality Gates**: Results and feedback are preserved
- **Memory Operations**: Connections to past patterns noted

## Context Management Commands

### Core Context Commands

| Command | Purpose | Usage |
|---------|---------|-------|
| `/context` | Display current context state | Shows work progress, decisions, pending items |
| `/context save` | Explicitly save context checkpoint | Before major changes or breaks |
| `/context restore` | Restore previous context | Resume after interruption |
| `/context history` | View context timeline | Track progress over time |
| `/context share` | Export context for team | Enable team collaboration |

### Context-Aware Commands

These commands automatically leverage context:

| Command | Context Usage |
|---------|--------------|
| `/handoff {persona}` | Transfers complete context to new persona |
| `/suggest` | Recommendations based on current context |
| `/quality-gate` | Considers context in validation |
| `/memory recall` | Searches relevant to current context |

## Context Management Workflows

### Workflow 1: Session Interruption and Resume

**Scenario**: You're called away mid-development

```bash
# Before interruption (optional - auto-saves every 5 min)
/context save "auth implementation - JWT setup complete"

# ... Hours or days later ...

# Resume work
/context
# Shows: Last working on auth implementation, JWT setup done, next: endpoint creation

/context restore
# Fully restores: persona, task state, pending items, decisions
```

### Workflow 2: Intelligent Persona Handoff

**Scenario**: Transitioning from architecture to development

```bash
# As Architect persona
/architect
# Complete technical design...

# Handoff to Developer
/handoff dev
# Context automatically includes:
# - Architecture decisions
# - Technology choices  
# - Implementation priorities
# - Quality requirements

# Developer starts with full context
/dev
# "I see we're implementing JWT auth with PostgreSQL. Starting with user model..."
```

### Workflow 3: Multi-Project Context Switching

**Scenario**: Working on multiple projects simultaneously

```bash
# Project A: E-commerce platform
/context save --tag "ecommerce-payment-integration"

# Switch to Project B: Analytics dashboard  
/context switch "analytics-dashboard"
# or
/context restore --tag "analytics-v2-charts"

# Later, return to Project A
/context switch "ecommerce-payment-integration"
# All Project A context restored
```

### Workflow 4: Emergency Handoff

**Scenario**: Urgent issue requires immediate context transfer

```bash
# Current developer hits blocker
/context save --emergency "Critical: Auth bug in production, investigating JWT expiry"

# New developer takes over
/context restore --latest-emergency
# Receives:
# - Current investigation state
# - Attempted solutions
# - Error patterns discovered
# - Next debugging steps

/suggest --emergency-response
# Context-aware emergency recommendations
```

## Advanced Context Features

### Context Templates

Create reusable context templates for common scenarios:

```bash
# Save context as template
/context save-template "new-feature-start"

# Apply template to new work
/context apply-template "new-feature-start"
# Initializes with predefined:
# - Persona sequence
# - Quality gates
# - Memory patterns
# - Workflow steps
```

### Context Analytics

Track productivity and patterns:

```bash
# View context analytics
/context analytics --period=week

# Shows:
# - Time spent per persona
# - Decision velocity
# - Interruption patterns
# - Handoff efficiency
# - Completion rates
```

### Context Integration with Memory

Context and memory work together:

```bash
# Context-aware memory operations
/memory recall
# Automatically filtered by current context

/memory patterns
# Shows patterns relevant to current work

/memory insights
# Provides context-specific recommendations
```

## Best Practices

### 1. Regular Context Checkpoints

```bash
# Before major decisions
/context save "pre-architecture-decision"

# After completing phases
/context save "requirements-complete"

# Before planned breaks
/context save "EOD-auth-implementation-75%"
```

### 2. Descriptive Context Tags

```bash
# Use meaningful tags
/context save --tag "payment-gateway-stripe-integration"

# Not vague tags
/context save --tag "work-stuff"  # Bad
```

### 3. Context Hygiene

```bash
# Review and clean old contexts periodically
/context cleanup --older-than=30d

# Archive completed project contexts
/context archive --project="v1-launch"
```

### 4. Team Context Standards

Establish team conventions:

```yaml
context_naming:
  format: "{project}-{feature}-{phase}"
  examples:
    - "ecommerce-auth-design"
    - "analytics-charts-implementation"
    - "platform-deploy-testing"

checkpoint_triggers:
  - "Major decision made"
  - "Phase completion"
  - "Before handoff"
  - "End of work session"
```

## Troubleshooting Context Issues

### Lost Context Recovery

**Problem**: Context seems lost or corrupted

```bash
# List recent contexts
/context history --limit=10

# Recover from backup
/context restore --backup

# Rebuild from memory
/context rebuild --from-memory
```

### Context Merge Conflicts

**Problem**: Multiple contexts for same work

```bash
# View conflicting contexts
/context conflicts

# Merge contexts
/context merge --strategy=newest

# Manual resolution
/context resolve --interactive
```

### Context Performance

**Problem**: Context operations slow

```bash
# Optimize context storage
/context optimize

# Reduce context size
/context compact --remove-duplicates

# Archive old contexts
/context archive --inactive-days=14
```

## Context Management Patterns

### Pattern 1: Daily Standup Context

```bash
# Morning startup routine
/context restore --yesterday
/context summary
/suggest --based-on-yesterday

# Evening shutdown routine
/context save --tag "EOD-$(date +%Y%m%d)"
/context report --today
```

### Pattern 2: Feature Development Context

```bash
# Feature start
/context new --feature "user-notifications"
/pm  # Requirements
/context checkpoint "requirements-documented"

/architect  # Design
/context checkpoint "architecture-approved"

/dev  # Implementation
/context checkpoint "implementation-phase"

# Feature complete
/context finalize --feature "user-notifications"
```

### Pattern 3: Debugging Context

```bash
# Start debugging session
/context new --debug "performance-issue-API"

# Track investigation
/context note "Identified N+1 query in user endpoint"
/context note "Attempting query optimization"

# Save solution
/context solution "Added eager loading, 10x performance improvement"
```

## Integration with Other Systems

### IDE Integration

```json
// .vscode/settings.json
{
  "bmad.context.autoSave": true,
  "bmad.context.saveInterval": 300,
  "bmad.context.showInStatusBar": true,
  "bmad.context.warnOnSwitch": true
}
```

### Git Integration

```bash
# Auto-save context on commit
git config --local bmad.context.onCommit true

# Include context in commit message
git commit -m "feat: Add user auth [context: auth-implementation-complete]"
```

### CI/CD Integration

```yaml
# .github/workflows/context.yml
- name: Restore BMAD Context
  run: bmad context restore --ci
  
- name: Run Context Validation
  run: bmad context validate
  
- name: Archive Context
  run: bmad context archive --build=${{ github.run_id }}
```

## Next Steps

Now that you understand context management:

1. **[Memory Bootstrap Guide](memory-bootstrap.md)** - Extract knowledge from existing codebases
2. **[Workflow Guide](index.md)** - Master intelligent workflows
3. **[Quality Framework](quality-framework.md)** - Ensure quality with context
4. **[Command Reference](../commands/quick-reference.md)** - All context commands detailed

---

**Remember**: Context management is automatic in BMAD v3.0, but understanding how it works helps you leverage its full power for seamless, interruption-proof development. 