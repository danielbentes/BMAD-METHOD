#!/usr/bin/env python3
"""
BMAD Method → Claude Code Command Generator
Converts BMAD command registry to Claude Code compatible commands
"""

import yaml
import os
from pathlib import Path
from typing import Dict, List, Any
import json

class BMADToClaudeGenerator:
    """Generates Claude Code commands from BMAD command registry."""
    
    def __init__(self, registry_path: str = "bmad-agent/commands/command-registry.yml"):
        self.registry_path = registry_path
        self.output_dir = Path(".claude/commands")
        self.registry_data: Dict[str, Any] = {}
        
        # Command grouping strategy
        self.command_groups = {
            'persona': {
                'commands': ['analyst', 'pm', 'architect', 'dev', 'sm', 'po', 'quality', 'design-architect'],
                'template': 'persona_activation_template'
            },
            'memory': {
                'commands': ['remember', 'recall', 'insights', 'patterns', 'bootstrap-memory'],
                'template': 'memory_operation_template'
            },
            'quality': {
                'commands': ['udtm', 'quality-gate', 'anti-pattern-check', 'brotherhood-review'],
                'template': 'quality_enforcement_template'
            },
            'workflow': {
                'commands': ['suggest', 'handoff', 'core-dump', 'tasks', 'run-task'],
                'template': 'workflow_management_template'
            },
            'consultation': {
                'commands': ['consult', 'panel-status', 'consensus-check'],
                'template': 'consultation_template'
            },
            'analysis': {
                'commands': ['diagnose', 'optimize', 'learn'],
                'template': 'analysis_template'
            },
            'behavioral': {
                'commands': ['balance', 'achievements', 'streaks', 'leaderboard', 'behavioral-report', 'behavioral-preferences'],
                'template': 'behavioral_tracking_template'
            },
            'system': {
                'commands': ['init', 'status', 'config', 'session', 'validate'],
                'template': 'system_management_template'
            },
            'core': {
                'commands': ['help', 'agents', 'context', 'checklist', 'exit', 'yolo'],
                'template': 'core_helper_template'
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
    
    def create_output_directory(self) -> None:
        """Create .claude/commands directory structure."""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        print(f"📁 Created output directory: {self.output_dir}")
    
    def generate_persona_command(self, persona_commands: List[str]) -> str:
        """Generate unified persona activation command."""
        personas_info = {}
        
        for cmd in persona_commands:
            if cmd in self.registry_data.get('commands', {}):
                cmd_data = self.registry_data['commands'][cmd]
                personas_info[cmd] = {
                    'description': cmd_data.get('description', ''),
                    'behavioral_requirements': cmd_data.get('behavioral_requirements', []),
                    'usage': cmd_data.get('usage', '')
                }
        
        return f"""# BMAD Persona Activation

You are activating a BMAD Method persona with the following command:

**PERSONA**: $ARGUMENTS

## Available Personas:
{self._format_persona_list(personas_info)}

## Behavioral Requirements (All Personas):
- **Example-Driven Learning**: Reference relevant examples from BMAD library
- **Structured Thinking**: Use appropriate analysis tags for decisions
- **Anti-Pattern Prevention**: Zero tolerance for prohibited patterns
- **Progressive Disclosure**: Start essential, expand on request
- **Evidence-Based**: All claims backed by verifiable data

## Persona-Specific Activation:
Based on the persona specified in $ARGUMENTS, apply the specific domain expertise, behavioral rules, and success criteria for that persona.

**ACTIVATION PROTOCOL**:
1. Identify the requested persona from $ARGUMENTS
2. Load domain expertise and behavioral profile
3. Apply persona-specific anti-patterns and requirements
4. Execute with full behavioral compliance

Execute persona activation now with behavioral excellence.
"""
    
    def generate_memory_command(self, memory_commands: List[str]) -> str:
        """Generate unified memory operations command."""
        return f"""# BMAD Memory Operations

Execute memory operation: $ARGUMENTS

## Available Operations:
- **remember** [content] --category --tags --priority: Add to persistent memory
- **recall** [query] --category --limit --since: Search memory with natural language  
- **insights** --focus --depth --actionable: Get AI-powered pattern insights
- **patterns** --type --success-rate --context: Show recognized behavioral and workflow patterns
- **bootstrap-memory** --mode --focus --depth: Initialize from existing codebase

## Memory Integration Requirements:
- **Structured Storage**: Categorize and tag for efficient retrieval
- **Context Enrichment**: Add context for future understanding  
- **Pattern Recognition**: Identify and capture reusable patterns
- **Evidence Linking**: Connect memories to decisions and outcomes

## Pattern Recognition Features:
- **Working Style Patterns**: Identify user's preferred approaches and successful workflows
- **Decision Patterns**: Track decision-making approaches and their outcomes
- **Collaboration Patterns**: Recognize effective team interaction and consultation methods
- **Quality Patterns**: Monitor what quality approaches work best for the user/team
- **Learning Patterns**: Understand how the user best acquires and applies new knowledge

## Behavioral Compliance:
- All memory operations follow example-driven learning principles
- Memory insights must be actionable and evidence-based
- Progressive disclosure adapts detail level to user needs
- Anti-pattern detection applies to memory content
- Pattern recognition enables proactive intelligence and optimization

Parse the operation from $ARGUMENTS and execute with memory system integration.
"""
    
    def generate_quality_command(self, quality_commands: List[str]) -> str:
        """Generate unified quality enforcement command."""
        return f"""# BMAD Quality Enforcement

Execute quality operation: $ARGUMENTS

## Quality Operations:
- **udtm** [topic] --perspectives --depth: Ultra-Deep Thinking Mode analysis
- **quality-gate** [phase] --strict --report: Milestone quality validation
- **anti-pattern-check** --scope --severity --autofix: Pattern violation scan
- **brotherhood-review** --reviewers --focus: Honest peer review process

## Quality Standards (Non-Negotiable):
- **Zero Tolerance**: Binary accept/reject decisions only
- **Evidence Required**: All assessments backed by specific data
- **Structured Analysis**: Mandatory use of quality_analysis tags
- **Penalty Enforcement**: 2x multiplier for quality violations

## Forbidden Patterns (Immediate Blocking):
- "Should work fine" (-$2000 penalty)
- "Probably okay" (-$1500 penalty) 
- "Good enough for now" (-$3000 penalty)
- Any TODO/FIXME in production code (-$3000 penalty)

Execute quality operation from $ARGUMENTS with uncompromising standards.
"""
    
    def generate_workflow_command(self, workflow_commands: List[str]) -> str:
        """Generate unified workflow management command."""
        return f"""# BMAD Workflow Management

Execute workflow operation: $ARGUMENTS

## Workflow Operations:
- **suggest** --context --confidence --alternatives: AI-powered next steps
- **handoff** [persona] --summary --checklist: Structured persona transition
- **core-dump** --format --include-memory: Save comprehensive session state
- **tasks** --category --recommended: List available tasks with insights
- **run-task** [task-name] [...args]: Execute specific BMAD task

## Workflow Requirements:
- **Context Preservation**: No information loss during transitions
- **Quality Continuity**: Maintain standards across workflow steps
- **Memory Integration**: Leverage and update system memory
- **Progressive Execution**: Break complex workflows into manageable steps

## Behavioral Compliance:
- All workflow operations use structured thinking
- Evidence-based recommendations only
- Example-driven approach for task execution
- Anti-pattern prevention throughout workflow

Parse workflow operation from $ARGUMENTS and execute with behavioral excellence.
"""
    
    def generate_consultation_command(self, consultation_commands: List[str]) -> str:
        """Generate unified consultation command."""
        return f"""# BMAD Multi-Persona Consultation

Execute consultation: $ARGUMENTS

## Consultation Types:
- **consult** [type] --personas --duration: Multi-persona collaboration session
- **panel-status** --detailed --timeline: Active consultation status
- **consensus-check** --threshold --require-all: Agreement assessment

## Consultation Protocol:
1. **Individual Analysis Phase**: Each persona analyzes independently
2. **Structured Sharing Phase**: Present findings with evidence
3. **Evidence Evaluation Phase**: Cross-validate claims and data
4. **Synthesis Phase**: Collaborative solution building
5. **Decision Phase**: Consensus or documented dissent

## Behavioral Coordination:
- Each participant maintains domain expertise
- All responses use structured analysis tags
- Evidence-based arguments only
- Quality aggregation across perspectives

Execute consultation from $ARGUMENTS with collaborative excellence.
"""
    
    def generate_analysis_command(self, analysis_commands: List[str]) -> str:
        """Generate unified analysis command."""
        return f"""# BMAD System Analysis

Execute analysis operation: $ARGUMENTS

## Analysis Operations:
- **diagnose** --component --deep --fix: System health diagnostics
- **optimize** --target --aggressive --simulate: Performance optimization
- **learn** --scope --feedback --apply: Outcome analysis and system updates

## Analysis Requirements:
- **Comprehensive Coverage**: Check all relevant system components
- **Evidence-Based Conclusions**: All findings backed by data
- **Actionable Recommendations**: Specific, implementable next steps
- **Memory Integration**: Update system intelligence based on findings

## Analysis Standards:
- Use appropriate analysis tags (problem_analysis, architecture_analysis, etc.)
- Multiple perspective consideration for complex issues
- Risk assessment with mitigation strategies
- Success criteria and validation methods

Execute analysis from $ARGUMENTS with systematic excellence.
"""
    
    def generate_behavioral_command(self, behavioral_commands: List[str]) -> str:
        """Generate unified behavioral tracking command."""
        return f"""# BMAD Behavioral Tracking

Execute behavioral operation: $ARGUMENTS

## Behavioral Operations:
- **balance** --detailed --history --trend: Check current behavioral balance and status
- **achievements** --category --available --progress: View unlocked achievements and progress
- **streaks** --all --category --potential: Display active quality and efficiency streaks
- **leaderboard** --timeframe --category --team: View anonymized team rankings
- **behavioral-report** --period --focus --compare: Generate detailed analytics
- **behavioral-preferences** --set --get --reset: Configure tracking preferences

## Gamification Framework:
- **Scoring System**: Transparent reward/penalty calculations
- **Achievement System**: Unlock badges for consistent excellence
- **Streak Tracking**: Build momentum through consistency
- **Team Rankings**: Healthy competition with learning focus
- **Progress Visualization**: Clear indicators of improvement

## Privacy & Control:
- Full user control over tracking preferences
- Anonymized team comparisons by default
- Granular privacy settings for all features
- Easy opt-out mechanisms

## Behavioral Requirements:
- **Real-Time Tracking**: Current balance reflects all recent actions
- **Motivation Enhancement**: Celebrate achievements and progress milestones
- **Pattern Recognition**: Identify successful approaches and anti-patterns
- **Goal Alignment**: Track progress toward behavioral objectives
- **Privacy Protection**: Maintain anonymity and user control

## Anti-Pattern Prevention:
- Never use "probably fine" or "mostly correct" in quality assessments
- Avoid "I think" - always provide evidence-based insights
- Block "quick hack" or "temporary solution" approaches
- Prevent TODO/FIXME in production code

Execute behavioral operation from $ARGUMENTS with motivational excellence.
"""

    def generate_system_command(self, system_commands: List[str]) -> str:
        """Generate unified system management command."""
        return f"""# BMAD System Management

Execute system operation: $ARGUMENTS

## System Operations:
- **init** --config --memory --force --minimal: Initialize BMAD orchestrator
- **status** --detailed --components --performance: Show system health
- **config** --validate --reload --backup --restore: Manage configuration
- **session** --save --restore --new --info: Manage session state
- **validate** --full --memory --personas --fix: Comprehensive validation

## System Management Framework:
- **Initialization Protocol**: Systematic startup with component validation
- **Health Monitoring**: Real-time status tracking with performance metrics
- **Configuration Management**: Safe configuration changes with rollback
- **Session Persistence**: Reliable state management across sessions
- **Validation Pipeline**: Comprehensive checks with automated recovery

## Core Components:
- **Configuration System**: Load and validate all BMAD configuration files
- **Memory Integration**: Establish connection to OpenMemory MCP if available
- **Persona System**: Verify all persona files are accessible and valid
- **Quality Framework**: Initialize behavioral enforcement and tracking
- **Session Management**: Maintain context and state across interactions

## Operational Excellence:
- **Proactive Monitoring**: Identify issues before they impact functionality
- **Automated Recovery**: Attempt safe fixes for common problems
- **Rollback Capabilities**: Enable undo for configuration changes
- **Performance Optimization**: Monitor and improve system performance
- **Security Compliance**: Ensure all operations follow security best practices

## Error Handling:
- Graceful degradation when components are unavailable
- Clear error reporting with specific remediation steps
- Automatic backup creation before risky operations
- Validation of all inputs and configurations

Execute system operation from $ARGUMENTS with operational excellence.
"""

    def generate_core_command(self, core_commands: List[str]) -> str:
        """Generate unified core helper command."""
        return f"""# BMAD Core Operations

Execute core operation: $ARGUMENTS

## Core Operations:
- **help** [topic] --examples --advanced: Contextual help with examples
- **agents** --stats --recommended: List personas with usage insights
- **context** --full --memory --suggestions: Rich context with recommendations
- **checklist** [name] --interactive --fix: Validation checklist execution
- **exit** --save --handoff: Exit current persona with state preservation
- **yolo** --confirm: Toggle YOLO mode for streamlined execution

## Core Behavioral Requirements:
- **Progressive Disclosure**: Essential information first, details on request
- **Context Awareness**: Adapt responses to user expertise and project phase
- **Memory Enhanced**: Surface relevant memories and patterns
- **Example Driven**: Include relevant examples from BMAD library
- **State Management**: Proper context preservation across persona switches

## Orchestrator Integration:
- **Exit Operations**: Preserve work progress and suggest appropriate handoffs
- **YOLO Mode**: Maintains safety while reducing process overhead
- **Help System**: Memory-enhanced assistance adapted to user expertise
- **Context Display**: Session state combined with relevant memory insights

## Help Integration:
All core operations provide contextual assistance that:
- References successful patterns from memory
- Suggests appropriate next steps
- Maintains behavioral compliance
- Offers relevant examples and guidance

Execute core operation from $ARGUMENTS with helpful excellence.
"""
    
    def _format_persona_list(self, personas_info: Dict[str, Any]) -> str:
        """Format persona information for display."""
        formatted = []
        for persona, info in personas_info.items():
            formatted.append(f"- **{persona}**: {info.get('description', 'N/A')}")
        return '\n'.join(formatted)
    
    def generate_all_commands(self) -> None:
        """Generate all Claude Code command files."""
        self.create_output_directory()
        
        generated_count = 0
        
        for group_name, group_config in self.command_groups.items():
            commands = group_config['commands']
            template_method = getattr(self, f"generate_{group_name}_command")
            
            # Generate command content
            command_content = template_method(commands)
            
            # Write to file
            output_file = self.output_dir / f"{group_name}.md"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(command_content)
            
            print(f"✅ Generated: {output_file} ({len(commands)} commands)")
            generated_count += 1
        
        print(f"\n🎉 Successfully generated {generated_count} Claude Code command files!")
        print(f"📁 Commands available in: {self.output_dir}")
        print("\n💡 Usage examples:")
        print("  /project:persona architect")
        print("  /project:memory remember 'API patterns' --category=technical")
        print("  /project:quality udtm 'microservices vs monolith'")
        print("  /project:workflow suggest --alternatives=3")
    

    
    def _get_timestamp(self) -> str:
        """Get current timestamp for generation tracking."""
        from datetime import datetime
        return datetime.now().isoformat()


def main():
    """Main execution function."""
    print("🚀 BMAD Method → Claude Code Command Generator")
    print("=" * 50)
    
    try:
        generator = BMADToClaudeGenerator()
        generator.load_registry()
        generator.generate_all_commands()
        
        print("\n✨ Generation complete! Your BMAD commands are ready for Claude Code.")
        print("\n📖 Next steps:")
        print("1. Review generated commands in .claude/commands/")
        print("2. Test commands in Claude Code: /project:persona architect")
        print("3. Customize templates if needed")
        print("4. Add to git: git add .claude/commands/")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main()) 