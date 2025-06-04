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
```bash
# CRITICAL FIRST STEP: Initialize the BMAD orchestrator system
/project:system init --config --memory

# Verify all components are operational
/project:system status --detailed

# Validate configuration and personas
/project:system validate --full
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
| `/project:memory` | remember, recall, insights, patterns, bootstrap-memory | `/project:memory recall "auth patterns"` |
| `/project:quality` | udtm, quality-gate, anti-pattern-check, brotherhood-review | `/project:quality udtm "database design"` |
| `/project:workflow` | suggest, handoff, core-dump, tasks, run-task | `/project:workflow handoff architect` |
| `/project:consultation` | consult, panel-status, consensus-check | `/project:consultation consult technical-review` |
| `/project:analysis` | diagnose, optimize, learn | `/project:analysis optimize --target=performance` |
| `/project:behavioral` | balance, achievements, streaks, leaderboard, behavioral-report, behavioral-preferences | `/project:behavioral balance --detailed` |
| `/project:system` | init, status, config, session, validate | `/project:system init --config --memory` |
| `/project:core` | help, agents, context, checklist, exit, yolo | `/project:core help personas` |

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

### Development Workflow
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
3. **Behavioral Tracking & Gamification**: Motivational system with achievements, streaks, and rankings
4. **System Management**: Full orchestrator control with health monitoring and validation
5. **Behavioral Consistency**: All commands inherit BMAD framework with zero-tolerance quality
6. **Native Claude Integration**: Full argument support and completion
7. **Easy Maintenance**: Single source of truth in YAML registry
8. **Flexible Grouping**: Logical organization by function with progressive disclosure
9. **Auto-Generation**: Updates automatically from registry changes
10. **Comprehensive Documentation**: Complete reference with ALL 46 commands documented
11. **Team Collaboration**: Shareable documentation for team onboarding
12. **Privacy-Controlled**: Granular privacy settings for all behavioral tracking
13. **Multi-IDE Ready**: System management enables deployment across different IDEs
14. **Professional Grade**: Production-ready documentation and behavioral enforcement

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