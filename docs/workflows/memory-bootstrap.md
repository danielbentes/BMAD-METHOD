# Memory Bootstrap Guide for BMAD Method v3.0

**Extract knowledge, patterns, and conventions from existing codebases to accelerate development and ensure consistency.**

!!! success "Game-Changer for Brownfield Projects"
    Memory bootstrap transforms how you work with existing codebases by automatically extracting patterns, conventions, and architectural decisions - turning tribal knowledge into actionable intelligence.

## What is Memory Bootstrap?

Memory bootstrap is BMAD Method v3.0's intelligent system for extracting and organizing knowledge from existing codebases. It goes beyond simple code analysis to understand:

- **Architectural Patterns**: How the system is structured and why
- **Coding Conventions**: Style patterns, naming conventions, and team preferences  
- **Business Logic**: Domain rules and constraints embedded in code
- **Technical Decisions**: Past choices and their rationale (from comments/commits)
- **Quality Patterns**: What works well and what doesn't
- **Team Knowledge**: Undocumented conventions and practices

### Key Benefits

1. **Instant Context**: New team members productive in hours, not weeks
2. **Pattern Recognition**: Automatically identify successful (and problematic) patterns
3. **Style Consistency**: Enforce discovered conventions automatically
4. **Decision History**: Understand why things were built a certain way
5. **Continuous Learning**: System improves with every interaction

## Bootstrap Modes

### 1. Automatic Bootstrap (Recommended for First Run)

**Best for**: Initial project analysis, general pattern discovery

```bash
# Basic automatic bootstrap
/memory bootstrap-memory --mode=auto

# With progress tracking (recommended for large codebases)
/memory bootstrap-memory --mode=auto --progress

# Specific depth levels
/memory bootstrap-memory --mode=auto --depth=shallow  # Quick overview
/memory bootstrap-memory --mode=auto --depth=standard # Balanced analysis
/memory bootstrap-memory --mode=auto --depth=deep     # Comprehensive extraction
```

**What it captures**:
- File structure and organization patterns
- Technology stack and dependencies
- Common coding patterns and conventions
- Basic architectural patterns
- TODO/FIXME comments and technical debt markers

### 2. Interactive Bootstrap (Recommended for Deep Knowledge)

**Best for**: Capturing business logic, historical decisions, team knowledge

```bash
# Interactive session with team
/memory bootstrap-memory --mode=interactive

# Focused interactive sessions
/memory bootstrap-memory --mode=interactive --focus=architecture
/memory bootstrap-memory --mode=interactive --focus=decisions
/memory bootstrap-memory --mode=interactive --focus=patterns
/memory bootstrap-memory --mode=interactive --focus=issues
```

**Guided questions include**:
- Why were certain technologies chosen?
- What are the critical business rules?
- Which patterns have worked well?
- What mistakes should be avoided?
- Who are the domain experts for different areas?

### 3. Incremental Bootstrap (For Ongoing Learning)

**Best for**: Large codebases, interrupted sessions, continuous improvement

```bash
# Resume interrupted bootstrap
/memory bootstrap-memory --mode=incremental

# Focus on recent changes
/memory bootstrap-memory --mode=incremental --since="7 days ago"

# Target specific directories
/memory bootstrap-memory --mode=incremental --path=src/services
```

## Step-by-Step Bootstrap Process

### Phase 1: Preparation (5 minutes)

1. **Identify Codebase Characteristics**
   ```bash
   # Get codebase overview
   /memory analyze-codebase
   
   # Check size and complexity
   /memory estimate-bootstrap-time
   ```

2. **Set Bootstrap Goals**
   ```yaml
   bootstrap_goals:
     primary:
       - Understand architecture
       - Extract coding standards
       - Identify key patterns
     secondary:
       - Find improvement opportunities
       - Document technical debt
   ```

### Phase 2: Automatic Extraction (10-30 minutes)

1. **Start Automatic Bootstrap**
   ```bash
   /memory bootstrap-memory --mode=auto --progress
   ```

2. **Monitor Progress**
   ```
   Bootstrap Progress: [████████████████░░░░] 78%
   Analyzing: src/services/auth/
   Patterns found: 147
   Conventions detected: 23
   Architecture elements: 12
   ```

3. **Review Initial Findings**
   ```bash
   /memory patterns --type=all --limit=10
   /memory insights --focus=architecture
   ```

### Phase 3: Interactive Refinement (30-60 minutes)

1. **Gather Team for Interactive Session**
   ```bash
   /memory bootstrap-memory --mode=interactive --team-size=3
   ```

2. **Guided Conversation Topics**
   - **Architecture**: "Why microservices vs monolith?"
   - **Patterns**: "What's the reason for this repository pattern?"
   - **Decisions**: "Why PostgreSQL over MongoDB?"
   - **Gotchas**: "What breaks if we change X?"

3. **Capture Critical Knowledge**
   ```bash
   /memory remember "Critical: User service must never directly access payment data - compliance requirement"
   /memory remember "Pattern: All API responses use envelope pattern for consistency"
   /memory remember "Decision: Chose Redis for sessions due to 10ms latency requirement"
   ```

### Phase 4: Validation and Insights (15 minutes)

1. **Validate Extracted Patterns**
   ```bash
   /memory patterns --validate
   /memory test-patterns --sample-size=20
   ```

2. **Generate Actionable Insights**
   ```bash
   /memory insights --actionable
   /memory recommendations --priority=high
   ```

3. **Create Bootstrap Report**
   ```bash
   /memory bootstrap-report --format=detailed
   ```

## Understanding Bootstrap Output

### Pattern Categories

Bootstrap organizes findings into categories:

```yaml
extracted_patterns:
  architecture:
    - "Service-oriented architecture with API gateway"
    - "Event-driven communication via RabbitMQ"
    - "Separate read/write models (CQRS pattern)"
    
  coding_style:
    - "camelCase for functions, PascalCase for classes"
    - "Async/await preferred over callbacks"
    - "Destructuring for multiple returns"
    
  business_rules:
    - "Orders must have at least one item"
    - "Prices include tax in EU regions"
    - "Inventory updates are eventually consistent"
    
  quality_markers:
    good:
      - "Comprehensive error handling in payment service"
      - "Well-documented API contracts"
    concerns:
      - "Inconsistent validation in user service"
      - "Missing tests in inventory module"
```

### Memory Insights

Bootstrap generates intelligent insights:

```bash
/memory insights

# Output:
ARCHITECTURAL INSIGHTS:
✓ Strong separation of concerns in service layer
✓ Consistent use of dependency injection
⚠ Some services bypass API gateway (security risk)
⚠ Database queries could benefit from caching layer

PATTERN INSIGHTS:
✓ Repository pattern used consistently (87% of data access)
✓ Factory pattern for complex object creation
⚠ Inconsistent error handling patterns across services
  → Recommendation: Standardize on Result<T> pattern

STYLE INSIGHTS:
✓ ESLint configuration well-maintained
✓ Naming conventions mostly consistent (92%)
⚠ Mixed async patterns (callbacks vs promises vs async/await)
  → Recommendation: Migrate remaining callbacks to async/await
```

## Advanced Bootstrap Techniques

### 1. Focused Analysis

Target specific aspects of the codebase:

```bash
# Architecture-specific bootstrap
/memory bootstrap-memory --focus=architecture --depth=deep

# Performance pattern extraction
/memory bootstrap-memory --focus=performance --include="**/critical/**"

# Security pattern analysis
/memory bootstrap-memory --focus=security --priority=high
```

### 2. Differential Bootstrap

Understand changes and evolution:

```bash
# Compare current patterns with 6 months ago
/memory bootstrap-memory --differential --baseline="6 months ago"

# Track pattern evolution
/memory pattern-evolution --timeline

# Identify emerging patterns
/memory emerging-patterns --threshold=3
```

### 3. Cross-Project Bootstrap

Learn from multiple related projects:

```bash
# Bootstrap multiple services
/memory bootstrap-memory --projects="auth-service,user-service,payment-service"

# Find common patterns across projects
/memory cross-project-patterns --similarity=80%

# Identify inconsistencies
/memory pattern-conflicts --severity=high
```

## Applying Bootstrap Knowledge

### 1. Style Enforcement

Use discovered patterns for consistency:

```bash
# Generate style guide from patterns
/memory generate-style-guide

# Configure automatic enforcement
/memory enable-style-enforcement --level=strict

# Check new code against patterns
/memory check-style "src/new-feature/**"
```

### 2. Architecture Compliance

Ensure new code follows discovered patterns:

```bash
# Validate against architectural patterns
/memory validate-architecture "src/new-service/"

# Get architecture recommendations
/memory suggest-architecture --for="new payment integration"

# Check for anti-patterns
/memory detect-antipatterns --fix
```

### 3. Knowledge Queries

Leverage bootstrap knowledge during development:

```bash
# Ask about specific patterns
/memory recall "how do we handle authentication"
/memory recall "database transaction patterns"

# Get examples of good code
/memory show-examples "error handling"
/memory show-examples "API response formatting"

# Find similar implementations
/memory find-similar "user registration flow"
```

## Bootstrap for Different Scenarios

### Scenario 1: Large Legacy Monolith

```bash
# Start with shallow analysis
/memory bootstrap-memory --mode=auto --depth=shallow --timeout=30m

# Focus on critical paths
/memory bootstrap-memory --mode=incremental --path="src/core/**" --depth=deep

# Interactive session for business logic
/memory bootstrap-memory --mode=interactive --focus=business-rules
```

### Scenario 2: Microservices Architecture

```bash
# Bootstrap each service
for service in auth user payment inventory; do
  /memory bootstrap-memory --mode=auto --path="services/$service" --tag=$service
done

# Analyze cross-service patterns
/memory cross-service-analysis

# Find integration patterns
/memory bootstrap-memory --focus=integration --path="services/**/api/**"
```

### Scenario 3: Rapid Onboarding

```bash
# Quick bootstrap for new developer
/memory bootstrap-memory --mode=auto --depth=shallow --quick

# Generate onboarding guide
/memory generate-onboarding --role=developer

# Create pattern cheatsheet
/memory pattern-summary --format=cheatsheet
```

## Troubleshooting Bootstrap Issues

### Performance Issues

**Problem**: Bootstrap taking too long

```bash
# Use incremental mode
/memory bootstrap-memory --mode=incremental --batch-size=100

# Skip large generated files
/memory bootstrap-memory --exclude="**/node_modules/**,**/dist/**"

# Parallel processing
/memory bootstrap-memory --parallel=4
```

### Incomplete Extraction

**Problem**: Missing important patterns

```bash
# Deep dive specific areas
/memory bootstrap-memory --mode=deep --path="src/business-logic/**"

# Adjust pattern detection sensitivity
/memory bootstrap-memory --sensitivity=high

# Manual pattern addition
/memory add-pattern "Custom validation uses ValidatorChain class"
```

### Conflicts and Inconsistencies

**Problem**: Conflicting patterns detected

```bash
# Review conflicts
/memory show-conflicts --severity=high

# Resolve with team input
/memory resolve-conflicts --interactive

# Set pattern precedence
/memory set-precedence "New patterns override legacy in src/legacy/**"
```

## Best Practices

### 1. Regular Re-bootstrap

Keep knowledge current:

```bash
# Weekly incremental updates
/memory bootstrap-memory --mode=incremental --schedule=weekly

# Monthly deep refresh
/memory bootstrap-memory --mode=auto --depth=deep --schedule=monthly

# Quarterly validation with team
/memory bootstrap-memory --mode=interactive --schedule=quarterly
```

### 2. Team Involvement

Maximize knowledge capture:

- Include senior developers in interactive sessions
- Rotate team members for different perspectives
- Document "why" not just "what"
- Capture edge cases and gotchas

### 3. Bootstrap Hygiene

Maintain quality:

```bash
# Validate patterns regularly
/memory validate-patterns --auto-fix

# Remove obsolete patterns
/memory cleanup-patterns --obsolete

# Merge duplicate patterns
/memory deduplicate-patterns
```

## Integration with Development Workflow

### Pre-Development

```bash
# Before starting new feature
/memory recall "similar features"
/memory suggest-patterns --for="user notification system"
/memory show-examples "notification implementation"
```

### During Development

```bash
# Real-time pattern compliance
/memory watch --path="src/**" --enforce-patterns

# Get contextual suggestions
/memory suggest --context="implementing user auth"

# Validate against patterns
/memory validate-code --real-time
```

### Code Review

```bash
# Automated pattern checking
/memory review-code --pr=123

# Generate review comments
/memory suggest-improvements --based-on-patterns

# Check for anti-patterns
/memory detect-antipatterns --pr=123
```

## Next Steps

After mastering memory bootstrap:

1. **[Context Management](context-management.md)** - Leverage bootstrap data for context
2. **[Brownfield Projects](../getting-started/brownfield-projects.md)** - Apply bootstrap to legacy code
3. **[Quality Framework](quality-framework.md)** - Enforce patterns through quality gates
4. **[Command Reference](../commands/quick-reference.md)** - Complete bootstrap command reference

---

**Remember**: Memory bootstrap is not just about code analysis - it's about capturing the collective intelligence of your team and making it accessible to everyone. The more you invest in bootstrap, the more value you get from BMAD Method v3.0. 