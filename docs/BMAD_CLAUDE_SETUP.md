# BMAD Method → Claude Code Integration Guide

This guide explains how to automatically convert your BMAD Method commands into Claude Code compatible slash commands with complete behavioral tracking and system management.

## 🎯 Solution Overview

We've implemented a **Hybrid Template-Based Generator** that:
- ✅ Groups related BMAD commands into logical Claude Code commands
- ✅ Preserves full behavioral framework and requirements
- ✅ Reduces complexity from 46 individual commands to 9 manageable groups
- ✅ Maintains native Claude Code argument handling with `$ARGUMENTS`
- ✅ Enables automatic updates when BMAD registry changes
- ✅ Includes complete behavioral tracking and gamification system
- ✅ Provides comprehensive system management and orchestrator control

## 🚀 Quick Start

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Generate Claude Commands and Documentation
```bash
# Quick way - runs both generators and cleans up
./update_bmad_commands.sh

# Or manually run each step:
python generate_claude_commands.py    # Generate command files
python generate_claude_docs.py        # Generate comprehensive docs
```

### Step 3: Initialize BMAD Orchestrator

#### For Greenfield Projects (New Codebases)
```bash
# CRITICAL FIRST STEP: Initialize the BMAD orchestrator system
/project:system init --config --memory

# Verify all components are operational
/project:system status --detailed

# Validate configuration and personas
/project:system validate --full
```

#### For Brownfield Projects (Existing Codebases)
```bash
# CRITICAL FIRST STEP: Initialize with memory bootstrap
/project:system init --config --memory

# ESSENTIAL: Bootstrap memory from existing codebase
/project:memory bootstrap-memory --mode=auto --depth=standard

# Analyze current state and patterns
/project:memory patterns --type=all --context=current
/project:memory insights --focus=architecture --actionable

# Verify system health with brownfield context
/project:system validate --full --memory
```

### Step 4: Use BMAD Commands in Claude Code
```bash
# Activate a persona
/project:persona architect

# Execute memory operations
/project:memory remember "API authentication patterns" --category=technical

# Run quality enforcement
/project:quality udtm "microservices vs monolith architecture"

# Manage workflow
/project:workflow suggest --alternatives=3

# Start multi-persona consultation
/project:consultation consult design-review

# Track behavioral performance
/project:behavioral balance --detailed

# Advanced system analysis
/project:analysis diagnose --component=performance --deep
```

## 🏗️ Brownfield Project Guide

!!! info "Working with Existing Codebases"
    Most real-world projects involve existing code. BMad Method provides systematic approaches for brownfield initialization with memory bootstrapping to capture existing knowledge.

### Quick Brownfield Start (30 Minutes)

**Step 1: System Initialization**
```bash
# Initialize BMad with memory system
/project:system init --config --memory
/project:system status --detailed
```

**Step 2: Automated Memory Bootstrap**
```bash
# Auto-scan existing codebase for patterns and decisions
/project:memory bootstrap-memory --mode=auto --depth=standard

# Analyze discovered patterns
/project:memory patterns --type=all --context=current
```

**Step 3: Quality Baseline Assessment**
```bash
# Assess current quality state (non-strict for brownfield)
/project:quality quality-gate custom --strict=false --report

# Identify current anti-patterns (start with high severity)
/project:quality anti-pattern-check --scope=all --severity=high
```

### Comprehensive Brownfield Analysis (First Week)

#### **Day 1-2: Deep Memory Bootstrap**
```bash
# Interactive bootstrap for complex systems
/project:memory bootstrap-memory --mode=interactive --focus=all --depth=deep

# Capture architecture decisions and constraints
/project:memory remember "Legacy system constraints: [details]" --category=decisions
/project:memory remember "Current architecture patterns: [patterns]" --category=patterns

# Document technical debt and known issues
/project:memory remember "Technical debt assessment: [findings]" --category=issues --priority=high
```

#### **Day 3-4: Pattern Analysis and Documentation**
```bash
# Analyze all pattern types in current context
/project:memory patterns --type=technical --context=current --success-rate=all
/project:memory patterns --type=workflow --context=current --success-rate=high

# Get actionable insights for improvement
/project:memory insights --focus=architecture --actionable
/project:memory insights --focus=quality --actionable
```

#### **Day 5-7: Strategic Planning**
```bash
# Switch to Product Manager persona for strategic analysis
/project:persona pm

# Conduct ultra-deep thinking on brownfield improvement strategy
/project:quality udtm "brownfield improvement approach" --perspectives=7 --evidence

# Multi-persona consultation for comprehensive strategy
/project:consultation consult product-strategy

# Document strategic decisions
/project:memory remember "Brownfield improvement strategy: [strategy]" --category=decisions --priority=critical
```

### Memory Bootstrap Command Reference

The `/project:memory bootstrap-memory` command is specifically designed for brownfield projects to automatically discover and capture existing codebase knowledge.

#### **Bootstrap Modes**

##### **Auto Mode - Recommended Starting Point**
```bash
/project:memory bootstrap-memory --mode=auto --depth=standard
```
- **Best For**: Well-structured codebases with clear patterns
- **Automatically Captures**: Architecture patterns, naming conventions, tech stack, data flows
- **Time Required**: 5-15 minutes depending on codebase size
- **Human Input**: Minimal, fully automated analysis

##### **Interactive Mode - Best for Complex Systems**
```bash
/project:memory bootstrap-memory --mode=interactive --focus=architecture
```
- **Best For**: Complex systems requiring business context
- **Guides You Through**: Historical decisions, business logic, critical components
- **Time Required**: 30-60 minutes with team input
- **Human Input**: Collaborative discovery with questions and validation

##### **Guided Mode - Best for Learning Teams**
```bash
/project:memory bootstrap-memory --mode=guided --depth=shallow
```
- **Best For**: Teams new to BMad Method
- **Provides**: Step-by-step process with explanations and templates
- **Time Required**: 45-90 minutes with learning included
- **Human Input**: Training-focused with built-in quality checks

#### **Focus Areas**

##### **Architecture Focus**
```bash
/project:memory bootstrap-memory --focus=architecture --depth=deep
```
**Captures**:
- System component relationships and dependencies
- Data flow patterns and integration points
- Performance bottlenecks and scaling considerations
- Security architecture and access patterns

##### **Decisions Focus**
```bash
/project:memory bootstrap-memory --focus=decisions --depth=standard
```
**Captures**:
- Historical technical decisions and their rationale
- Technology choices and trade-offs made
- Process and workflow decisions
- Quality standards and practices currently in use

##### **Patterns Focus**
```bash
/project:memory bootstrap-memory --focus=patterns --depth=standard
```
**Captures**:
- Code patterns, conventions, and style guidelines
- Successful implementation approaches
- Anti-patterns currently present in codebase
- Architectural patterns and design approaches

##### **Issues Focus**
```bash
/project:memory bootstrap-memory --focus=issues --depth=deep
```
**Captures**:
- Known bugs, technical debt, and maintenance issues
- Performance problems and bottlenecks
- Security vulnerabilities and concerns
- Developer pain points and workflow friction

#### **Depth Levels**

##### **Shallow Analysis** (`--depth=shallow`)
- Quick overview of major components and patterns
- High-level architecture understanding
- Critical issues identification
- Basic pattern recognition
- **Time**: 5-10 minutes

##### **Standard Analysis** (`--depth=standard`)
- Comprehensive component analysis
- Detailed architecture documentation
- Pattern and anti-pattern identification
- Quality assessment with recommendations
- **Time**: 10-20 minutes

##### **Deep Analysis** (`--depth=deep`)
- Line-by-line analysis where relevant
- Historical git analysis for decision context
- Performance profiling opportunities
- Security audit and vulnerability assessment
- **Time**: 20-45 minutes

### Brownfield Success Patterns

#### **The Progressive Enhancement Pattern**
```bash
# Week 1: Understanding
/project:memory bootstrap-memory --mode=auto --depth=deep
/project:memory patterns --type=all

# Week 2: Quality Assessment
/project:quality quality-gate custom --strict=false
/project:quality anti-pattern-check --scope=all --autofix

# Week 3: Strategic Planning
/project:persona pm
/project:quality udtm "improvement priorities"
/project:consultation consult product-strategy

# Week 4+: Gradual Implementation
/project:persona dev
/project:quality quality-gate pre-implementation --strict
# Focus on new code first, improve legacy gradually
```

#### **The Knowledge Preservation Pattern**
```bash
# Capture tribal knowledge before team changes
/project:memory bootstrap-memory --mode=interactive --focus=decisions

# Interview key team members
/project:memory remember "Senior dev insights: [knowledge]" --category=patterns
/project:memory remember "Historical context: [decisions]" --category=decisions

# Validate and organize knowledge
/project:memory patterns --type=decision --context=team
/project:memory insights --focus=workflow --actionable
```

#### **The Technical Debt Reduction Pattern**
```bash
# Assess current debt systematically
/project:quality anti-pattern-check --scope=all --severity=all

# Prioritize with business impact
/project:persona pm
/project:quality udtm "technical debt prioritization" --perspectives=5

# Incremental improvement with quality gates
/project:persona dev
/project:quality quality-gate 25% --strict
# Improve incrementally while maintaining quality standards
```

### Brownfield Anti-Patterns to Avoid

#### **🚫 Anti-Pattern: Big Bang Adoption**
```bash
# WRONG: Trying to apply all BMad standards immediately
/project:quality quality-gate completion --strict
# This will fail on existing codebase and demoralize team
```
```bash
# RIGHT: Gradual adoption with baseline assessment
/project:quality quality-gate custom --strict=false --report
/project:quality anti-pattern-check --scope=changed --autofix
# Focus on new code, improve existing gradually
```

#### **🚫 Anti-Pattern: Memory Bootstrap Neglect**
```bash
# WRONG: Starting BMad without understanding existing system
/project:persona architect  # No context about existing system
```
```bash
# RIGHT: Always bootstrap memory first
/project:memory bootstrap-memory --mode=auto --focus=all --depth=deep
/project:memory patterns --type=all --context=current
/project:persona architect  # Now has full context
```

#### **🚫 Anti-Pattern: Documentation Replacement**
```bash
# WRONG: Treating BMad memory as documentation replacement
/project:memory remember "Code does X" --category=general
```
```bash
# RIGHT: Capture decisions, patterns, and insights
/project:memory remember "Decision: Chose Redis over database for caching due to performance requirements" --category=decisions
/project:memory remember "Pattern: API pagination using cursor-based approach works well for large datasets" --category=patterns
```

### Brownfield Integration Workflow

#### **Week 1: Discovery & Assessment**
```bash
# Day 1-2: System initialization and memory bootstrap
/project:system init --config --memory
/project:memory bootstrap-memory --mode=auto --focus=all --depth=deep

# Day 3-4: Pattern analysis and quality assessment
/project:memory patterns --type=all --context=current
/project:quality quality-gate custom --strict=false --report

# Day 5: Team consultation and alignment
/project:consultation consult quality-assessment
/project:memory remember "Team assessment results and alignment" --category=consultations
```

#### **Week 2: Strategic Planning**
```bash
# Strategic analysis with Product Manager persona
/project:persona pm
/project:quality udtm "brownfield improvement strategy" --perspectives=7

# Multi-persona strategic consultation
/project:consultation consult product-strategy
/project:consensus-check --threshold=80

# Document strategic decisions
/project:memory remember "Brownfield improvement strategy and priorities" --category=decisions --priority=critical
```

#### **Week 3-4: Pilot Implementation**
```bash
# Choose pilot area for BMad implementation
/project:persona architect
/project:memory recall "improvement strategy"

# Implement BMad practices in pilot area
/project:persona dev
/project:quality quality-gate pre-implementation --strict

# Measure results and document learnings
/project:memory remember "Pilot implementation results and lessons" --category=patterns
/project:behavioral behavioral-report --period=month --focus=improvement
```

### Troubleshooting Brownfield Issues

#### **Issue: Bootstrap Taking Too Long**
**Symptoms**: Memory bootstrap runs for hours without completion
**Solutions**:
```bash
# Start with shallow analysis first
/project:memory bootstrap-memory --mode=auto --depth=shallow

# Then focus on specific areas
/project:memory bootstrap-memory --focus=architecture --depth=standard
/project:memory bootstrap-memory --focus=issues --depth=standard
```

#### **Issue: Team Resistance to Quality Standards**
**Symptoms**: Team pushes back on BMad quality requirements
**Solutions**:
```bash
# Start with non-strict quality gates
/project:quality quality-gate custom --strict=false

# Focus on preventing new debt, not fixing all old debt
/project:quality anti-pattern-check --scope=changed --autofix

# Gradual improvement with team buy-in
/project:consultation consult quality-assessment
```

#### **Issue: Memory Bootstrap Misses Important Context**
**Symptoms**: Bootstrap doesn't capture critical business logic or decisions
**Solutions**:
```bash
# Use interactive mode with team input
/project:memory bootstrap-memory --mode=interactive --focus=decisions

# Manual capture of critical knowledge
/project:memory remember "Critical business rule: [rule and rationale]" --category=decisions
/project:memory remember "Key architectural constraint: [constraint and reason]" --category=patterns
```

## 📁 Generated Structure

After running the generator, you'll have:

```
.claude/commands/
├── persona.md             # Persona activation (/project:persona)
├── memory.md              # Memory operations (/project:memory)
├── quality.md             # Quality enforcement (/project:quality)
├── workflow.md            # Workflow management (/project:workflow)
├── consultation.md        # Multi-persona consultation (/project:consultation)
├── analysis.md            # System analysis (/project:analysis)
├── behavioral.md          # Behavioral tracking (/project:behavioral)
├── system.md              # System management (/project:system)
└── core.md               # Core helpers (/project:core)

docs/claude-code-commands/
├── index.md                            # Documentation index  
└── claude-code-commands-reference.md   # Complete command reference
```

> **Note:** We do NOT generate a README.md in `.claude/commands/` as Claude Code treats it as a command. All documentation is in the `/docs` directory.

## 🎯 Command Groups Mapping

| Claude Command | BMAD Commands Included | Usage Example |
|----------------|------------------------|---------------|
| `/project:persona` | analyst, architect, pm, dev, quality, design-architect, sm, po | `/project:persona architect` |
| `/project:memory` | remember, recall, insights, patterns, **bootstrap-memory** | `/project:memory bootstrap-memory --mode=auto` 🏗️ |
| `/project:quality` | udtm, quality-gate, anti-pattern-check, brotherhood-review | `/project:quality udtm "database design"` |
| `/project:workflow` | suggest, handoff, core-dump, tasks, run-task | `/project:workflow handoff architect` |
| `/project:consultation` | consult, panel-status, consensus-check | `/project:consultation consult technical-review` |
| `/project:analysis` | diagnose, optimize, learn | `/project:analysis optimize --target=performance` |
| `/project:behavioral` | balance, achievements, streaks, leaderboard, behavioral-report, behavioral-preferences | `/project:behavioral balance --detailed` |
| `/project:system` | **init**, status, config, session, validate | `/project:system init --config --memory` 🏗️ |
| `/project:core` | help, agents, context, checklist, exit, yolo | `/project:core help personas` |

> **🏗️ Brownfield Essentials**: Commands marked with 🏗️ are particularly important for existing codebases and brownfield projects.

## 🔧 Customization

### Modifying Command Groups
Edit the `command_groups` dictionary in `generate_claude_commands.py`:

```python
self.command_groups = {
    'persona': {
        'commands': ['analyst', 'architect', 'pm', 'dev'],  # Add/remove personas
        'template': 'persona_activation_template'
    },
    # Add new groups or modify existing ones
}
```

### Creating New Templates
Add new template methods to the generator class:

```python
def generate_custom_command(self, custom_commands: List[str]) -> str:
    """Generate custom command group."""
    return f"""# Custom BMAD Operations
    
Execute custom operation: $ARGUMENTS

[Your custom template content here]
"""
```

### Updating Existing Commands
Modify the template methods (e.g., `generate_persona_command`) to change the prompt structure.

## 📚 Comprehensive Documentation

The system generates complete documentation in `/docs/claude-code-commands/`:

### [Claude Code Commands Reference](claude-code-commands/claude-code-commands-reference.md)
- **Complete Command Listing**: All 46 BMAD commands with full specifications across 9 command groups
- **Parameter Documentation**: Detailed parameter descriptions, types, and constraints
- **Behavioral Requirements**: Command-specific behavioral enforcement rules
- **Usage Examples**: Real-world usage patterns for each command group
- **Troubleshooting Guide**: Common issues and solutions
- **Advanced Workflows**: Complex multi-persona collaboration patterns
- **Behavioral Tracking**: Complete gamification and performance tracking documentation
- **System Management**: Comprehensive orchestrator control and monitoring guide

### Documentation Features
- **Auto-Generated**: Updates automatically when BMAD registry changes
- **Comprehensive**: Covers ALL commands, not just examples
- **Behavioral Integration**: Full BMAD framework documentation
- **Team-Ready**: Shareable reference for team onboarding

## 🔄 Automatic Updates

### Recommended: Use Update Script
```bash
# Updates commands AND documentation
./update_bmad_commands.sh
```

### Manual Update
```bash
# After modifying BMAD command registry
python generate_claude_commands.py    # Commands only
python generate_claude_docs.py        # Documentation only
```

### Automated Update (Optional)
Create a git hook to regenerate commands on BMAD registry changes:

```bash
# .git/hooks/pre-commit
#!/bin/bash
if git diff --cached --name-only | grep -q "bmad-agent/commands/"; then
    echo "🔄 BMAD commands changed, regenerating Claude commands..."
    python generate_claude_commands.py
    git add .claude/commands/
fi
```

## 💡 Usage Patterns

### Greenfield Development Workflow
```bash
# FIRST: Initialize BMAD orchestrator
/project:system init --config --memory
/project:system validate --full

# Start with analysis
/project:persona analyst
/project:analysis diagnose --component=architecture

# Switch to architect for design
/project:workflow handoff architect
/project:persona architect

# Quality validation
/project:quality quality-gate pre-implementation

# Team consultation
/project:consultation consult design-review

# Track behavioral progress
/project:behavioral balance --trend
```

### Brownfield Development Workflow
```bash
# FIRST: Initialize with memory bootstrap
/project:system init --config --memory
/project:memory bootstrap-memory --mode=auto --depth=deep

# Understand current state
/project:memory patterns --type=all --context=current
/project:memory insights --focus=architecture --actionable

# Baseline quality assessment
/project:quality quality-gate custom --strict=false --report
/project:quality anti-pattern-check --scope=all --severity=high

# Strategic improvement planning
/project:persona pm
/project:quality udtm "brownfield improvement strategy" --perspectives=5
/project:consultation consult product-strategy

# Document strategic decisions
/project:memory remember "Improvement strategy and priorities" --category=decisions
```

### Memory-Enhanced Development
```bash
# Capture learnings
/project:memory remember "PostgreSQL performs better than MongoDB for this use case" --category=decisions

# Recall patterns
/project:memory recall "database performance patterns"

# Get insights
/project:memory insights --focus=architecture --actionable
```

### Quality-First Approach
```bash
# Deep analysis for critical decisions
/project:quality udtm "authentication architecture" --perspectives=5

# Pattern validation
/project:quality anti-pattern-check --scope=all --autofix

# Peer review
/project:quality brotherhood-review --focus=security
```

### Behavioral Tracking & Gamification
```bash
# Check your behavioral performance
/project:behavioral balance --detailed --trend

# View achievements and unlock badges
/project:behavioral achievements --category=quality --progress

# Track quality streaks and momentum
/project:behavioral streaks --category=quality --potential

# View team rankings (anonymized)
/project:behavioral leaderboard --timeframe=weekly

# Generate comprehensive analytics
/project:behavioral behavioral-report --period=monthly --focus=patterns

# Configure privacy preferences
/project:behavioral behavioral-preferences --set notifications=minimal
```

### System Management & Monitoring
```bash
# Initialize with full configuration
/project:system init --config --memory --force

# Monitor system health in real-time
/project:system status --detailed --components --performance

# Validate and backup configuration
/project:system config --validate --backup

# Manage session persistence
/project:system session --save

# Run comprehensive system validation
/project:system validate --full --fix --report
```

## 🛠 Troubleshooting

### Command Not Found
- Ensure `.claude/commands/` directory exists
- Verify file names match group names (e.g., `persona.md`)
- Check file permissions

### Arguments Not Parsing
- Commands use `$ARGUMENTS` placeholder
- All text after command name becomes `$ARGUMENTS`
- Use specific format: `/project:group operation --flags`

### Behavioral Framework Not Working
- Verify BMAD behavioral requirements are included in templates
- Check that analysis tags are properly formatted
- Ensure anti-patterns list is current

### Registry Updates Not Reflected
- Re-run `python generate_claude_commands.py`
- Check that YAML file path is correct
- Verify YAML syntax is valid

## 🎉 Benefits of This Solution

1. **Simplified Command Management**: 9 intuitive commands instead of 46 individual ones
2. **Complete BMAD Implementation**: All documented BMAD commands now available
3. **Brownfield Project Support**: Memory bootstrapping captures existing codebase knowledge automatically
4. **Behavioral Tracking & Gamification**: Motivational system with achievements, streaks, and rankings
5. **System Management**: Full orchestrator control with health monitoring and validation
6. **Behavioral Consistency**: All commands inherit BMAD framework with zero-tolerance quality
7. **Native Claude Integration**: Full argument support and completion
8. **Easy Maintenance**: Single source of truth in YAML registry
9. **Flexible Grouping**: Logical organization by function with progressive disclosure
10. **Auto-Generation**: Updates automatically from registry changes
11. **Comprehensive Documentation**: Complete reference with ALL 46 commands documented
12. **Team Collaboration**: Shareable documentation for team onboarding
13. **Privacy-Controlled**: Granular privacy settings for all behavioral tracking
14. **Multi-IDE Ready**: System management enables deployment across different IDEs
15. **Professional Grade**: Production-ready documentation and behavioral enforcement

## 📈 Advanced Features

### Command Analytics
Track usage patterns by parsing Claude Code logs:

```python
# Future enhancement: command usage analytics
def analyze_command_usage():
    # Parse Claude Code usage logs
    # Generate insights on most-used commands
    # Optimize command groupings based on usage
```

### Dynamic Templates
Create context-aware templates that adapt based on project type:

```python
# Future enhancement: context-aware templates
def generate_contextual_template(project_type: str, team_size: int):
    # Adapt command templates based on project context
    # Customize behavioral requirements for team maturity
    # Optimize for specific development phases
```

### Behavioral Analytics Integration
Enhanced behavioral tracking with advanced analytics:

```python
# Current feature: Behavioral tracking
def track_behavioral_patterns():
    # Real-time behavioral score tracking
    # Achievement and streak management
    # Team performance analytics with privacy controls
    # Comprehensive behavioral reporting
```

### System Health Monitoring
Proactive system management and health monitoring:

```python
# Current feature: System management
def monitor_system_health():
    # Real-time component status tracking
    # Automated issue detection and recovery
    # Configuration validation and backup
    # Session state persistence and restoration
```

### Integration with MCP
Connect with Memory Control Protocol for enhanced context:

```python
# Future enhancement: MCP integration
def integrate_with_mcp():
    # Connect to OpenMemory MCP server
    # Sync command usage with memory system
    # Enable cross-session learning and optimization
```

This solution provides the optimal balance of functionality, maintainability, and Claude Code integration for your complete BMAD Method implementation with behavioral optimization, system management, and comprehensive team collaboration features. 