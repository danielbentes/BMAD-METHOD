#!/usr/bin/env python3
"""
BMAD Method → Claude Code Documentation Generator
Creates comprehensive documentation for all Claude Code commands
"""

import yaml
import os
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

class BMADDocsGenerator:
    """Generates comprehensive documentation for BMAD Claude Code commands."""
    
    def __init__(self, registry_path: str = "bmad-agent/commands/command-registry.yml"):
        self.registry_path = registry_path
        self.docs_dir = Path("docs")
        self.claude_docs_dir = self.docs_dir / "claude-code-commands"
        self.registry_data: Dict[str, Any] = {}
        
        # Command grouping (should match generate_claude_commands.py)
        self.command_groups = {
            'persona': {
                'commands': ['analyst', 'pm', 'architect', 'dev', 'sm', 'po', 'quality', 'design-architect'],
                'description': 'Persona Management',
                'claude_command': '/project:persona'
            },
            'memory': {
                'commands': ['remember', 'recall', 'insights', 'patterns', 'bootstrap-memory'],
                'description': 'Memory Operations',
                'claude_command': '/project:memory'
            },
            'quality': {
                'commands': ['udtm', 'quality-gate', 'anti-pattern-check', 'brotherhood-review'],
                'description': 'Quality Enforcement',
                'claude_command': '/project:quality'
            },
            'workflow': {
                'commands': ['suggest', 'handoff', 'core-dump', 'tasks', 'run-task'],
                'description': 'Workflow Management', 
                'claude_command': '/project:workflow'
            },
            'consultation': {
                'commands': ['consult', 'panel-status', 'consensus-check'],
                'description': 'Multi-Persona Consultation',
                'claude_command': '/project:consultation'
            },
            'analysis': {
                'commands': ['diagnose', 'optimize', 'learn'],
                'description': 'System Analysis',
                'claude_command': '/project:analysis'
            },
            'behavioral': {
                'commands': ['balance', 'achievements', 'streaks', 'leaderboard', 'behavioral-report', 'behavioral-preferences'],
                'description': 'Behavioral Tracking',
                'claude_command': '/project:behavioral'
            },
            'system': {
                'commands': ['init', 'status', 'config', 'session', 'validate'],
                'description': 'System Management',
                'claude_command': '/project:system'
            },
            'core': {
                'commands': ['help', 'agents', 'context', 'checklist', 'exit', 'yolo'],
                'description': 'Core Operations',
                'claude_command': '/project:core'
            }
        }
    
    def load_registry(self) -> None:
        """Load BMAD command registry from YAML file."""
        try:
            with open(self.registry_path, 'r', encoding='utf-8') as file:
                self.registry_data = yaml.safe_load(file)
            print(f"✅ Loaded command registry: {len(self.registry_data.get('commands', {}))} commands")
        except FileNotFoundError:
            raise FileNotFoundError(f"Registry file not found: {self.registry_path}")
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML in registry: {e}")
    
    def create_output_directories(self) -> None:
        """Create documentation directory structure."""
        self.claude_docs_dir.mkdir(parents=True, exist_ok=True)
        print(f"📁 Created docs directory: {self.claude_docs_dir}")
    
    def generate_command_reference(self) -> str:
        """Generate the main Claude Code Commands Reference document."""
        
        registry_version = self.registry_data.get('registry_metadata', {}).get('version', 'Unknown')
        timestamp = self._get_timestamp()
        
        content = f"""# Claude Code Commands Reference

> **Auto-generated from BMAD Method Command Registry v{registry_version}**  
> **Generated:** {timestamp}

This reference provides comprehensive documentation for all BMAD Method commands available in Claude Code through the integrated command system.

## Quick Reference

| Command Group | Claude Code Command | Description | Available Operations |
|---------------|-------------------|-------------|---------------------|
"""
        
        # Generate quick reference table
        for group_name, group_config in self.command_groups.items():
            claude_cmd = group_config['claude_command']
            description = group_config['description']
            # Ensure all commands are strings before joining
            commands_list = [str(cmd) for cmd in group_config['commands'][:4]]
            operations = ', '.join(commands_list)  # Show first 4
            if len(group_config['commands']) > 4:
                operations += f", +{len(group_config['commands']) - 4} more"
            
            content += f"| {description} | `{claude_cmd}` | {self._get_group_summary(group_name)} | {operations} |\n"
        
        content += f"""

## Usage Format

All BMAD commands in Claude Code follow this pattern:
```
{self.command_groups['persona']['claude_command']} [operation] [arguments] [--flags]
```

**Examples:**
- `{self.command_groups['persona']['claude_command']} architect` - Activate architect persona
- `{self.command_groups['memory']['claude_command']} remember "API patterns" --category=technical` - Store in memory
- `{self.command_groups['quality']['claude_command']} udtm "microservices vs monolith"` - Deep analysis

## Behavioral Framework

All commands operate under the **BMAD Behavioral Framework**:

### 🎯 Core Principles
- **Example-Driven Learning**: Reference proven patterns from BMAD library
- **Structured Thinking**: Use appropriate analysis tags for all decisions
- **Anti-Pattern Prevention**: Zero tolerance for prohibited patterns  
- **Progressive Disclosure**: Start essential, expand on request
- **Evidence-Based**: All claims backed by verifiable data

### 🚫 Prohibited Patterns (Automatic Penalties)
- "Should work fine" (-$2,000 penalty)
- "Probably okay" (-$1,500 penalty)
- "Good enough for now" (-$3,000 penalty)
- TODO/FIXME in production code (-$3,000 penalty)
- Vague language without evidence (-$1,000 penalty)

### ✅ Required Analysis Tags
- `<decision_analysis>` for strategic choices
- `<problem_analysis>` for issue investigation
- `<architecture_analysis>` for system design
- `<quality_analysis>` for quality assessment
- `<risk_analysis>` for risk evaluation

## Command Groups

"""
        
        # Generate detailed sections for each command group
        for group_name, group_config in self.command_groups.items():
            content += self._generate_group_documentation(group_name, group_config)
            content += "\n"
        
        content += f"""## Integration Notes

### Claude Code Specific Features
- **Command Completion**: Type `/project:` to see available command groups
- **Argument Handling**: All text after the command becomes `$ARGUMENTS`
- **Project Context**: Commands automatically access your project context
- **Session Persistence**: Memory operations persist across Claude Code sessions

### BMAD Method Integration
- **Persona Continuity**: Activated personas maintain state throughout session
- **Quality Gates**: Automatic quality validation at key checkpoints
- **Memory Enhancement**: All interactions contribute to system learning
- **Behavioral Tracking**: Anti-pattern detection and behavioral optimization

### Team Collaboration
- **Shared Commands**: All team members can use the same command set
- **Consistent Behavior**: BMAD framework ensures consistent AI behavior
- **Knowledge Sharing**: Memory operations capture and share team insights
- **Quality Standards**: Unified quality enforcement across team

## Troubleshooting

### Command Not Found
- Ensure `.claude/commands/` directory exists in project root
- Verify command files are present: `ls .claude/commands/`
- Check file permissions and syntax

### Behavioral Framework Issues
- Commands automatically enforce BMAD behavioral requirements
- Anti-patterns trigger immediate penalties and corrections
- Quality gates may block progress until standards are met
- Use `/project:core help` for behavioral guidance

### Memory System Issues  
- Memory operations require proper categorization and tagging
- Bootstrap memory from existing codebases with `/project:memory bootstrap-memory`
- Use `/project:memory insights` to verify memory system health

## Advanced Usage

### Workflow Patterns
```bash
# Analysis → Design → Implementation workflow
/project:persona analyst
/project:analysis diagnose --component=architecture
/project:workflow handoff architect
/project:persona architect
/project:quality quality-gate pre-implementation
```

### Quality-First Development
```bash
# Deep thinking for critical decisions
/project:quality udtm "authentication system design" --perspectives=7
/project:quality anti-pattern-check --scope=all
/project:quality brotherhood-review --focus=security
```

### Memory-Enhanced Learning
```bash
# Capture and leverage organizational knowledge
/project:memory remember "JWT tokens expire in 1 hour for security" --category=decisions
/project:memory recall "authentication best practices"
/project:memory insights --focus=security --actionable
```

### Multi-Persona Consultation
```bash
# Complex decision making with multiple perspectives
/project:consultation consult design-review --personas=architect,designer,quality
/project:consultation consensus-check --threshold=80
```

---

**Generated by BMAD Method Documentation System**  
**Last Updated:** {timestamp}  
**Source:** {self.registry_path}  
**Command Count:** {len(self.registry_data.get('commands', {}))} total commands across {len(self.command_groups)} groups
"""
        
        return content
    
    def _generate_group_documentation(self, group_name: str, group_config: Dict[str, Any]) -> str:
        """Generate detailed documentation for a command group."""
        
        description = group_config['description']
        claude_command = group_config['claude_command']
        commands = group_config['commands']
        
        content = f"""### {description}

**Claude Command:** `{claude_command} [operation] [args]`

{self._get_group_description(group_name)}

#### Available Operations

"""
        
        # Generate detailed command documentation
        for cmd in commands:
            if cmd in self.registry_data.get('commands', {}):
                cmd_data = self.registry_data['commands'][cmd]
                content += self._generate_command_documentation(cmd, cmd_data, claude_command)
        
        # Add group-specific behavioral requirements
        content += f"""
#### Behavioral Requirements for {description}
{self._get_group_behavioral_requirements(group_name)}

#### Usage Examples
```bash
{self._get_group_examples(group_name, claude_command)}
```

---

"""
        
        return content
    
    def _generate_command_documentation(self, cmd_name: str, cmd_data: Dict[str, Any], claude_command: str) -> str:
        """Generate documentation for a specific command."""
        
        description = cmd_data.get('description', 'No description available')
        aliases = cmd_data.get('aliases', [])
        parameters = cmd_data.get('parameters', {})
        behavioral_requirements = cmd_data.get('behavioral_requirements', [])
        
        content = f"""##### `{cmd_name}`
**Description:** {description}

**Usage:** `{claude_command} {cmd_name} [args]`

"""
        
        if aliases:
            # Ensure all aliases are strings
            alias_strings = [str(alias) for alias in aliases if alias is not None]
            if alias_strings:
                content += f"**Aliases:** {', '.join(alias_strings)}\n\n"
        
        if parameters:
            content += "**Parameters:**\n"
            for param_name, param_data in parameters.items():
                param_type = param_data.get('type', 'string')
                required = 'Required' if param_data.get('required', False) else 'Optional'
                param_desc = param_data.get('description', '')
                default = param_data.get('default')
                values = param_data.get('values')
                
                content += f"- `{param_name}` ({param_type}, {required}): {param_desc}"
                if default:
                    content += f" (default: {default})"
                if values:
                    if isinstance(values, list):
                        content += f" (values: {', '.join(map(str, values))})"
                    else:
                        content += f" (values: {str(values)})"
                content += "\n"
            content += "\n"
        
        if behavioral_requirements:
            content += "**Behavioral Requirements:**\n"
            for req in behavioral_requirements:
                if isinstance(req, dict):
                    for key, value in req.items():
                        content += f"- **{key.replace('_', ' ').title()}**: {value}\n"
                elif isinstance(req, str):
                    content += f"- {req}\n"
                else:
                    content += f"- {str(req)}\n"
            content += "\n"
        
        return content
    
    def _get_group_summary(self, group_name: str) -> str:
        """Get a brief summary for a command group."""
        summaries = {
            'persona': 'Activate specialized AI personas with domain expertise',
            'memory': 'Manage persistent learning and pattern recognition',
            'quality': 'Zero-tolerance quality standards and validation',
            'workflow': 'Task automation and structured handoffs',
            'consultation': 'Multi-perspective collaborative decision making',
            'analysis': 'System analysis and performance optimization',
            'behavioral': 'Behavioral tracking and gamification for motivation',
            'system': 'System management and orchestrator control',
            'core': 'Essential operations including help, context, and orchestrator functions'
        }
        return summaries.get(group_name, 'BMAD Method operations')
    
    def _get_group_description(self, group_name: str) -> str:
        """Get detailed description for a command group."""
        descriptions = {
            'persona': 'Activate specialized AI personas that bring domain expertise and specific behavioral patterns to your development process. Each persona maintains consistent behavior and applies domain-specific best practices.',
            'memory': 'Manage the persistent memory system that enables continuous learning and pattern recognition across sessions. Store insights, recall patterns, leverage organizational knowledge, and identify successful behavioral patterns.',
            'quality': 'Enforce zero-tolerance quality standards through systematic validation, deep analysis, and anti-pattern prevention. Maintains excellence through behavioral compliance.',
            'workflow': 'Automate and manage development workflows with intelligent suggestions, structured handoffs, and comprehensive state management.',
            'consultation': 'Facilitate multi-persona collaboration for complex decisions requiring diverse perspectives and expertise synthesis.',
            'analysis': 'Perform comprehensive system analysis including diagnostics, optimization, and continuous learning from outcomes.',
            'behavioral': 'Track behavioral performance through gamification, achievements, and analytics. Motivate consistent excellence through scoring systems, streaks, and team rankings while maintaining privacy and user control.',
            'system': 'Manage BMAD orchestrator initialization, configuration, health monitoring, and system validation. Provides essential infrastructure management and operational control for optimal system performance.',
            'core': 'Essential operations providing contextual assistance, persona information, system guidance, and orchestrator functions including help, context display, and session management.'
        }
        return descriptions.get(group_name, 'BMAD Method operations for enhanced development workflow.')
    
    def _get_group_behavioral_requirements(self, group_name: str) -> str:
        """Get behavioral requirements specific to a command group."""
        requirements = {
            'persona': """- **Domain Expertise Application**: Each persona applies specific domain knowledge and patterns
- **Behavioral Consistency**: Maintain persona characteristics throughout session
- **Anti-Pattern Enforcement**: Persona-specific anti-patterns strictly forbidden
- **Structured Analysis**: Use persona-appropriate analysis tags for decisions""",
            
            'memory': """- **Structured Storage**: Categorize and tag all memory entries for efficient retrieval
- **Context Enrichment**: Add sufficient context for future understanding
- **Pattern Recognition**: Identify and capture reusable patterns and insights
- **Evidence Linking**: Connect memories to decisions and outcomes
- **Proactive Intelligence**: Surface relevant insights to prevent problems before they occur""",
            
            'quality': """- **Zero Tolerance**: Binary accept/reject decisions with no exceptions
- **Evidence Required**: All quality assessments backed by specific data and metrics
- **Structured Analysis**: Mandatory use of quality_analysis tags
- **Penalty Enforcement**: 2x penalty multiplier for quality violations""",
            
            'workflow': """- **Context Preservation**: No information loss during workflow transitions
- **Quality Continuity**: Maintain standards across all workflow steps
- **Memory Integration**: Update and leverage system memory throughout workflow
- **Progressive Execution**: Break complex workflows into manageable, validated steps""",
            
            'consultation': """- **Independent Analysis**: Each participant analyzes independently before collaboration
- **Evidence-Based Arguments**: All positions backed by verifiable data
- **Structured Synthesis**: Systematic integration of diverse perspectives
- **Consensus Documentation**: Clear recording of agreements and dissents""",
            
            'analysis': """- **Comprehensive Coverage**: Analyze all relevant system components and factors
- **Evidence-Based Conclusions**: All findings backed by measurable data
- **Actionable Recommendations**: Provide specific, implementable next steps
- **Memory Integration**: Update system intelligence based on analysis outcomes""",
            
            'behavioral': """- **Real-Time Tracking**: Current balance reflects all recent actions and decisions
- **Motivation Enhancement**: Celebrate achievements and progress milestones prominently
- **Pattern Recognition**: Identify successful approaches and anti-patterns for improvement
- **Goal Alignment**: Track progress toward behavioral objectives and quality standards
- **Privacy Protection**: Maintain anonymity and user control over all tracking features
- **Gamification Balance**: Focus on improvement and learning, not just competition""",
            
            'system': """- **Configuration Integrity**: Ensure all configuration files are valid and complete
- **Change Management**: Track and safely manage configuration changes with rollback
- **Health Monitoring**: Real-time status tracking with proactive issue identification
- **Session Persistence**: Reliable state management across session boundaries
- **Automated Recovery**: Attempt safe fixes for common problems before escalation
- **Operational Excellence**: Monitor and optimize system performance continuously""",
            
            'core': """- **Progressive Disclosure**: Provide essential information first, details on request
- **Context Awareness**: Adapt responses to user expertise and project phase
- **Memory Enhanced**: Surface relevant memories and successful patterns
- **Example Driven**: Include relevant examples from BMAD library
- **State Management**: Proper preservation of context across operations
- **Orchestrator Functions**: Support session management and persona coordination"""
        }
        return requirements.get(group_name, 'Standard BMAD behavioral requirements apply.')
    
    def _get_group_examples(self, group_name: str, claude_command: str) -> str:
        """Get usage examples for a command group."""
        examples = {
            'persona': f"""# Activate architect persona for system design
{claude_command} architect

# Switch to quality enforcer for code review
{claude_command} quality

# Activate product manager for strategic decisions
{claude_command} pm""",
            
            'memory': f"""# Store technical decision with context
{claude_command} remember "PostgreSQL chosen for ACID compliance needs" --category=decisions

# Recall authentication patterns
{claude_command} recall "authentication best practices"

# Get actionable insights on architecture
{claude_command} insights --focus=architecture --actionable

# Show recognized patterns in working style
{claude_command} patterns --type=workflow --success-rate=high""",
            
            'quality': f"""# Deep analysis for critical architectural decision
{claude_command} udtm "microservices vs monolith for user management" --perspectives=7

# Run comprehensive quality gate validation
{claude_command} quality-gate pre-implementation --strict --report

# Scan for anti-patterns across codebase
{claude_command} anti-pattern-check --scope=all --autofix""",
            
            'workflow': f"""# Get intelligent next step suggestions
{claude_command} suggest --alternatives=3 --confidence=high

# Structured handoff from analyst to architect
{claude_command} handoff architect --summary --checklist

# Execute specific BMAD task
{claude_command} run-task create-prd""",
            
            'consultation': f"""# Start design review consultation
{claude_command} consult design-review --personas=architect,designer,quality

# Check consensus on technical decision
{claude_command} consensus-check --threshold=80

# View active consultation status
{claude_command} panel-status --detailed""",
            
            'analysis': f"""# Comprehensive system diagnostic
{claude_command} diagnose --component=performance --deep --fix

# Optimize for memory efficiency
{claude_command} optimize --target=memory --aggressive

# Learn from recent development outcomes
{claude_command} learn --scope=project --feedback""",
            
            'behavioral': f"""# Check current behavioral balance and trends
{claude_command} balance --detailed --trend

# View achievements and progress
{claude_command} achievements --category=quality --progress

# Show active quality streaks
{claude_command} streaks --category=quality --potential

# View team performance rankings (anonymized)
{claude_command} leaderboard --timeframe=weekly --anonymous

# Generate comprehensive behavioral analytics
{claude_command} behavioral-report --period=monthly --focus=patterns

# Configure tracking preferences
{claude_command} behavioral-preferences --set notifications=minimal""",
            
            'system': f"""# Initialize BMAD orchestrator with full setup
{claude_command} init --config --memory

# Check comprehensive system health
{claude_command} status --detailed --components --performance

# Validate configuration files
{claude_command} config --validate --backup

# Save current session state
{claude_command} session --save

# Run comprehensive system validation
{claude_command} validate --full --fix --report""",
            
            'core': f"""# Get help on persona system
{claude_command} help personas --examples

# List available personas with recommendations
{claude_command} agents --stats --recommended

# Show rich context with suggestions
{claude_command} context --full --memory --suggestions

# Exit current persona with state preservation
{claude_command} exit --save --handoff

# Toggle YOLO mode for streamlined execution
{claude_command} yolo --confirm"""
        }
        return examples.get(group_name, f'{claude_command} [operation] [args]')
    
    def _get_timestamp(self) -> str:
        """Get current timestamp for documentation."""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    def generate_documentation(self) -> None:
        """Generate all documentation files."""
        self.create_output_directories()
        
        # Generate main command reference
        reference_content = self.generate_command_reference()
        reference_file = self.claude_docs_dir / "claude-code-commands-reference.md"
        
        with open(reference_file, 'w', encoding='utf-8') as f:
            f.write(reference_content)
        
        print(f"✅ Generated: {reference_file}")
        
        # Generate index file for docs navigation
        self._generate_docs_index()
        
        print(f"\n📚 Documentation generated successfully!")
        print(f"📁 Available at: {self.claude_docs_dir}")
        print(f"🔗 Main reference: {reference_file}")
    
    def _generate_docs_index(self) -> None:
        """Generate an index file for the Claude Code documentation."""
        index_content = f"""# Claude Code Integration

Welcome to the BMAD Method integration with Claude Code! This section provides everything you need to use BMAD commands directly within Claude Code.

## Overview

The BMAD Method provides **{len(self.registry_data.get('commands', {}))} specialized commands** organized into **{len(self.command_groups)} logical groups** for Claude Code. Each command maintains the full BMAD behavioral framework including:

- **Example-driven learning** from proven patterns
- **Structured thinking** with analysis tags  
- **Anti-pattern prevention** with zero tolerance
- **Progressive disclosure** adapting to context
- **Evidence-based decision making** throughout

## Quick Start

!!! tip "Ready to Begin?"
    1. **[Setup Integration](../BMAD_CLAUDE_SETUP.md)** - Install and configure BMAD commands
    2. **[View Commands Reference](claude-code-commands-reference.md)** - Complete command documentation
    3. **Test Your First Command**: `/project:persona architect`

## Available Command Groups

| Command Group | Claude Code Command | Purpose |
|---------------|-------------------|---------|
| **Persona Management** | `/project:persona [name]` | Activate specialized AI personas with domain expertise |
| **Memory Operations** | `/project:memory [operation]` | Manage persistent learning and pattern recognition |
| **Quality Enforcement** | `/project:quality [operation]` | Zero-tolerance quality standards and validation |
| **Workflow Management** | `/project:workflow [operation]` | Task automation and structured handoffs |
| **Multi-Persona Consultation** | `/project:consultation [operation]` | Collaborative decision making with multiple perspectives |
| **System Analysis** | `/project:analysis [operation]` | Performance optimization and system intelligence |
| **Core Helpers** | `/project:core [operation]` | Essential assistance and information commands |

## Key Features

### 🎯 **Behavioral Excellence**
Every command enforces the BMAD behavioral framework with automatic penalties for anti-patterns and rewards for excellence.

### 🧠 **Memory Integration** 
Persistent learning across sessions with intelligent pattern recognition and organizational knowledge capture.

### 👥 **Multi-Persona Workflows**
Seamless collaboration between specialized AI personas with structured handoffs and context preservation.

### 🔍 **Quality Enforcement**
Zero-tolerance quality gates with comprehensive validation and automated improvement suggestions.

## Example Usage

```bash
# Activate architect persona for system design
/project:persona architect

# Store important technical decisions  
/project:memory remember "PostgreSQL chosen for ACID compliance" --category=decisions

# Run deep analysis for critical choices
/project:quality udtm "microservices vs monolith architecture" --perspectives=7

# Get intelligent next step suggestions
/project:workflow suggest --alternatives=3 --confidence=high

# Start collaborative design review
/project:consultation consult design-review --personas=architect,designer,quality
```

## Documentation Structure

- **[Setup Guide](../BMAD_CLAUDE_SETUP.md)** - Complete integration and configuration instructions
- **[Commands Reference](claude-code-commands-reference.md)** - Comprehensive documentation for all 34 commands
- **Usage Examples** - Real-world patterns and workflows throughout the documentation

---

!!! info "Auto-Generated Documentation"
    This documentation is automatically generated from BMAD Method Registry v{self.registry_data.get('registry_metadata', {}).get('version', 'Unknown')} and updates when the command registry changes.
    
    **Last Updated:** {self._get_timestamp()}
"""
        
        index_file = self.claude_docs_dir / "index.md"
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        print(f"📋 Generated: {index_file}")


def main():
    """Main execution function."""
    print("📚 BMAD Method → Claude Code Documentation Generator")
    print("=" * 55)
    
    try:
        generator = BMADDocsGenerator()
        generator.load_registry()
        generator.generate_documentation()
        
        print("\n✨ Documentation generation complete!")
        print("\n📖 Next steps:")
        print("1. Review generated documentation in docs/claude-code-commands/")
        print("2. Share the reference with your team")
        print("3. Update docs when BMAD registry changes")
        
    except Exception as e:
        import traceback
        print(f"❌ Error: {e}")
        print("Full traceback:")
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main()) 